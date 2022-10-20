#PROJECT SETUP

1 activate vertualenv = source venv/bin/activate

2 intall all requirement = pip3 install -r requirements.txt

3 run project = python3 manage.py runserver

4 admin-pannel = http://127.0.0.1:8000/admin/

username = admin

password = admin

#Api-Endpoint

#User-module

register_user = http://127.0.0.1:8000/user/register/

its give you a access token and refresh token

login_user = http://127.0.0.1:8000/user/login/ its give you a access token and refresh token

#Todo-module

get-todo = http://127.0.0.1:8000/app/api/

about this api = when you send your jwt token its show your todo only

post-todo = http://127.0.0.1:8000/app/api/

In post api you can create your own todo you need to add your access token in bearer_token its takes your userid throu your jwt so you only pass #title and #body

ex:- { "title" : "test", "body" : "Hye, my name is sumit kumar roy. " }

edit-todo = http://127.0.0.1:8000/app/api/

In edit todo you pass your jwt token and #todo_id and what you want to change in #body and #title

ex:- { "todo" : 1, "body" : "updated" }

delete-todo = http://127.0.0.1:8000/app/api/

pass your todo_id and access token

ex:- { "todo" : 1 }

#work on this module

1 first i create a custom user

2 then i add jwt authantication

3 then i crete todo application

#how this all are work

first a create user using #register_user api ,register api gives in access token and refresh token ,and #login_user also give me assess and refresh token using this token we create our todo using #post-todo then after we get our todo using #get-todo api this api show your todo only ,not all todo you can access your todo only through jwt token after get you are usig edit #edit-todo api this api edit your todo, you only pass todo_id in body then delete-todo you only pass your todo_id in body and todo deleted
