from mycroft import MycroftSkill, intent_handler
import redis
import json

class SmartMirrorNavigationSkill(MycroftSkill):
    def __init__(self):
        super(SmartMirrorNavigationSkill, self).__init__("SmartMirrorNavigationSkill")

    def initialize(self):
        self.register_entity_file('location.entity')
        self.redis_client = redis.Redis(host="192.168.1.11", port=6379, db=0)

    @intent_handler('navigate.to.intent')
    def handle_navigate_to(self, message):
        destination = message.data.get('location')
        print(message)
        
        if destination is not None:
            publish_message = {
                'navigation': {
                    'location': destination,    
                }
            }

            self.redis_client.publish(json.dumps(publish_message, separators=(',', ':')))
    

def create_skill():
    return SmartMirrorNavigationSkill()
