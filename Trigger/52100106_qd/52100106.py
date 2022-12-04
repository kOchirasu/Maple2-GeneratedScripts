""" trigger/52100106_qd/52100106.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[91000880], questStates=[3]):
            return 들킴(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[91000890], questStates=[2]):
            return 들킴(self.ctx)


class 들킴(trigger_api.Trigger):
    def on_enter(self):
        self.set_ambient_light(primary=[232,92,53])
        self.set_directional_light(diffuseColor=[41,21,18], specularColor=[130,130,130])
        self.set_effect(triggerIds=[6000], visible=True)
        self.set_actor(triggerId=201, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=203, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=204, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=206, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=207, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=208, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=211, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=212, visible=True, initialSequence='sf_quest_light_A01_On')


initial_state = Ready
