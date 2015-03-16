# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = A(B('BeutFix'),XML('&trade;&nbsp;'),
                 _class="brand",_href="index")
response.title = ''
response.subtitle = ''

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Your Name <you@example.com>'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (T('Home'), False, URL('default', 'index'), []),
    (T('Write a review'), False, URL('default', 'reviews'), []),
    (T('Forums'), False, URL('default', 'forums'), []),
    (T('Account'), False, URL('default', 'account'), [])
]
response.menu2 = [
    (T('Makeup'), False, URL('default', 'index', args = ['makeup']), [
        (T('Face Makeup'), False,
         URL(
         'default', 'index', args = ['makeup', 'FaceMakeup'])),
        (T('Body Makeup'), False,
         URL(
         'default', 'index', args = ['makeup', 'BodyMakeup'])),
        (T('Eye Makeup'), False,
         URL(
         'default', 'index', args = ['makeup', 'EyeMakeup'])),
        (T('Lips'), False,
         URL(
         'default', 'index', args = ['makeup', 'Lips'])),
        (T('Nails'), False,
         URL(
         'default', 'index', args = ['makeup', 'Nails'])),
    ]),

    (T('Skin Care'), False, URL('default', 'index', args=['skinCare']), [
        (T('Wash'), False,
         URL(
         'default', 'index', args = ['skinCare', 'Wash'])),
        (T('Moisturizers'), False,
         URL(
         'default', 'index', args = ['skinCare', 'Moisturizers'])),
        (T('Treatments'), False,
         URL(
         'default', 'index', args = ['skinCare', 'Treatments'])),
        (T('Sunscreens'), False,
         URL(
         'default', 'index', args = ['skinCare' 'Sunscreens'])),
        (T('Tanners'), False,
         URL(
         'default', 'index', args = ['skinCare', 'Tanners'])),
        (T('Whiteners'), False,
         URL(
         'default', 'index', args = ['skinCare', 'Whiteners'])),
        (T('Other'), False,
         URL(
         'default', 'index', args = ['skinCare', 'Other'])),
    ]),
    (T('Bath and Body'), False, URL('default', 'index', args = ['bathBody']), [
        (T('Lotions and Creams'), False,
         URL(
         'default', 'index', args = ['bathBody', 'LotionCreams'])),
        (T('Bath and Shower'), False,
         URL(
         'default', 'index', args = ['bathBody', 'BathShower'])),
        (T('Sun'), False,
         URL(
         'default', 'index', args = ['bathBody', 'Sun'])),
        (T('Other'), False,
         URL(
         'default', 'index', args = ['bathBody', 'Other'])),
    ]),
    (T('Hair'), False, URL('default','index', args = ['hair']), [
        (T('Styling products & tools'), False,
         URL(
         'default', 'index', args = ['hair', 'StylingTools'])),
        (T('Treatment'), False,
         URL(
         'default', 'index', args = ['hair', 'Treatment'])),
        (T('Shampoo & Conditioner'), False,
         URL(
         'default', 'index', args = ['hair', 'ShampooConditioner'])),
        (T('Other'), False,
         URL(
         'default', 'index', args = ['hair', 'Other'])),
    ]),
    (T('Tools and Brushes'), False, URL('default', 'index', args = ['toolsBrushes']), [
        (T('Hair Styling Tools'), False,
         URL(
         'default', 'index', args = ['toolsBrushes', 'HairStyleTools'])),
        (T('Makeup brushes & Applicators'), False,
         URL(
         'default', 'index', args = ['toolsBrushes', 'MakeupBrushesApplicators'])),
        (T('Other'), False,
         URL(
         'default', 'index', args = ['toolsBrushes', 'Other'])),
    ]),
    (T('Men'), False, URL('default', 'index', args = ['men']), [
        (T('Fragrance'), False,
         URL(
         'default', 'index', args = ['men', 'Fragrance'])),
        (T('Skin Care'), False,
         URL(
         'default', 'index', args = ['men', 'SkinCare'])),
        (T('Shaving'), False,
         URL(
         'default', 'index', args = ['men', 'Shaving'])),
        (T('Hair'), False,
         URL(
         'default', 'index', args = ['men', 'Hair'])),
        (T('Other'), False,
         URL(
         'default', 'index', args = ['men', 'Other'])),
    ])
]

DEVELOPMENT_MENU = True

#########################################################################
## provide shortcuts for development. remove in production
#########################################################################

def _():
    # shortcuts
    app = request.application
    ctr = request.controller
    # useful links to internal and external resources
    response.menu += [
        (SPAN('web2py', _class='highlighted'), False, 'http://web2py.com', [
        (T('My Sites'), False, URL('admin', 'default', 'site')),
        (T('This App'), False, URL('admin', 'default', 'design/%s' % app), [
        (T('Controller'), False,
         URL(
         'admin', 'default', 'edit/%s/controllers/%s.py' % (app, ctr))),
        (T('View'), False,
         URL(
         'admin', 'default', 'edit/%s/views/%s' % (app, response.view))),
        (T('Layout'), False,
         URL(
         'admin', 'default', 'edit/%s/views/layout.html' % app)),
        (T('Stylesheet'), False,
         URL(
         'admin', 'default', 'edit/%s/static/css/web2py.css' % app)),
        (T('DB Model'), False,
         URL(
         'admin', 'default', 'edit/%s/models/db.py' % app)),
        (T('Menu Model'), False,
         URL(
         'admin', 'default', 'edit/%s/models/menu.py' % app)),
        (T('Database'), False, URL(app, 'appadmin', 'index')),
        (T('Errors'), False, URL(
         'admin', 'default', 'errors/' + app)),
        (T('About'), False, URL(
         'admin', 'default', 'about/' + app)),
        ]),
            ('web2py.com', False, 'http://www.web2py.com', [
             (T('Download'), False,
              'http://www.web2py.com/examples/default/download'),
             (T('Support'), False,
              'http://www.web2py.com/examples/default/support'),
             (T('Demo'), False, 'http://web2py.com/demo_admin'),
             (T('Quick Examples'), False,
              'http://web2py.com/examples/default/examples'),
             (T('FAQ'), False, 'http://web2py.com/AlterEgo'),
             (T('Videos'), False,
              'http://www.web2py.com/examples/default/videos/'),
             (T('Free Applications'),
              False, 'http://web2py.com/appliances'),
             (T('Plugins'), False, 'http://web2py.com/plugins'),
             (T('Layouts'), False, 'http://web2py.com/layouts'),
             (T('Recipes'), False, 'http://web2pyslices.com/'),
             (T('Semantic'), False, 'http://web2py.com/semantic'),
             ]),
            (T('Documentation'), False, 'http://www.web2py.com/book', [
             (T('Preface'), False,
              'http://www.web2py.com/book/default/chapter/00'),
             (T('Introduction'), False,
              'http://www.web2py.com/book/default/chapter/01'),
             (T('Python'), False,
              'http://www.web2py.com/book/default/chapter/02'),
             (T('Overview'), False,
              'http://www.web2py.com/book/default/chapter/03'),
             (T('The Core'), False,
              'http://www.web2py.com/book/default/chapter/04'),
             (T('The Views'), False,
              'http://www.web2py.com/book/default/chapter/05'),
             (T('Database'), False,
              'http://www.web2py.com/book/default/chapter/06'),
             (T('Forms and Validators'), False,
              'http://www.web2py.com/book/default/chapter/07'),
             (T('Email and SMS'), False,
              'http://www.web2py.com/book/default/chapter/08'),
             (T('Access Control'), False,
              'http://www.web2py.com/book/default/chapter/09'),
             (T('Services'), False,
              'http://www.web2py.com/book/default/chapter/10'),
             (T('Ajax Recipes'), False,
              'http://www.web2py.com/book/default/chapter/11'),
             (T('Components and Plugins'), False,
              'http://www.web2py.com/book/default/chapter/12'),
             (T('Deployment Recipes'), False,
              'http://www.web2py.com/book/default/chapter/13'),
             (T('Other Recipes'), False,
              'http://www.web2py.com/book/default/chapter/14'),
             (T('Buy this book'), False,
              'http://stores.lulu.com/web2py'),
             ]),
            (T('Community'), False, None, [
             (T('Groups'), False,
              'http://www.web2py.com/examples/default/usergroups'),
                        (T('Twitter'), False, 'http://twitter.com/web2py'),
                        (T('Live Chat'), False,
                         'http://webchat.freenode.net/?channels=web2py'),
                        ]),
                (T('Plugins'), False, None, [
                        ('plugin_wiki', False,
                         'http://web2py.com/examples/default/download'),
                        (T('Other Plugins'), False,
                         'http://web2py.com/plugins'),
                        (T('Layout Plugins'),
                         False, 'http://web2py.com/layouts'),
                        ])
                ]
         )]
if DEVELOPMENT_MENU: _()

if "auth" in locals(): auth.wikimenu()
