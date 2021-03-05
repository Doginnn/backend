# DESAFIO EMPRESA X

Sistema como etapa de desafio de uma empresa.

Sistema de E-commerce para `'listar'` todos os produtos disponíveis. No modo `'edição'` é possível `'criar'` e `'apagar'` produtos.

## Dependências

- [Python](https://www.python.org/downloads/)
- [django](http://www.djangoproject.com)
- [django-rest-framework](https://pypi.org/project/djangorestframework/)
- [django-rest-swagger](https://django-rest-swagger.readthedocs.io/en/latest/)

## Instalação:

1. Instalar o Virtualenv ([Virtualenv](https://virtualenv.pypa.io/en/latest/index.html))
   ```bash
    python -m pip install --user virtualenv
    python -m virtualenv --help
   ```
   
2. Clone o projeto

    ```bash
   git clone https://github.com/Doginnn/backend.git
    ```

3. Crie uma virtualenv e instale as dependências

    ```bash
    cd backend
    python3 -m virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

    ```

4. Sincronize a base de dados

    ```bash
    python manage.py makemigrations
   python manage.py migrate
    ```
    
5. Crie um usuário (Administrador do sistema): Nesse caso o meu user ADM é `"teste"` e password ADM é `"123Teste!"`.

    ```bash
    python manage.py createsuperuser
    ```

6. Migre as novas modificações para o Banco de Dados e teste a instalação carregando o servidor de desenvolvimento (http://127.0.0.1:5000/ no navegador):

    ```bash
   python manage.py migrate
    python manage.py runserver
    ```
## Documentação

Para mais informações sobre a documentação da API acesse o end point `/docs/`:

   ```bash
   http://127.0.0.1:5000/docs/
   ```

## Créditos

- [Diógenes Dantas - Blog](https://doginnn.github.io/)
- [GitHub](https://github.com/Doginnn)
- [LinkedIn](https://www.linkedin.com/in/doginnn/)

## Ajuda

Para relatar bugs ou fazer perguntas utilize o [Issues](https://github.com/Doginnn/backend/issues) ou via email diogenesemmanuel@gmail.com
