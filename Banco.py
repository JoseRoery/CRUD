import psycopg2

class Banco():
    
    def __init__(self, tbName):
        self.conn = psycopg2.connect(database='postgres', 
                        host='localhost', 
                        user='postgres', 
                        password='root', 
                        port='5432')
        self.cursor = self.conn.cursor()
        self.tbName = tbName
        
    def selectOne(self, idSensor):
        self.cursor.execute("SELECT * FROM {} WHERE idsensor = {};".format(self.tbName, idSensor))
        return self.cursor.fetchone()
    
    def deleteOne(self, idSensor):
        self.cursor.execute("DELETE FROM {} WHERE idsensor = {};".format(self.tbName, idSensor))
        
    def insertOne(self, idSensor, variavel, medicao, unidade, registro, latitutde, longitude):
        self.cursor.execute("INSERT INTO {} VALUES ({},'{}',{},'{}','{}',{},{}) RETURNING idSensor;".format(self.tbName, idSensor, variavel, medicao, unidade, registro, latitutde, longitude))    
        return self.cursor.fetchone()
    
    def updateOne(self, idSensor, variavel, medicao, unidade, registro, latitutde, longitude):
        self.cursor.execute("UPDATE {} SET variavel='{}', medicao={}, unidade='{}', registro='{}', latitude={}, longitude={} WHERE idSensor = {};".format(self.tbName, variavel, medicao, unidade, registro, latitutde, longitude,idSensor))
        
    def commitChanges(self):
        self.conn.commit()
        