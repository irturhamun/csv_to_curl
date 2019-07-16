import PySimpleGUI as sg
import csv
import pyperclip
# All the stuff inside your window. This is the PSG magic code compactor...


layout = [  [sg.Text('Insert MSIDN',size=(15,1)), sg.InputText()],
            [sg.Text('Insert ML Taxonomy',size=(15,1)), sg.InputText()],
            [sg.Text('Insert CSV file', size = (15,1)),sg.InputText(), sg.FileBrowse()],
            [sg.Output(size=(80, 20))],
            [sg.OK(), sg.Cancel(),sg.Button('Next'),sg.Button('Enter')]]
            # [sg.OK(), sg.Cancel(),sg.Button('Copy'),sg.Button('Next'),sg.Button('Enter')]]
text1 = "curl -X GET --header 'Accept: application/json' --header 'CHANNELID: UX' 'https://personalizedmenu-co-v2-preprod-esb.ocp.digitalcore.telkomsel.co.id/offer/filteroffers/"
text2 = "?filteredby=boid%7c"
text3 = "&version=v2' -vik"
# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events"
def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
while True:

    event, values = window.Read()
    msidn = values[0]
    ml = values[1]
    file = values[2]
    join = text1+msidn+text2+ml+text3
    print(join)
    # if event == 'Copy':
    #     pyperclip.copy(join)
    # print('\n\n')
    # sg.Print(file)
    rows = []
    fields = []
    dump = []
    with open(file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        #     fields = csvreader.next()
        for row in csvreader:
            rows.append(row)
    for row in rows:
        index = []
        for col in row:
            index.append(col)
        fields.append(index)
    sg.Combo(fields)
    # x = 2
    # y = 4
    # print(fields[x][y])
    if ml.startswith('ML2'):
        if event == 'Enter':
            flag = 3
            sg.Combo(dump)
            sg.Combo(fields)
            for row in range(len(fields)):
                y = fields[row][2]
                if y == ml:
                    ml1 = fields[row][3]
                    dump.append(ml1)
        outer = Remove(dump)
        for row in range(len(outer)):
            ml1 = outer[row]
            join = text1 + msidn + text2 + ml1 + text3
            print(join)

    elif ml.startswith('ML3'):
            if event == 'Enter':
                flag = 4
                sg.Combo(dump)
                sg.Combo(fields)
                for row in range(len(fields)):
                    y = fields[row][3]
                    if y == ml:
                        ml1 = fields[row][4]
                        dump.append(ml1)
            outer = Remove(dump)
            for row in range(len(outer)):
                ml1 = outer[row]
                join = text1 + msidn + text2 + ml1 + text3
                print(join)



    if event in (None, 'Cancel'):
        break

window.Close()