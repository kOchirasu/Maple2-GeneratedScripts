""" trigger/52000071_qd/03_truedoor.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3002], visible=False, arg3=0, arg4=0, arg5=0) # 미니맵용_Invisible
        set_portal(portalId=10, visible=False, enabled=False, minimapVisible=False)
        set_interact_object(triggerIds=[10001105], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001105], arg2=0):
            return MobSpawn()


class MobSpawn(state.State):
    def on_enter(self):
        set_portal(portalId=10, visible=True, enabled=True, minimapVisible=True)


