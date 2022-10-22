""" trigger/63000018_cs/chat03.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        create_monster(spawnIds=[301,302], arg2=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9900]):
            return Delay01()


class Delay01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=20000):
            return Chat01()


class Chat01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=301, script='$63000018_CS__CHAT03__0$', arg4=4, arg5=0)
        set_conversation(type=1, spawnId=302, script='$63000018_CS__CHAT03__1$', arg4=4, arg5=4)
        set_conversation(type=1, spawnId=301, script='$63000018_CS__CHAT03__2$', arg4=4, arg5=8)
        set_conversation(type=1, spawnId=302, script='$63000018_CS__CHAT03__3$', arg4=4, arg5=12)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=16000):
            return Delay02()


class Delay02(state.State):
    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[9900]):
            return Quit()
        if wait_tick(waitTick=4000):
            return Delay01()


class Quit(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9900]):
            return Delay01()


