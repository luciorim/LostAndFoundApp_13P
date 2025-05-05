up:
	docker-compose up -d --build

down:
	docker-compose down -v

logs:
	docker-compose logs -f

migrate:
	docker-compose exec django python manage.py migrate

collectstatic:
	docker-compose exec django python manage.py collectstatic --noinput