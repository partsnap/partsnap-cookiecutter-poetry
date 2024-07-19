""" Sample Data Model

    - Author: {{cookiecutter.author}}
    - Email: {{cookiecutter.email}}
    - License: {{cookiecutter.license_released_under}}
"""

import contextlib
from typing import Union

from fastapi import status as http_status
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError, NoResultFound
from sqlmodel import Session, select

import {{cookiecutter.project_slug}}.model.db_crud as db_crud
from {{cookiecutter.project_slug}}.api_model.sample import SampleAPIModelCreate, SampleAPIModelRead, SampleAPIModelUpdate
from {{cookiecutter.project_slug}}.db_tables import {{cookiecutter.project_slug}}DBTables
from {{cookiecutter.project_slug}}.logging import psnap_get_logger

LOGGER = psnap_get_logger("model.sample")

__all__ = ["SampleDBModel"]


class SampleDBModel(SampleAPIModelRead, table=True):
    __tablename__ = {{cookiecutter.project_slug}}DBTables.samples

    @classmethod
    def create(
        cls, db_session: Session, sample_model: SampleAPIModelCreate
    ) -> Union["SampleDBModel", JSONResponse]:
        db_error_handling = {}  # type: ignore[var-annotated]
        response = db_crud.create(
            model_cls=SampleDBModel,  # type: ignore[arg-type]
            db_session=db_session,
            logger=LOGGER,
            data=sample_model,  # type: ignore[arg-type]
            db_error_handling=db_error_handling,  # type: ignore[arg-type]
        )
        if isinstance(response, SampleDBModel):
            # First we create the read model instance
            tmp = SampleAPIModelRead(**response.model_dump())
            return tmp  # type: ignore[return-value]
        else:
            return response  # type: ignore[return-value]

    @classmethod
    def update(
        cls, db_session: Session, sample_id: str | int, sample_model: SampleAPIModelUpdate,
    ) -> Union["SampleDBModel", JSONResponse]:
        db_error_handling = {
            NoResultFound: db_crud.DBErrorHandling(
                http_status=http_status.HTTP_404_NOT_FOUND, msg=f"Sample {sample_id} not found!"
            )
        }

        data = sample_model.model_dump()

        statement = select(SampleDBModel).where(sample_id == SampleDBModel.id)
        with contextlib.suppress(ValueError):
            statement = select(SampleDBModel).where(SampleDBModel.id == int(sample_id))
        response = db_crud.update(
            model_cls=SampleDBModel,  # type: ignore[arg-type]
            db_session=db_session,
            logger=LOGGER,
            query_statement=statement,
            data=data,  # type: ignore[arg-type]
            db_error_handling=db_error_handling,  # type: ignore[arg-type]
        )

        if isinstance(response, SampleDBModel):
            # First we create the read model instance
            tmp = SampleAPIModelRead(**response.model_dump())
            return tmp  # type: ignore[return-value]
        else:
            return response  # type: ignore[return-value]

    @classmethod
    def delete(cls, db_session: Session, sample_id: str | int) -> SampleAPIModelRead | JSONResponse:
        db_error_handling = {
            NoResultFound: db_crud.DBErrorHandling(
                http_status=http_status.HTTP_404_NOT_FOUND, msg=f"Sample {sample_id} not found!"
            )
        }

        statement = select(SampleDBModel).where(sample_id == SampleDBModel.id)
        with contextlib.suppress(ValueError):
            statement = select(SampleDBModel).where(SampleDBModel.id == int(sample_id))
        response = db_crud.delete(
            model_cls=SampleDBModel,  # type: ignore[arg-type]
            db_session=db_session,
            logger=LOGGER,
            query_statement=statement,
            db_error_handling=db_error_handling,  # type: ignore[arg-type]
        )

        if isinstance(response, SampleDBModel):
            return SampleAPIModelRead(**response.model_dump())
        else:
            return response  # type: ignore[return-value]

    @classmethod
    def get(
        cls, db_session: Session, sample_id: str | int | None = None, db_model: bool = False
    ) -> SampleAPIModelRead | JSONResponse | list[SampleAPIModelRead]:
        db_error_handling = {
            NoResultFound: db_crud.DBErrorHandling(
                http_status=http_status.HTTP_404_NOT_FOUND, msg=f"Sample {sample_id} not found!"
            )
        }
        statement = None
        if sample_id or sample_id == 0:
            statement = select(SampleDBModel).where(sample_id == SampleDBModel.id)
            with contextlib.suppress(ValueError):
                statement = select(SampleDBModel).where(SampleDBModel.id == int(sample_id))

        response = db_crud.get(
            model_cls=SampleDBModel,  # type: ignore[arg-type]
            db_session=db_session,
            logger=LOGGER,
            query_statement=statement,
            db_error_handling=db_error_handling,  # type: ignore[arg-type]
        )
        if db_model:
            return response  # type: ignore[return-value]

        if isinstance(response, SampleDBModel):
            tmp = SampleAPIModelRead(**response.model_dump())
            return tmp
        elif isinstance(response, list):
            record_list = []
            for record_obj in response:
                record_list.append(SampleAPIModelRead(**record_obj.model_dump()))
            return record_list
        return response  # type: ignore[return-value]