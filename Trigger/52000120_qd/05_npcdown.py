""" trigger/52000120_qd/05_npcdown.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001169], state=2)
        destroy_monster(spawnIds=[231]) # NPC
        set_user_value(key='NpcDown', value=0)
        set_user_value(key='BattleEnd', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='NpcDown', value=1):
            return Delay()


class Delay(state.State):
    def on_enter(self):
        set_user_value(key='NpcDown', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=20000):
            return NpcDown()


class NpcDown(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[221])
        set_interact_object(triggerIds=[10001169], state=1)

    def on_tick(self) -> state.State:
        if user_value(key='BattleEnd', value=1):
            return Quit()
        if object_interacted(interactIds=[10001169], arg2=0):
            return NpcWakeUp()


class NpcWakeUp(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001169], state=2)
        create_monster(spawnIds=[231], arg2=False)

    def on_tick(self) -> state.State:
        if user_value(key='BattleEnd', value=1):
            return Quit()
        if npc_detected(boxId=9900, spawnIds=[221]):
            return Delay02()


class Delay02(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001169], state=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=45000):
            return NpcDown02()


class NpcDown02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[231])
        set_interact_object(triggerIds=[10001169], state=1)

    def on_tick(self) -> state.State:
        if user_value(key='BattleEnd', value=1):
            return Quit()
        if object_interacted(interactIds=[10001169], arg2=0):
            return NpcWakeUp()


class Quit(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[221,231])
        set_interact_object(triggerIds=[10001169], state=0)


