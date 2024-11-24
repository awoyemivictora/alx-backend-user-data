#!/usr/bin/env python3
from time import timezone
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
# from app.database import Base
from sqlalchemy.ext.declarative import declarative_base
from datetime import date, datetime, timedelta, timezone
from typing import List, Optional
from sqlalchemy.sql import func
from sqlalchemy import Column, String, Boolean, Date, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship, declarative_base, mapped_column, Mapped
from datetime import datetime
from sqlalchemy import Enum as SAEnum, String
from enum import Enum as PyEnum

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    
    id: Mapped[int] = mapped_column(nullable=False, primary_key=True, unique=True)
    email: Mapped[str] = mapped_column(nullable=False, unique=True) 
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    session_id: Mapped[str] = mapped_column(nullable=True)
    reset_token: Mapped[str] = mapped_column(nullable=True)
   
   