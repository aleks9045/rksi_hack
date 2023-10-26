from fastapi_mail import FastMail, MessageSchema, MessageType

from app.deferred_tasks.config import conf

async def sending_message(email, html):
    message = MessageSchema(
        subject="Уведомления",
        recipients=email,
        body=html,
        subtype=MessageType.html)

    fm = FastMail(conf)
    await fm.send_message(message)


async def deadline(email, html):
    message = MessageSchema(
        subject="Время подходит к концу!",
        recipients=email,
        body=html,
        subtype=MessageType.html)

    fm = FastMail(conf)
    await fm.send_message(message)
