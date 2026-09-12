import os
import uuid

import boto3
from dotenv import load_dotenv
from fastapi import UploadFile

load_dotenv()

MINIO_ENDPOINT = os.getenv("MINIO_ENDPOINT")
MINIO_ACCESS_KEY= os.getenv("MINIO_ACCESS_KEY")
MINIO_SECRET_KEY = os.getenv("MINIO_SECRET_KEY")
MINIO_BUCKET = os.getenv("MINIO_BUCKET")
MINIO_PUBLIC_URL = os.getenv("MINIO_PUBLIC_URL")

s3_client = boto3.client(
    "s3",
    endpoint_url=MINIO_ENDPOINT,
    aws_access_key_id=MINIO_ACCESS_KEY,
    aws_secret_access_key=MINIO_SECRET_KEY,
    config=boto3.session.Config(s3={"addressing_style": "path"}),
)



def upload_image(file: UploadFile, folder: str) -> str:
    extension = file.filename.rsplit(".",1)[-1] if "." in file.filename else "bin"
    object_key = f"{folder}/{uuid.uuid4()}.{extension}"

    s3_client.upload_fileobj(
        file.file,
        MINIO_BUCKET,
        object_key,
        ExtraArgs={"ContentType": file.content_type},
    )

    return f"{MINIO_PUBLIC_URL}/{MINIO_BUCKET}/{object_key}"