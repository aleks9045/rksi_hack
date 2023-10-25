from fastapi import APIRouter, HTTPException

from app.deferred_tasks.schema import EmailSchema
from app.deferred_tasks.tasks import sending_message

router = APIRouter(
    prefix="/deferred_api",
    tags=["Deferred api"]
)


@router.post('/send_new_admin')
async def send_new_admin(email: EmailSchema):
    try:
        email = email.dict().get("email")
        html = '''
        <h1>Вас добавили в администраторы</h1>
        '''
        await sending_message(email, html)
        return {
            "status": "success",
            "data": None,
            "details": "message sent"
        }
    except Exception:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": "message not sent"
        })
