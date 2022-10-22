""" trigger/63000017_cs/chat01.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101,102,103], arg2=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9900]):
            return Delay01()


class Delay01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=15000):
            return Chat01()


class Chat01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=101, script='$63000017_CS__CHAT01__0$', arg4=4, arg5=0)
        set_conversation(type=1, spawnId=102, script='$63000017_CS__CHAT01__1$', arg4=4, arg5=5)
        set_conversation(type=1, spawnId=101, script='$63000017_CS__CHAT01__2$', arg4=4, arg5=10)
        set_conversation(type=1, spawnId=102, script='$63000017_CS__CHAT01__3$', arg4=4, arg5=16)
        set_conversation(type=1, spawnId=103, script='$63000017_CS__CHAT01__4$', arg4=4, arg5=20)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=25000):
            return Delay02()


class Delay02(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Chat02()


class Chat02(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=101, script='$63000017_CS__CHAT01__5$', arg4=4, arg5=0)
        set_conversation(type=1, spawnId=102, script='$63000017_CS__CHAT01__6$', arg4=4, arg5=6)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Delay03()


class Delay03(state.State):
    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[9900]):
            return Quit()
        if wait_tick(waitTick=5000):
            return Delay01()


class Quit(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9900]):
            return Delay01()


