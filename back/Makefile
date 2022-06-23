all:
	@printf "Available commands: \n\
		make install: install requirements\n\
		make migrations : make migrations & migrate\n\
		make adminuser : create a superuser to access django admin\n\
		make run : launch django on localhost:8000\n\
	"

install: 
	python -m pip install requirements.txt

migrations: 
	python manage.py makemigrations
	python manage.py migrate

adminuser:
	python manage.py createsuperuser

run:
	python manage.py runserver
