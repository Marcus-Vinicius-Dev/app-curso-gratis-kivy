from kivy.core.window import Window
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database import DataBase

# Definição das janelas de tela

class CreateAccountWindow(Screen):
    # Definição de propriedades de objetos para os elementos de interface do usuário
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    
    def submit(self):
        # Método para lidar com a submissão do formulário de criação de conta
        if self.namee.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)
                self.reset()
                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()
                
    def login(self):
        # Método para navegar de volta para a tela de login
        self.reset()
        sm.current = "login"
        
    def reset(self):
        # Método para redefinir os campos do formulário
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""
        
        
class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    
    def loginBtn(self):
        if self.email.text == "user" and self.password.text == "password":
            self.reset()
            sm.current = "main"
        else:
            invalidLogin()
            
    def createBtn(self):
        # Método para navegar para a tela de criação de conta
        self.reset()
        sm.current = "create"
        
    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.ids.error_msg.text = ""


class CreateAccountWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        # Here you can add logic for account creation
        print("Account created successfully")
        sm.current = "login"

    def login(self):
        sm.current = "login"


class WindowManager(ScreenManager):
    pass


class MyApp(App):
    def build(self):
        return sm


# Load the kv file
kv = Builder.load_file("my.kv")

# Create the screen manager
sm = WindowManager()

# Add screens to the screen manager
screens = [LoginWindow(name="login"), CreateAccountWindow(name="create")]
for screen in screens:
    sm.add_widget(screen)
    sm.current = "login"
        
# Definição da classe principal do aplicativo Kivy

class MyMainApp(App):
    def build(self):
        return sm
    
# Verificação se o script está sendo executado diretamente e inicialização do aplicativo

if __name__ == "__main__":
    MyApp().run()
