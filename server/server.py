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
    await top10()
    await vacancies5()
    return templates.TemplateResponse("index.html", {"request": request, "message": "Hello, World!"})

@app.post('/search')
async def search(data = Body()):
    print(data['search'])
    vacancy_id = db_get_vacancy_id(data['search'])
    vacancy_info = db_get_vacancy_info(vacancy_id)
    print(vacancy_info)
    return {'vacancy_info': vacancy_info, 'vacancy_name': data['search']}

@app.get('/top10')
async def top10():
    vacancySkillsTop10 = db_get_vacancy_skills_top10()
    print(vacancySkillsTop10)
    return {'vacancySkillsTop10': vacancySkillsTop10}

@app.get('/vacancies5')
async def vacancies5():
    vacanciesTop5 = db_get_vacancy_top5(id)
    print(vacanciesTop5)
    return {'vacanciesTop5': vacanciesTop5}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)

