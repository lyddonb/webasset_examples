from django_assets import Bundle, register

js = Bundle(
    'js/jquery-1.9.1.js',
    'js/bootstrap.js',
    'js/underscore.js',
    'js/backbone.js',
    filters='jsmin',
    output='asset_demo/static/lib.js'
)

css = Bundle(
    'css/bootstrap.css',
    'css/bootstrap-responsive.css',
    filters='cssmin',
    output='asset_demo/static/lib.css'
)

register('js_all', js)
register('css_all', css)
