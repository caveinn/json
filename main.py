import PySimpleGUI as sg
from general_settings_page import window2 as general_settingsWindow
# from incoming_settings_page import window2 as incoming_settingsWindow
# from json_settings_page import window2 as json_settingsWindow
# from delivery_settings_page import window2 as delivery_settingsWindow
# from after_effects_settings_page import window2 as effects_settingsWindow
from email_settings_page import window2 as email_settingsWindow


# class WindowStack():
#     stack = []
#     def __init__(self, window = None):
#          '''
#             params:
#                 - windows= a window to add to stack
#          '''
#          stack = [window]
#     def append(window):
#         '''
#         params:
#             - window= a window to add to stack
#         '''
#         stack.append(window)

#     def get_window():

#         return stack[-1] if stack else None


info_column = [
    [
        sg.Text("APP Status"),
    ],
    [
        sg.Text("Settings",key="-settings-", enable_events=True),
    ],
    [
        sg.Text("About"),
    ],
]

navigator_column = [
    [sg.Text("Application Running for:")],
    [sg.Text("Last Delivered campaign")],
    [sg.Text("Last Sync Campaign JSON")],
    [sg.Text("Last Sync /Ads folder", pad=((6,400),(0,400) ))],
    [sg.Text("Sart /stop services:"), sg.Button("stop")],
    [sg.Text("Automatically start at login"), sg.Checkbox("", key="-autostart-", enable_events=True)],
    # [sg.Text(size=(40, 1), key="-TOUT-")],
    # [sg.Image(key="-IMAGE-")],

]
# ----- Full layout -----
layout = [
    [
        sg.Column(info_column,vertical_alignment="t"),
        sg.VSeperator(),
        sg.Column(navigator_column),
    ]
]

# Create the window
window = sg.Window("Support App", layout, finalize=True)
# windowStack = WindowStack()
# Create an event loop
while True:

    # event, values = window.read()
    # End program if user closes window or
    # presse

    # if(event == "-settings-"):
    #    event, values = general_settingsWindow.read()
    general_settingsWindow.finalize =True

    window, event, values = sg.read_all_windows()
    print(event, values)
    if window == sg.WIN_CLOSED:     # if all windows were closed
        break
    if event == sg.WIN_CLOSED or event == 'Exit':
        window.close()
        if window == email_settingsWindow:       # if closing win 2, mark as closed
            window2 = None
        elif window == email_settingsWindow:     # if closing win 1, mark as closed
            window1 = None
    # elif event == 'Reopen':
    #     if not window2:
    #         window2 = make_win2()
    #         window2.move(window1.current_location()[0], window1.current_location()[1] + 220)
    # elif event == '-IN-':
    #     output_window = window2 if window == window1 else window1
    #     if output_window:           # if a valid window, then output to it
    #         output_window['-OUTPUT-'].update(values['-IN-'])
    #     else:
    #             window['-OUTPUT-'].update('Other window is closed')
