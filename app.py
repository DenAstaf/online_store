from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers.views import router as view_router
from routers.api import router as api_router


# Создает экземпляр класса FastAPI
app = FastAPI()
# Подключает роутеры
app.include_router(view_router)
app.include_router(api_router)
# Подключает static(js, css)
app.mount("/static", StaticFiles(directory="static"), name="static")
