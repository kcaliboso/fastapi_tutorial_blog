from pydantic import BaseModel
from typing import List, Generic, Optional, TypeVar

T = TypeVar("T")

class APIResponse(BaseModel, Generic[T]):
    status: str
    status_code: int
    message: str
    data: Optional[List[T] | T] = None