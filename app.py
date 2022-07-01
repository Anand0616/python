from engine import *

db = "Dog"
connect()
create(db)
engine = use(db)
engine.execute("""CREATE TABLE IF NOT EXISTS dogs (
    dogId INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(255) NULL,
  breed VARCHAR(255) NULL,
  age INT NULL,
  PRIMARY KEY (dogId`))
""")

engine.execute(
    "INSERT INTO dogs (name, breed, age) VALUES (alex, 1, doberman)")

engine.execute(
    "SELECT * FROM dogs")