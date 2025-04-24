from sqlmodel import Field, SQLModel
from typing import Optional
#from database import Base
#
class Tasks(SQLModel, table=True):
    #__tablename__ = "tasks"       
    id: int | None = Field(default=None, primary_key=True)
    title: str
    description: str
    urgent: int
    project: str
    due_date: str
    progress: int
    status: str
    order_column: int
    created_at: Optional[str] = Field(default=None)
    updated_at: Optional[str] = Field(default=None)