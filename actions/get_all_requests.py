from lib import action

class GetAllRequests(action.JenkinsBaseAction):
    def run(self):
        return self.vra7.getAllRequests()
