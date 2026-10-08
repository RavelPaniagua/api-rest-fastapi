from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.src.routers.route_clientes import router_clientes
from pathlib import Path

DIST_DIR = Path(__file__).resolve().parents[2] / "dist"

app = FastAPI()

app.title = "My FastAPI Application"
app.description = "This is a sample FastAPI"

router_clientes.frontend("/", directory=str(DIST_DIR))

@app.get("/", tags=["Home"], response_class=HTMLResponse)
async def get():
    index_file = DIST_DIR / "index.html"
    return HTMLResponse(content=index_file.read_text(encoding="utf-8"), status_code=200)

app.include_router(router_clientes, tags=["Clientes"])