"""add roles and permissions

Revision ID: a1b2c3d4e5f6
Revises: 71e4e233d45e
Create Date: 2026-09-15 19:32:00

"""

import uuid

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import JSONB, UUID

revision = "a1b2c3d4e5f6"
down_revision = "71e4e233d45e"
branch_labels = None
depends_on = None

ROLES_TABLE = "roles"
PERMISSIONS_TABLE = "permissions"
ROLE_PERMISSIONS_TABLE = "role_permissions"


def upgrade() -> None:
    conn = op.get_bind()

    # --- Роли ---
    roles_data = [
        {"uuid": uuid.uuid4(), "name": "user", "data": {}},
        {"uuid": uuid.uuid4(), "name": "advanced_user", "data": {}},
        {"uuid": uuid.uuid4(), "name": "superuser", "data": {}},
        {"uuid": uuid.uuid4(), "name": "watcher", "data": {}},
        {"uuid": uuid.uuid4(), "name": "admin", "data": {}},
    ]
    op.bulk_insert(
        sa.table(
            ROLES_TABLE,
            sa.column("uuid", UUID(as_uuid=True)),
            sa.column("name", sa.String),
            sa.column("data", JSONB),
        ),
        roles_data,
    )

    # --- Пермишены ---
    permissions_data = [
        {"uuid": uuid.uuid4(), "name": "watch", "layer": "backend", "data": {}},
        {"uuid": uuid.uuid4(), "name": "edit", "layer": "backend", "data": {}},
        {"uuid": uuid.uuid4(), "name": "admin", "layer": "backend", "data": {}},
    ]
    op.bulk_insert(
        sa.table(
            PERMISSIONS_TABLE,
            sa.column("uuid", UUID(as_uuid=True)),
            sa.column("name", sa.String),
            sa.column("layer", sa.String),
            sa.column("data", JSONB),
        ),
        permissions_data,
    )

    # --- Связи ролей и пермишенов ---
    role_rows = conn.execute(
        sa.text(f"SELECT uuid, name FROM {ROLES_TABLE}")
    ).fetchall()
    perm_rows = conn.execute(
        sa.text(f"SELECT uuid, name FROM {PERMISSIONS_TABLE}")
    ).fetchall()

    role_map = {row.name: row.uuid for row in role_rows}
    perm_map = {row.name: row.uuid for row in perm_rows}

    role_permissions = {
        "user": ["watch"],
        "advanced_user": ["watch", "edit"],
        "watcher": ["watch"],
        "superuser": ["watch", "edit", "admin"],
        "admin": ["watch", "edit", "admin"],
    }

    rp_rows = [
        {
            "uuid": uuid.uuid4(),
            "role_uuid": role_map[r],
            "permission_uuid": perm_map[p],
            "data": {},
        }
        for r, perms in role_permissions.items()
        for p in perms
    ]

    if rp_rows:
        op.bulk_insert(
            sa.table(
                ROLE_PERMISSIONS_TABLE,
                sa.column("uuid", UUID(as_uuid=True)),
                sa.column("role_uuid", UUID(as_uuid=True)),
                sa.column("permission_uuid", UUID(as_uuid=True)),
                sa.column("data", JSONB),
            ),
            rp_rows,
        )


def downgrade() -> None:
    op.execute(f"DELETE FROM {ROLE_PERMISSIONS_TABLE}")
    op.execute(
        f"DELETE FROM {PERMISSIONS_TABLE} " f"WHERE name IN ('watch', 'edit', 'admin')"
    )
    op.execute(
        f"DELETE FROM {ROLES_TABLE} "
        f"WHERE name IN ('user', 'advanced_user', 'superuser', 'watcher', 'admin')"
    )
