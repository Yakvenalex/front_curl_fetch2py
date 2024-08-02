def execute_request(context, target):
    method = context.method.upper()
    url = context.url
    headers = dict(context.headers) if context.headers else None
    if isinstance(headers, dict):
        try:
            del headers['Accept-Encoding']
        except:
            pass

    data = dict(context.data) if context.data else None
    cookies = dict(context.cookies) if context.cookies else None

    if target == "httpx":
        return f'''import httpx
import asyncio


async def fetch():
    async with httpx.AsyncClient() as client:
        response = await client.request(
            method="{method}",
            url="{url}",
            headers={headers},
            data={data},
            cookies={cookies}
        )
        return response.text


rez = asyncio.run(fetch())
print(rez)
'''
    elif target == "requests":
        return f'''import requests

def fetch():
    response = requests.request(
        method="{method}",
        url="{url}",
        headers={headers},
        data={data},
        cookies={cookies}
    )
    return response.text


rez = fetch()
print(rez)
'''
    else:
        raise ValueError("Unsupported target")
