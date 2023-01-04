import PySimpleGUI as sg
import wolframalpha

app_id = "UEVH54-4XWTW9JR6H"
client = wolframalpha.Client(app_id)

import wikipediaapi
wiki_wiki = wikipediaapi.Wikipedia('en')

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
        res_wolfram = next(res.results).text
    except:
        res_wolfram = "No result to be found."
    try:
        res_wiki = wiki_wiki.page(values[0]).summary[:500]
        if len(res_wiki)==0:
            res_wiki = "No result to be found."
    except:
        res_wiki = "No result to be found."
    sg.popup("Wolfram Result: " + res_wolfram, 
                "Wikipedia Result: " + res_wiki 
            )
window.close()