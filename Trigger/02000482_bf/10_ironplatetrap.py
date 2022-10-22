""" trigger/02000482_bf/10_ironplatetrap.xml """
from common import *
import state


class Setting(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3410,3411,3412,3413], visible=True, arg3=0, arg4=0, arg5=0) # IronPlateHold
        set_effect(triggerIds=[5100], visible=False) # CubeSkillNotice
        set_effect(triggerIds=[5101], visible=False) # CubeSkillNotice
        set_effect(triggerIds=[5102], visible=False) # CubeSkillNotice
        set_effect(triggerIds=[5103], visible=False) # CubeSkillNotice
        destroy_monster(spawnIds=[201,301])
        set_interact_object(triggerIds=[10002027], state=0, arg4=False) # LeverForTrap
        set_user_value(key='TrapOn', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='TrapOn', value=1):
            return LeverOnDelay()


class LeverOnDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return LeverOn()


class LeverOn(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002027], state=1) # LeverForTrap
        set_effect(triggerIds=[5100], visible=True) # CubeSkillNotice
        set_effect(triggerIds=[5101], visible=True) # CubeSkillNotice
        set_effect(triggerIds=[5102], visible=True) # CubeSkillNotice
        set_effect(triggerIds=[5103], visible=True) # CubeSkillNotice

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10002027], arg2=0):
            return TrapOn()


class TrapOn(state.State):
    def on_enter(self):
        create_monster(spawnIds=[201,301], arg2=False)
        set_mesh(triggerIds=[3410,3411,3412,3413], visible=False, arg3=500, arg4=0, arg5=2) # IronPlateHold
        set_effect(triggerIds=[5100], visible=False) # CubeSkillNotice
        set_effect(triggerIds=[5101], visible=False) # CubeSkillNotice
        set_effect(triggerIds=[5102], visible=False) # CubeSkillNotice
        set_effect(triggerIds=[5103], visible=False) # CubeSkillNotice

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Remove()


class Remove(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[201,301])


