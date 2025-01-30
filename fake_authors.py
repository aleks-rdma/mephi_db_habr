import random
from datetime import date
import constants as c
from sqlalchemy.orm import sessionmaker, Session
from faker import Faker
from create_db import Author


def unit_authors(session: Session, fake: Faker) -> list[Author]:
    a = [i for i in range(1, c.USER_NUM + 1)]
    user_id_sample = random.sample(a, c.AUTHOR_NUM)
    authors = []
    for i in range(c.AUTHOR_NUM):
        rating = random.randint(-1 * c.RATING_MAX_ABS, c.RATING_MAX_ABS)
        user_id = user_id_sample[i]
        authors.append(Author(rating=rating, user_id=user_id))
    session.add_all(authors)
    session.commit()
    return authors
