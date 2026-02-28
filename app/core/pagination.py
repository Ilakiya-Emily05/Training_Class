from fastapi import Query
from typing import Optional


class PaginationParams:
    def __init__(
        self,
        page: int = Query(1, ge=1),
        size: int = Query(20, ge=1, le=100),
        sort_by: Optional[str] = None,
        order: Optional[str] = "asc"
    ):
        self.page = page
        self.size = size
        self.sort_by = sort_by
        self.order = order

    @property
    def offset(self) -> int:
        return (self.page - 1) * self.size