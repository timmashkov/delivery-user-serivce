# User Service Service

Микросервис управления пользователями, ролями и разрешениями (RBAC) для системы доставки.

## Стек технологий

- **Python 3.14**
- **FastAPI** — веб-фреймворк
- **SQLAlchemy 2.0** — ORM (async)
- **asyncpg** — PostgreSQL драйвер
- **Alembic** — миграции БД
- **Dishka** — DI контейнер
- **Pydantic** — валидация данных

## Архитектура проекта

Проект построен на принципах **Clean Architecture** с элементами **DDD**:

```
src/
├── presentation/          # API слой (FastAPI роутеры, DTO)
│   ├── routers/           # HTTP эндпоинты
│   └── models/            # Pydantic модели (request/response)
├── application/           # Слой прикладной логики
│   ├── use_cases/         # Use Case классы
│   └── providers/         # DI провайдеры (dishka)
├── domain/                # Доменная модель
│   ├── user/              # Агрегат User
│   └── event/             # Domain Events
└── infrastructure/        # Инфраструктура
    ├── database/
    │   ├── models/        # SQLAlchemy модели
    │   ├── repositories/  # Репозитории
    │   ├── utils/         # Утилиты (mixin, query modifiers)
    │   └── migrations/    # Alembic миграции
    └── providers/         # DI провайдеры
```

### Слои

| Слой | Назначение |
|------|------------|
| **Presentation** | HTTP API, валидация запросов, сериализация ответов |
| **Application** | Бизнес-логика, координация процессов |
| **Domain** | Бизнес-сущности, правила, события |
| **Infrastructure** | Работа с БД, репозитории, миграции |

## API Endpoints

### Users

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/user/` | Получить список пользователей |
| `GET` | `/user/{user_uuid}` | Получить пользователя по UUID |
| `POST` | `/user/` | Создать пользователя |
| `PATCH` | `/user/{user_uuid}` | Обновить пользователя |
| `DELETE` | `/user/{user_uuid}` | Удалить пользователя |
| `POST` | `/user/{user_uuid}/roles` | Назначить роли пользователю |

### Roles

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/role/` | Получить список ролей |
| `GET` | `/role/{role_uuid}` | Получить роль по UUID |
| `POST` | `/role/` | Создать роль |
| `PATCH` | `/role/{role_uuid}` | Обновить роль |
| `DELETE` | `/role/{role_uuid}` | Удалить роль |

### Permissions

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/permission/` | Получить список разрешений |
| `GET` | `/permission/{perm_uuid}` | Получить разрешение по UUID |
| `POST` | `/permission/` | Создать разрешение |
| `PATCH` | `/permission/{perm_uuid}` | Обновить разрешение |
| `DELETE` | `/permission/{perm_uuid}` | Удалить разрешение |

## Модель данных

### ER-диаграмма

```
┌──────────────────┐       ┌──────────────────────┐       ┌──────────────────┐
│     users        │       │     user_roles       │       │     roles        │
├──────────────────┤       ├──────────────────────┤       ├──────────────────┤
│ uuid (PK)        │◄──────│ user_uuid (PK, FK)   │       │ uuid (PK)        │
│ username (UQ)    │       │ role_uuid (PK, FK)   │──────►│ name (UQ)        │
│ email (UQ)       │       │ created_at           │       │ data (JSONB)     │
│ age              │       │ updated_at           │       ├──────────────────┤
│ phone_number (UQ)│       └──────────────────────┘       │ users []         │
│ created_at       │                                      │ permissions []   │
│ updated_at       │       ┌──────────────────────┐       └──────────────────┘
│ data (JSONB)     │       │  role_permissions    │
└──────────────────┘       ├──────────────────────┤
                           │ permission_uuid (PK, │       ┌──────────────────────┐
                           │  FK)                 │       │   permissions        │
                           │ role_uuid (PK, FK)   │──────►├──────────────────────┤
                           │ created_at           │       │ uuid (PK)            │
                           │ updated_at           │       │ name                 │
                           └──────────────────────┘       │ layer                │
                                                          │ data (JSONB)       │
                                                          │ created_at         │
                                                          │ updated_at         │
                                                          └──────────────────────┘

┌──────────────────────┐
│      outbox          │
├──────────────────────┤
│ uuid (PK)            │
│ event_type           │
│ entity_id (FK*)      │
│ status               │
│ sent_at              │
│ created_at           │
└──────────────────────┘
* Ссылается на сущность в другом микросервисе
```