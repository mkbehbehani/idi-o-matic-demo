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

def add(self, server):
    self.servers.append(server)

def _create_sample(self, hmm_file, qsr_type):
    with open(hmm_file, 'r') as f:
        hmm = json.load(f)
    s = self.r.call_service(HMMRepRequestSample(qsr_type=qsr_type,
        dictionary=hmm, max_length=10, num_samples=1))
    return s
