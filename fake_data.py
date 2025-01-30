from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from faker import Faker
from fake_users import unit_users
from fake_authors import unit_authors
from fake_articles import unit_articles
from fake_tags import unit_sections
from fake_comms import unit_comments


if __name__ == "__main__":
    engine = create_engine("postgresql://postgres:923709@localhost/mephi_db_habr_v1", echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    fake = Faker()

    unit_users(session, fake)
    unit_authors(session, fake)
    article_count = unit_articles(session, fake)
    unit_sections(session, fake, article_count)
    unit_comments(session, fake, article_count)

    session.close()