from tkinter import *

class View():
    def __init__(self, master=None):                       
        self.fonte = ("Verdana", "8")
        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        
        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()
        
        self.container71 = Frame(master)
        self.container71["padx"] = 20
        self.container71["pady"] = 5
        self.container71.pack()
        
        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.pack()
        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()

        self.titulo = Label(self.container1, text="Informe os dados :")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack ()

        self.lblidSensor = Label(self.container2,
        text="idSensor:", font=self.fonte, width=10)
        self.lblidSensor.pack(side=LEFT)

        self.txtidSensor = Entry(self.container2)
        self.txtidSensor["width"] = 10
        self.txtidSensor["font"] = self.fonte
        self.txtidSensor.pack(side=LEFT)

        self.btnBuscar = Button(self.container2, text="Buscar",
        font=self.fonte, width=10)
        self.btnBuscar.pack(side=RIGHT)

        self.lblVariavel = Label(self.container3, text="Variável:",
        font=self.fonte, width=10)
        self.lblVariavel.pack(side=LEFT)

        self.txtVariavel = Entry(self.container3)
        self.txtVariavel["width"] = 25
        self.txtVariavel["font"] = self.fonte
        self.txtVariavel.pack(side=LEFT)

        self.lblMedicao = Label(self.container4, text="Medição:",
        font=self.fonte, width=10)
        self.lblMedicao.pack(side=LEFT)

        self.txtMedicao = Entry(self.container4)
        self.txtMedicao["width"] = 25
        self.txtMedicao["font"] = self.fonte
        self.txtMedicao.pack(side=LEFT)

        self.lblUnidade= Label(self.container5, text="Unidade:",
        font=self.fonte, width=10)
        self.lblUnidade.pack(side=LEFT)

        self.txtUnidade = Entry(self.container5)
        self.txtUnidade["width"] = 25
        self.txtUnidade["font"] = self.fonte
        self.txtUnidade.pack(side=LEFT)

        self.lblRegistro= Label(self.container6, text="Registro:",
        font=self.fonte, width=10)
        self.lblRegistro.pack(side=LEFT)

        self.txtRegistro = Entry(self.container6)
        self.txtRegistro["width"] = 25
        self.txtRegistro["font"] = self.fonte
        self.txtRegistro.pack(side=LEFT)

        self.lblLatitude= Label(self.container7, text="Latitude:",
        font=self.fonte, width=10)
        self.lblLatitude.pack(side=LEFT)

        self.txtLatitude = Entry(self.container7)
        self.txtLatitude["width"] = 25
        self.txtLatitude["font"] = self.fonte
        self.txtLatitude.pack(side=LEFT)
        
        self.lblLongitude= Label(self.container71, text="Longitude:",
        font=self.fonte, width=10)
        self.lblLongitude.pack(side=LEFT)

        self.txtLongitude = Entry(self.container71)
        self.txtLongitude["width"] = 25
        self.txtLongitude["font"] = self.fonte
        self.txtLongitude.pack(side=LEFT)

        self.bntInsert = Button(self.container8, text="Inserir", font=self.fonte, width=12)
        #self.bntInsert["command"] = self.inserirUsuario
        self.bntInsert.pack (side=LEFT)

        self.bntAlterar = Button(self.container8, text="Alterar",
        font=self.fonte, width=12)
        #self.bntAlterar["command"] = self.alterarUsuario
        self.bntAlterar.pack (side=LEFT)

        self.bntExcluir = Button(self.container8, text="Excluir",
        font=self.fonte, width=12)
        #self.bntExcluir["command"] = self.excluirUsuario
        self.bntExcluir.pack(side=LEFT)
        
        self.bntAtualizarBanco = Button(self.container8, text="Atualizar BD",
        font=self.fonte, width=12)
        #self.bntExcluir["command"] = self.atualizarBD
        self.bntAtualizarBanco.pack(side=LEFT)

        self.lblmsg = Label(self.container9, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()
    
    
    def setCommandSearch(self, method):
        self.btnBuscar["command"] = method
        
    def setCommandInsert(self, method):
        self.bntInsert["command"] = method
        
    def setCommandDelete(self, method):
        self.bntExcluir["command"] = method
    
    #Crie aqui o método para inserir o comando no botão de atualizar!
    def setCommandUpdate(self, method) :
        self.bntAlterar["command"]= method
    
    def setCommandCommit(self, method):
        self.bntAtualizarBanco["command"] = method
    
    def resetAllFieds(self):
        self.txtidSensor.delete(0, END)
        self.txtVariavel.delete(0, END)
        self.txtMedicao.delete(0, END)
        self.txtUnidade.delete(0, END)
        self.txtRegistro.delete(0, END)
        self.txtLatitude.delete(0, END)
        self.txtLongitude.delete(0, END)
    
    def logUpdate(self, idSensor):
        self.lblmsg["text"] = "Sensor {} adicionado!".format(idSensor);
    
    def updateBySearch(self, sensor):
        if(sensor):
            self.lblmsg["text"] = "Busca realizada"
            self.resetAllFieds()
            
            self.txtidSensor.insert(INSERT, sensor[0])
            self.txtVariavel.insert(INSERT, sensor[1])
            self.txtMedicao.insert(INSERT, sensor[2])
            self.txtUnidade.insert(INSERT, sensor[3])
            self.txtRegistro.insert(INSERT, sensor[4])
            self.txtLatitude.insert(INSERT, sensor[5])
            self.txtLongitude.insert(INSERT, sensor[6])
        else:
            self.lblmsg["text"] = "Não existe esse sensor!"
            self.resetAllFieds()
    #mensagem no botão alterar
    def alterar(self, idSensor):
        self.lblmsg["text"] = "Sensor {} foi atualizado!".format(idSensor);
    #mensagem no  botão excluir
    def excluir(self,idSensor):
        self.lblmsg["text"] = "Sensor {} foi excluído!".format(idSensor);
    #mensagem no botão atualizar
    def commit(self):
        self.lblmsg["text"] = "Banco atualizado"