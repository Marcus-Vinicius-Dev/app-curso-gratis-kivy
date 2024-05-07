import datetime

class DataBase():
    def __init__(self, filename):
        self.filename = filename
        self.users = None
        self.file = None
        self.load()
        
    def load(self):
        '''Carrega os usuários a partir do arquivo users.txt'''
        self.file = open(self.filename, "r")
        self.users = {}
        
        for line in self.file:
            email, password, name, created = line.strip().split(";")
            self.users[email] = (password, name, created)
            
        self.file.close()
        
    def get_user(self, email):
        '''Obtém informações de um usuário com base no e-mail'''
        if email in self.users:
            return self.users[email]
        else:
            return -1
        
    def add_user(self, email, password, name):
        '''Adiciona um novo usuário'''
        if email.strip() not in self.users:
            self.users[email.strip()] = (password.strip(), name.strip(), DataBase.get_date())
            self.save()
            return 1
        else:
            print("Email já existe!")
            return -1
            
    def validate(self, email, password):
        '''Valida as credenciais de um usuário'''
        if self.get_user(email) != -1:
            return self.users[email][0] == password
        else:
            return False
        
    def save(self):
        '''Salva os usuários de volta no arquivo'''
        with open(self.filename, "w") as f:
            for user in self.users:
                f.write(user + ";" + self.users[user][0] + ";" + self.users[user][1] + ";" + self.users[user][2] + "\n")
                
    @staticmethod
    def get_date():
        '''Obtém a data atual no formato yyyy-mm-dd'''
        return str(datetime.datetime.now()).split(" ")[0]
