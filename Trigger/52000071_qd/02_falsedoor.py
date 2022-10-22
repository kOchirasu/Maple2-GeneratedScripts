""" trigger/52000071_qd/02_falsedoor.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3001], visible=False, arg3=0, arg4=0, arg5=0) # 미니맵용_Invisible
        set_interact_object(triggerIds=[10001104], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001104], arg2=0):
            return MobSpawn()


class MobSpawn(state.State):
    def on_enter(self):
        create_monster(spawnIds=[902], arg2=True)


