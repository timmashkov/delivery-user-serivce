from presentation.routers import user_router

from .server import APIServer

service_app = APIServer(
    name="service_app",
    routers=[user_router],
).app
