from fastapi import FastAPI, UploadFile
import uvicorn

from get_data.upload_csv import load_csv


app = FastAPI()

@app.get("/")
def hello():
    return {"message":"Hello"}



@app.post("/assignWithCsv/")
def upload_csv(file: UploadFile):
    load_csv(file)









if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)