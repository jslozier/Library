#!/usr/bin/env python3.3

"""
    Library_mongodb is a small, single user library management program 
    Copyright (C) 2013 Jay Lozier, jslozier@fastmail.net

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
# imports from external libraries
import pymongo as py
import json
import csv
from bson.dbref import DBRef

# imports from local libraries
import schema_create as sc
import verify as v
import updates as u

LIBRARY = 'library'
AUTHORS = 'authors'
PUBLISHERS = 'publishers'
BOOKS = 'books'

connection = py.MongoClient()

class Authors:
    def __init__(self, first_name, middle_name, last_name , pre_nominative,
                 post_nominative, id):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.pre_nominative = pre_nominative
        self.post_nominative = post_nominative
        self.id = id

    def update_first_name(self, first_name):
        self.first_name = first_name

    def update_middle_name(self, middle_name):
        self.middle_name = middle_name

    def update_last_name(self, last_name):
        self.last_name

    def update_pre_nominative(self, pre_nominative):
        self.pre_nominative = pre_nominative

    def update_post_nominative(self, post_nominative):
        self.post_nominative = post_nominative

    def update_id(self, id):
        self.id = id


class Publishers:
    def __init__(self, publishers, city, id):
        self.publishers = publishers
        self.city = city
        self.id = id

    def update_publisher(self, publishers):
        self.publishers = publishers

    def update_city(self, city):
        self.city = city

    def update_id(self, id):
        self.id = id


class Books:
    def __init__(self, title, edition, cost, pages, acquired, source, dewey,
                 lc_classification, isbn, extra, subject, authors, editors,
                 translators, illustrators):
        self.title = title
        self.edition = edition
        self.cost = cost
        self.pages = pages
        self.acquired = acquired
        self.source = source
        self.dewey = dewey
        self.lc_classification = lc_classification
        self.isbn = isbn
        self.extra = extra
        self.subject = subject
        self.authors = authors
        self.editors = editors
        self.translators = translators
        self.illustrators = illustrators

    def update_title(self, title):
        self.title = title

    def update_edition(self, edition):
        self.edition = edition

    def update_cost(self, cost):
        self.cost = cost

    def update_pages(self, pages):
        self.pages = pages

    def update_source(self, source):
        self.source = source

    def update_dewey(self, dewey):
        for key, value in dewey.items():
            self.dewey[key] = value

    def update_lc_classification(self, lc_classification):
        self.lc_classification = lc_classification

    def update_isbn(self, isbn):
        self.isbn = isbn

    def update_extra(self, item):
        self.extra.append(item)

    def update_subject(self, item):
        self.subject.append(item)

    def update_authors(self, item):
        self.authors.append(item)

    def update_editors(self, item):
        self.editors.append(item)

    def update_translators(self,item):
        self.translators.append(item)

    def update_illustrators(self, item):
        self.illustrators.append(item)


def get_database(conn):
    if LIBRARY in conn.database_names():
        return conn[LIBRARY]
    else:
        name_database(conn)


def name_database(c):
    for name in c.database_names():
        print(name)
    print('\n')
    answer = input('Enter the name of the database to use or hit return: ')
    if answer in c.database_names():
        return c[answer]
    else:
        db = LIBRARY
        print('The default name for the database is:', LIBRARY)
        reply = input('Enter C to change the default name: ').lower()
        if reply == 'c':
            db = input('Enter the database name: ')
            return c[db]
        else:
            return c[db]


def get_collection(db):
    if v.verify_collections(db):
        return True
    else:
        print('Not all the expected collections are present')
        print('The expected collections are:', AUTHORS, BOOKS, PUBLISHERS)
        print('The following are the collections in the database')
        for coll in db.collection_names():
            print(coll)
        print('Attempting to add the missing collection(s)')
        return v.verification_collections(db)


def update_operations(db,collection):
    if collection == AUTHORS:
        u.update_authors(db)
    elif collection == BOOKS:
        u.update_books(db)
    else:
        u.update_publishers(db)
