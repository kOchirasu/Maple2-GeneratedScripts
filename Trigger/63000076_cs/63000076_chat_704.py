""" trigger/63000076_cs/63000076_chat_704.xml """
from common import *
import state


class 준비(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[704]):
            return 잡담_01_704()


class 잡담_01_704(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=107, msg='$63000076_CS__63000076_CHAT_704__0$', duration=2000, delayTick=0) # 너 피부 좋아졌다?

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 잡담_02_704()


class 잡담_02_704(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=105, msg='$63000076_CS__63000076_CHAT_704__1$', duration=2500, delayTick=0) # 요즘 스팀 마사지하고 있거든

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 종료()


class 종료(state.State):
    pass


