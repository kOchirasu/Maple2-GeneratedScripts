""" trigger/63000076_cs/63000076_chat_707.xml """
from common import *
import state


class 준비(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[707]):
            return 잡담_01_707()


class 잡담_01_707(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=119, msg='$63000076_CS__63000076_CHAT_707__0$', duration=2500, delayTick=0) # 이거 이거 열어봐도 돼요?

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 잡담_02_707()


class 잡담_02_707(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=119, msg='$63000076_CS__63000076_CHAT_707__1$', duration=2500, delayTick=0) # 안 돼요?

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 종료()


class 종료(state.State):
    pass


