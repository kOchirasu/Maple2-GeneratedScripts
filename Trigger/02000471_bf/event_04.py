""" trigger/02000471_bf/event_04.xml """
from common import *
import state


class idle(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1803], visible=True, arg3=0, arg4=200, arg5=0)
        set_mesh(triggerIds=[1804], visible=False, arg3=0, arg4=200, arg5=0)
        set_mesh(triggerIds=[1805], visible=False, arg3=0, arg4=200, arg5=0)
        set_mesh(triggerIds=[1806], visible=False, arg3=0, arg4=200, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[705]):
            return Ready()


class Ready(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1803], visible=False, arg3=0, arg4=200, arg5=85)
        set_mesh(triggerIds=[1804], visible=True, arg3=0, arg4=200, arg5=85)
        set_mesh(triggerIds=[1805], visible=False, arg3=0, arg4=200, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=15000):
            return Ready_02()


class Ready_02(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1803], visible=False, arg3=0, arg4=200, arg5=5)
        set_mesh(triggerIds=[1804], visible=True, arg3=0, arg4=200, arg5=5)
        set_mesh(triggerIds=[1806], visible=True, arg3=0, arg4=200, arg5=5)
        set_achievement(triggerId=705, type='trigger', achieve='Hauntedmansion')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Ready_03()


class Ready_03(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1806], visible=False, arg3=0, arg4=200, arg5=5)


