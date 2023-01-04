import PySimpleGUI as sg
import wolframalpha

app_id = "UEVH54-4XWTW9JR6H"
client = wolframalpha.Client(app_id)
sg.theme('SandyBeach')   

layout = [  [sg.Text('Hello, Can I help you?')],
            [sg.Text('Write your question here please:'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('PyAssistant', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': 
        break
    try:
        res = client.query(values[0])
        sg.Text(next(res.results).text)
        print(next(res.results).text)
        layout = [  [sg.Text(values[0]+"?")],
                [sg.Text(next(res.results).text)],
                [sg.Text('Any other question?'), sg.InputText()],
                [sg.Button('Ok'), sg.Button('Cancel')] ]
        window.close()
        window = sg.Window('PyAssistant', layout)
    except:
        break
window.close()