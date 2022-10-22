""" trigger/02000315_bf/wounded_105.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_user_value(key='BridgeOpen', value=0)
        set_interact_object(triggerIds=[10001040], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001040], arg2=0):
            return WakeUp()


class WakeUp(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001040], state=2)
        create_monster(spawnIds=[105], arg2=False)

    def on_tick(self) -> state.State:
        if user_value(key='BridgeOpen', value=2):
            return Patrol02()
        if user_value(key='BridgeOpen', value=3):
            return Patrol03()


class Patrol02(state.State):
    def on_enter(self):
        move_npc(spawnId=105, patrolName='MS2PatrolData_1051')

    def on_tick(self) -> state.State:
        if user_value(key='BridgeOpen', value=3):
            return Patrol03()


class Patrol03(state.State):
    def on_enter(self):
        move_npc(spawnId=105, patrolName='MS2PatrolData_1052')


