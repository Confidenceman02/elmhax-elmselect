# ElmHax

> [!IMPORTANT]
> This project assumes you have the Elm compiler installed.
>
> Get it [here](https://guide.elm-lang.org/install/elm.html) if not.

## Start project

Start a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install python packages

```bash
pip install -r requirements.txt
```

## Migrate

```bash
python manage.py makemigrations
python manage.py migrate
```

## Install npm packages

> [!IMPORTANT]
> This project assumes you have pnpm.
>
> Get it [here](https://pnpm.io/installation) if not.

```bash
python manage.py djelm npm elm_programs install
```

## Watch and compile

```bash
python manage.py djelm watch elm_programs
```

## Start server

```bash
python manage.py runserver
```

## Open browser

`localhost:8000/promotion`
