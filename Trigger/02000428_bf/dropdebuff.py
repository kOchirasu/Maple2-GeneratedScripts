""" trigger/02000428_bf/dropdebuff.xml """
from common import *
import state


class Ready(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=750, boxId=1):
            return 드랍어뷰징디버프_작동시작()


class 드랍어뷰징디버프_작동시작(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=780, boxId=1):
            return 전투판에떨어지면디버프걸기()


class 전투판에떨어지면디버프걸기(state.State):
    def on_enter(self):
        add_buff(boxIds=[780], skillId=50000512, level=1, arg4=False, arg5=False) # MS2TriggerBox   TriggerObjectID = 780, 이 트리거 박스 안에 있는 플레이어 Sp 0 상태이상 걸리게 하기

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return 드랍어뷰징디버프_작동시작()


