from Banco import Banco

class Model():
    def __init__(self, tbName):
        self.banco = Banco(tbName)
    
    def read_one_sensor(self, idSensor):
        return self.banco.selectOne(idSensor)
    
    def delete_one_sensor(self, idSensor):
        self.banco.deleteOne(idSensor)
    
    def insert_one_sensor(self, idSensor, variavel, medicao, unidade, registro, latitutde, longitude):
        return self.banco.insertOne(idSensor, variavel, medicao, unidade, registro, latitutde, longitude);
    
    def update_one_sensor(self, idSensor, variavel, medicao, unidade, registro, latitutde, longitude):
        self.banco.updateOne(idSensor, variavel, medicao, unidade, registro, latitutde, longitude);
    
    def commit_changes(self):
        self.banco.commitChanges()