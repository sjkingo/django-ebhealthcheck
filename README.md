# django-ebhealthcheck

By default, Elastic Beanstalk's health check system uses the public IP of each
load balanced instance as the request's host header when making a request.
Unless added to `ALLOWED_HOSTS`, this causes Django to return a `400 Bad
Request` and a failed health check.

This app dynamically adds your instance's public IP address to Django's
`ALLOWED_HOSTS` setting to permit health checks to succeed.

Note this only adds the host to settings - the health check system still
requires `/` to return `200 OK`, unless configured differently in EB.

## Installation

Simply add `ebhealthcheck` to your `INSTALLED_APPS`:

```
INSTALLED_APPS = [
    ...
    'ebhealthcheck',
    ...
]
```
