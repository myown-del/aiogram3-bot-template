generate:
	alembic revision --autogenerate

migrate:
	alembic upgrade head

start-new-app:
    docker compose up -d --build

start-app:
	docker compose up -d

stop-app:
	docker compose stop && docker compose rm --force

start-db:
	docker compose up -d postgres

stop-db:
	docker compose stop postgres && docker compose rm postgres --force