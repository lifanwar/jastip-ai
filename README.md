# Django Starter (apps/ + Tailwind)

Starter setup best practice Django:

- `apps/` all apps django start here
- `config/settings/` switch: `base`, `dev`, `staging`, `prod`
- move env just edit in .env `DJANGO_ENV=dev|staging|prod`
- frontend integration with `django-tailwind`, `alpinejs` 

## Tree base project

```text
.
├── manage.py
├── shell.nix
├── apps/
├── theme/
├── static/
└── config/
    └── settings/
        ├── __init__.py
        ├── base.py
        ├── dev.py
        ├── staging.py
        └── prod.py
```

## Switch Environment

`Rename env.example to .env`

```bash
DJANGO_ENV=prod/dev/staging
```

## Make New App (in `apps/`)

```bash
python manage.py startapp yournewapps apps/yournewapps
```

or simply in nixos:
```bash
nix-shell
```
> **Note:** `nix-shell` automatically creates a Python virtual environment in the `venv` folder and activates it.

Then:
```bash
startapp <appname>    # python manage.py startapp <appname> apps/<appname>
tw-install            # python manage.py tailwind install
tw-watch              # python manage.py tailwind start
run                   # python manage.py runserver 0.0.0.0:8000
```


sign up yournewapps in: `LOCAL_APPS` ( `config/settings/base.py`):

```py
LOCAL_APPS = [
    "apps.yournewapps"
]
```

Update file apps in: `apps.yournewapps.app.py`

```py
name = 'yournewapps'
```

To:

```py
name = 'apps.yournewapps'
```


## Instalation Django + tailwindcss built in

Install:

```bash
pip install -r requirements.txt
```

`tailwindcss apps in`
```py
THIRD_PARTY_APPS = [
    "tailwind",
    "theme",
]
```

Init + install + run Tailwind:

```bash
python manage.py tailwind install
python manage.py tailwind start
```

## Load Tailwind di Template

in templates (ex: `templates/base.html`):

```django
{% load tailwind_tags %}
{% tailwind_css %}
```

## Run Server

```bash
python manage.py runserver
```
