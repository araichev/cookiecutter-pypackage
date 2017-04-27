{{ cookiecutter.package_name }}
{{ cookiecutter.package_name|count * "*" }}

{% if cookiecutter.readme_travis_badge -%}
.. image:: {{ cookiecutter.readme_travis_url }}.png
   :target: {{ cookiecutter.readme_travis_url }}
   :alt: Latest Travis CI build status
{%- endif %}

{{ cookiecutter.package_description }}


Usage
======


Installation
=============


Authors
========
- {{ cookiecutter.author_name }}, {{ cookiecutter.date }}


History
========

{{ cookiecutter.package_version }}, {{ cookiecutter.date }}
------------------------------
- Initial release