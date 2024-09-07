from typing import List
from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy import String

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

# We start by declaring a base class and is created by making a simple subclass against the DeclarativeBase class.
class Base(DeclarativeBase):
    pass

# ------------- Base Class and Mapped Classes -------------
# After creating the Base class, we can individual mapped classes that inherit this base class
# Each Mapped Class is a Table the name of which is indicated by using the __tablename__ class-level attribute.

# Next, columns that are part of the table are declared, by adding attributes that include a special 
# typing annotation called Mapped. The name of each attribute corresponds to the column that is to be part of the database table.

# The datatype of each column is taken first from the Python datatype that’s associated with each Mapped 
# annotation; int for INTEGER, str for VARCHAR, etc. Nullability derives from whether or not the Optional[] type modifier is used.

# Each table aka Mapped class must have a column with primary key set too True, i.e. mappend_column(primary=True)

# This is a Mapped Class, it creates a table called "user_account"
class User(Base):
    __tablename__ = "user_account" 
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]

    # In contrast to the column-based attributes, relationship() denotes a linkage between two ORM classes
    # User.addresses links User to Address, and Address.user links Address to User. 
    addresses: Mapped[List["Address"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

class Address(Base):
    __tablename__ = "address"
    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))

    # In contrast to the column-based attributes, relationship() denotes a linkage between two ORM classes
    user: Mapped["User"] = relationship(back_populates="addresses")

    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"
    
# Now to create the Above tables, we head to the 02-create-engine.py