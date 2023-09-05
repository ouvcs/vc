from api_utils import *

router = APIRouter(tags=["default"])

@router.get("/admin/", response_class=HTMLResponse)
async def admin():
    with open("html/admin.html", "r", encoding="utf8") as f:
        return HTMLResponse(f.read())