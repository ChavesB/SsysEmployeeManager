Autor: Bruno Costa

No teste de codificação django admin foi feito o painel para gerenciar os funcionários com as funções de listar, adicionar e remover.

Foi criado a api django com as funcionalidades de listar, adicionar e remover. Comandos para acessar api:

-> Listar: curl -H "Content-Type: application/javascript" http://localhost:8000/employee/

-> Adicionar: curl -i -d "name=value1&email=value2&department=value3" http://localhost:8000/employee/add/

-> Remover: curl -i -d "name=value1&email=value2&department=value3" http://localhost:8000/employee/remove/


--- Para executar a aplicação django ---

Comandos para instalar aplicação (Linux):

-> Criar um ambiente virtual: #$ python3 -m venv myvenv

-> Ativar o ambiente virtual: #$ source myvenv/bin/activate

-> Baixar o repositório do git

-> Dentro da pasta do repositório: .../SsysEmployeeManager$ pip install -r requirements.txt

-> Depois de instalado: .../SsysEmployeeManager/$ python manage.py migrate

-> Executar: .../SsysEmployeeManager/$ pyhton manage.py runserver
