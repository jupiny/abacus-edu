import os

from .base import BASE_DIR
from .base import PROJECT_ROOT_DIR


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# Media files
MEDIA_ROOT = os.path.join(
    PROJECT_ROOT_DIR,
    "dist",
    "media",
)

MEDIA_URL = '/media/'
