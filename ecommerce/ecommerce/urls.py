"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from shop_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('cart/', views.cart, name="cart"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('order-complete/', views.order_complete, name="order_complete"),
    path('product/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('register/', views.register, name="register"),
    path('search-result/', views.search_result, name="search_result"),
    path('signin/', views.signin, name="signin"),
    path('store/', views.store, name="store"),
    path('store/<slug:category_slug>/', views.store, name="products_by_category"),
    path('place_order/', views.place_order, name="place_order"),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
