from datetime import datetime
from core.config import SQLITE_URL
from models.models import File
from tortoise.contrib.fastapi import register_tortoise


def init(app):
    register_tortoise(
        app,
        db_url=SQLITE_URL,
        modules={'models': ['models.models']},
        generate_schemas=True,
        add_exception_handlers=True,
    )

async def save_file(file_name:str, description:str, uploaded_by:str ):
    await File.create(
        file_name = file_name, 
        file_name_extension = file_name_extension, # derive from fileName
        description = description, 
        uploaded_by = uploaded_by, 
        uploaded_at = datetime.utcnow()
    )

async def get_files():
    files = await File.all()
    return list(files)

async def get_file_by_name(file_name:str):
    file = await File.filter(file_name=file_name)
    return list(file)

