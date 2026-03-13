import os
import uuid
from fastapi import UploadFile
from app.config.settings import settings


def generate_unique_filename(filename: str):

    ext = filename.split(".")[-1]
    unique_name = f"{uuid.uuid4()}.{ext}"

    return unique_name


async def save_upload_file(upload_file: UploadFile, upload_dir: str):

    os.makedirs(upload_dir, exist_ok=True)

    filename = generate_unique_filename(upload_file.filename)

    file_path = os.path.join(upload_dir, filename)

    with open(file_path, "wb") as buffer:
        buffer.write(await upload_file.read())

    return file_path


def delete_file(file_path: str):

    if os.path.exists(file_path):
        os.remove(file_path)