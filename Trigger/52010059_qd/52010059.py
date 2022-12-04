""" trigger/52010059_qd/52010059.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[201], animationEffect=False) # 콘대르
        self.create_monster(spawnIds=[202], animationEffect=False) # 샤텐
        self.create_monster(spawnIds=[203], animationEffect=False) # 네이린
        self.create_monster(spawnIds=[204], animationEffect=False) # 메이슨
        self.set_actor(triggerId=501, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=502, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=503, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=504, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=505, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=506, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=507, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=508, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=509, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=510, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=511, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=512, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=513, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=514, visible=True, initialSequence='sf_quest_light_A01_Off')


initial_state = Wait
