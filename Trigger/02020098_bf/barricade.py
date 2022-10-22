""" trigger/02020098_bf/barricade.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[301,302,303,304,305,306,307,308,309,310,311], visible=False, arg3=0, arg4=0, arg5=0) # 스타트포인트 지점의 칸막이 트리거메쉬 최초에는 감추기

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[10]):
            return 칸막이대기시작()


class 칸막이대기시작(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 칸막이대기알림()


class 칸막이대기알림(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02020098_BF__BARRICADE__0$', arg3='3000')
        dungeon_enable_give_up(isEnable='1')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=22000):
            return 칸막이막기()


class 칸막이막기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[301,302,303,304,305,306,307,308,309,310,311], visible=True, arg3=1, arg4=120, arg5=0.5) # 시작지점의 칸막이 막기

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 트리거종료()


class 트리거종료(state.State):
    pass


