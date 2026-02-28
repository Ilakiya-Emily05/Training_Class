from fastapi import Query
from app.core.config import get_settings

settings = get_settings()


def pagination_params(
    page: int = Query(1, ge=1),
    size: int = Query(settings.DEFAULT_PAGE_SIZE, ge=1, le=settings.MAX_PAGE_SIZE),
):
    offset = (page - 1) * size
    return {"limit": size, "offset": offset}