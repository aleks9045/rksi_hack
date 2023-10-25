from fastapi_mail import FastMail, MessageSchema, MessageType
from celery import Celery

from app.deferred_tasks.config import conf


celery = Celery('tasks', broker='redis://redis:6379')


@celery.task
async def sending_message(email, html):
    message = MessageSchema(
        subject="Здраствуйте!",
        recipients=email,
        body=html,
        subtype=MessageType.html)

    fm = FastMail(conf)
    await fm.send_message(message)




