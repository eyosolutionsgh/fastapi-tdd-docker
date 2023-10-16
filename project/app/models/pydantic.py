from pydantic import AfterValidator, BaseModel, HttpUrl
from typing_extensions import Annotated

HttpUrlString = Annotated[HttpUrl, AfterValidator(lambda v: str(v))]


class SummaryPayloadSchema(BaseModel):
    url: HttpUrlString


class SummaryResponseSchema(SummaryPayloadSchema):
    id: int


class SummaryUpdatePayloadSchema(SummaryPayloadSchema):
    summary: str
