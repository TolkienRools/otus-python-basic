from fastapi import APIRouter


router = APIRouter()


@router.get("/ping/",
            response_model=dict)
def hello():
    return {"message": "pong"}