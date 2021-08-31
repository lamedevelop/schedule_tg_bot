from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from DbManager import DbManager

app = FastAPI()
templates = Jinja2Templates(directory="static")
dbManager = DbManager()


# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


@app.on_event("startup")
async def startup():
    pass


@app.get("/user/register")
async def root(
        id,
        first_name,
        last_name,
        username,
        photo_url,
        auth_date,
        request: Request
):
    # http://127.0.0.1:8000/user/register?tg_id=1&university=МЭИ&group=а-06м-20
    res = dbManager.getLoginRequestByClient(request.client.host)
    res['id'] = id
    res['first_name'] = first_name
    res['last_name'] = last_name
    res['username'] = username
    res['photo_url'] = photo_url
    res['auth_date'] = auth_date

    dbManager.dropLoginRequest(res['request_id'])

    return res


@app.get("/tg")
async def tg_test(university: str, group: str, request: Request):
    university = dbManager.getUniversityByName(university[1:])
    university_id = university['university_id']

    group = dbManager.getGroup({
        'group_name': group,
        'university_id': university_id
    })
    group_id = group['group_id']

    dbManager.setLoginRequest(
        {
            'university_id': university_id,
            'group_id': group_id,
            'client_ip': request.client.host
        }
    )

    return templates.TemplateResponse("register.html", {"request": request})
