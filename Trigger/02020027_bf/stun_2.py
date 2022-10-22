""" trigger/02020027_bf/stun_2.xml """
from common import *
import state


class 시작(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[1001]):
            return 전투시작()


class 전투시작(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='summon_3_2', value=1):
            return 버프()


class 버프(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=11000):
            return 버프_2()


class 버프_2(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=301, script='$02020027_BF__stun_1__0$', arg4=3, arg5=0)
        set_conversation(type=1, spawnId=302, script='$02020027_BF__stun_1__1$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 버프_4()


class 버프_4(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=303, script='$02020027_BF__stun_1__2$', arg4=3, arg5=0)
        set_conversation(type=1, spawnId=304, script='$02020027_BF__stun_1__3$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 버프_5()


class 버프_5(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=305, script='$02020027_BF__stun_1__4$', arg4=3, arg5=0)
        set_conversation(type=1, spawnId=306, script='$02020027_BF__stun_1__5$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if true():
            return 버프_제거()


class 버프_제거(state.State):
    def on_enter(self):
        add_buff(boxIds=[201], skillId=62000002, level=1, arg4=True)

    def on_tick(self) -> state.State:
        if true():
            return None


