from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from controller.v1 import image_processing
from controller.v1 import image_processing_test_api

app = FastAPI(title="Pixelshowroom API")

#  Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include your image processing router
app.include_router(image_processing.router, prefix="/api/v1", tags=["ImageProcessing"])
app.include_router(image_processing_test_api.router, prefix="/api/v1", tags=["test_api"])