from ninja import NinjaAPI

from apps.jastip.api import router as jastip_router


api = NinjaAPI(
    title="Jastip API",
    version="1.0.0",
)

api.add_router("/jastip/", jastip_router)