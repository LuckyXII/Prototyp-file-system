from datetime import datetime
from config import SQLITE_URL
from models import File
from tortoise.query_utils import Q
from tortoise.contrib.fastapi import register_tortoise


def init(app):
    register_tortoise(
        app,
        db_url=SQLITE_URL,
        modules={'models': ['models']},
        generate_schemas=True,
        add_exception_handlers=True,
    )

async def save_file(file_name:str, file_type_extension:str, description:str, uploaded_by:str, file):
    return await File.create(
        file_name = file_name, 
        file_type_extension = file_type_extension, 
        description = description, 
        uploaded_by = uploaded_by, 
        uploaded_at = datetime.utcnow(),
        file = file
    )

async def get_files():
    files = await File.all()
    return list(files)

async def delete_files(file_name, file_type_extension):
    if file_name and file_type_extension:
        return await File.filter(Q(file_name = file_name) & Q(file_type_extension = file_type_extension)).delete()
    elif file_name and not file_type_extension :
        return await File.filter(file_name = file_name).delete()
    else:
        return await File.all().delete()


async def get_file_by_name(file_name:str):
    file = await File.filter(file_name=file_name)
    return file

