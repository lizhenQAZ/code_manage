from distutils.core import setup


# setup_keywords = ('distclass', 'script_name', 'script_args', 'options',
#                   'name', 'version', 'author', 'author_email',
#                   'maintainer', 'maintainer_email', 'url', 'license',
#                   'description', 'long_description', 'keywords',
#                   'platforms', 'classifiers', 'download_url',
#                   'requires', 'provides', 'obsoletes',
#                   )
info = {
    "name": "liZhen",
    "version": "1.0",
    "author": "liZhen",
    "description": "liZhen's module",
    "py_modules": ["suba.aa", "suba.bb", "subb.cc", "subb.dd"]
}
setup(**info)
