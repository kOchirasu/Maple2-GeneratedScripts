""" trigger/52020009_qd/main.xml """
import trigger_api


class Idle(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[8001], visible=False)
        self.set_interact_object(triggerIds=[10001266], state=0)
        self.set_effect(triggerIds=[5001], visible=False)
        self.set_effect(triggerIds=[5002], visible=False)
        self.set_effect(triggerIds=[5003], visible=False)
        self.set_effect(triggerIds=[5004], visible=False)
        self.set_effect(triggerIds=[5005], visible=False)
        self.set_effect(triggerIds=[5006], visible=False)
        self.set_effect(triggerIds=[5100], visible=True) # 웃는 소리
        self.set_effect(triggerIds=[5101], visible=True) # 까마귀 소리
        self.set_effect(triggerIds=[5102], visible=True) # 뛰는 소리

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[60200020], questStates=[1]):
            return Ready(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[60200020], questStates=[2]):
            return MeshOff(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[60200020], questStates=[3]):
            return MeshOff(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[201], animationEffect=True)
        self.create_monster(spawnIds=[202], animationEffect=True)
        self.create_monster(spawnIds=[203], animationEffect=True)
        self.create_monster(spawnIds=[204], animationEffect=True)
        self.create_monster(spawnIds=[205], animationEffect=True)
        self.create_monster(spawnIds=[206], animationEffect=True)
        self.create_monster(spawnIds=[207], animationEffect=True)
        self.set_effect(triggerIds=[5001], visible=True)
        self.set_effect(triggerIds=[5002], visible=True)
        self.set_effect(triggerIds=[5003], visible=True)
        self.set_effect(triggerIds=[5004], visible=True)
        self.set_effect(triggerIds=[5005], visible=True)
        self.set_effect(triggerIds=[5006], visible=True)
        self.set_mesh(triggerIds=[8001], visible=True)
        self.add_balloon_talk(spawnId=0, msg='!', duration=3000, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[201,202,203,204,205,206,207]):
            return Event_01(self.ctx)


class Event_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001266], state=1)
        self.set_mesh(triggerIds=[8001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000449], stateValue=0):
            return MeshOff(self.ctx)


class MeshOff(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[8001], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[60200020], questStates=[1]):
            return Event_01(self.ctx)


initial_state = Idle
