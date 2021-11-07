import typing as t
from datetime import datetime

from fastapi import UploadFile, File
from pydantic import BaseModel



class TaskResponseModel(BaseModel):
    url: t.Optional[str]
    employee_number: str
    title: str

    object: str
    process: str
    created: datetime
    deadline: datetime
    completed: t.Optional[datetime]

    application_id: int
    files: t.Optional[list[File]]







