# Trabalho final da disciplina de Programação Para Internet II
## Este trabalho corresponde a uma bilioteca e possui as entidades:
- Funcionário
- Livro
- Autor
- Leitor
- Emprestimo
- Reserva
## Configuração do ambiente:
Devem ser seguidos os comandos:
```python
    python manage.py makemigrations

    python manage.py migrate

    python manage.py runserver 8000

```
Para criar um super usuário:
```python
    python manage.py createsuperuser
```
## Tokens:
Acessar ```python http://localhost:8000/api/token/ ``` e obter o token de acesso
No header Authorization colocar : Bearer <token>

## Pacotes necessários:
- Python==3.8.0
- Django==3.1.5
- django-filter==2.4.0
- djangorestframework==3.12.2
- djangorestframework-simplejwt==4.6.0
- drf-spectacular==0.13.1