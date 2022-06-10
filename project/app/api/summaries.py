from typing import List

from fastapi import APIRouter, HTTPException, Path
from starlette.background import BackgroundTasks

from app.api import crud
from app.models.pydantic import (
    SummaryPayloadSchema,
    SummaryResponseSchema,
    SummaryUpdatePayloadSchema,
)
from app.models.tortoise import SummarySchema
from app.summarizer import generate_summary

router = APIRouter()


@router.post("/", response_model=SummaryResponseSchema, status_code=201)
async def create_summary(
    payload: SummaryPayloadSchema, background_tasks: BackgroundTasks
) -> SummaryResponseSchema:
    summary = await crud.post(payload)

    background_tasks.add_task(generate_summary, summary.id, payload.url)

    return SummaryResponseSchema(id=summary.id, url=summary.url)


@router.get("/{id_}/", response_model=SummarySchema, status_code=200)
async def read_summary(id_: int = Path(..., gt=0)) -> SummarySchema:
    summary = await crud.get(id_)
    if not summary:
        raise HTTPException(status_code=404, detail="Summary not found")
    return summary


@router.get("/", response_model=List[SummarySchema])
async def read_all_summaries() -> List[SummarySchema]:
    return await crud.get_all()


@router.put("/{id_}/", response_model=SummarySchema, status_code=200)
async def update_summary(
    payload: SummaryUpdatePayloadSchema, id_: int = Path(..., gt=0)
) -> SummarySchema:
    summary = await crud.put(id_, payload)
    if not summary:
        raise HTTPException(status_code=404, detail="Summary not found")
    return summary


@router.delete("/{id_}/", status_code=204)
async def delete_summary(id_: int = Path(..., gt=0)) -> None:
    deleted = await crud.delete(id_)
    if not deleted:
        raise HTTPException(status_code=404, detail="Summary not found")
