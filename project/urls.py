from django.contrib import admin
from django.urls import path
from app.views import home, create, store, painel, dologin, dashboard, logouts, changePassword, index
from app.views import form, view, edit, update, delete
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('create/', create),
    path('store/', store),
    path('painel/', painel),
    path('dologin/', dologin),
    path('dashboard/', dashboard),
    path('logouts/', logouts),
    path('password/', changePassword),
    path('index/', index),
    path('form/', form, name='form'),
    path('createLivro/', create, name='createLivro'),
    path('view/<int:pk>/', view, name='view'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),

]
