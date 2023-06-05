from __future__ import annotations

import sqlite3

DB_PATH = 'todo.db'
TASK_DONE_SYMBOL = '✔'
TASK_PENDING_SYMBOL = '⎕'


class Task:
    '''Crear atributos de clase:
    - con: para la conexión a la base de datos.
    - cur: para el cursor de manejo.'''
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    
    def __init__(self, name: str, done: bool = False, id: int = -1):
        '''Crea los atributos homónimos a los parámetros'''
        self.name = name
        self.done = done
        self.id = id     

    def save(self):
        '''Guarda esta tarea en la base de datos.
        El identificador asignado en la base de datos se debe usar para actualizar el
        atributo id de la tarea.'''
        sql = 'INSERT INTO tasks(name,done) VALUES(?,?)'
        Task.cur.execute(sql,(self.name, self.done))
        Task.con.commit()
        self.id = Task.cur.lastrowid
    
    def update(self):
        '''Actualiza la tarea (nombre y estado) en la base de datos'''
        Task.cur.execute(f'UPDATE tasks SET name="{self.name}", done={self.done} WHERE id={self.id}')
        Task.con.commit()

    def check(self):
        '''Marca la tarea como completada. Haz uso también de .update()'''
        self.done = True
        self.update()

    def uncheck(self):
        '''Marca la tarea como no completada. Haz uso también de .update()'''
        self.done = False
        self.update()

    def __repr__(self):
        '''Muestra la tarea en formato:
        <SYMBOL> <name> (id=<id>)'''
        SYMBOL = TASK_DONE_SYMBOL if self.done else TASK_PENDING_SYMBOL
        return f'{SYMBOL} {self.name} (id={self.id})'

    @classmethod
    def from_db_row(cls, row: sqlite3.Row) -> Task:
        '''Construye una nueva tarea a partir de una fila de consulta devuelta por execute()'''
        # return Task(row[1], row[2], row[0])
        return Task(row['name'], row['done'], row['id'])

    @classmethod
    def get(cls, task_id: int) -> Task:
        '''Devuelve un objeto Task desde la consulta a la base de datos'''
        res = Task.cur.execute(f'SELECT * FROM tasks WHERE id={task_id}')
        return cls.from_db_row(res.fetchone())


class ToDo:
    '''Crear atributos de clase:
    - con: para la conexión a la base de datos.
    - cur: para el cursor de manejo.'''
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    def create_db(self):
        '''Crea la base de datos con los campos "id", "name" y "done"'''
        sql = '''CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    done INTEGER
                )'''
        ToDo.cur.execute(sql)
        ToDo.con.commit()

    def get_tasks(self, *, done: int = -1):
        '''Devuelve todas las tareas como objetos de tipo Task consultando la BBDD.
        - Si done = 0 se devuelven las tareas pendientes.
        - Si done = 1 se devuelven las tareas completadas.
        Ojo! Esto es una función generadora.'''
        for row in ToDo.cur.execute(f'SELECT * FROM tasks WHERE done={done}'):
            yield ToDo(row)

    def add_task(self, name: str):
        '''Añade la tarea con nombre "name"'''
        Task(name).save()
        
    def complete_task(self, task_id: int):
        '''Marca la tarea con identificador "task_id" como completada'''
        Task.get(task_id).check()

    def reopen_task(self, task_id: int):
        '''Marca la tarea con identificador "task_id" como pendiente'''
        Task.get(task_id).uncheck()