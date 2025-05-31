from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from auth.routes import router as auth_router
from images.routes import router as image_router
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from utils.rate_limit import limiter

app = FastAPI(title="Image Processing Service")

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(image_router, prefix="/images", tags=["Images"])
