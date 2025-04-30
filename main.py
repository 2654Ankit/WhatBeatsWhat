from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.api import router
from app.database import Base
from app.api import game_data

from app.database import Base,engine
Base.metadata.create_all(bind=engine)


app = FastAPI()
templates = Jinja2Templates(directory='templates')

app.include_router(router)

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    user_id = request.client.host
    if user_id in game_data:
        history = game_data[user_id].history()
        seed = history[-1] if history else 'Rock'
    else:
        seed = 'Rock'
    
    return templates.TemplateResponse('home.html', {'request': request, 'seed': seed})
