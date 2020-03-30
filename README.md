# COVID-19-Reporting

A web application for reporting COVID 19 data, using Postman's [API](https://documenter.getpostman.com/view/10808728/SzS8rjbc?version=latest).

## Project Goal
***

Build a database, and web client, to store global data for the SARS2-CoV-2 (Covid 19) pandemic, using [Postman's APIs](https://documenter.getpostman.com/view/10808728/SzS8rjbc?version=latest).

## Core Tools
***

- Python
- PostgreSQL
- Django
- Pandas
- Requests

## Project Setup
*** 

**How to setup the project locally on one's own machine:**

Required Technologies:

- Python 3
- PostgreSQL

Steps:

- Clone repository.
- Open a terminal, and cd into repo.
- Create, and activate a `venv`.
- Run `pip install -r requirements.txt` to install dependencies.
- Create a `.env` file, and add the necessary environment variables, in the same directory as `manage.py`.
- Once you have created a db in Postgres, run migrations.
- Run the `python manage.py runserver` (with `venv` activated) from a terminal to bootstrap the web application.

## Future Goals
***

- Setup an automated pipeline to keep data up-to-date
- Implement data visualization
