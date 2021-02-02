from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.throttling import ScopedRateThrottle
from .models import Funcionario, Autor, Livro, Leitor, Emprestimo, Reserva
from .serializers import FuncionarioSerializer, AutorSerializer, LivroSerializer, LeitorSerializer, EmprestimoSerializer, ReservaSerializer, UserSerializer

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from rest_framework import filters
from django_filters import NumberFilter, DateTimeFilter, AllValuesFilter

class FuncionarioList(generics.ListCreateAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    name = 'funcionario-list'
    throttle_scope = 'funcionarios'
    throttle_classes = (ScopedRateThrottle,)
    filter_fields = ('nome',)
    search_fields = ('^nome',)
    ordering_fields = ('nome',)


class FuncionarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    name = 'funcionario-detail'
    throttle_scope = 'funcionarios'
    throttle_classes = (ScopedRateThrottle,)

class AutorList(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    name = 'autor-list'
    throttle_scope = 'autores'
    throttle_classes = (ScopedRateThrottle,)
    filter_fields = ('nome',)
    search_fields = ('^nome',)
    ordering_fields = ('nome',)

class AutorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    name = 'autor-detail'
    throttle_scope = 'autores'
    throttle_classes = (ScopedRateThrottle,)

class LivroList(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    name = 'livro-list'
    throttle_scope = 'livros'
    throttle_classes = (ScopedRateThrottle,)
    filter_fields = ('nome', 'descricao', 'localizacao', 'nome_autor')
    search_fields = ('^nome',)
    ordering_fields = ('nome',)

class LivroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    name = 'livro-detail'
    throttle_scope = 'livros'
    throttle_classes = (ScopedRateThrottle,)

class LeitorList(generics.ListCreateAPIView):
    queryset = Leitor.objects.all()
    serializer_class = LeitorSerializer
    name = 'leitor-list'
    throttle_scope = 'leitores'
    throttle_classes = (ScopedRateThrottle,)

class LeitorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Leitor.objects.all()
    serializer_class = LeitorSerializer
    name = 'leitor-detail'
    throttle_scope = 'leitores'
    throttle_classes = (ScopedRateThrottle,)

class EmprestimoList(generics.ListCreateAPIView):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer
    name = 'emprestimo-list'
    permission_classes = (IsAuthenticated,)

class EmprestimoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer
    name = 'emprestimo-detail'
    permission_classes = (IsAuthenticated,)

class ReservaList(generics.ListCreateAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    name = 'reserva-list'
    permission_classes = (IsAuthenticated,)

class ReservaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    name = 'reserva-detail'
    permission_classes = (IsAuthenticated,)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'
    

class UserList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
    name = 'user-list'

class ApiRoot(generics.GenericAPIView):

    name = 'api-root'

    def get_serializer_class(self, *args, **kwargs):
        try:
            return Response({
            'funcionarios': reverse(FuncionarioList.name, request=request),
            'autores': reverse(AutorList.name, request=request),
            'livros': reverse(LivroList.name, request=request),
            'leitores': reverse(LeitorList.name, request=request),
            'emprestimos':reverse(EmprestimoList.name, request=request),
            'reservas':reverse(ReservaList.name, request=request),
            'users': reverse(UserList.name, request=request),})
        except( KeyError, AttributeError):
            return super().get_serializer_class()  

    #def get(self, request,*args, **kwargs):
        #return Response({
            #'funcionarios': reverse(FuncionarioList.name, request=request),
            #'autores': reverse(AutorList.name, request=request),
            #'livros': reverse(LivroList.name, request=request),
            #'leitores': reverse(LeitorList.name, request=request),
            #'emprestimos':reverse(EmprestimoList.name, request=request),
            #'reservas':reverse(ReservaList.name, request=request),
            #'users': reverse(UserList.name, request=request),
        #})