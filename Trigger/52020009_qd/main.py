""" trigger/52020009_qd/main.xml """
from common import *
import state


class Idle(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8001], visible=False)
        set_interact_object(triggerIds=[10001266], state=0)
        set_effect(triggerIds=[5001], visible=False)
        set_effect(triggerIds=[5002], visible=False)
        set_effect(triggerIds=[5003], visible=False)
        set_effect(triggerIds=[5004], visible=False)
        set_effect(triggerIds=[5005], visible=False)
        set_effect(triggerIds=[5006], visible=False)
        set_effect(triggerIds=[5100], visible=True) # 웃는 소리
        set_effect(triggerIds=[5101], visible=True) # 까마귀 소리
        set_effect(triggerIds=[5102], visible=True) # 뛰는 소리

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[60200020], questStates=[1]):
            return Ready()
        if quest_user_detected(boxIds=[2001], questIds=[60200020], questStates=[2]):
            return MeshOff()
        if quest_user_detected(boxIds=[2001], questIds=[60200020], questStates=[3]):
            return MeshOff()


class Ready(state.State):
    def on_enter(self):
        create_monster(spawnIds=[201], arg2=True)
        create_monster(spawnIds=[202], arg2=True)
        create_monster(spawnIds=[203], arg2=True)
        create_monster(spawnIds=[204], arg2=True)
        create_monster(spawnIds=[205], arg2=True)
        create_monster(spawnIds=[206], arg2=True)
        create_monster(spawnIds=[207], arg2=True)
        set_effect(triggerIds=[5001], visible=True)
        set_effect(triggerIds=[5002], visible=True)
        set_effect(triggerIds=[5003], visible=True)
        set_effect(triggerIds=[5004], visible=True)
        set_effect(triggerIds=[5005], visible=True)
        set_effect(triggerIds=[5006], visible=True)
        set_mesh(triggerIds=[8001], visible=True)
        add_balloon_talk(spawnId=0, msg='!', duration=3000, delayTick=0)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[201,202,203,204,205,206,207]):
            return Event_01()


class Event_01(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001266], state=1)
        set_mesh(triggerIds=[8001], visible=True)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000449], arg2=0):
            return MeshOff()


class MeshOff(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8001], visible=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[60200020], questStates=[1]):
            return Event_01()


