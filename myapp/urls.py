from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('blog/',views.blog,name='blog'),
    path('contact/',views.contact,name='contact'),
    path('menu/',views.menu,name='menu'),
    path('services/',views.services,name='services'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('change-password/',views.change_password,name='change-password'),
    path('seller-add-pizza/',views.seller_add_pizza,name='seller-add-pizza'),
    path('seller-view-pizza-order/',views.seller_view_pizza_order,name='seller-view-pizza_order'),

]

