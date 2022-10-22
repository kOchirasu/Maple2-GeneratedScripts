""" trigger/02020027_bf/door.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[9001,9002,9003,9004,9005,9006,9007], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if check_npc_hp(compare='lower', value=50, spawnId=201, isRelative=True):
            return 문열림()


class 문열림(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[9001,9002,9003,9004,9005,9006,9007], visible=False, arg3=0, arg4=0, arg5=10)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[1002]):
            return 문닫힘()


class 문닫힘(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[9001,9002,9003,9004,9005,9006], visible=True, arg3=0, arg4=0, arg5=10)
        set_mesh(triggerIds=[9007], visible=True, arg3=0, arg4=0, arg5=0) # <두번째 방 튀어나갈 사람에 대한 예외처리로 페이드없이 바로 생기는 투명 메쉬>

    def on_tick(self) -> state.State:
        if true():
            return 종료()


class 종료(state.State):
    pass


