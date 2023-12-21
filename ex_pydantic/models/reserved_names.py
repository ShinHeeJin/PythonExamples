import logging
from typing import Dict

from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy import JSON, Column, Integer
from sqlalchemy.orm import declarative_base

logger = logging.getLogger(__name__)
Base = declarative_base()


class MyModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    metadata: Dict[str, str] = Field(alias="metadata_")


class SQLModel(Base):
    __tablename__ = "my_table"
    id = Column("id", Integer, primary_key=True, index=True)
    metadata_ = Column("metadata", JSON)


def test_reserved_names():
    sql_model = SQLModel(metadata_={"key": "value"}, id=1)
    pydantic_model = MyModel.model_validate(sql_model)
    logger.info(f"{pydantic_model=}")  # pydantic_model=MyModel(metadata={'key': 'value'})

    assert pydantic_model.model_dump() == {"metadata": {"key": "value"}}
    assert pydantic_model.model_dump(by_alias=True) == {"metadata_": {"key": "value"}}
