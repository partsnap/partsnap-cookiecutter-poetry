""" CLI for API interface

    - Author: {{cookiecutter.author}}
    - Email: {{cookiecutter.email}}
    - License: {{cookiecutter.license_released_under}}
"""

import typer

import {{cookiecutter.project_slug}}.cli.api.samples as samples

api_app = typer.Typer(no_args_is_help=True)
api_app.add_typer(samples.app, name="samples", help="manage samples", no_args_is_help=True)
