from decouple import config
from split_settings.tools import include


# base.py
include(
    'base.py',   
)


# dev or prod  
if config('DJANGO_ENV') == 'dev':
    include('dev.py')
elif config('DJANGO_ENV') == 'prod':
    include('prod.py')