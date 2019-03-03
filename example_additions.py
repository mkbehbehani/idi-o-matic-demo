def get_host(self):
    return self.domain or self.address_s

def start_app(self):
    self.flask_app.run(debug=self.debug)

def is_running(pid):
    try:
        os.kill(pid, 0)
    except OSError as err:
        if err.errno == errno.ESRCH:
            return False
    return True
