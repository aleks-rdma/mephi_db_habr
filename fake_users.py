from datetime import date
import constants as c
from sqlalchemy.orm import sessionmaker, Session
from faker import Faker
from create_db import User


def unit_users(session: Session, fake: Faker) -> list[User]:
    users = []
    for i in range(c.USER_NUM):
        name = fake.unique.user_name()
        country = fake.country()
        email = fake.unique.email(),
        biographic = fake.text(max_nb_chars=200)
        registration_date = fake.date()
        last_activity_date = fake.date_between(start_date=date.fromisoformat(registration_date))
        contact = fake.basic_phone_number()
        users.append(User(name=name, country=country, email=email, biography=biographic, registration_date=registration_date,
             last_activity_date=last_activity_date, contact=contact))
    session.add_all(users)
    session.commit()
    return users


