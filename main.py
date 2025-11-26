from fastapi import FastAPI, UploadFile
import uvicorn
from dal.reset_db import initialize_scheme
from get_data.upload_csv import load_csv


app = FastAPI()

@app.post("/assignWithCsv/")
def soldier_insert(file: UploadFile):
    data = load_csv(file)
    return data


@app.get("/initializeScheme/")
def reset_db():
    initialize_scheme()
    return {"message":"Tables have been reinitialized"}








if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)