""" trigger/99999883/testtrigger3.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001010], state=0) # FlyingCloud
        set_breakable(triggerIds=[4000], enabled=False)
        set_visible_breakable_object(triggerIds=[4000], arg2=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9900]):
            return Enter01()


class Enter01(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001010], state=1) # FlyingCloud

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001010], arg2=0):
            return TakeOffFlyingCloud01()


class TakeOffFlyingCloud01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        set_interact_object(triggerIds=[10001010], state=2) # FlyingCloud
        set_visible_breakable_object(triggerIds=[4000], arg2=True)
        set_breakable(triggerIds=[4000], enabled=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return TakeOffFlyingCloud02()


class TakeOffFlyingCloud02(state.State):
    def on_enter(self):
        move_user(mapId=99999883, portalId=100, boxId=9900)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return TakeOffFlyingCloud03()


class TakeOffFlyingCloud03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return TakeOffFlyingCloud04()


class TakeOffFlyingCloud04(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        move_user(mapId=99999883, portalId=101, boxId=9900)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        set_breakable(triggerIds=[4000], enabled=False)
        set_visible_breakable_object(triggerIds=[4000], arg2=False)


