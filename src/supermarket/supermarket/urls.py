"""supermarket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
"""
    Imported views

-------
        database_upload
        show_database
        user_selection_save
        show_checked_products
        show_path
        choose_solver
-------

    Urls

-------
        /upload_database/
        /show_database/
        /user_selection/
        /user_checked_products/
        /show_path/
        /choose_solver/
-------

"""

from django.contrib import admin
from django.urls import path


from solvers.views import database_upload
from solvers.views import show_database
from solvers.views import user_selection_save
from solvers.views import show_checked_products
from solvers.views import show_path
from solvers.views import choose_solver


urlpatterns = [

    path('admin/', admin.site.urls),
    path('upload_database/', database_upload, name="products_upload"),
    path('show_database/', show_database, name="show_products"),
    path('user_selection/', user_selection_save, name="user_selection"),
    path('user_checked_products/', show_checked_products, name="user_checked_products"),
    path('show_path/', show_path, name="show_path"),
    path('choose_solver/', choose_solver, name="choose_solver"),
    path('', user_selection_save, name="user_selection")

]