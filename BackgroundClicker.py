import PurepyHook
import enumWindows
import mido
import mido.backends.rtmidi

# pyinstaller --onefile BackgroundClicker.py

# Keyboard codes
PAGE_UP = 33
PAGE_DN = 34
F5_BUTTON = 116

# Midi Notes
SLIDE_NEXT = 50
SLIDE_PREV = 49
GO_ON_AIR = 36
REA_PLAY = 99

# searchfor = ['- Proclaim', '- PowerPoint','Proclaim Slides']


def proclaimClick(e):
    activeWindowName = enumWindows.getForegroundWindowTitle()
    # print(activeWindowName)
    if(activeWindowName is None
            or ("- Proclaim" not in activeWindowName
                and "- PowerPoint" not in activeWindowName
                and "Proclaim Slides" not in activeWindowName)):
        if(e.event_type == 'key down'):
            if(e.key_code == PAGE_DN):
                print_event(e)
                outport.send(mido.Message('note_on', note=SLIDE_NEXT))
            elif(e.key_code == PAGE_UP):
                print_event(e)
                outport.send(mido.Message('note_on', note=SLIDE_PREV))
            elif(e.key_code == F5_BUTTON):
                print_event(e)
                outport.send(mido.Message('note_on', note=REA_PLAY))


def print_event(e):
    print(e)


ports = mido.get_output_names()
for s in ports:
    if('ClickerMidi' in s):
        outport = mido.open_output(s)


def main():
    print("PAGE_DN key " + str(PAGE_DN) + " SLIDE_NEXT Note " + str(SLIDE_NEXT))
    print("PAGE_UP key " + str(PAGE_UP) + " SLIDE_PREV Note " + str(SLIDE_PREV))
    print("F5 key " + str(F5_BUTTON) + " Reaper Play Note " + str(REA_PLAY))
    print("Listening for keystrokes")
    PurepyHook.handlers.append(proclaimClick)
    PurepyHook.listener()


if __name__ == "__main__":
    main()
