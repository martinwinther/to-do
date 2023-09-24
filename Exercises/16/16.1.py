import PySimpleGUI as sg

label_feet = sg.Text("Enter feet:")
label_inches = sg.Text("Enter inches:")
input_feet = sg.InputText(tooltip="Enter feet")
input_inches = sg.InputText(tooltip="Enter inches")
convert_button = sg.Button("Convert")

window = sg.Window('Convertor', layout=[
    [label_feet, input_feet],
    [label_inches, input_inches],
    [convert_button]
])

window.read()
window.close()