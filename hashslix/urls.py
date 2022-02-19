"""hashslix URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# comando geral de links do projeto
urlpatterns = [
    path('admin/', admin.site.urls),
    # foi definido uma url para inicio de página tipo home, apontando para app.py do app (filme.urls)
    # se fosse colocado "filme/" como no exemplo do admin, a url teria o nome: http://xxxxxx/filme como principal...
    # se a url principal aponta para o arquivo urls.py de app será necessário configurar os links gerais do app.
    # namespace identificador de urls de app filme, app_name = 'filme'
    path('', include('filme.urls', namespace='filme')),

]
# administrador carregar imagens
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# permissão para usuários/admin enviar imagens
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
