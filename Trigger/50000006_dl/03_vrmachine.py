""" trigger/50000006_dl/03_vrmachine.xml """
from common import *
import state


#  제논 시스템 연구소 : VR머신 
class Wait(state.State):
    def on_enter(self):
        set_user_value(key='machineon', value=0)
        set_interact_object(triggerIds=[10001246], state=2)
        set_portal(portalId=3, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if user_value(key='machineon', value=1):
            return MachineOn()


class MachineOn(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001246], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001246], arg2=0):
            return PortalOn()


class PortalOn(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='DungeonRoomOpened', value=1)
        set_portal(portalId=3, visible=False, enabled=True, minimapVisible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return ResetDelay()


class ResetDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Reset()


class Reset(state.State):
    def on_enter(self):
        set_portal(portalId=3, visible=False, enabled=False, minimapVisible=False)
        set_interact_object(triggerIds=[10001246], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001246], arg2=0):
            return PortalOn()


