import FreeSimpleGUI as sG

def convert(feet, inches):
    total_inches = (feet * 12) + inches
    return total_inches * 0.0254

feet_label = sG.Text("Enter feet:")
feet_input = sG.InputText(key="feet")
inches_label = sG.Text("Enter inches:")
inches_input = sG.InputText(key="inches")
button = sG.Button("Convert")
meters_label = sG.Text(key="meters")

window = sG.Window('Convertor',
                   layout=[[feet_label, feet_input],
                           [inches_label, inches_input],
                           [button, meters_label]])

while True:
    event, values = window.read()
    print(event)
    print(values)

    if event == 'Convert':
        meters = convert(int(values['feet']), int(values['inches']))
        window['meters'].update(value=meters)
        print (meters)
    elif event == sG.WIN_CLOSED:
        break

window.close()