from typing import Optional

from sqlmodel import Field, SQLModel, create_engine, Session, select

class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None
 
#   
# Create Rows
#
hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
hero_3 = Hero(name="Rusty-Man", secret_name="Tommie Sharp", age=48)

# Create Database Engine
engine = create_engine("sqlite:///database2.db", echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

with Session(engine) as session:
    session.add(hero_1)
    session.add(hero_2)
    session.add(hero_3)
    session.commit()

if __name__ == "__main__":
    # Creates database and tables when running this file directly
    create_db_and_tables()
    
# with Session(engine) as session:
#     statement = select(Hero).where(Hero.name == "Spider-Boy")
#     hero = session.exec(statement).first()
#     print(hero, type(hero))