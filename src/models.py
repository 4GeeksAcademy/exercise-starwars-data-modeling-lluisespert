from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

# URL de la base de datos (SQLite en este caso)
DATABASE_URL = "sqlite:///database.db"

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL, echo=True)

# Base del ORM
Base = declarative_base()

# Definir una tabla (modelo)
class Character(Base):
    __tablename__ = "characters"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    height = Column(String, nullable=True)
    mass = Column(String, nullable=True)
    hair_color = Column(String, nullable=True)
    skin_color = Column(String, nullable=True)
    eye_color = Column(String, nullable=True)
    birth_year = Column(String, nullable=True)
    gender = Column(String, nullable=True)

class Planet(Base):
    __tablename__ = "planets"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    diameter = Column(String, nullable=True)
    rotation_period = Column(String, nullable=True)
    orbital_period = Column(String, nullable=True)
    gravity = Column(String, nullable=True)
    population = Column(String, nullable=True)
    climate = Column(String, nullable=True)
    terrain = Column(String, nullable=True)
    surface_water = Column(String, nullable=True)

class Starship(Base):
    __tablename__ = "starships"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    model = Column(String, nullable=True)
    starship_class = Column(String, nullable=True)
    manufacturer = Column(String, nullable=True)
    cost_in_credits = Column(String, nullable=True)
    length = Column(String, nullable=True)
    crew = Column(String, nullable=True)
    passengers = Column(String, nullable=True)
    max_atmosphering_speed = Column(String, nullable=True)
    hyperdrive_rating = Column(String, nullable=True)
    mglt = Column(String, nullable=True)
    cargo_capacity = Column(String, nullable=True)
    consumables = Column(String, nullable=True)

class Contact(Base):
    __tablename__ = "contacts"
    
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email_address = Column(String, nullable=False, unique=True)
    phone = Column(String, nullable=True)
    address = Column(String, nullable=True)

class Favorite(Base):
    __tablename__ = "favorites"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    character_id = Column(Integer, ForeignKey('characters.id'), nullable=True)
    planet_id = Column(Integer, ForeignKey('planets.id'), nullable=True)
    starship_id = Column(Integer, ForeignKey('starships.id'), nullable=True)

    character = relationship("Character")
    planet = relationship("Planet")
    starship = relationship("Starship")

# Crear las tablas en la base de datos
Base.metadata.create_all(engine)

# Crear una sesión
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# Función para listar los favoritos de un usuario
def list_favorites(user_id):
    favorites = session.query(Favorite).filter_by(user_id=user_id).all()
    for fav in favorites:
        fav_details = {
            "character": fav.character.name if fav.character else None,
            "planet": fav.planet.name if fav.planet else None,
            "starship": fav.starship.name if fav.starship else None
        }
        print(f"Favorite: {fav_details}")

# Función para eliminar un favorito
def remove_favorite(favorite_id):
    favorite = session.query(Favorite).filter_by(id=favorite_id).first()
    if favorite:
        session.delete(favorite)
        session.commit()
        print(f"Favorite {favorite_id} deleted successfully.")
    else:
        print(f"Favorite {favorite_id} not found.")

# Cerrar la sesión
session.close()

