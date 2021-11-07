import sqlalchemy as sa
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

