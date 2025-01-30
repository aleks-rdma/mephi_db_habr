import random
import constants as c
from sqlalchemy.orm import Session
from faker import Faker
from create_db import Comment
import csv

def unit_comments(session: Session, fake: Faker, article_count: int) -> list[Comment]:
    comms = []
    comms_from_file = []
    with open('comments.csv', newline='\n', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            comms_from_file.append(row[0])
    comms_count = len(comms_from_file)
    for i in range(article_count):
        comms_to_article = random.sample(comms_from_file, random.randint(1, comms_count))
        for j in range(len(comms_to_article)):
            rating = random.randint(-1 * c.RATING_MAX_ABS, c.RATING_MAX_ABS)
            date_comm = fake.date()
            user_id = random.randint(1, c.USER_NUM)
            article_id = i + 1
            comms.append(Comment(rating=rating, date=date_comm, content=comms_to_article[j], user_id=user_id,
                                 article_id=article_id))
    session.add_all(comms)
    session.commit()
    return comms