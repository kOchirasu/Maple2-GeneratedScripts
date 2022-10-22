""" trigger/02010052_bf/invisiblewall03.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[20300,20301,20302,20303,20304,20305,20306,20307,20308,20309,20310,20311,20312,20313,20314,20315,20316,20317,20318,20319,20320,20321,20322,20323,20324,20325,20326,20327,20328,20329,20330], visible=True, arg4=0, arg5=3) # 벽 해제

    def on_tick(self) -> state.State:
        if count_users(boxId=712, boxId=1):
            return 벽면처리()


class 벽면처리(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[20300,20301,20302,20303,20304,20305,20306,20307,20308,20309,20310,20311,20312,20313,20314,20315,20316,20317,20318,20319,20320,20321,20322,20323,20324,20325,20326,20327,20328,20329,20330], visible=False, arg4=0, arg5=3) # 벽 해제

    def on_tick(self) -> state.State:
        if not count_users(boxId=712, boxId=1):
            return 시작()


