from utils.custom_types import *
from utils.settings import settings
import utils.accounts as accounts
import opened
import closed
import api_utils
import ui

app = FastAPI(debug=True, docs_url="/ds", redoc_url="")

app.mount("/static", StaticFiles(directory="html/static"), name="static")

app.include_router(opened.router)
app.include_router(closed.router)
app.include_router(api_utils.router)
app.include_router(ui.router)

@app.get("/", response_class=PrettyJSONResponse, tags=["default"])
async def index():
    return {"response": "Эта страница не подходит для запросов."}

@app.exception_handler(HTTPException)
async def exception(request: Request, e: HTTPException):
    return PrettyJSONResponse(status_code=e.status_code, content={"error_code": e.status_code, "error": e.detail})

if __name__ == "__main__":
    os.system("uvicorn main:app --reload --host 0.0.0.0 --port 5000")