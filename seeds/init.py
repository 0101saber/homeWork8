import argparse
import json

from mongoengine import DoesNotExist

from conf.models import *
import conf.connect


def create_author(fullname, born_date, born_location, description):
    result = Author(fullname=fullname, born_date=born_date, born_location=born_location, description=description)
    result.save()


def create_quotes(tags, author, quote):
    result = Quotes(tags=tags, author=author, quote=quote)
    result.save()


def find_author_by_name(fullname):
    result = Author.objects(fullname=fullname).first()
    return result


if __name__ == '__main__':
    with open('../seeds/author.json') as json_file:
        authors = json.load(json_file)

    with open('../seeds/quotes.json') as json_file:
        quotes = json.load(json_file)

    for author in authors:
        create_author(author['fullname'], author['born_date'], author['born_location'], author['description'])

    for quote in quotes:
        create_quotes(quote['tags'], find_author_by_name(quote['author']), quote['quote'])
