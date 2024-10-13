from fastapi import APIRouter, Request, HTTPException, Path
from fastapi.responses import HTMLResponse
from typing import Annotated
from fastapi.templating import Jinja2Templates
from model_db import read_csv

router = APIRouter(prefix='', tags=['Получение информации (GUI)'])

# Шаблонизатор, указывает директорию для шаблонов
templates = Jinja2Templates(directory="templates")


# маршрут для получения инфо о всех товарах
@router.get("/", response_class=HTMLResponse)
async def show_all_products(request: Request):
    list_products = read_csv()  # Лист, содержащий словари с данными о всех товарах
    context = {
        "request": request,
        "info_products": list_products
    }
    return templates.TemplateResponse("index.html", context)


# маршрут для получения инфо о конкретном товаре по id
@router.get("/product/{id_product}", response_class=HTMLResponse)
async def show_one_product(request: Request, id_product: Annotated[int, Path(gt=0)]):
    list_products = read_csv()  # Лист, содержащий словари с данными о всех товарах
    dict_product = next((product for product in list_products if int(product['id']) == id_product), 0)  # Словарь с данными одного студента
    if int(dict_product['id']) == 0:
        raise HTTPException(status_code=404, detail="Product not found")

    context = {
        "request": request,
        "id_product": id_product,
        "info_product": dict_product
    }
    return templates.TemplateResponse("product.html", context)


# маршрут для получения инфо о всех шариковых ручках
@router.get("/pens", response_class=HTMLResponse)
async def show_all_products(request: Request):
    list_products = read_csv("Шариковые ручки")  # Лист, содержащий словари с данными о всех товарах
    context = {
        "request": request,
        "info_products": list_products
    }
    return templates.TemplateResponse("pens.html", context)


# маршрут для получения инфо о всех цветных карандашах
@router.get("/color-pencils", response_class=HTMLResponse)
async def show_all_products(request: Request):
    list_products = read_csv("Цветные карандаши")  # Лист, содержащий словари с данными о всех товарах
    context = {
        "request": request,
        "info_products": list_products
    }
    return templates.TemplateResponse("color-pencils.html", context)


# маршрут для получения данных со страницы about
@router.get("/about", response_class=HTMLResponse)
async def show_about(request: Request):
    context = {
        "request": request
    }
    return templates.TemplateResponse("about.html", context)
