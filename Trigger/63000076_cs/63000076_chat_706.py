""" trigger/63000076_cs/63000076_chat_706.xml """
from common import *
import state


class 준비(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[706]):
            return 잡담_01_706()


class 잡담_01_706(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=118, msg='$63000076_CS__63000076_CHAT_706__0$', duration=2500, delayTick=0) # 신발… 아…이 신발, 신어보고 싶어요

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 종료()


class 종료(state.State):
    pass


