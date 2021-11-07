from http import client
from typing import Optional
from PIL import Image

from fastapi.responses import Response
from os import path
from urllib.parse import urlparse

from fastapi.responses import FileResponse

from app.db.images import create_images
from app.utils import async_request_file
from app.views import api_router
from fastapi import File, UploadFile

import shutil


@api_router.post("/image", status_code=201, tags=['api'])
async def create_file(file: UploadFile = File(None), url: Optional[str] = None,):
    if file:
        with open(f'files/{file.filename}', 'wb') as buffer:
            shutil.copyfileobj(file.file, buffer)
            im = Image.open(f'files/{file.filename}')
            (width, height) = im.size
            # print(type(width), type(height), width, height)
            return await create_images(name=file.filename,
                                       url='None',
                                       picture=f'files/{file.filename}',
                                       width=width,
                                       height=height)
    if url:
        filename = await async_request_file(url)
        im = Image.open(f'files/{file.filename}')
        (width, height) = im.size
        print(type(width), type(height), width, height)
        return await create_images(name=file.filename,
                                   url=url,
                                   picture=f'files/{file.filename}',
                                   width=width,
                                   height=height)

