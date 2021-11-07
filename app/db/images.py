import sqlalchemy as sa
import typing as t
from sqlalchemy import literal_column
import app
from app.db import metadata
from app.db.utils import row_to_dict

images = sa.Table(
    "images",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("name", sa.String, nullable=False),
    sa.Column("url", sa.String, nullable=True),
    sa.Column('picture', sa.String, nullable=True),
    sa.Column("width", sa.Integer, nullable=False),
    sa.Column("height", sa.Integer, nullable=False),
    sa.Column("parent_picture", sa.Integer, nullable=True))


async def create_images(name: str, url: str, picture: str, width: int, height: int) -> dict:
    query = images.insert().values(
        name=name,
        url=url,
        picture=picture,
        width=width,
        height=height).returning(literal_column('*'))
    row = await app.database.fetch_one(query)
    return row_to_dict(row)


async def get_images_all() -> t.Optional[dict]:
    query = images.select()
    row = await app.database.fetch_all(query)
    return row


async def get_images_by_id(img_id: int) -> t.Optional[dict]:
    query = images.select().where(images.c.id == img_id)
    row = await app.database.fetch_one(query)
    return row


async def delete_image_by_id(img_id: int):
    query = images.delete().where(images.c.id == img_id)
    await app.database.execute(query)
