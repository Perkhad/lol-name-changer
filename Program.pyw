import PySimpleGUI as sg
import changename as cn


class ScreenPython:
    def __init__(self):
        sg.theme('DarkAmber')
        # Layout
        layout = [
            [sg.Text('Name', size=(5, 0)), sg.Input(size=(15, 0), key='name')],
            [sg.Button('Start')],
            [sg.Output(size=(52, 10))]
        ]

        # Window
        window = sg.Window('Change Name').layout(layout)

        # Extrair dados da tela
        self.button, self.values = window.read()

    def Start(self):
        cn.main(self.values['name'])
        print('Thanks for using this program')


screen = ScreenPython()
screen.Start()
