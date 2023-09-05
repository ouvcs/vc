from utils.custom_types import *
from utils.settings import settings
import utils.accounts as accounts

async def check_token(token: str = ""):
    if token != settings.api_key:
        raise HTTPException(status_code=403, detail="Неверный токен.")

router = APIRouter(prefix="/sapi", tags=["sapi"], dependencies=[Depends(check_token)])

@router.get("/country/", response_class=PrettyJSONResponse)
async def sapi_country(id: str = "", cid: str = "", flag: str = "", name: str = "", group: str = "", goverment_type: str = "", goverment_form: str = "", ideology: str = "", political_type: str = "", desc: str = "", dates: str = "", hash: str = ""):
    if id == "" or cid == "" or flag == "" or name == "" or group == "" or goverment_type == "" or goverment_form == "" or ideology == "" or political_type == "" or dates == "":
        raise HTTPException(status_code=400, detail="Неверные параметры.")
    if hashlib.md5((id+cid+flag+name+group+goverment_type+goverment_form+ideology+political_type+dates+settings.vk_admin).encode()).hexdigest() != hash:
        raise HTTPException(status_code=403, detail="Неверный хеш.")
    
    user = accounts.User(id, registration=True, need_vk=True)
    
    user.account["id"] = id
    user.account["cid"] = cid
    user.account["moderation"] = True
    
    user.country["flag"] = flag
    user.country["name"] = name
    user.country["group"] = group
    user.country["goverment_type"] = goverment_type
    user.country["goverment_form"] = goverment_form
    user.country["ideology"] = ideology
    user.country["political_type"] = political_type
    user.country["desc"] = desc
    user.country["date"] = date(int(dates.split(".")[2]), int(dates.split(".")[1]), int(dates.split(".")[0]))
    
    return user.write().to_json()

@router.get("/valute/", response_class=PrettyJSONResponse)
async def sapi_valute(id: str = "", vid: str = "", photo: str = "", name: str = "", desc: str = "", change: str = "", abbreviation: str = "", symbol: str = "", hash: str = ""):
    if id == "" or vid == "" or name == "" or photo == "" or name == "" or desc == "" or change == "" or abbreviation == "" or symbol == "":
        raise HTTPException(status_code=400, detail="Неверные параметры.")
    if hashlib.md5((id+vid+photo+name+change+abbreviation+symbol+settings.vk_admin).encode()).hexdigest() != hash:
        raise HTTPException(status_code=403, detail="Неверный хеш.")
    
    user = accounts.User(id, need_vk=True)
    if user.account["id"] != "000000000":
        user.account.vid = vid
        user.account.moderation = True
        
        user.valute.id = id
        user.valute.vid = vid
        user.valute.photo = photo
        user.valute.name = name
        user.valute.desc = desc
        user.valute.change = float(change)
        user.valute.abbreviation = abbreviation
        user.valute.symbol = symbol

        return user.write().to_json()
    else:
        raise HTTPException(status_code=403, detail="неверный аккаунт.")
    

@router.get("/admin/{command}")
async def sapi_admin(command: str = "", key: str = "", value: str = "", id: str = "", admin_token: str = "", redirect: str = ""):
    if admin_token == settings.api_admin:
        if command != "" and key != "" and value != "" and id != "":
            if key in ["flag", "name", "group", "goverment_type", "goverment_form", "ideology", "political_type" ,"desc", "date", "photo", "change", "abbreviation", "symbol", "id", "cid", "vid"]:
                raise HTTPException(status_code=400, detail="Неверные параметры.")
            else:
                account = accounts.User(id)
                if command == "country":
                    account.country[key] = str(value)
                elif command == "valute":
                    account.valute[key] = str(value)
                elif command == "account":
                    if key == "moderation" or key == "banned" or key == "admin":
                        account.account[key] = value == "true"
                    else:
                        account.account[key] = str(value)
                        
                account.write()
                
                if redirect != "":
                    return RedirectResponse(url=redirect, status_code=302)
                else:
                    return PrettyJSONResponse(status_code=200, content=account.to_json())
        else:
            raise HTTPException(status_code=400, detail="Неверные параметры.")
    else:
        raise HTTPException(status_code=403, detail="Неверный админ-код.")
    

        
