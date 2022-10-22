""" trigger/52100106_qd/52100106.xml """
from common import *
import state


class Ready(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[91000880], questStates=[3]):
            return 들킴()
        if quest_user_detected(boxIds=[2001], questIds=[91000890], questStates=[2]):
            return 들킴()


class 들킴(state.State):
    def on_enter(self):
        set_ambient_light(primary=[232,92,53])
        set_directional_light(diffuseColor=[41,21,18], specularColor=[130,130,130])
        set_effect(triggerIds=[6000], visible=True)
        set_actor(triggerId=201, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=203, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=204, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=206, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=207, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=208, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=211, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=212, visible=True, initialSequence='sf_quest_light_A01_On')


