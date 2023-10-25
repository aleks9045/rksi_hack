from sqlalchemy import Table, Column, MetaData, Integer, String, Boolean

metadata = MetaData()

user = Table(
    'user',
    metadata,
    Column('id', type_=Integer, primary_key=True),
    Column('email', String, nullable=False, unique=True),
    Column('name', String(16), nullable=False),
    Column('is_admin', Boolean, nullable=False),
    Column('photo', String, nullable=True),
    Column("hashed_password", String(length=1024), nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False)
)
