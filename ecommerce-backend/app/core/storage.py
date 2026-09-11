import os
import uuid


from fastapi import UploadFile

UPLOAD_DIR = "static/uploads"

def upload_image(file: UploadFile, folder: str) -> str:
    extension = file.filename.rsplit(".",1)[-1] if "." in file.filename else "bin"
    filename = f"{uuid.uuid4()}.extension"

    folder_path = os.path.join(UPLOAD_DIR, folder)
    os.makedirs(folder_path, exist_ok=True)

    file_path = os.path.join(folder_path, filename)
    with open(file_path, "wb") as f:
        f.write(file.file.read())

    return f"/static/uploads/{folder}/{filename}"