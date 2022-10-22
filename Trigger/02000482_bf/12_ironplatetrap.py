""" trigger/02000482_bf/12_ironplatetrap.xml """
from common import *
import state


class Setting(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3430,3431,3432,3433], visible=True, arg3=0, arg4=0, arg5=0) # IronPlateHold
        set_effect(triggerIds=[5300], visible=False) # CubeSkillNotice
        set_effect(triggerIds=[5301], visible=False) # CubeSkillNotice
        set_effect(triggerIds=[5302], visible=False) # CubeSkillNotice
        set_effect(triggerIds=[5303], visible=False) # CubeSkillNotice
        destroy_monster(spawnIds=[203,303])
        set_interact_object(triggerIds=[10002029], state=0, arg4=False) # LeverForTrap
        set_user_value(key='TrapOn', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='TrapOn', value=1):
            return LeverOnDelay()


class LeverOnDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return LeverOn()


class LeverOn(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002029], state=1) # LeverForTrap
        set_effect(triggerIds=[5300], visible=True) # CubeSkillNotice
        set_effect(triggerIds=[5301], visible=True) # CubeSkillNotice
        set_effect(triggerIds=[5302], visible=True) # CubeSkillNotice
        set_effect(triggerIds=[5303], visible=True) # CubeSkillNotice

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10002029], arg2=0):
            return TrapOn()


class TrapOn(state.State):
    def on_enter(self):
        create_monster(spawnIds=[203,303], arg2=False)
        set_mesh(triggerIds=[3430,3431,3432,3433], visible=False, arg3=500, arg4=0, arg5=2) # IronPlateHold
        set_effect(triggerIds=[5300], visible=False) # CubeSkillNotice
        set_effect(triggerIds=[5301], visible=False) # CubeSkillNotice
        set_effect(triggerIds=[5302], visible=False) # CubeSkillNotice
        set_effect(triggerIds=[5303], visible=False) # CubeSkillNotice

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Remove()


class Remove(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[203,303])


