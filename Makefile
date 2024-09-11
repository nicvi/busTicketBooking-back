.PHONY: install run create-db run-db run-migrations

install:
	@echo "====================================Installing dependencies Performance================================="
	pip install --upgrade pip
	pip install -r requirements.txt
	pip install uvicorn
	@echo "Completed!"

run:
	@echo "====================================Running app================================="
	source .venv/bin/activate && python3 runner.py

create-db:
	@echo "====================================Create DB================================="
	docker run --name bus_ticket_booking_db -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=busTicketBooking -p 5439:5439 -d postgres:15
	@echo "Completed!"

run-db:
	@echo "====================================Running DB================================="
	docker compose up

run-migrations:
	@echo "====================================Running migrations================================="
	alembic upgrade head
	@echo "Completed!"