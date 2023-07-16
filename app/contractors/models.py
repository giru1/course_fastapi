from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Organization(Base):
    __tablename__ = 'organization'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]


class Contractors(Base):
    """
    Модель контрагентов
    """
    __tablename__ = 'contractors'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    inn: Mapped[int] = mapped_column(nullable=False)
    kpp: Mapped[int] = mapped_column(nullable=False)
    address_juridical: Mapped[str]
    address_actual: Mapped[str]
    phone: Mapped[str]
    email: Mapped[str] = mapped_column(nullable=False)
    hide: Mapped[bool] = True

    # id_type_organization: Mapped[int] = mapped_column(ForeignKey("type_organization.id"))
    # type_organization: Mapped["type_organization"] = relationship(back_populates='contractors')
    #
    # organization_id: Mapped[int] = mapped_column(ForeignKey("organization.id"))
    # organization: Mapped["organization"] = relationship(back_populates='contractors')

    # def __str__(self):
    #     return f"contractors(" \
    #            f"id={self.id}, " \
    #            f"name={self.name}, " \
    #            f"inn={self.inn}, " \
    #            f"kpp={self.kpp}, " \
    #            f"address_juridical={self.address_juridical}, " \
    #            f"address_actual={self.address_actual}, " \
    #            f"phone={self.phone}, " \
    #            f"email={self.email}, " \
    #            f"hide={self.hide})"
    #
    # def __repr__(self):
    #     return str(self)
