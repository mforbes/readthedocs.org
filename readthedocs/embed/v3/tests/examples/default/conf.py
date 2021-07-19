# conf.py to run tests

master_doc = 'index'
extensions = [
    'sphinx.ext.autosectionlabel',
]

try:
    import sphinxcontrib.bibtex
    extensions.append('sphinxcontrib.bibtex')
    bibtex_bibfiles = ['refs.bib']
except ImportError:
    pass


def setup(app):
    app.add_object_type(
        'confval',  # directivename
        'confval',  # rolename
        'pair: %s; configuration value',  # indextemplate
    )
