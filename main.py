from fastapi import FastAPI, Request, Depends, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from models import Item
from database import engine, SessionLocal
from crud import get_items, create_item, update_item, delete_item

app = FastAPI()

# Создаем таблицы
Item.metadata.create_all(bind=engine)

# Настройка шаблонов и статических файлов
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def read_items(request: Request, db: Session = Depends(get_db)):
    items = get_items(db)
    return templates.TemplateResponse("index.html", {"request": request, "items": items})

@app.post("/items/")
async def create_item_post(
    request: Request,
    name: str = Form(...),
    description: str = Form(...),
    db: Session = Depends(get_db)
):
    create_item(db, {"name": name, "description": description})
    items = get_items(db)
    return templates.TemplateResponse("index.html", {"request": request, "items": items})

@app.post("/items/{item_id}/delete")
async def delete_item_post(
    request: Request,
    item_id: int,
    db: Session = Depends(get_db)
):
    delete_item(db, item_id)
    items = get_items(db)
    return templates.TemplateResponse("index.html", {"request": request, "items": items})
