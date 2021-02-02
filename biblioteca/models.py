from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(max_length=200)

    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome

class Autor(models.Model):
    nome = models.CharField(max_length=200)

    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    localizacao = models.TextField()
    nome_autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome

class Leitor(models.Model):
    nome = models.CharField(max_length=200)

    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome

class Emprestimo(models.Model):
    leitor = models.ForeignKey(Leitor, on_delete=models.CASCADE)
    livros = models.ForeignKey(Livro, on_delete=models.CASCADE)
    funcionarios = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    data_emprestimo = models.DateField()
    data_prevista_devolucao = models.DateField()
    data_devolucao = models.DateField()

class Reserva(models.Model):
    leitor = models.ForeignKey(Leitor, on_delete=models.CASCADE)
    livros = models.ForeignKey(Livro, on_delete=models.CASCADE)
    data_reserva = models.DateField()
    status = models.CharField(max_length=200)