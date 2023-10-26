import datetime

from app.tasks.models import Task as Task_model
from fastapi import APIRouter, HTTPException, BackgroundTasks, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_async_session
from app.deferred_tasks.schema import EmailSchemaAdmin, EmailSchemaTask, TestSchema
from app.deferred_tasks.tasks import sending_message

router = APIRouter(
    prefix="/deferred_tasks",
    tags=["deferred_tasks"]
)


# mail

@router.post('/mail/send')
async def admin_send(email: EmailSchemaAdmin, background_tasks: BackgroundTasks):
    try:
        email = email.dict().get("email")
        html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        *{
            font-family: Arial, Helvetica, sans-serif;
        }
        body{
            padding: 30px;
            background-color: #1B1D2C;
            color: #FFFFFF;
        }
        a{
            color: #D35077 !important;
            text-decoration: underline;
            font-size: 20px;
        }
        p{
            font-size: 20px;
        }
    </style>
</head>
<body>

    <h1>Здравствуйте!</h1>
    <h2>Вы были зарегистрированы на сервисе командной работы</h2>
    <p>Вы можете <a href="http://90.156.210.55/me">перейти по этой ссылке</a>, чтобы узнать подробнее</p>
</body>
</html>
        '''
        background_tasks.add_task(sending_message, email, html)
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


@router.post('/mail/getting_a_task')
async def getting_a_task(email: EmailSchemaTask, background_tasks: BackgroundTasks):
    try:
        html = f'''
        <h1>Вам присвоили задание: {email.dict().get('name_task')}</h1>
        <p></p>
        <h3>Вы можете посмотреть её в личном кабинете: (будущая ссылка)</h3>
        '''
        background_tasks.add_task(sending_message, email.dict().get("email"), html)
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


# report

@router.post("/report")
async def report(session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(Task_model)
        result = await session.execute(query)
        result = result.scalars().all()

        all_tasks = len(result)

        # status
        success = len([i.status for i in result if i.status == 'success'])
        in_progress = len([i.status for i in result if i.status == 'in_progress'])
        not_started = len([i.status for i in result if i.status == 'not_started'])

        # weight
        average_weight = round(sum([i.weight for i in result]) / len([i.weight for i in result]), 2)

        # category
        category_dictionary = dict.fromkeys([i.category.lower() for i in result], 0)
        for word in [i.category.lower() for i in result]:
            if word in category_dictionary:
                category_dictionary[word] += 1
            else:
                category_dictionary[word] = 1
        most_common_category = max(category_dictionary, key=category_dictionary.get)

        # priority
        priority_dictionary = dict.fromkeys([i.priority.lower() for i in result], 0)
        for word in [i.priority.lower() for i in result]:
            if word in priority_dictionary:
                priority_dictionary[word] += 1
            else:
                priority_dictionary[word] = 1
        most_common_priority = max(priority_dictionary, key=priority_dictionary.get)

        data = {
            'success': success,
            'in_progress': in_progress,
            'not_started': not_started,
            'average_weight': average_weight,
            'most_common_category': most_common_category,
            'most_common_priority': most_common_priority,
            'all': {
                'count': all_tasks,
                'data': result
            }
        }
        return data
    except Exception:
        raise HTTPException(status_code=503, detail={
            "status": "error",
            "data": Exception,
            "details": "the report is not generated"
        })


@router.post("/report/date")
async def report_date(date: datetime.date, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(Task_model).where(Task_model.begin == date)
        result = await session.execute(query)
        result = result.scalars().all()

        all_tasks = len(result)

        # status
        success = len([i.status for i in result if i.status == 'success'])
        in_progress = len([i.status for i in result if i.status == 'in_progress'])
        not_started = len([i.status for i in result if i.status == 'not_started'])

        # weight
        average_weight = round(sum([i.weight for i in result]) / len([i.weight for i in result]), 2)

        # category
        category_dictionary = dict.fromkeys([i.category.lower() for i in result], 0)
        for word in [i.category.lower() for i in result]:
            if word in category_dictionary:
                category_dictionary[word] += 1
            else:
                category_dictionary[word] = 1
        most_common_category = max(category_dictionary, key=category_dictionary.get)

        # priority
        priority_dictionary = dict.fromkeys([i.priority.lower() for i in result], 0)
        for word in [i.priority.lower() for i in result]:
            if word in priority_dictionary:
                priority_dictionary[word] += 1
            else:
                priority_dictionary[word] = 1
        most_common_priority = max(priority_dictionary, key=priority_dictionary.get)

        data = {
            'success': success,
            'in_progress': in_progress,
            'not_started': not_started,
            'average_weight': average_weight,
            'most_common_category': most_common_category,
            'most_common_priority': most_common_priority,
            'all': {
                'count': all_tasks,
                'data': result
            }
        }
        return data
    except Exception:
        raise HTTPException(status_code=503, detail={
            "status": "error",
            "data": None,
            "details": "the report is not generated"
        })


@router.post("/report/date/count")
async def report_date(date: datetime.date, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(Task_model).where(Task_model.begin == date)
        result = await session.execute(query)
        result = result.scalars().all()

        all_tasks = len(result)

        return all_tasks
    except Exception:
        raise HTTPException(status_code=503, detail={
            "status": "error",
            "data": None,
            "details": "the report is not generated"
        })


@router.post("/deadline")
async def deadline(background_tasks: BackgroundTasks, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(Task_model).where(Task_model.status == 'in_progress')
        result = await session.execute(query)
        result = result.scalars().all()

        ls1 = [TestSchema(email=i.users) for i in result if (i.end - i.begin) == datetime.timedelta(seconds=86400)]
        ls_mail1 = [i.dict().get("email") for i in ls1]
        html1 = '''
                <h1>До дедлайна остался один день!</h1>
                <p></p>
                <h3>Посмотрите свои задачи в личном кабинете: <a href="http://90.156.210.55/me">Твои задачи!</a></h3>
                '''

        ls7 = [TestSchema(email=i.users) for i in result if (i.end - i.begin) == datetime.timedelta(seconds=604800)]
        ls_mail7 = [i.dict().get("email") for i in ls7]
        html7 = '''
                <h1>До дедлайна осталась неделя! </h1>
                <p></p>
                <h3>Посмотрите свои задачи в личном кабинете: <a href="http://90.156.210.55/me">Твои задачи!</a></h3>
                '''

        ls10 = [TestSchema(email=i.users) for i in result if (i.end - i.begin) == datetime.timedelta(seconds=864000)]
        ls_mail10 = [i.dict().get("email") for i in ls10]
        html10 = '''
                <h1>До дедлайна осталось десять дней! </h1>
                <p></p>
                <h3>Посмотрите свои задачи в личном кабинете: <a href="http://90.156.210.55/me">Твои задачи!</a></h3>
                 '''

        background_tasks.add_task(sending_message, ls_mail1, html1)
        background_tasks.add_task(sending_message, ls_mail7, html7)
        background_tasks.add_task(sending_message, ls_mail10, html10)
        return {
            "status": "success",
            "data": None,
            "details": "message sent"
        }

    except Exception:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": Exception,
            "details": "message not sent"
        })
