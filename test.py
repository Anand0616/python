from engine import *

db = "pythondb"
connect()
create(db)
engine = use(db)
engine.execute("""CREATE TABLE IF NOT EXISTS `dogs` (
  `dogID` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `breed` VARCHAR(255) NULL,
  `age` INT NULL,
  PRIMARY KEY (`Id`))
""")


def test():
    result = engine.execute(
        "SELECT COUNT(*) FROM `dogs`")

    row_num = int(list(result)[0][0])
    if row_num == 0:
        engine.execute(
            "INSERT INTO `cats` (`name`, `breed`, `age`) VALUES ('dory', '1', 'persian cat')")
    result = engine.execute(
        "SELECT * FROM `cats`")
    result_converted = str(list(result)[0][1])
    assert result_converted == "alex"


test()
print("pass")
