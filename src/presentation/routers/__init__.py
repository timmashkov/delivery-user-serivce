from .permission_router import perm_router
from .role_router import role_router
from .user_router import user_router

__all__: tuple[str] = ("user_router", "role_router", "permission_router")
