from django.contrib.admin import apps, AdminSite
from django.contrib import admin


class AdminConfig(apps.AdminConfig):
    default_site = "config.admin.MyAdminSite"
    label = 'admin'

class MyAdminSite(AdminSite):
    site_title = "Blog"
    site_header = "Django based blog"

admin_site = MyAdminSite()

def register(*models):
    return admin.register(*models, site=admin_site)

