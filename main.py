from beepy import beep
from time import sleep
from datetime import datetime
import subprocess

# fping 80.80.80.80 -s -l

CMD = ['fping', '80.80.80.80']

is_online = True

beep(sound='ready')

while True:
    iso_date = datetime.now()

    try:
        result = subprocess.check_output(CMD)
        iso_date = datetime.now()
        # print(f'{iso_date.isoformat()} - {result}')
        f = open("fping.txt", "a")
        f.write(f'{iso_date.isoformat()} - {result}' + '\n')
        f.close()
        if not is_online:
            beep(sound='coin')
            is_online = True
    except subprocess.CalledProcessError as e:
        f = open("fping.txt", "a")
        f.write(f'{iso_date.isoformat()} - {e.output}' + '\n')
        f.close()
        beep(sound='error')
        is_online = False
    sleep(0.5)

