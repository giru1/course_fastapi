from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class TypeOrganization(Base):
    """
    Модлеь типа организации
    """
    __tablename__ = 'type_organization'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)

    def __str__(self):
        return f"contractors(id={self.id}, name={self.name})"

    def __repr__(self):
        return str(self)
