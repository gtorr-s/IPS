import os, shutil
from fastapi import UploadFile, HTTPException

UPLOAD_DIR = "images"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def save_image(file: UploadFile, image_id: str):
    ext = file.filename.split(".")[-1]
    filename = f"{image_id}.{ext}"
    path = os.path.join(UPLOAD_DIR, filename)
    try:
        with open(path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao salvar imagem: {e}")
    return filename

def get_image_path(filename: str):
    path = os.path.join(UPLOAD_DIR, filename)
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Imagem não encontrada")
    return path

def list_user_images():
    try:
        return {"images": os.listdir(UPLOAD_DIR)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao listar imagens: {e}")


# Versão futura (comentada) com S3
"""
import boto3
from utils import config

s3 = boto3.client(
    "s3",
    aws_access_key_id=config.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY,
    region_name=config.AWS_REGION
)

def save_image(file: UploadFile, image_id: str):
    ext = file.filename.split(".")[-1]
    filename = f"{image_id}.{ext}"
    s3.upload_fileobj(
        file.file,
        config.S3_BUCKET_NAME,
        filename,
        ExtraArgs={"ContentType": file.content_type, "ACL": "public-read"}
    )
    return filename

def get_image_path(filename: str):
    return f"https://{config.S3_BUCKET_NAME}.s3.{config.AWS_REGION}.amazonaws.com/{filename}"

def list_user_images():
    response = s3.list_objects_v2(Bucket=config.S3_BUCKET_NAME)
    files = [
        f"https://{config.S3_BUCKET_NAME}.s3.{config.AWS_REGION}.amazonaws.com/{obj['Key']}"
        for obj in response.get("Contents", [])
    ]
    return {"images": files}
"""