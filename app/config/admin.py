from django.contrib.admin import apps, AdminSite
from django.utils.translation import gettext_lazy as _
from django.contrib import admin


class AdminConfig(apps.AdminConfig):
    default_site = "config.admin.MyAdminSite"
    label = 'admin'


class MyAdminSite(AdminSite):
    site_title = _("Blog")
    site_header = _("Blog")


admin_site = MyAdminSite()


def register(*models):
    return admin.register(*models, site=admin_site)

