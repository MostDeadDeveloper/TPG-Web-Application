from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.views import LoginView

from core.views import LoginGenericView, GenericView, LoginListView

