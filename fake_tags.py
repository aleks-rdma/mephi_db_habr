from datetime import date
import random
from sqlalchemy import Integer
import constants as c
from sqlalchemy.orm import sessionmaker, Session
from faker import Faker
from create_db import Section, ArticleSection
import csv


def unit_sections(session: Session, fake: Faker, article_count: int) -> list[Section]:
    sections = []
    section_article = []
    sections_from_file = []
    article_arr = [i for i in range(1, article_count + 1)]
    with open('sections.csv', newline='\n', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            sections_from_file.append(row[0])
    section_count = len(sections_from_file)
    for i in range(section_count):
        sections.append(Section(title=sections_from_file[i]))
        article_sample = random.sample(article_arr, random.randint(20, 1000))
        for j in range(len(article_sample)):
            section_article.append(ArticleSection(article_id=article_sample[j], section_id=i + 1))
    session.add_all(sections)
    session.commit()
    session.add_all(section_article)
    session.commit()
    return sections