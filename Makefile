all: test

export SQLALCHEMY_DATABASE_URI:=mysql://root@localhost/conaudio_db_local

test: prepare web

prepare:
	@pip install -U pip
	@pip install -r development.txt
	@npm install

clean:
	@git clean -Xdf # removing files that match patterns inside .gitignore

web:
	npm run build

run:
	tumbler run

migrate-forward:
	@[ "$(reset)" == "yes" ] && echo "drop database if exists conaudio_db_local;create database conaudio_db_local" | mysql -uroot || echo "Running new migrations..."
	@alembic upgrade head

migrate-back:
	@alembic downgrade -1

db:
	echo "drop database if exists conaudio_db_local;create database conaudio_db_local" | mysql -uroot
	python manage.py db

docs:
	markment -t .theme spec
	open "`pwd`/_public/index.html"

prod-simulation:
       PYTHONPATH=`pwd` PORT="4000" DOMAIN="0.0.0.0" REDIS_URI="redis://localhost:6379" gunicorn --worker-class conaudio.upstream.WebsocketsSocketIOWorker conaudio.server:application

static:
	bower install
