from fastapi import UploadFile, File

async def process_file(file_name:str,file_type_extension, file: UploadFile = File(...)):
    content = await file.read()
