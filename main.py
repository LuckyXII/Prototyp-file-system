from fastapi import FastAPI, HTTPException, File, UploadFile
import uvicorn
from file_processor import process_file
from base_repository import init, save_file, get_files, delete_files
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


@app.on_event('startup')
async def startup_event():
    app.add_middleware(
        CORSMiddleware,
        allow_origins='*',
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )
    init(app)

@app.get('/files')
async def files():
    try:
        files = await get_files()    
    except Exception as e:
        raise HTTPException(status_code=500, detail= e)
    finally:
        if not files : 
            raise HTTPException(status_code=404, detail='no files found')
        return files
        
        

@app.post("/file/{file_name}/{uploaded_by}/{description}/{file_type}")
async def upload_file(file_name:str, uploaded_by:str, description:str,file_type:str, file: UploadFile = File(...)):
    try:
        await process_file(file_name=file_name, uploaded_by=uploaded_by, description=description, file_type=file_type, file=file)
    except Exception as e:
        raise HTTPException(status_code=500, detail= e)
    finally: return 'Success!'


@app.delete('/file/{file_name}/{file_type_extension}')
async def delete_file(file_name, file_type_extension):
    try:
       delete_count = await delete_file(file_name=file_name, file_type_extension=file_type_extension)
    except Exception as e:
        raise HTTPException(status_code=500, detail= e)
    finally:
        if delete_count == 0: 
            raise HTTPException(
                status_code=404, 
                detail=f"Filename: {file_name} with Extension: {file_type_extension} not found for deletion"
            )
        return f'deleted {delete_count} files'

@app.delete('/file/{file_name}')
async def delete_file(file_name, file_type_extension):
    try:
       delete_count = await delete_file(file_name=file_name)
    except Exception as e:
        raise HTTPException(status_code=500, detail= e)
    finally:
        if delete_count == 0: 
            raise HTTPException(
                status_code=404, 
                detail=f"Filename: {file_name} not found for deletion"
            )
        return f'deleted {delete_count} files'

@app.delete('/file')
async def delete_file():
    try:
       delete_count = await delete_file()
    except Exception as e:
        raise HTTPException(status_code=500, detail= e)
    finally:
        if delete_count == 0: 
            raise HTTPException(
                status_code=404, 
                detail=f"No files found for deletion"
            )
        return f'deleted {delete_count} files'


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000, log_level='debug')