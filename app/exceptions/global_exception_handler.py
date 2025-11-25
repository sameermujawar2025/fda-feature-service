# app/exceptions/global_exception_handler.py
from fastapi import Request
from fastapi.responses import JSONResponse

async def global_exception_handler(request: Request, exc: Exception):
    """
    Catches ANY unhandled exception across the entire app.
    Logs it and returns a clean JSON response.
    """
    print(f"🔥 Feature-Service ERROR: {exc}")

    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal Server Error",
            "details": str(exc)
        }
    )
