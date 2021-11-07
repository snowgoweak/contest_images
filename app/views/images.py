
from typing import Optional
from PIL import Image

from app.db.images import create_images, get_images_by_id, get_images_all, delete_image_by_id
from app.utils import async_request_file
from app.views import api_router
from fastapi import File, UploadFile

import shutil


@api_router.get("/images", status_code=200, tags=['api'])
async def get_images():
    return await get_images_all()


@api_router.get("/images/{id}", status_code=200, tags=['api'])
async def get_image(img_id: int):
    return await get_images_by_id(img_id)


@api_router.post("/images", status_code=201, tags=['api'])
async def create_file(file: UploadFile = File(None), url: Optional[str] = None):
    if file:
        with open(f'files/{file.filename}', 'wb') as buffer:
            shutil.copyfileobj(file.file, buffer)
            im = Image.open(f'files/{file.filename}')
            (width, height) = im.size
            return await create_images(name=file.filename,
                                       url='None',
                                       picture=f'files/{file.filename}',
                                       width=width,
                                       height=height)
    if url:
        filename = await async_request_file(url)
        im = Image.open(f'files/{filename}')
        (width, height) = im.size
        return await create_images(name=filename,
                                   url=url,
                                   picture=f'files/{filename}',
                                   width=width,
                                   height=height)


@api_router.post("/images/{id}/resize", status_code=200, tags=['api'])
async def resize_image(img_id: int, width: int, height: int):
        file = await get_images_by_id(img_id)
        img = Image.open(file['picture'])
        width = width
        height = height
        resized_img = img.resize((width, height), Image.ANTIALIAS)
        resized_img.save(file['picture'])


@api_router.delete("/images/{id}", status_code=200, tags=['api'])
async def delete_image(img_id: int):
    return await delete_image_by_id(img_id)

