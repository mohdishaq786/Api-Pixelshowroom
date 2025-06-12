from fastapi import FastAPI
from controller.v1 import image_processing

app = FastAPI(title="Pixelshowroom API")

app.include_router(image_processing.router, prefix="", tags=["ImageProcessing"])
