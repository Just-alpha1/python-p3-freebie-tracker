#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Freebie

if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Seed companies
    google = Company(name="Google", founding_year=1998)
    facebook = Company(name="Facebook", founding_year=2004)

    # Seed devs
    rick = Dev(name="Rick")
    morty = Dev(name="Morty")

    # Seed freebies
    freebie1 = Freebie(item_name="Sticker", value=1, dev=rick, company=google)
    freebie2 = Freebie(item_name="T-shirt", value=10, dev=morty, company=facebook)

    session.add_all([google, facebook, rick, morty, freebie1, freebie2])
    session.commit()
