""" trigger/52000073_qd/hiddendoor02.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_actor(triggerId=3000, visible=True, initialSequence='Closed') # HiddenDoor
        set_mesh(triggerIds=[2000], visible=True, arg3=0, arg4=0, arg5=0) # Wall
        set_breakable(triggerIds=[4000], enabled=False) # Move
        set_visible_breakable_object(triggerIds=[4000], arg2=False) # Move
        set_interact_object(triggerIds=[10001082], state=1) # BookCase
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001082], arg2=0):
            return BookCaseMove01()


class BookCaseMove01(state.State):
    def on_enter(self):
        set_breakable(triggerIds=[4000], enabled=True) # Move
        set_visible_breakable_object(triggerIds=[4000], arg2=True) # Move
        set_mesh(triggerIds=[2000], visible=False, arg3=0, arg4=0, arg5=3) # Wall

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return DoorOpen01()


class DoorOpen01(state.State):
    def on_enter(self):
        set_actor(triggerId=3000, visible=True, initialSequence='Opened') # HiddenDoor
        set_portal(portalId=2, visible=True, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return DoorOpen02()


class DoorOpen02(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=57000):
            return DoorClose01()


class DoorClose01(state.State):
    def on_enter(self):
        set_actor(triggerId=3000, visible=True, initialSequence='Closed') # HiddenDoor
        set_portal(portalId=2, visible=True, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return DoorClose02()


class DoorClose02(state.State):
    def on_enter(self):
        set_breakable(triggerIds=[4000], enabled=False) # Move
        set_visible_breakable_object(triggerIds=[4000], arg2=False) # Move
        set_mesh(triggerIds=[2000], visible=True, arg3=0, arg4=0, arg5=3) # Wall
        set_interact_object(triggerIds=[10001082], state=1) # BookCase
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Reset()


class Reset(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001082], arg2=0):
            return BookCaseMove01()


