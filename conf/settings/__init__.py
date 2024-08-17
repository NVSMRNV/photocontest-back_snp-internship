from decouple import config
from split_settings.tools import include


# base.py
include(
    'base.py',
    'database.py'
)
