from fastapi import APIRouter, Request, HTTPException, Depends
from fastapi.templating import Jinja2Templates
from curl_fetch2py import CurlFetch2Py
from app.api.schemas import RequestData
from app.api.utils import execute_request

router = APIRouter(prefix='', tags=['API'])
templates = Jinja2Templates(directory='app/templates')


@router.get('/')
async def get_main_page(request: Request):
    return templates.TemplateResponse(name='index.html', context={'request': request})


@router.post('/api', summary='Основной API метод')
async def main_logic(request_body: RequestData):
    request_type = request_body.request_type
    target = request_body.target
    data_str = request_body.data_str

    try:
        if request_type == 'curl':
            context = CurlFetch2Py.parse_curl_context(data_str)
        elif request_type == 'fetch':
            context = CurlFetch2Py.parse_fetch_context(data_str)
        else:
            raise ValueError("Unsupported start type")
        return {"request_string": execute_request(context, target).strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))