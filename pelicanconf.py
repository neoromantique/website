AUTHOR = 'neoromantique'
SITENAME = 'nrmntq'
SITEURL = ''
SITESUBTITLE = 'Builder · Tinkerer'

PATH = 'content'
OUTPUT_PATH = 'output'
TIMEZONE = 'Europe/Warsaw'
DEFAULT_LANG = 'en'

THEME = 'theme/neotheme'
THEME_STATIC_DIR = 'theme'

# URL structure (matches current site)
ARTICLE_URL = 'blog/{slug}/'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'
ARCHIVES_SAVE_AS = 'blog.html'
INDEX_SAVE_AS = 'index.html'

# Disable unwanted pages
AUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
TAG_SAVE_AS = ''

# Static paths
STATIC_PATHS = ['images', 'extra/david.pdf']
EXTRA_PATH_METADATA = {
    'extra/david.pdf': {'path': 'david.pdf'},
}

# Markdown extensions (preserve HTML blocks)
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

# Feeds disabled for dev
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
