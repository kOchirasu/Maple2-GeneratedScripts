""" trigger/63000076_cs/63000076_chat_705.xml """
from common import *
import state


class 준비(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[705]):
            return 잡담_01_705()


class 잡담_01_705(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=116, msg='$63000076_CS__63000076_CHAT_705__0$', duration=2500, delayTick=0) # 이거 누르면 소리 나요

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 잡담_02_705()


class 잡담_02_705(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=117, msg='$63000076_CS__63000076_CHAT_705__1$', duration=2500, delayTick=0) # 소리 들어보고 싶어요

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 종료()


class 종료(state.State):
    pass

