import sqlite3


class schema:

    def __init__(self):
        self.conn = sqlite3.connect("my_database.db")
        self.create_family_table()
        self.create_task_table()

    def __del__(self):
        self.conn.commit()
        self.conn.close()

    def create_task_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "Task" (
          _id INTEGER PRIMARY KEY AUTOINCREMENT,
          Title TEXT,
          Description TEXT,
          _is_done boolean DEFAULT 0,
          _is_deleted boolean DEFAULT 0,
          CreatedOn Date DEFAULT CURRENT_DATE,
          UserId INTEGER FOREIGNKEY REFERENCES Family(_id),
          Repeat TEXT NOT NULL,
          Participants TEXT REFERENCES Family(Name),
          WhatTime TEXT, 
          Duration TEXT
        );
        """
        self.conn.cursor().execute(query)


    def create_family_table(self):
        query = """
         CREATE TABLE IF NOT EXISTS "Family" (
         _id INTEGER PRIMARY KEY AUTOINCREMENT, 
         Title TEXT, 
         Name TEXT NOT NULL, 
         _is_deleted boolean DEFAULT 0,
         CreatedOn Date default CURRENT_DATE
         );
         """
        self.conn.cursor().execute(query)


class Task:
    TABLENAME = "Task"

    def __init__(self):
        self.conn = sqlite3.connect("my_database.db")
        self.conn.row_factory = sqlite3.Row

    def __del__(self):
        self.conn.commit()
        self.conn.close()

    def get_by_id(self, _id):
        where_clause = f"AND _id={_id}"
        return self.list_tasks(where_clause)

    def create_task(self, params):
        query = f'INSERT INTO {self.TABLENAME} ' \
                f'(Title, Description, UserId, Repeat, Participants, WhatTime, Duration) ' \
                f'VALUES (?, ?, ?, ?, ?, ?, ?)'
        print("params: "+str(params))
        values = [params.get("Title"), params.get("Description"), params.get("UserId"),
                  params.get("Repeat"), params.get("Participants"), params.get("WhatTime"),
                  params.get("Duration")]
        print(query)
        result = self.conn.cursor().execute(query, values)

    # return self.get_by_id(result.lastrowid)

    def delete_task(self, item_id):
        query = f"UPDATE {self.TABLENAME} " \
                f"SET _is_deleted =  {1} " \
                f"WHERE _id = {item_id}"
        print(query)
        self.conn.execute(query)
        return self.list_tasks()

    def update_task(self, item_id, params):
        """
        column: value
        Title: new title
        """
        '''UPDATE books SET price = ? WHERE id = ?'''
        query = f"UPDATE {self.TABLENAME} " \
                f"SET Title  = ?, Description = ?, UserId = ?, Repeat = ?, Participants = ?, WhatTime = ?, Duration = ?"\
                f"WHERE _id = ?"
        self.conn.cursor().execute(query, [params.get("Title"), params.get("Description"), params.get("UserId"),\
                  params.get("Repeat"), params.get("Participants"), params.get("WhatTime"),\
                  params.get("Duration"), item_id])
        return self.get_by_id(item_id)

    def list_tasks(self, where_clause=""):
        query = f"SELECT _id, Title, Description, UserId, Repeat, Participants, WhatTime, Duration " \
                f"FROM {self.TABLENAME} WHERE _is_deleted != {1} " + where_clause
        print(query)
        result_set = self.conn.execute(query).fetchall()
        print(result_set)
        result = [{column: row[i]
                   for i, column in enumerate(result_set[0].keys())}
                  for row in result_set]
        return result


class Family:
    TABLENAME = "Family"

    def __init__(self):
        self.conn = sqlite3.connect("my_database.db")
        self.conn.row_factory = sqlite3.Row

    def __del__(self):
        self.conn.commit()
        self.conn.close()

    def get_by_id(self, _id):
        where_clause = f' AND id = {_id}'
        return self.list_tasks(where_clause)

    def create_member(self, title, name):
        query = f'INSERT INTO {self.TABLENAME} ' \
                f'(Title, Name) ' \
                f'VALUES(?,?)'
        print("Executing: "+query)
        result = self.conn.cursor().execute(query, [title, name])

        return result

    def delete_member(self, item_id):
        query = f'UPDATE {self.TABLENAME} ' \
                f'SET _is_deleted = {1} ' \
                f'WHERE _id = {item_id}'
        result = self.conn.execute(query)
        return result

    def update_member(self, item_id, update_dict):
        set_query = " ".join([f'{column} = {value}'
                              for column, value in update_dict.items()])
        query = f'UPDATE {self.TABLENAME} ' \
                f'SET {set_query} ' \
                f'WHERE _id = {item_id}'
        self.conn.execute(query)
        return self.get_member_by_id(item_id)

    def list_members(self, where_clause=""):
        query = f'SELECT _id, title, name ' \
                f'FROM {self.TABLENAME} ' \
                f'WHERE _is_deleted != 1' + where_clause
        result_set = self.conn.execute(query).fetchall()
        print("printing result_set: "+str(result_set))
        result = [{column: row[i] for i, column in enumerate(result_set[0].keys())} for row in result_set]
        return result
