from fastapi import UploadFile, File
from base_repository import save_file

async def process_file(file_name:str, uploaded_by, description:str, file_type:str, file: UploadFile = File(...)):
    return await save_file(file_name=file_name, file_type_extension = file_type, description=description, uploaded_by=uploaded_by, file=file)
    