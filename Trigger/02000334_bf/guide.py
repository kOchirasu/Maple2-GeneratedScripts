""" trigger/02000334_bf/guide.xml """
from common import *
import state


#  플레이어 감지 
class 대기시간(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=90099, spawnIds=[150]):
            return 차타이머1()


class 차타이머1(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 가이드_01()


class 가이드_01(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=101, textId=20000010) # 폭탄을 던지세요
        set_effect(triggerIds=[90021], visible=True) # 이벤트 UI 에 맞는 사운드
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=90001, spawnIds=[301]):
            return 차타이머2()
        if time_expired(timerId='5'):
            return 가이드_01_02()

    def on_exit(self):
        hide_guide_summary(entityId=101) # 폭탄을 던지세요


class 가이드_01_02(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=90001, spawnIds=[301]):
            return 차타이머2()


class 차타이머2(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 가이드_02()


class 가이드_02(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[90100]):
            return 오스칼_배웅()
        if monster_dead(boxIds=[190]):
            return 가이드_02_02()


class 가이드_02_02(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[90100]):
            return 오스칼_배웅()


class 오스칼_배웅(state.State):
    def on_enter(self):
        move_npc(spawnId=199, patrolName='MS2PatrolData_2016') # 오스칼 플레이어를 쳐다봄...


