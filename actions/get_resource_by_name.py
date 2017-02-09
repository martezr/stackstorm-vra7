from lib import action
import json

class GetResourceByName(action.vRealizeAutomationAction):
    def run(self, resourceName):
        resource = self.vra7.getResourceByName(name=resourceName)
        return json.dumps(resource)
