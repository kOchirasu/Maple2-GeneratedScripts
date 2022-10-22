""" trigger/52100052_qd/11_ironplatetrap.xml """
from common import *
import state


class Setting(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3420,3421,3422,3423], visible=True, arg3=0, arg4=0, arg5=0) # IronPlateHold
        set_effect(triggerIds=[5200], visible=False) # CubeSkillNotice
        set_effect(triggerIds=[5201], visible=False) # CubeSkillNotice
        set_effect(triggerIds=[5202], visible=False) # CubeSkillNotice
        set_effect(triggerIds=[5203], visible=False) # CubeSkillNotice
        destroy_monster(spawnIds=[202,302])
        set_interact_object(triggerIds=[10002081], state=0, arg4=False) # LeverForTrap
        set_user_value(key='TrapOn', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='TrapOn', value=1):
            return LeverOnDelay()


class LeverOnDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return LeverOn()


class LeverOn(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002081], state=1) # LeverForTrap
        set_effect(triggerIds=[5200], visible=True) # CubeSkillNotice
        set_effect(triggerIds=[5201], visible=True) # CubeSkillNotice
        set_effect(triggerIds=[5202], visible=True) # CubeSkillNotice
        set_effect(triggerIds=[5203], visible=True) # CubeSkillNotice

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10002081], arg2=0):
            return TrapOn()


class TrapOn(state.State):
    def on_enter(self):
        create_monster(spawnIds=[202,302], arg2=False)
        set_mesh(triggerIds=[3420,3421,3422,3423], visible=False, arg3=500, arg4=0, arg5=2) # IronPlateHold
        set_effect(triggerIds=[5200], visible=False) # CubeSkillNotice
        set_effect(triggerIds=[5201], visible=False) # CubeSkillNotice
        set_effect(triggerIds=[5202], visible=False) # CubeSkillNotice
        set_effect(triggerIds=[5203], visible=False) # CubeSkillNotice

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Remove()


class Remove(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[202,302])


