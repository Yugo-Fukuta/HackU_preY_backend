from database import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy_utils import UUIDType
from uuid import uuid4
from .mixins import TimestampMixin

class TwitterModel(Base, TimestampMixin):
    __tablename__ = 'twitter'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, nullable=False)
    whose = Column(String(20), nullable=False)
    nankome = Column(Integer, nullable=False)
    api_key = Column(String(50), nullable=False)
    api_key_secret = Column(String(50), nullable=False)
    access_token = Column(String(50), nullable=False)
    access_token_secret = Column(String(50), nullable=False)
