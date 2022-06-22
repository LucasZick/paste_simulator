from sys import exit as close
from pynput.keyboard import Controller
from time import sleep as wait
from pyautogui import keyDown, keyUp, press, prompt, alert
from inspect import cleandoc as clean_str

class App:
    title = "INSIRA O TEXTO"
    label = """Clique em "OK" e selecione a caixa de texto na qual deseja que seja digitado.
Cole aqui o texto:"""
    text = None

    def start(self):
        self.__controller()

    def __show_prompt(self):
        text = prompt(title = App.title, text = App.label, default=None)
        return text
    
    def __write(self) -> None:
        Controller().type(clean_str(self.text))
    
    def __delete_trash(self):
        keyDown("shift")
        keyDown("down")
        wait(3)
        keyUp("down")
        keyUp("shift")
        press("backspace")

    def __save_and_run(self):
        keyDown("ctrl")
        press('s')
        wait(2)
        press("f11")
        keyUp("ctrl")
    
    def __controller(self):
        self.text = self.__show_prompt()
        if self.text:
            wait(5)
            self.__write()
            self.__finish()

        elif self.text == "":
            alert(title="TEXTO VAZIO", text="É necessário inserir o texto a ser digitado.")
            self.__controller()

        else:
            alert(title="FECHANDO O PROGRAMA", text="Nenhum texto será digitado.")
            close(0)

    def __finish(self):
        self.__delete_trash()
        self.__save_and_run()
        alert(title="FINALIZADO", text="Aplicacao encerrada", timeout=1000)

if __name__ == "__main__":
    app = App()
    app.start()
    close(0)