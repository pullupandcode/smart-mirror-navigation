from mycroft import MycroftSkill, intent_handler
import redis
import json

def SmartMirrorNavigationSkill(MycroftSkill):
    def __init__(self):
        super(MycroftSkill, self).__init__("SmartMirrorNavigationSkill")
        self.register_entity_file('location.entity')
        self.redis_client = redis.Redis(host="192.168.1.11", port=6379, db=0)

        @intent_handler('navigate.to.intent')
        def handle_navigation_command(self, message):
            destination = message.data.get('location')

            if destination is not None:
                publish_message = {
                    'navigation': {
                        'location': destination,    
                    }
                }

                self.redis_client.publish(json.dumps(publish_message, separators=(',', ':')))
    

def create_skill():
    return MycroftSkill()
