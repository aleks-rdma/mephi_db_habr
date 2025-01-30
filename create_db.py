from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    biography = Column(Text, nullable=True)
    registration_date = Column(DateTime, server_default=func.now())
    last_activity_date = Column(DateTime, onupdate=func.now())
    contact = Column(String, nullable=True)


class Comment(Base):
    __tablename__ = 'comments'

    comm_id = Column(Integer, primary_key=True, autoincrement=True)
    rating = Column(Integer, nullable=False)
    parent_id = Column(Integer, nullable=True)
    date = Column(DateTime, server_default=func.now())
    content = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    article_id = Column(Integer, ForeignKey('articles.article_id'))


class Article(Base):
    __tablename__ = 'articles'

    article_id = Column(Integer, primary_key=True, autoincrement=True)
    views = Column(Integer, default=0)
    date = Column(DateTime, server_default=func.now())
    reading_time = Column(String, nullable=False)
    complexity = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    title = Column(String, nullable=False)
    rating = Column(Integer, nullable=True)


class UserArticle(Base):
    __tablename__ = 'user_article'

    user_article_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    article_id = Column(Integer, ForeignKey('articles.article_id'))


class AuthorUser(Base):
    __tablename__ = 'author_user'

    author_user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    author_id = Column(Integer, ForeignKey('authors.author_id'))


class Author(Base):
    __tablename__ = 'authors'

    author_id = Column(Integer, primary_key=True, autoincrement=True)
    rating = Column(Integer, nullable=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))


class AuthorArticle(Base):
    __tablename__ = 'author_article'

    author_article_id = Column(Integer, primary_key=True, autoincrement=True)
    article_id = Column(Integer, ForeignKey('articles.article_id'))
    author_id = Column(Integer, ForeignKey('authors.author_id'))


class Section(Base):
    __tablename__ = 'sections'

    section_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)


class ArticleSection(Base):
    __tablename__ = 'article_section'

    article_section_id = Column(Integer, primary_key=True, autoincrement=True)
    article_id = Column(Integer, ForeignKey('articles.article_id'))
    section_id = Column(Integer, ForeignKey('sections.section_id'))


if __name__ == "__main__":
    engine = create_engine("postgresql://postgres:923709@localhost/mephi_db_habr_v1", echo=True)

    engine.echo = False
    Base.metadata.drop_all(engine)
    engine.echo = True
    Base.metadata.create_all(engine)




