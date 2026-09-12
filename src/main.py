import uvicorn

from application import settings

if __name__ == "__main__":
    uvicorn.run(settings.FAST_API_PATH)
