from fastapi import FastAPI
from routers import api_router

from atleta.models import AtletaModel
from categorias.models import CategoriaModel
from centro_treinamento.models import CentroTreinamentoModel

app = FastAPI(title = "WorkoutApi", openapi_url="/workoutapi/v1/openapi.json")
app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host = "0.0.0.0", port = 8000, log_level = "info", reload = True)