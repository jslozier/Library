__author__ = 'Jay Lozier'

import schema_create as sc
from library_main import AUTHORS as AUTHORS
from library_main import BOOKS as BOOKS
from library_main import PUBLISHERS as PUBLISHERS


def verification_collections(db):
    if AUTHORS in db.collection_names() and BOOKS in db.collection_names() \
            and PUBLISHERS in db.collections():
        return True
    elif AUTHORS not in db.collection_names():
        db.authors.insert(sc.authors_schema_create())
        if BOOKS in db.collection_names() and PUBLISHERS in \
                db.collection_names:
            return True
    elif BOOKS not in db.collection_names():
        db.books.insert(sc.books_schema_create())
        if AUTHORS in db.collection_names() and PUBLISHERS in \
                db.collection_names():
            return True
    elif PUBLISHERS not in db.collection_names():
        db.publishers(sc.publishers_schema_create())
        if AUTHORS in db.collection_names() and BOOKS in db.collection_names():
            return True
    else:
        return False
