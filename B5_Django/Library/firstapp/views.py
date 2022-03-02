from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

import logging
logger = logging.getLogger("firstapp")


def firstapp_home(request):
    logger.info(f"{request.user} -- {request.build_absolute_uri()}")
    return HttpResponse("Hello .. m in firstapp_home")