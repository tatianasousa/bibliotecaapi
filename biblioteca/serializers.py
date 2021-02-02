from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Funcionario, Autor, Livro, Leitor, Emprestimo, Reserva

class FuncionarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Funcionario
        fields = ('url', 'pk', 'nome')

class AutorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Autor
        fields = ('url', 'pk', 'nome')

class LivroSerializer(serializers.HyperlinkedModelSerializer):
    nome_autor = serializers.SlugRelatedField(queryset=Autor.objects.all(), slug_field='nome')
    class Meta:
        model = Livro
        fields = ('url', 'pk', 'nome', 'descricao', 'localizacao', 'nome_autor')

class LeitorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Leitor
        fields = ('url', 'pk', 'nome')

class EmprestimoSerializer(serializers.HyperlinkedModelSerializer):
    leitor = serializers.SlugRelatedField(queryset=Leitor.objects.all(), slug_field='nome')
    livros = serializers.SlugRelatedField(queryset=Livro.objects.all(), slug_field='nome')
    funcionarios = serializers.SlugRelatedField(queryset=Funcionario.objects.all(), slug_field='nome')

    class Meta:
        model = Emprestimo
        fields = ('url', 'pk', 'leitor', 'livros', 'funcionarios', 'data_emprestimo', 'data_prevista_devolucao', 'data_devolucao')

class ReservaSerializer(serializers.HyperlinkedModelSerializer):
    leitor = serializers.SlugRelatedField(queryset=Leitor.objects.all(), slug_field='nome')
    livros = serializers.SlugRelatedField(queryset=Livro.objects.all(), slug_field='nome')

    class Meta:
        model = Reserva
        fields = ('url', 'pk', 'leitor', 'livros', 'data_reserva', 'status')

class UserLivroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Livro
        fields = ('url', 'nome')

class UserEmprestimoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Emprestimo
        fields = ('url', 'pk')

class UserReservaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reserva
        fields = ('url', 'pk')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    livros = UserLivroSerializer(many=True, read_only=True)
    emprestimos = UserEmprestimoSerializer(many=True, read_only=True)
    reservas = UserReservaSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('url', 'pk', 'username', 'livros', 'reservas', 'emprestimos')