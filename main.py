import opened
import closed
import api_utils
from api_utils import *
from api_utils import settings as settings
import ui

app = FastAPI(debug=True, docs_url="/ds", redoc_url="",             
    title="OUVC API",
    version="0.1",
    contact={
        "name": "Matvey Buldakov",
        "url": "https://vk.com/write541161804",
        "email": "m.buldakvo10min@gmail.com",
    },
    license_info={
        "name": "MIT License",
        "identifier": "MIT",
    }
)

app.mount("/static", StaticFiles(directory="html/static"), name="static")

app.include_router(opened.router)
app.include_router(closed.router)
app.include_router(api_utils.router)
app.include_router(ui.router)

@app.get("/", response_class=PrettyJSONResponse, tags=["default"])
@app.head("/", response_class=PrettyJSONResponse, tags=["default"])
async def index():
    return {"response": "Эта страница не подходит для запросов."}

@app.exception_handler(HTTPException)
async def exception(request: Request, e: HTTPException):
    return PrettyJSONResponse(status_code=e.status_code, content={"error_code": e.status_code, "error": e.detail})

if __name__ == "__main__":
    os.system("uvicorn main:app --reload --host 0.0.0.0 --port 5000")