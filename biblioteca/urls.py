from django.urls import path, include
from biblioteca import views

from rest_framework_simplejwt import views as jwt_views

from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

urlpatterns = [
     path('funcionarios/', views.FuncionarioList.as_view(),
          name=views.FuncionarioList.name),
     path('funcionarios/<int:pk>/', views.FuncionarioDetail.as_view(),
          name=views.FuncionarioDetail.name),
     path('autores/', views.AutorList.as_view(),
          name=views.AutorList.name),
     path('autores/<int:pk>/', views.AutorDetail.as_view(),
          name=views.AutorDetail.name),
     path('livros/', views.LivroList.as_view(),
          name=views.LivroList.name),
     path('livros/<int:pk>/', views.LivroDetail.as_view(),
          name=views.LivroDetail.name),
     path('leitores/', views.LeitorList.as_view(),
          name=views.LeitorList.name),
     path('leitores/<int:pk>/', views.LeitorDetail.as_view(),
          name=views.LeitorDetail.name),
     path('emprestimos/', views.EmprestimoList.as_view(),
          name=views.EmprestimoList.name),
     path('emprestimos/<int:pk>/', views.EmprestimoDetail.as_view(),
          name=views.EmprestimoDetail.name),
     path('reservas/', views.ReservaList.as_view(),
          name=views.ReservaList.name),
     path('reservas/<int:pk>/', views.ReservaDetail.as_view(),
          name=views.ReservaDetail.name),
     path('users/', views.UserList.as_view(),
          name=views.UserList.name),
     path('users/<int:pk>/', views.UserDetail.as_view(),
          name=views.UserDetail.name),

     path('', views.ApiRoot.as_view(),
          name=views.ApiRoot.name),

     path('api/token/', 
         jwt_views.TokenObtainPairView.as_view(), 
         name ='token_obtain_pair'), 
     path('api/token/refresh/', 
         jwt_views.TokenRefreshView.as_view(), 
         name ='token_refresh'), 

     path('openapi/', get_schema_view(
          title="Biblioteca",
          description="API de uma biblioteca"), name='openapi-schema'),

     path('docs/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}), name='swagger-ui'),

     ]
