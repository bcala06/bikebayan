from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.settings import settings
from app.api import health

app = FastAPI(title=settings.PROJECT_NAME)

# CORS config for future
# update allow_origins with frontend URL once deployed (e.g., ["https://mywebapp.com"])
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Change this in production!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(health.router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Hello world!"}
