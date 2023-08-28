from custom_types import *
import functions as fn
from functions import Settings
import accounts


app = FastAPI()
settings = Settings()

@app.get("/", response_class=PrettyJSONResponse)
async def index():
    return {"response": "This page is not allowed to request."}

@app.exception_handler(HTTPException)
async def exception(request: Request, e: HTTPException):
    return PrettyJSONResponse(status_code=e.status_code, content={"error": e.detail})


@app.get("/api/countries/", response_class=PrettyJSONResponse)
async def api_countries(search: str = ""):
    response = fn.countries(search)
    
    if "error" in response:
        raise HTTPException(status_code=int(response["error_code"]), detail=str(response["error"]))
    else:
        return {"response": response}

@app.get("/api/country/", response_class=PrettyJSONResponse)
async def api_country(id: str = ""):
    response = fn.country(id)
    
    if "error" in response:
        raise HTTPException(status_code=int(response["error_code"]), detail=str(response["error"]))
    else:
        return {"response": response}


@app.get("/api/valutes/", response_class=PrettyJSONResponse)
async def api_valutes(search: str = ""):
    response = fn.valutes(search)
    
    if "error" in response:
        raise HTTPException(status_code=int(response["error_code"]), detail=str(response["error"]))
    else:
        return {"response": response}

@app.get("/api/valute/", response_class=PrettyJSONResponse)
async def api_valute(id: str = ""):
    response = fn.valute(id)
    
    if "error" in response:
        raise HTTPException(status_code=int(response["error_code"]), detail=str(response["error"]))
    else:
        return {"response": response}


@app.get("/api/geo/", response_class=PrettyJSONResponse)
async def api_geo(id: str = "000000000"):
    if id != "000000000":
        response = fn.country_geo(id)

        if "error" in response:
            raise HTTPException(status_code=int(response["error_code"]), detail=str(response["error"]))
        else:
            return response
    else:
        response = fn.countries_geo()

        if "error" in response:
            raise HTTPException(status_code=int(response["error_code"]), detail=str(response["error"]))
        else:
            return response


@app.get("/api/geo/", response_class=PrettyJSONResponse)
async def api_geo_single(id: str = ""):



@app.get("/api/admin/{command}", response_class=PrettyJSONResponse)
async def api_admin(command: str = "", key: str = "", value: str = "", id: str = "", admin_code: str = ""):
    if admin_code == settings.api_admin:
        return {"response": fn.admin(command, key, value, id)}
    else:
        raise HTTPException(status_code=403, detail="Invalid admin code.")

if __name__ == "__main__":
    os.system("uvicorn main:app --reload")