import sqlalchemy as sa
from sqlalchemy import literal_column
import app
from app.db import metadata
from app.db.utils import row_to_dict

images = sa.Table(
    "images",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("name", sa.String),
    sa.Column("url", sa.String, nullable=True),
    sa.Column('picture', sa.String, nullable=True),
    sa.Column("width", sa.Integer),
    sa.Column("height", sa.String),
    sa.Column("parent_picture", sa.String, nullable=True))


async def create_application(**kwargs) -> dict:
    query = images.insert().values(kwargs).returning(literal_column('*'))
    row = await app.base.database.fetch_one(query)
    return row_to_dict(row)
