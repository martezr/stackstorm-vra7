from lib import action

class GetNumberOfVms(action.vRealizeAutomationAction):
    def run(self):
        test = self.vra7.getAllResourcesDetailed(show="json")
        count = 0
        for item in test:
          count += 1
        return count
