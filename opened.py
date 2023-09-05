from api_utils import *

router = APIRouter(prefix="/api", tags=["api"])

@router.get("/countries/", response_class=PrettyJSONResponse)
async def api_countries(search: str = ""):
    response = []
    for id in os.listdir("./accounts/"):
        account = accounts.User(id)
        if account.account["moderation"] or account.account["banned"]:
            continue
        
        if search == "":
            response.append(account.country)
        else:
            search = search.lower()
            searches = [0]
            for v in account.country.values():
                if isinstance(v, Enum):
                    searches.append(WRatio(v.value.lower(), search))
                else:
                    searches.append(WRatio(str(v).lower(), search))
                    
            if max(searches) >= 80:
                response.append(account.country)
                
    return {"response": response}

@router.get("/country/", response_class=PrettyJSONResponse)
async def api_country(id: str = "", preview: bool = False):
    response = accounts.User(id)
    
    if response.country["id"] == "000000000":
        raise HTTPException(status_code=404, detail="Страна не найдена.")
    if response.account["moderation"] and not preview:
        raise HTTPException(status_code=404, detail="Страна на модерации.")
    if response.account["banned"] and not preview:
        raise HTTPException(status_code=404, detail="Страна в бане.")
    
    return response.country


@router.get("/valutes/", response_class=PrettyJSONResponse)
async def api_valutes(search: str = ""):
    response = []
    for id in os.listdir("./accounts/"):
        account = accounts.User(id)
        if account.account["moderation"] or account.account["banned"]:
            continue
        
        if search == "":
            response.append(account.valute)
        else:
            search = search.lower()
            searches = [0]
            for v in account.valute.values():
                if isinstance(v, Enum):
                    searches.append(WRatio(v.value.lower(), search))
                else:
                    searches.append(WRatio(str(v).lower(), search))
                    
            if max(searches) >= 80:
                response.append(account.valute)
                
    return {"response": response}

@router.get("/valute/", response_class=PrettyJSONResponse)
async def api_valute(id: str = "", preview: bool = False):
    response = accounts.User(id)
    
    if response.valute["id"] == "000000000":
        raise HTTPException(status_code=404, detail="Валюта не найдена.")
    if response.account["moderation"] and not preview:
        raise HTTPException(status_code=404, detail="Валюта на модерации.")
    if response.account["banned"] and not preview:
        raise HTTPException(status_code=404, detail="Валюта в бане.")
    
    return response.valute

@router.get("/account/", response_class=PrettyJSONResponse)
async def api_account(id: str = ""):
    response = accounts.User(id, need_vk=True)
    
    if response.account["id"] == "000000000":
        raise HTTPException(status_code=404, detail="Аккаунт не найден.")
    
    return response.to_json()