from pydantic import BaseModel, Field, ConfigDict


class DocumentCreate(BaseModel):
    title: str = Field(..., max_length=255, min_length=1)
    subject: str = Field(..., max_length=100, min_length=1)
    document_type: str = Field(..., max_length=50, min_length=1)
    file_url: str = Field(..., max_length=500, min_length=1)


class DocumentResponse(BaseModel):
    id: int
    title: str
    subject: str
    document_type: str
    file_url: str

    model_config = ConfigDict(from_attributes=True)