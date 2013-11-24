__author__ = 'Jay Lozier'

"""
These functions create the schemas for each collection in the database. The key
and its type are described in the schema. These functions are only called once,
when the collections are initially created. The classes Authors, Books, and
Publishers are derived from the schemas.
"""


def authors_schema_create():
    doc = {}
    doc['_id'] = 'schema'
    doc['first_name'] = 'string'
    doc['middle_name'] = 'string'
    doc['last_name'] = 'string'
    doc['pre_nominative'] = 'string'
    doc['post_nominative'] = 'string'
    return doc


def publishers_schema_create():
    doc = {}
    doc['_id'] = 'schema'
    doc['publisher'] = 'string'
    doc['city'] = 'string'
    return doc


def books_schema_create():
    doc = {}
    doc['_id'] = 'schema'
    doc['title'] = 'string'
    doc['edition'] = 'string or integer'
    doc['cost'] = 'integer'
    doc['pages'] = 'integer'
    doc['acquired'] = 'integer'
    doc['source'] = 'string'
    doc['dewey'] = 'dictionary'
    doc['lc_classification'] = 'string'
    doc['isbn'] = 'string'
    doc['dewey_keys'] = {'suffix':'string', 'code':'string', 'prefix':'string'}
    doc['extra'] = 'list'
    doc['subject'] = 'list'
    doc['authors'] = 'dbref'
    doc['editors'] = 'dbref'
    doc['translators'] = 'dbref'
    doc['illustrators'] = 'dbref'
    return doc
