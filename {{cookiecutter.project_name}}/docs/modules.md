{%- if cookiecutter.template_type == 'web-service' %}
::: {{cookiecutter.project_slug}}.foo
{%- else %}
::: {{cookiecutter.project_slug}}
{%- endif %}
