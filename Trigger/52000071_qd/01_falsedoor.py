""" trigger/52000071_qd/01_falsedoor.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3000], visible=False, arg3=0, arg4=0, arg5=0) # 미니맵용_Invisible
        set_interact_object(triggerIds=[10001103], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001103], arg2=0):
            return MobSpawn()


class MobSpawn(state.State):
    def on_enter(self):
        create_monster(spawnIds=[901], arg2=True)


