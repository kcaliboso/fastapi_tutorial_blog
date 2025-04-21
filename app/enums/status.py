from enum import Enum

class Status(str, Enum):
    Draft = "draft"
    Pending = "pending"
    Published = "published"