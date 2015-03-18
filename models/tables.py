# coding: utf8
# coding: utf8
from datetime import datetime
import re
import unittest

def get_first_name():
    author = 'Nobody'
    if auth.user:
        author = auth.user.first_name
    return author

# Format for wiki links.
RE_LINKS = re.compile('(<<)(.*?)(>>)')
CATEGORY = ['Makeup', 'SkinCare', 'Fragrance', 'Bath&Body', 'Nails', 'Hair', 'Tools&Brushes', 'Men']
MAKEUP_CATEGORY = ['FaceMakeup', 'BodyMakeup', 'EyeMakeup', 'Lips', 'Nails']
SKIN_CATEGORY = ['Wash', 'Mosturizers', 'Treatments', 'Sunscreens', 'Tanners', 'Whiteners', 'Other']
BATHBODY_CATEGORY = ['LotionCreams', 'BathShower', 'Sun', 'Other' ]
HAIR_CATEGORY = ['StylingTools', 'Treatment', 'ShampooConditioner', 'Other']
TOOLSBRUSHES_CATEGORY = ['HairStyleTools', 'MakeupBrushesApplicators', 'Other']
MEN_CATEGORY = ['Fragrance', 'SkinCare', 'Shaving', 'Hair', 'Other']
PRICE_RANGE = [1, 2, 3, 4, 5]
RATING = [1, 2, 3, 4, 5]
db.define_table('forum',
                Field('title'),
                Field('category'),
                Field('body', 'text'),
                Field('date_posted', 'datetime'),
                Field('author'),
                Field('likes', writable=False)
    )

db.define_table('post',
                Field('thread_id', readable = False, writable = False),
                Field('body', 'text'),
                Field('date_posted', 'datetime'),
                Field('author'),
    )

db.define_table('makeup',
                Field('product', required = True),
                Field('author', default = get_first_name(), writable = False),
                Field('category', requires = IS_IN_SET(MAKEUP_CATEGORY, error_message = 'Field Required')),
                Field('total_price_range', 'float', requires = IS_IN_SET(PRICE_RANGE, error_message = 'Choose price range')),
                Field('price_range', 'float', writable = False),
                Field('totalRating', 'float', requires = IS_IN_SET(RATING, error_message = 'Choose a Rating')),
                Field('rating', 'float', writable = False),
                Field('body', 'text'),
                Field('image'),
                Field('date_posted', 'datetime', default = datetime.utcnow(), writable = False),
                Field('reviewCount', 'integer', default = 0, writable = False),
    )

db.define_table('skinCare',
                Field('product', required = True),
                Field('author', default = get_first_name(), writable = False),
                Field('category', requires = IS_IN_SET(SKIN_CATEGORY , error_message = 'Field Required')),
                Field('total_price_range', 'float', requires = IS_IN_SET(PRICE_RANGE, error_message = 'Choose price range')),
                Field('price_range', 'float', writable = False),
                Field('totalRating', 'float', requires = IS_IN_SET(RATING, error_message = 'Choose a Rating')),
                Field('rating', 'float', writable = False),
                Field('body', 'text'),
                Field('image'),
                Field('date_posted', 'datetime', default = datetime.utcnow(), writable = False),
                Field('reviewCount', 'integer', default = 0, writable = False),
    )

db.define_table('bathBody',
                Field('product', required = True),
                Field('author', default = get_first_name(), writable = False),
                Field('category', requires = IS_IN_SET(BATHBODY_CATEGORY , error_message = 'Field Required')),
                Field('total_price_range', 'float', requires = IS_IN_SET(PRICE_RANGE, error_message = 'Choose price range')),
                Field('price_range', 'float', writable = False),
                Field('totalRating', 'float', requires = IS_IN_SET(RATING, error_message = 'Choose a Rating')),
                Field('rating', 'float', writable = False),
                Field('body', 'text'),
                Field('image'),
                Field('date_posted', 'datetime', default = datetime.utcnow(), writable = False),
                Field('reviewCount', 'integer', default = 0, writable = False),
    )

db.define_table('hair',
                Field('product', required = True),
                Field('author', default = get_first_name(), writable = False),
                Field('category', requires = IS_IN_SET(HAIR_CATEGORY, error_message = 'Field Required')),
                Field('total_price_range', 'float', requires = IS_IN_SET(PRICE_RANGE, error_message = 'Choose price range')),
                Field('price_range', 'float', writable = False),
                Field('totalRating', 'float', requires = IS_IN_SET(RATING, error_message = 'Choose a Rating')),
                Field('rating', 'float', writable = False),
                Field('body', 'text'),
                Field('image'),
                Field('date_posted', 'datetime', default = datetime.utcnow(), writable = False),
                Field('reviewCount', 'integer', default = 0, writable = False),
    )

db.define_table('toolsBrushes',
                Field('product', required = True),
                Field('author', default = get_first_name(), writable = False),
                Field('category', requires = IS_IN_SET(TOOLSBRUSHES_CATEGORY, error_message = 'Field Required')),
                Field('total_price_range', 'float', requires = IS_IN_SET(PRICE_RANGE, error_message = 'Choose price range')),
                Field('price_range', 'float', writable = False),
                Field('totalRating', 'float', requires = IS_IN_SET(RATING, error_message = 'Choose a Rating')),
                Field('rating', 'float', writable = False),
                Field('body', 'text'),
                Field('image'),
                Field('date_posted', 'datetime', default = datetime.utcnow(), writable = False),
                Field('reviewCount', 'integer', default = 0, writable = False),
    )

db.define_table('men',
                Field('product', required = True),
                Field('author', default = get_first_name(), writable = False),
                Field('category', requires = IS_IN_SET(MEN_CATEGORY, error_message = 'Field Required')),
                Field('total_price_range', 'float', requires = IS_IN_SET(PRICE_RANGE, error_message = 'Choose price range')),
                Field('price_range', 'float', writable = False),
                Field('totalRating', 'float', requires = IS_IN_SET(RATING, error_message = 'Choose a Rating')),
                Field('rating', 'float', writable = False),
                Field('body', 'text'),
                Field('image'),
                Field('date_posted', 'datetime', default = datetime.utcnow(), writable = False),
                Field('reviewCount', 'integer', default = 0, writable = False),
    )

db.define_table('comments',
                Field('product_id'),
                Field('category'),
                Field('quality'),
                Field('price'),
                Field('reviews', 'text'),
                Field('author', default = get_first_name(), writable = False),
    )

def create_wiki_links(s):
    """This function replaces occurrences of '<<polar bear>>' in the 
    wikitext s with links to default/page/polar%20bear, so the name of the 
    page will be urlencoded and passed as argument 1."""
    def makelink(match):
        # The tile is what the user puts in
        title = match.group(2).strip()
        # The page, instead, is a normalized lowercase version.
        page = title.lower()
        return '[[%s %s]]' % (title, URL('default', 'index', args=[page]))
    return re.sub(RE_LINKS, makelink, s)

def represent_wiki(s):
    """Representation function for wiki pages.  This takes a string s
    containing markup language, and renders it in HTML, also transforming
    the <<page>> links to links to /default/index/page"""
    return MARKMIN(create_wiki_links(s))

def represent_content(v, r):
    """In case you need it: this is similar to represent_wiki, 
    but can be used in db.table.field.represent = represent_content"""
    return represent_wiki(v)

# We associate the wiki representation with the body of a revision.
db.forum.category.requires = IS_IN_SET(CATEGORY)
db.forum.category.default = ''
db.forum.category.required = True
db.forum.author.default = get_first_name()
db.forum.author.writable = False
db.forum.date_posted.writable = False
db.forum.date_posted.default = datetime.utcnow()
db.post.author.default = get_first_name()
db.post.author.writable = False
db.post.date_posted.writable = False
db.post.date_posted.default = datetime.utcnow()
db.forum.likes.default = 0
