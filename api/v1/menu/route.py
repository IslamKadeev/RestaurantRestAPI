from fastapi import APIRouter


router = APIRouter(
    prefix="api/v1/menus",
    tags=["Menus CRUD"]
)


@router.get("/")
def get_menus():
    return
