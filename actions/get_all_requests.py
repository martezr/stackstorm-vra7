from lib import action

class GetAllRequests(action.vRealizeAutomationAction):
    def run(self):
        return self.vra7.getAllRequests()
