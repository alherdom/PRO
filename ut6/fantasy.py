from __future__ import annotations
import re
import sqlite3

DB_PATH = "fantasy.db"
DRIVERS_PATH = "info.dat"


def create_database(db_path: str):
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    tables = """CREATE TABLE user(
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT,
    email TEXT
    );
    CREATE TABLE driver(
    id INTEGER PRIMARY KEY,
    name TEXT,
    surname TEXT,
    scuderia TEXT,
    points TEXT
    );
    """
    cur.executescript(tables)
    con.commit()
    con.close()


def create_drivers(db_path: str, path: str):
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    with open(path, "r") as f:
        for line in f:
            sql = "INSERT INTO drivers values(?, ?, ?, ?, ?)"
            number, full_name, scuderia, points = line.strip().split(",")
            name, surname = full_name.split()
            cur.execute(sql, (number, name, surname, scuderia, points))
    con.commit()
    con.close()


class User:
    def __init__(self, username: str, password: str, email: str, user_id: int = -1):
        self.con = sqlite3.connect(DB_PATH)
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()
        self.log_status = False
        self.team = []
        self.points = 0
        self.username = username
        self.password = password
        self.email = email
        self.id = user_id

    def save(self) -> None:
        sql = "INSERT INTO user(username, password, email) values (?, ?, ?)"
        self.cur.execute(sql, (self.username, self.password, self.email))
        self.id = self.cur.lastrowid
        self.con.commit()

    def login(self, password: str) -> None:
        user_existence = self.cur.execute("SELECT * from user where id=?", (self.id,))
        if exist := user_existence.fetchone():
            user_password = exist["password"]
            self.log_status = True if password == user_password else False
        else:
            raise UserError(f"The user is not registered in database")

    @staticmethod
    def check_login(method):
        def wrapper(self, *args, **kwargs):
            if self.log_status == False:
                raise UserError(f"User must be logged before doing an action")
            return method(self, *args, **kwargs)

        return wrapper

    @check_login
    def join_driver(self, driver_number: int):
        driver_existence = self.cur.execute(
            "SELECT * from drivers where id=?", (driver_number,)
        )
        if driver := driver_existence.fetchone():
            driver_info = {key: info for key, info in zip(driver.keys(), driver)}
            self.team.append(driver_info)
        else:
            raise DriverError(f"Driver with number {driver_number} is not in database")

    @check_login
    def update_points(self):
        for driver in self.drivers:
            sql = "SELECT * from drivers where id=?"
            points = self.cur.execute(sql, (driver["id"],)).fetchone()["points"]
            self.points += points

    @staticmethod
    def from_db_row(cls, row: sqlite3.Row) -> User:
        return cls(row["username"], row["password"], row["email"], row["id"])


class Driver:
    def __init__(
        self, number: int, name: str, surname: str, scuderia: str, points: str
    ):
        self.con = sqlite3.connect(DB_PATH)
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()
        self.number = number
        self.name = name
        self.surname = surname
        self.scuderia = scuderia
        self.points = points

    def save(self) -> None:
        sql = "INSERT INTO drivers values(?, ?, ?, ?, ?)"
        self.cur.execute(
            sql, (self.number, self.name, self.surname, self.scuderia, self.points)
        )
        self.con.commit()

    def change_scuderia(self, new_scuderia: str) -> None:
        scuderia_existence = self.cur.execute("SELECT scuderia from drivers")
        if new_scuderia not in scuderia_existence.fetchall():
            raise ScuderiaError(f"Scuderia not exist")
        self.scuderia = new_scuderia
        self.save()

    @staticmethod
    def from_db_row(cls, row: sqlite3.Row) -> Driver:
        return cls(
            row["id"], row["name"], row["surname"], row["scuderia"], row["points"]
        )


class UserError(Exception):
    pass


class DriverError(Exception):
    pass


class ScuderiaError(Exception):
    pass
