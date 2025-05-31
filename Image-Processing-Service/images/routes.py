from fastapi import APIRouter, UploadFile, File, HTTPException, Depends, Query, Request
from fastapi.responses import FileResponse
from auth.routes import get_current_user
from images.storage import save_image, get_image_path, list_user_images
from images.transform import apply_transformations
from utils.rate_limit import limiter
import uuid

router = APIRouter()

@router.post("/")
def upload_image(file: UploadFile = File(...), user: str = Depends(get_current_user)):
    image_id = str(uuid.uuid4())
    path = save_image(file, image_id)
    return {"image_id": image_id, "url": f"/images/{path}"}

@router.post("/{filename}/transform")
@limiter.limit("10/minute")
def transform_image(
    request: Request,
    filename: str,
    resize: str = None,
    grayscale: bool = False,
    rotate: int = 0,
    crop: str = None,
    flip: str = None,
    compress: int = 100,
    format: str = None,
    sepia: bool = False,
    blur: bool = False,
    sharpen: bool = False,
    watermark_text: str = None
):
    path = get_image_path(filename)
    new_path = apply_transformations(
        path,
        resize=resize,
        grayscale=grayscale,
        rotate=rotate,
        crop=crop,
        flip=flip,
        compress=compress,
        format=format,
        sepia=sepia,
        blur=blur,
        sharpen=sharpen,
        watermark_text=watermark_text
    )
    return {"url": f"/images/{new_path}"}

@router.get("/{filename}")
def get_image(filename: str):
    path = get_image_path(filename)
    return FileResponse(path)

@router.get("/")
def list_images(user: str = Depends(get_current_user)):
    return list_user_images()
