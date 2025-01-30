from datetime import date
import random
from sqlalchemy import Integer
import constants as c
from sqlalchemy.orm import sessionmaker, Session
from faker import Faker
from create_db import Article, AuthorArticle, UserArticle


def unit_articles(session: Session, fake: Faker) -> int:
    articles = []
    author_article = []
    article_id = 1
    for i in range(c.AUTHOR_NUM):
        for j in range(random.randint(0, c.ARTICLE_COEFF)):
            views = random.randint(0, 100000)
            reading_time = random.choice(['30 min', '12 min', '1 hour', 'less then 5 min', '10 min', '2 hour'])
            complexity = random.choice(['hard', 'medium', 'easy'])
            content = 'Let\'s imagine that it\'s the text of an article' + fake.unique.text(1000)
            title = 'It\'s title' + fake.unique.text(25)
            date_article = fake.date()
            rating = random.randint(-1 * c.RATING_MAX_ABS, c.RATING_MAX_ABS)
            articles.append(Article(views=views, date=date_article, reading_time=reading_time, complexity=complexity,
                                    content=content, title=title, rating=rating))
            author_article.append(AuthorArticle(article_id=article_id, author_id=(i + 1)))
            while random.randint(1, 10) <= 3:
                author_article.append(AuthorArticle(article_id=article_id, author_id=random.randint(1,c.AUTHOR_NUM)))
            article_id += 1
    article_id -= 1
    user_article = []
    article_arr = [i for i in range(1, article_id + 1)]
    user_arr = [i for i in range(1, c.USER_NUM + 1)]
    article_sample = random.sample(article_arr, article_id - 1000)
    for i in range(len(article_sample)):
        user_count = random.randint(1, 100)
        user_sample = random.sample(user_arr, user_count)
        for j in range(len(user_sample)):
            user_article.append(UserArticle(user_id=user_sample[j], article_id=article_sample[i]))

    session.add_all(articles)
    session.add_all(author_article)
    session.add_all(user_article)
    session.commit()

    return article_id