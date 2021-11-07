from http import client
from typing import Optional
from PIL import Image

from fastapi.responses import Response
from os import path
from urllib.parse import urlparse

from fastapi.responses import FileResponse

from app.db.images import create_application
from app.utils import async_request_file
from app.views import api_router
from fastapi import File, UploadFile

import shutil


@api_router.post("/image", status_code=201, tags=['api'])
async def create_file(url: Optional[str] = None, file: UploadFile = File(None)):
    if file:
        with open(f'files/{file.filename}', 'wb') as buffer:
            shutil.copyfileobj(file.file, buffer)
            im = Image.open(f'files/{file.filename}')
            (width, height) = im.size
            print(file.filename, type(file.filename))

            return await create_application(name=file.filename,
                                            picture=f'files/{file.filename}',
                                            width=width, height=height)
    if url:
        await async_request_file(url)

        return
