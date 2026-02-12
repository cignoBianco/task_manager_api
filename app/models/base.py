import uuid
from sqlalchemy.orm import declared_attr
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column

class UUIDMixin:
    @declared_attr
    def id(cls):
        return Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
