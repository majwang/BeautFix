# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations
import math
import logging

CATEGORY = ['Makeup', 'SkinCare', 'Fragrance', 'Bath&Body', 'Nails', 'Hair', 'Tools&Brushes', 'Men', 'Other']

def view():
    """View a post."""
    # p = db(db.bboard.id == request.args(0)).select().first()
    #p = db.post(request.args(0))
    #form = SQLFORM(db.post, record=p, readonly=True)
    row_id = request.args(0)
    title = db.forum[row_id].title
    body = db.forum[row_id].body
    post = True if request.vars.post == 'y' else False
    backbutton = A('Back', _class='btn', _href=URL('default', 'forums'))
    button = A('Post', _class='btn', _href=URL('default', 'view', args = [row_id], vars=dict(post='y')))  
    thread = db(db.forum.title == title).select().first()
    thread_id = thread.id if thread is not None else None
    if post:
        backbutton = ""
        button = ""
        form = SQLFORM.factory(db.post)
        form.add_button('Cancel', URL('default', 'view', args = [row_id]))
        if form.process().accepted:
           if not auth.user:
               session.flash = T("Please login first")
               redirect(URL('default', 'forums'))
           db.post.insert(body=form.vars.body, thread_id = thread_id)
           redirect(URL('default', 'view', args = [row_id]))

    else:
        form = SQLFORM.grid(db.post.thread_id == thread_id, user_signature = False,
                fields=[db.post.date_posted,db.post.body, db.post.author],
                editable=False, deletable=False, details = False, create = False, searchable = False, csv = False, 
                paginate=50, orderby = db.post.date_posted,maxtextlength = 250)

    # p.name would contain the name of the poster.
    return dict(form=form, title=title, body=body, button=button, backbutton = backbutton)

@auth.requires_login()
def addLike():
    row_id = request.args(0)
    title = db.forum[row_id].title
    thread = db(db.forum.title == title).select().first()
    thread.likes = int(thread.likes) + 1
    thread.update_record()
    redirect(URL('default', 'forums'))

def forums():
    title = 'Forums'
    display_title = title.title()
    editing = True if request.vars.edit == 'y' else False
    button = A('+ Thread', _class='btn', _href=URL('default', 'forums', vars=dict(edit='y')))
    def generate_goto_button(row):
        b = A('Go to', _class='btn', _href=URL('default', 'view', args=[row.id]))
        return b
    def generate_like_button(row):
        b = A('^', _class='btn', _href=URL('default', 'addLike', args=[row.id]))
        return b
    
    if editing:
        button = ""
        form = SQLFORM.factory(db.forum)
        form.add_button('Cancel', URL('default', 'forums'))
        if form.process().accepted:
           if not auth.user:
               session.flash = T("Please login first")
               redirect(URL('default', 'forums'))
           db.forum.insert(body=form.vars.body, title=form.vars.title, category=form.vars.category)
           redirect(URL('default', 'forums'))

    else:
        links=[dict(header='', body = generate_like_button), dict(header='', body = generate_goto_button)]

        form = SQLFORM.grid(db.forum, user_signature = False,
                fields=[db.forum.title, db.forum.category, db.forum.date_posted, db.forum.author, db.forum.likes],
                editable=False, deletable=False, details = False, create = False, searchable = False, csv = False, 
                paginate=50, orderby =~ db.forum.date_posted,maxtextlength = 50, links=links)

    return dict(display_title=display_title, form=form, addThread = button)


def writeAreview():
    category = request.args(0)
    subCategory = request.args(1) if request.args(1) is not None else None
    redirect(URL('default', 'index', args = [category, subCategory], vars=dict(posting='y')))

def reviews():
    title = 'Write a Review'
    display_title = title.title()

    select = SQLFORM.widgets.options.widget(db.forum.category, db.forum.category.default)
    
    subselect2 = SQLFORM.widgets.options.widget(db.makeup.category, db.makeup.category.default)
    subselect3 = SQLFORM.widgets.options.widget(db.skinCare.category, db.skinCare.category.default)
    subselect4 = SQLFORM.widgets.options.widget(db.bathBody.category, db.bathBody.category.default)
    subselect5 = SQLFORM.widgets.options.widget(db.hair.category, db.hair.category.default)
    subselect6 = SQLFORM.widgets.options.widget(db.toolsBrushes.category, db.toolsBrushes.category.default)
    subselect7= SQLFORM.widgets.options.widget(db.men.category, db.men.category.default)

    return dict(display_title=display_title,select=select, subselect2=subselect2, subselect3=subselect3, subselect4=subselect4, subselect5=subselect5, subselect6=subselect6, subselect7=subselect7)

@auth.requires_login()
def account():
    title = 'Account'
    display_title = title.title()
    form = auth.profile()
    return dict(display_title=display_title,form=form)



def viewProduct():
    category = request.args(0) if request.args(0) is not None else None
    subCategory = request.args(1) if request.args(1) is not None else None
    product_id = request.args(2) if request.args(2) is not None else None

    if category == "makeup":
       display_title2 = "MAKEUP"
       displayDB = db.makeup

    if category == "skinCare":
        display_title2 = "SKINCARE"
        displayDB = db.skinCare

    if category == "bathBody":
        display_title2 = "BATH AND BODY"
        displayDB = db.bathBody

    if category == "hair":
        display_title2 = "HAIR"
        displayDB = db.hair

    if category == "toolsBrushes":
        display_title2 = "TOOLS AND BRUSHES"
        displayDB = db.toolsBrushes

    if category == "men":
        display_title2 = "MEN"
        displayDB = db.men

    product_selected = db(displayDB.id == product_id).select().first()
    product_title = product_selected.product
    product_id = product_selected.id
    product_price = product_selected.price_range
    product_rating = product_selected.rating

    def picture(x):
        return{
            1.0 : A(IMG(_src="http://i.imgur.com/vBphvSK.png?1")),
            2.0 : A(IMG(_src="http://i.imgur.com/hX0Su5L.png?1")),
            3.0 : A(IMG(_src="http://i.imgur.com/OiNpTYg.png?1")),
            4.0 : A(IMG(_src="http://i.imgur.com/7TicHMP.png?1")),
            5.0 : A(IMG(_src="http://i.imgur.com/qpaKKaw.png?2"))
        }[x]

    def money(x):
        return{
            1.0 : A(IMG(_src="http://i.imgur.com/jYA0anS.png?1")),
            2.0 : A(IMG(_src="http://i.imgur.com/6kDHxEd.png?1")),
            3.0 : A(IMG(_src="http://i.imgur.com/cLhLFIx.png?1")),
            4.0 : A(IMG(_src="http://i.imgur.com/pycceWR.png?1")),
            5.0 : A(IMG(_src="http://i.imgur.com/QQHqsaw.png"))
        }[x]

    product_rating = picture(float(product_rating))
    product_price = money(float(product_price))
    product_image = product_selected.image
    product_image = A(IMG(_src=product_image))

    query = (db.comments.product_id==product_id) & (db.comments.category==category)
    form = SQLFORM.grid(query, user_signature = False,
                          fields=[db.comments.reviews, db.comments.author, db.comments.quality, db.comments.price],
                          editable=False, deletable=False, details = False, create = False,
                          searchable = False, csv = False,
                          paginate=50, maxtextlength=100)

    backbutton = A('Back', _class='btn', _href=URL('default', 'index', args=[category, subCategory]))
    postbutton = A('Write a Review', _class='btn', _href=URL('default', 'index', args=[category, subCategory, product_title], vars=dict(posting='y')))

    return dict(display_title=product_title, form=form, backbutton=backbutton, postbutton=postbutton,
                product_rating=product_rating, product_price=product_price, product_image=product_image)


def index():
    title = 'BeautFix'
    display_title = title
    display_title2 = ""
    requiredCategory = ""

    category = request.args(0) if request.args(0) is not None else None
    subCategory = request.args(1) if request.args(1) is not None else None
    product_title = request.args(2) if request.args(2) is not None else None
    product_title = re.sub(r'_', ' ', product_title) if product_title is not None else None

    posting = True if request.vars.posting == 'y' else False
    if subCategory is not None:
        button = A('Post', _class='btn', _href=URL('default', 'index', args = [category, subCategory], vars=dict(posting='y'))) if category is not None else ""
    else:
        button = A('Post', _class='btn', _href=URL('default', 'index', args = [category], vars=dict(posting='y'))) if category is not None else ""
    form = ""

    if category == "makeup":
       display_title2 = "MAKEUP"
       displayDB = db.makeup
       requiredCategory = MAKEUP_CATEGORY

    if category == "skinCare":
        display_title2 = "SKINCARE"
        displayDB = db.skinCare
        requiredCategory = SKIN_CATEGORY

    if category == "bathBody":
        display_title2 = "BATH AND BODY"
        displayDB = db.bathBody
        requiredCategory = BATHBODY_CATEGORY

    if category == "hair":
        display_title2 = "HAIR"
        displayDB = db.hair
        requiredCategory = HAIR_CATEGORY

    if category == "toolsBrushes":
        display_title2 = "TOOLS AND BRUSHES"
        displayDB = db.toolsBrushes
        requiredCategory = TOOLSBRUSHES_CATEGORY

    if category == "men":
        display_title2 = "MEN"
        displayDB = db.men
        requiredCategory = MEN_CATEGORY

    if posting:
        if not auth.user:
            session.flash = T("Please login first")
            redirect(URL('default', 'index', args = [category]))
        button = ""
        if product_title is not None:
            form = SQLFORM.factory(
                Field('product', default=product_title, writable = False),
                Field('category', default=subCategory, writable=False),
                Field('price_range', requires = IS_IN_SET(PRICE_RANGE, error_message = 'Choose price range')),
                Field('rating', requires = IS_IN_SET(RATING, error_message = 'Choose a Rating')),
                Field('body', 'text'),
                Field('image'),
            )
        else:
            if subCategory is not None:
                form = SQLFORM.factory(
                    Field('product', required = True),
                    Field('category', default=subCategory, writable=False),
                    Field('price_range', requires = IS_IN_SET(PRICE_RANGE, error_message = 'Choose price range')),
                    Field('rating', requires = IS_IN_SET(RATING, error_message = 'Choose a Rating')),
                    Field('body', 'text'),
                    Field('image')
                )
            else:
               form = SQLFORM.factory(
                    Field('product', required = True),
                    Field('category', requires = IS_IN_SET(requiredCategory, error_message = 'Field Required')),
                    Field('price_range', requires = IS_IN_SET(PRICE_RANGE, error_message = 'Choose price range')),
                    Field('rating', requires = IS_IN_SET(RATING, error_message = 'Choose a Rating')),
                    Field('body', 'text'),
                    Field('image'),
                )
        if product_title is None:
            form.add_button('Cancel', URL('default', 'index', args = [category]))
        else:
            product_id = db(displayDB.product == product_title).select().first().id
            form.add_button('Cancel', URL('default', 'viewProduct' , args=[category, subCategory, product_id]))

        if form.process().accepted:
            product_id = ""
            product_title = form.vars.product.title() if form.vars.product is not None else product_title
            if db(displayDB.product == product_title).select().first() is not None:
                existingProduct = db(displayDB.product == product_title).select().first()
                existingProduct.reviewCount += 1
                count = existingProduct.reviewCount + 1
                newRating = math.ceil((existingProduct.totalRating + float(form.vars.rating))/count)
                existingProduct.totalRating += float(form.vars.rating)
                existingProduct.rating = newRating

                newPrice = math.ceil((existingProduct.total_price_range + float(form.vars.price_range))/count)
                existingProduct.total_price_range += float(form.vars.price_range)
                existingProduct.price_range = newPrice
                existingProduct.update_record()
                product_id = existingProduct.id

            else:
                if subCategory is not None:
                    product_id = displayDB.insert(body=form.vars.body, category=subCategory, price_range = form.vars.price_range,
                         total_price_range = form.vars.price_range, rating = form.vars.rating, totalRating = form.vars.rating,
                         image = form.vars.image, product = form.vars.product.title())
                else:
                    product_id = displayDB.insert(body=form.vars.body, category=form.vars.category, price_range = form.vars.price_range,
                         total_price_range = form.vars.price_range, rating = form.vars.rating, totalRating = form.vars.rating,
                         image = form.vars.image, product = form.vars.product.title())
            db.comments.insert(product_id=product_id, category=category, reviews=form.vars.body, quality=form.vars.rating, price=form.vars.price_range)
            redirect(URL('default', 'viewProduct' , args=[category, form.vars.category, product_id]))

    else:
        def generate_view_button(row):
            b = A('View', _class='btn', _href=URL('default', 'viewProduct',
                                                  args=[category, row.category, row.id]))
            return b

        links = [
             dict(header='', body = generate_view_button),
        ]
        if subCategory is not None:
            display_title2 = display_title2 + ' - ' + subCategory.title()
            form = SQLFORM.grid(displayDB.category == subCategory, user_signature = False,
                          fields=[displayDB.product, displayDB.category, displayDB.date_posted,
                                  displayDB.rating, displayDB.price_range],
                          editable=False, deletable=False, details = False, create = False,
                          searchable = False, csv = False, 
                          paginate=50, orderby =~displayDB.date_posted, maxtextlength=100,
                          links=links)
        else:
            if category is not None:
                form = SQLFORM.grid(displayDB, user_signature = False,
                          fields=[displayDB.product, displayDB.category, displayDB.date_posted,
                                  displayDB.rating, displayDB.price_range],
                          editable=False, deletable=False, details = False, create = False,
                          searchable = False, csv = False, 
                          paginate=50, orderby =~displayDB.date_posted, maxtextlength=100,
                          links=links)
            else:
                form = ""

    return dict(display_title=display_title, display_title2=display_title2, form = form, button = button)

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_login() 
def api():
    """
    this is example of API with access control
    WEB2PY provides Hypermedia API (Collection+JSON) Experimental
    """
    from gluon.contrib.hypermedia import Collection
    rules = {
        '<tablename>': {'GET':{},'POST':{},'PUT':{},'DELETE':{}},
        }
    return Collection(db).process(request,response,rules)
