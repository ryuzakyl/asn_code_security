# asn_code_security
Testing security measures in Django

## Authors
* Victor M. Mendiola Lau <[ryuzakyl@gmail.com](mailto:ryuzakyl@gmail.com)>
* Madelin Díaz Ramos <[madelinkind@gmail.com](mailto:madelinkind@gmail.com)>

## Development stack details:
* Python 3.6.x
* Django 2.2.7
* SQLite 3

## How to run
1. git clone https://github.com/ryuzakyl/asn_code_security
2. cd asn_code_security
3. docker-compose up -d
4. Open browser at [http://localhost:8000](http://localhost:8000)

## References
1. Docker docs for Django and Compose. [Quickstart: Compose and Django](https://docs.docker.com/compose/django/)
2. StackOverflow [Post](https://stackoverflow.com/questions/14647723/django-forms-if-not-valid-show-form-with-error-message)
regarding custom field validation in forms.
3. StackOverflow [Post](https://stackoverflow.com/questions/3289860/how-can-i-embed-django-csrf-token-straight-into-html)
regarding CSRF token usage in Django view.
4. Django [docs](https://docs.djangoproject.com/en/2.2/ref/templates/language/#automatic-html-escaping) regarding *Cross Site Scripting (XSS)* protection.
