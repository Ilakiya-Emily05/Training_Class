import time
from fastapi import Request
from fastapi.responses import Response

async def logging_middleware(request: Request, call_next):
    start_time = time.time()
    response: Response = await call_next(request)
    process_time = time.time() - start_time
    print(f"{request.method} {request.url} completed_in={process_time:.2f}s status_code={response.status_code}")
    return response