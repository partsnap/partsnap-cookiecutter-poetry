""" CLI for API interface

    - Author: {{cookiecutter.author}}
    - Email: {{cookiecutter.email}}
    - License: {{cookiecutter.license_released_under}}
"""

from fastapi import Depends

from .database import ps_db_session

basic_dependencies = [Depends(ps_db_session)]
