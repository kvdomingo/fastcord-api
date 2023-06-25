from fastapi import APIRouter

router = APIRouter(prefix="/guild")


@router.get("/")
async def list_users():
    return []
