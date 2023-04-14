'''calls subprocess periodically, intentionally set to every second'''
import subprocess
import time,schedule

def call_script():
    subprocess.call(['python','main.py'])

schedule.every().day.at("07:00").do(call_script)

while True:
    schedule.run_pending()
    time.sleep(1)