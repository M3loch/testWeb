from pydantic import BaseModel, ConfigDict

from models import test


# Best pratice is Get model inhereted from Post model
class TestPostDTO(BaseModel):
    value : int

class TestGetDTO(TestPostDTO):
    id : int

