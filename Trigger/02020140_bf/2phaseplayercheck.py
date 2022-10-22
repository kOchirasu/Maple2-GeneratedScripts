""" trigger/02020140_bf/2phaseplayercheck.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_tick(self) -> state.State:
        if check_user():
            return 안잡힌플레이어체크()


class 안잡힌플레이어체크(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='2PhasePlayerCheckStart', value=1):
            return 페이즈지점체크하기1()


class 페이즈지점체크하기1(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[98]):
            return 종료()
        if wait_tick(waitTick=900):
            return 추가로최초시작지점체크하기()


class 추가로최초시작지점체크하기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[99]):
            return 종료()
        if wait_tick(waitTick=900):
            return 안잡힌플레이어없음확인()


class 안잡힌플레이어없음확인(state.State):
    def on_enter(self):
        set_ai_extra_data(key='TwoPhaseMainBattle', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 페이즈복격진행_안내메시지출력2()


class 페이즈복격진행_안내메시지출력2(state.State):
    def on_enter(self):
        set_skill(triggerIds=[91], isEnable=True) # CubeBreak ,  MS2TriggerSkill = 91 스킬코드 70000105(레벨1) 발동시켜 마법구슬 지점에 계단을 막고 있는 큐브 제거함
        show_guide_summary(entityId=29200003, textId=29200003)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6500):
            return 종료()

    def on_exit(self):
        hide_guide_summary(entityId=29200003)


class 종료(state.State):
    pass


