""" trigger/02000419_bf/1122338_barricade.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014], visible=False, arg3=0, arg4=0, arg5=0) # 시작지점 철창벽 셋팅 최초에는 숨김 설정

    def on_tick(self) -> state.State:
        if monster_in_combat(boxIds=[2000]):
            return 카운트()


class 카운트(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000419_BF__BARRICADE__0$', arg3='3000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=30000):
            return 차단()


class 차단(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014], visible=True, arg3=1, arg4=1, arg5=1) # 시작지점 철창벽 생성

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2000]):
            return 차단해제()


class 차단해제(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014], visible=False, arg3=0, arg4=0, arg5=0) # 보스가 죽으면 시작지점 철창벽 제거


