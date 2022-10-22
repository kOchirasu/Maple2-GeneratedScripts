""" trigger/63000018_cs/chat02.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        create_monster(spawnIds=[201,202], arg2=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9900]):
            return Delay01()


class Delay01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=12000):
            return Chat01()


class Chat01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=201, script='$63000018_CS__CHAT02__0$', arg4=4, arg5=0)
        set_conversation(type=1, spawnId=202, script='$63000018_CS__CHAT02__1$', arg4=4, arg5=4)
        set_conversation(type=1, spawnId=201, script='$63000018_CS__CHAT02__2$', arg4=4, arg5=8)
        set_conversation(type=1, spawnId=202, script='$63000018_CS__CHAT02__3$', arg4=4, arg5=12)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=16000):
            return Delay02()


class Delay02(state.State):
    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[9900]):
            return Quit()
        if wait_tick(waitTick=12000):
            return Delay01()


class Quit(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9900]):
            return Delay01()


