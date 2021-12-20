from beepy import beep
from time import sleep
from datetime import datetime
import subprocess

# fping 80.80.80.80 -s -l

CMD = ['fping', '80.80.80.80']

is_online = True

beep(sound='ready')

start_fail_time = datetime.now()
end_fail_time = datetime.now()

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
            end_fail_time = datetime.now()
            total_fail_time = end_fail_time - start_fail_time
            f = open("fping_log.txt", "a")
            f.write(f'{start_fail_time.isoformat()} - dur - {total_fail_time.total_seconds()}' + '\n')
            f.close()
    except subprocess.CalledProcessError as e:
        f = open("fping.txt", "a")
        f.write(f'{iso_date.isoformat()} - {e.output}' + '\n')
        f.close()
        beep(sound='error')
        if is_online:
            start_fail_time = datetime.now()
        is_online = False
    sleep(0.5)

