""" trigger/52010059_qd/52010059.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        create_monster(spawnIds=[201], arg2=False) # 콘대르
        create_monster(spawnIds=[202], arg2=False) # 샤텐
        create_monster(spawnIds=[203], arg2=False) # 네이린
        create_monster(spawnIds=[204], arg2=False) # 메이슨
        set_actor(triggerId=501, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=502, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=503, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=504, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=505, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=506, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=507, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=508, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=509, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=510, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=511, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=512, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=513, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=514, visible=True, initialSequence='sf_quest_light_A01_Off')


