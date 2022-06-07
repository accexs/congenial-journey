from typing import List, Optional

from app.models.pydantic import (SummaryPayloadSchema,
                                 SummaryUpdatePayloadSchema)
from app.models.tortoise import TextSummary


async def post(payload: SummaryPayloadSchema) -> TextSummary:
    summary = TextSummary(
        url=payload.url,
        summary="dummy summary",
    )
    await summary.save()
    return summary


async def get(summary_id: int) -> Optional[TextSummary]:
    summary = await TextSummary.filter(id=summary_id).first()
    if summary:
        return summary
    return None


async def get_all() -> List[TextSummary]:
    return await TextSummary.all()


async def put(
    summary_id: int, payload: SummaryUpdatePayloadSchema
) -> Optional[TextSummary]:
    summary = await TextSummary.filter(id=summary_id).update(
        url=payload.url, summary=payload.summary
    )
    if summary:
        return await TextSummary.filter(id=summary_id).first()
    return None


async def delete(summary_id: int) -> None:
    await TextSummary.filter(id=summary_id).delete()
