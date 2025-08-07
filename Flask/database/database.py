from peewee import SqliteDatabase, MySQLDatabase

# db = SqliteDatabase('customermanager.db')


db = MySQLDatabase('db_gestao_flask', host='localhost', port=3306, user='root', password='')
