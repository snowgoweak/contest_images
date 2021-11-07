import aiohttp
import aiofiles


async def async_request_file(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                filename = url.split("/")[-1]
                file = await aiofiles.open(f'files/{filename}', mode='wb')
                await file.write(await resp.read())
                await file.close()

