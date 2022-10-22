""" trigger/02020141_bf/message.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_tick(self) -> state.State:
        if check_user():
            return 메시지작동준비()


class 메시지작동준비(state.State):
    def on_enter(self):
        set_user_value(key='MessageAlarm', value=0) # 메시지 출력 유무를 결정하는 변수
        set_user_value(key='TriggerEnd', value=0) # 이 변수 99가 되면 이 트리거 작동 중지함, 이 변수 99 신호는 AI_TurkaHoodForce_Phase03.xml에서 받음

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=15000):
            return 메시지작동대기버프체크()


class 메시지작동대기버프체크(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='TriggerEnd', value=99):
            return 트리거종료()
        if user_value(key='MessageAlarm', value=13): # 애디셔널 50000348(레벨1) 졸몹이 보스에게 보호 5중첩 버프 애디셔널 부여함
            return 경고메시지출력()
        if check_npc_additional_effect(spawnId=99, additionalEffectId=50000348, level=1):
            return 카운트다운체크()
        if not check_npc_additional_effect(spawnId=99, additionalEffectId=50000348, level=1):
            return 카운트다운초기화()


class 카운트다운체크(state.State):
    def on_enter(self):
        add_user_value(key='MessageAlarm', value=1) # 이 변수 1씩 더하는데, 이 변수가 13이 되면 메시지 출력함

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 메시지작동대기버프체크()


class 카운트다운초기화(state.State):
    def on_enter(self):
        set_user_value(key='MessageAlarm', value=0) # 보스가 50000348 버프가 없는 상태라면 이 변수 0 초기화
        hide_guide_summary(entityId=29200006)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 메시지작동대기버프체크()


class 경고메시지출력(state.State):
    def on_enter(self):
        show_guide_summary(entityId=29200006, textId=29200006, duration=4000)
        add_user_value(key='MessageAlarm', value=-11) # 이 변수 -11을 빼서 2로 만들기, 계속 보스가 버프 상태를 유지한다면 11초 뒤에 다시 메시지 출력될 것임

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 메시지작동대기버프체크()


class 트리거종료(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=29200006)


