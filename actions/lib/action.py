from vraapiclient import catalog
from st2actions.runners.pythonrunner import Action

class vRealizeAutomationAction(Action):

    def __init__(self, config):
        super(vRealizeAutomationAction, self).__init__(config)
        self.vra7 = self._get_client()

    def _get_client(self):
        hostname = self.config['hostname']
        username = self.config['username']
        password = self.config['password']
        tenant = self.config['tenant']

        client = catalog.ConsumerClient(hostname, username, password, tenant)
        return client
