django-admin-twitter-bootstrap
==============================

Django admin templates that are compatible with Twitter Bootstrap version 2.

## Usage

1. Clone the repository into your Django project.
2. Add the path to 'admin_bootstrap/templates' to your `TEMPLATE_DIRS` setting.
3. Add 'admin_bootstrap' to your `INSTALLED_APPS` setting.
4. Run `python manage.py collectstatic`.

Alternatively to #2, you can symlink the 'admin', 'admin_doc' and 'registration' folders in 'admin_bootstrap/templates' to your templates folder.

_This has only been tested in Django 1.4._

## TODO

* Test more Django form field types and admin options.

## LICENSE

Offered under a [BSD 3 Clause License](https://github.com/dryan/django-admin-twitter-bootstrap/blob/master/LICENSE).
