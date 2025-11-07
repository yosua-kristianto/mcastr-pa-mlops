from sqlalchemy import (
    Column, String, Text, SmallInteger,
    TIMESTAMP, func
)
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Knowledge(Base):
    __tablename__ = "mlops_tbl_knowledge"

    id = Column(String(36), primary_key=True)
    prompt = Column(Text)
    label = Column(SmallInteger, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())
    updated_at = Column(TIMESTAMP, nullable=True)
    deleted_at = Column(TIMESTAMP, nullable=True)


class ModelLog(Base):
    __tablename__ = "mlops_tbl_model_log"

    uuid = Column(String(36), primary_key=True)
    user_session_id = Column(Text, nullable=False)
    prompt = Column(Text, nullable=False)
    model_output = Column(SmallInteger, nullable=False)
    feedback_actual_output = Column(SmallInteger, nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())
    updated_at = Column(TIMESTAMP, nullable=True)
    deleted_at = Column(TIMESTAMP, nullable=True)
