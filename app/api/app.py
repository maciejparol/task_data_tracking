from config import Config
from fastapi import APIRouter, Depends, FastAPI
from fastapi.requests import Request
from fastapi.responses import Response
from loguru import logger
from views import RESOURCES

APP = FastAPI(
    version=Config.VERSION,
    title=Config.APP_TITLE,
    description=Config.APP_DESCRIPTION,
    openapi_url=Config.OPENAPI_URL,
)
API_ROUTER = APIRouter()


async def log_request(request: Request) -> None:
    """
    Logs incoming request information
    """
    logger.info(f"[{request.client.host}:{request.client.host}] {request.method} {request.url}")
    logger.info(f"header: {request.headers}, body: ")
    logger.info(await request.body())


@APP.middleware("http")
async def log_response(request: Request, call_next) -> Response:
    """
    Log response status code and body
    """
    response = await call_next(request)
    body = b""
    async for chunk in response.body_iterator:
        body += chunk

    logger.info(f"{response.status_code} {body}")

    return Response(
        content=body, status_code=response.status_code, headers=dict(response.headers), media_type=response.media_type
    )


# Add routes from resources
for resource in RESOURCES:
    API_ROUTER.add_api_route(
        f"/api{resource.route}",
        resource.endpoint,
        description=resource.description,
        summary=resource.summary,
        methods=[resource.method],
        responses=resource.doc,
    )

APP.include_router(API_ROUTER, dependencies=[Depends(log_request)])
