from utils.custom_types import *
from utils.settings import settings
import utils.accounts as accounts

router = APIRouter(prefix="/utils", tags=["utils"])

@router.get("/id/{id}", response_class=PrettyJSONResponse)
async def utils_account(id: str):
    response = accounts.User(id)
    
    if response.account["id"] == "000000000":
        raise HTTPException(status_code=404, detail="Аккаунт не найден.")
    
    return {"response": response.account["id"]}

@router.get("/checklink/", response_class=PrettyJSONResponse)
async def utils_checklink(link: str):
    response = str(requests.get(request.args.get("link")).status_code)

    return {"response": response}