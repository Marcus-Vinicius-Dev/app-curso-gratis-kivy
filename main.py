from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty


class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        if self.email.text == "user" and self.password.text == "password":
            self.reset()
            sm.current = "main"
        else:
            self.ids.error_msg.text = "Invalid username or password"

    def createBtn(self):
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

# Set the initial screen
sm.current = "login"

if __name__ == "__main__":
    MyApp().run()
