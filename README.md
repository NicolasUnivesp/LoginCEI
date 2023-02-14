# LoginCEI
login funcionando para o projeto bibliotecaCEI


para rodar basta:

Ativar ambiente:
  venv/Scripts
  activate
pip install -r requirements.txt
(usei WampServer para reproduzir o erro é necessario, o wamp exige pacotes c++ VSC 20** atualizados)
pip install mysqlclient
python manage.py migrate
python manage.py runserver

para reproduzir o erro:
>login>acervo>adicionar>salvar

erro:

[13/Feb/2023 23:37:37] "GET /edit/8/ HTTP/1.1" 200 3339
Not Found: /edit/8/>/update8/
[13/Feb/2023 23:37:45] "POST /edit/8/%3E/update8/ HTTP/1.1" 404 3889




