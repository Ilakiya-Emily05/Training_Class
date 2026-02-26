import time
import logging
from fastapi import Request

logger = logging.getLogger("app")

async def logging_middleware(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    process_time = round(time.time() - start_time, 4)

    logger.info(
        f"{request.method} {request.url.path} "
        f"- {response.status_code} "
        f"- {process_time}s"
    )

    return response