from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get('/')
async def health():
    try:
        response = {'status': True}
        return response
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))
