from sqlalchemy import Column, String, DateTime, func, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.database.database import Base
from app.common.consts import VELOG_DEFAULT_PROFILE_IMG


class User(Base):
    __tablename__ = "users"
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = Column(
        String(100),
        primary_key=True,
        unique=True,
        nullable=False,
        comment="유저 고유 번호",
    )
    email = Column(
        String(100),
        nullable=True,
        comment="이메일",
    )
    bookmarks = relationship("Bookmark", back_populates="user")
    is_subscribed = Column(
        Boolean,
        nullable=False,
        default=True,
        comment="이메일 구독 여부",
    )
    created_at = Column(
        DateTime,
        nullable=False,
        default=func.now(),
        comment="생성 시점",
    )
    updated_at = Column(
        DateTime,
        nullable=False,
        default=func.now(),
        onupdate=func.now(),
        comment="마지막 수정 시점"
    )

    class Config:
        orm_mode = True


class Blog(Base):
    __tablename__ = "blogs"
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = Column(
        String(100),
        primary_key=True,
        unique=True,
        nullable=False,
        comment="블로그 고유 번호",
    )
    profile_img = Column(
        String(200),
        nullable=False,
        default=VELOG_DEFAULT_PROFILE_IMG,
        comment="프로필 이미지 링크",
    )
    bookmarks = relationship("Bookmark", back_populates="blog")
    posts = relationship("Post", back_populates="blog")
    last_uploaded_at = Column(
        DateTime,
        nullable=False,
        default=func.now(),
        onupdate=func.now(),
        comment="마지막 포스트 업로드 시점"
    )
    created_at = Column(
        DateTime,
        nullable=False,
        default=func.now(),
        comment="생성 시점",
    )
    updated_at = Column(
        DateTime,
        nullable=False,
        default=func.now(),
        onupdate=func.now(),
        comment="마지막 수정 시점"
    )


class Post(Base):
    __tablename__ = "posts"
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = Column(
        String(100),
        primary_key=True,
        unique=True,
        nullable=False,
        comment="포스트 고유 번호",
    )
    title = Column(
        String(100),
        nullable=False,
        comment="포스트 제목",
    )
    blog_id = Column(
        String(100),
        ForeignKey("blogs.id")
    )
    blog = relationship("Blog", back_populates="posts")
    blog_img = Column(
        String(200),
        nullable=False
    )
    link = Column(
        String(100),
        nullable=False
    )
    short_description = Column(
        String(200),
        nullable=True,
        default=None
    )
    body_hash = Column(
        String(100),
        nullable=True,
        default=None
    )
    created_at = Column(
        DateTime,
        nullable=False,
        default=func.now(),
        comment="생성 시점",
    )
    updated_at = Column(
        DateTime,
        nullable=False,
        default=func.now(),
        onupdate=func.now(),
        comment="마지막 수정 시점"
    )


class Bookmark(Base):
    __tablename__ = "bookmarks"
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = Column(
        Integer,
        primary_key=True,
        unique=True,
        nullable=False,
        comment="북마크 고유 번호",
    )
    user_id = Column(String(100), ForeignKey("users.id"))
    user = relationship("User", back_populates="bookmarks")
    blog_id = Column(String(100), ForeignKey("blogs.id"))
    blog = relationship("Blog", back_populates="bookmarks")
    created_at = Column(
        DateTime,
        nullable=False,
        default=func.now(),
        comment="생성 시점",
    )
    updated_at = Column(
        DateTime,
        nullable=False,
        default=func.now(),
        onupdate=func.now(),
        comment="마지막 수정 시점"
    )
