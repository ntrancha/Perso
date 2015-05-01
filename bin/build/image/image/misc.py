#-*- coding: UTF-8 -*-

from django.core.urlresolvers import reverse

from image.views import image as image_view
from image.utils import image_create_token


def get_image_url(image, parameters):
    if 'autogen=true' in parameters:
        image_view(None, str(image), parameters, True)
    
    return reverse(
        'image.views.image',
        args=(
            unicode(image),
            image_create_token(parameters)
        )
    )


