from lib import action
import json

class GetResourceByName(action.vRealizeAutomationAction):
    def run(self, resourceName):
        resourceJSONString = ''
        resource = self.vra7.getResourceByName(name=resourceName)
        data = json.dumps(resource)
        jsondata = json.loads(data)
        resourceId = jsondata["id"]
        resourceDetail = self.vra7.getResource(id=resourceId, show='json')
        return json.dumps(resourceDetail)
