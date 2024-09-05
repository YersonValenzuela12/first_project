from fastapi import FastAPI

#instanciamos la clase FastAPI
app = FastAPI()

@app.get("/")
async def root():
    return {"mame": "yerson valenzuela"}

class Post(BaseModel):
    autor: str
    title: str
    content: str

