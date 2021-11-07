from pydantic import BaseModel


class ResolutionImagesModel(BaseModel):
    width: int
    height: int
