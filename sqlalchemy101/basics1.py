# start of any SQLAlchemy app is an object called Engine.  It acts a source
# of conns to a particular db providing both a factory as well as holding space
# called a connection pool for db conns. Its a global obj i.e. created only
# once for a particular db as is configured using a URL string

# here we will use in-memory SQL Database4

from sqlalchemy import create_engine

# create_engine takes the URL and craetd the engine
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

# "sqlite+pysqlite:///:memory:" indicates 3 things
# 1. The database we are connecting with - sqlite
# 2. THE DBAPI we are using - pysqlite. DBAPI is a 3rd part driver that SQLAlchemy
# uses to interact with a particular db and for SQLite its pysqlite
# 3. How do we locate the database - /:memory: which indicates that we will
# be using an in-memory-only database

# right now, the create engine has not yet connected to the database. It gets
# connected right once we perform a task against a datbase, hence a lazy initialization
