from fastapi import FastAPI, HTTPException, File, UploadFile
import uvicorn
from core.file_processor import process_file
from db.base_repository import init, save_file, get_files


app = FastAPI()


@app.on_event("startup")
async def startup_event():
    init(app)

@app.get("/files")
async def get_files():
    try:
        files = await get_files()    
    except Exception as e:
        raise HTTPException(status_code=500, detail= e)
    finally:
        if files is None: 
            raise HTTPException(status_code=404, detail="no files found")
        return files
        
        

@app.post("/file/{file_name}/{uploaded_by}/{description}")
async def upload_file(file: UploadFile = File(...)):
    try:
        await process_file(
            file_name=file.filename,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail= e)
    finally: return 'Success!'


@app.delete("/file/{file_name}")
async def delete_file(file_name):
    try:
       pass
    except Exception as e:
        raise HTTPException(status_code=500, detail= e)
    finally:
        pass     

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
