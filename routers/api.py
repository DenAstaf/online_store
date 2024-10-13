from fastapi import APIRouter, HTTPException
from fastapi.templating import Jinja2Templates
from model_db import read_csv, write_csv
from validation import DataValidation, IdValidation


router = APIRouter(prefix='/api', tags=['Взаимодействие с товарами (API)'])

# Шаблонизатор, указывает директорию для шаблонов
templates = Jinja2Templates(directory="templates")


# маршрут для добавления товара через API
@router.post("/add-product", description='Добавление новой записи')
async def add_product(type_catalog: str, name: str, price: int):
    list_products = read_csv()  # Лист, содержащий словари с данными всех товаров
    new_id = max(int(product['id']) for product in list_products) + 1  # Получает следующий id
    new_row = DataValidation(id=new_id, type_catalog=type_catalog, name=name, price=price)  # Валидация query параметров, правила прописаны в validation.py
    list_products.append(new_row.model_dump())  # Добавляет новые данные в общий список, model_dump() переводит new_row в формат словаря
    write_csv(list_products)
    return f"Запись успешно добавлена! {new_row}"


# маршрут для удаления товара через API
@router.delete("/delete-product", description='Удаление новой записи')
async def delete_product(id_product: int):
    list_products = read_csv()  # Лист, содержащий словари с данными всех товаров
    validation_id_product = IdValidation(id=id_product)  # Валидация query параметра, правила прописаны в validation.py
    dict_product = next((product for product in list_products if int(product['id']) == validation_id_product.model_dump()['id']), None)  # Словарь с данными одного товара
    if not dict_product:
        raise HTTPException(status_code=404, detail="Id Product not found")
    new_product = [product for product in list_products if int(product['id']) != validation_id_product.model_dump()['id']]  # Обновленный список с данными
    write_csv(new_product)
    return f"Запись успешно удалена! {dict_product}"
