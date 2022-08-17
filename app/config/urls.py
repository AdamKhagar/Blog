from django.urls import path, include

from config.admin import admin_site

urlpatterns = [
    path('admin/', admin_site.urls),
    path('auth/', include(('auth.urls', 'auth'), namespace ='auth'), name='auth'),
    path('', include(('main.urls', 'main'), namespace = 'main'), name='main')
]
