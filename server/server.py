from fastapi import FastAPI, Request, Body
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from database import *

 
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Hello, World!"})

@app.post('/search')
async def search(data = Body()):
    print(data['search'])
    vacancy_id = db_get_vacancy_id(data['search'])
    vacancy_info = db_get_vacancy_info(vacancy_id)
    print(vacancy_info)
    return {'vacancy_info': vacancy_info, 'vacancy_name': data['search']}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)

