from utils.custom_types import *
from utils.settings import settings
import utils.accounts as accounts

router = APIRouter(tags=["default"])

@router.get("/admin/", response_class=HTMLResponse)
async def admin():
    with open("html/admin.html", "r", encoding="utf8") as f:
        return HTMLResponse(f.read())