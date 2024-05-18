from fastapi import APIRouter

router = APIRouter(
    prefix="/restaurants",
    tags=["Restaurants"],
    responses={404: {"description": "Not found"}},
)

@router.get("/hello")
def hello():
    return "hello wold"
