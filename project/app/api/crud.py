from typing import Optional, List

from app.models.pydantic import SummaryPayloadSchema
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
