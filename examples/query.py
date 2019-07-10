import os
import asyncio
import aiohttp
from onlaw_api_client.client import Onlaw


async def main():
    client: Onlaw = Onlaw(os.environ['ONLAW_CLIENT_ID'],
                          os.environ['ONLAW_CLIENT_SECRET'])

    query: str = '{document(uid: "LBK nr 1010 af 03/07/2018") { uid } }'

    async with aiohttp.ClientSession() as session:
        response: dict = await client.execute(query, session)

    print(response)


if __name__ == '__main__':
    asyncio.run(main())
