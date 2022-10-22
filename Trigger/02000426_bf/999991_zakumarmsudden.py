""" trigger/02000426_bf/999991_zakumarmsudden.xml """
from common import *
import state


#  MS2TriggerModel ID : 999991, 자쿰 몸통과 싸울 때 자쿰팔이 소환되면, 자쿰 몸체에 무적 버프 걸거, 자쿰팔 다 제거되면 자쿰몸 무적버프 지우는 기능의 트리거임
class 시작(state.State):
    def on_enter(self):
        set_user_value(key='SummonZakumArmRegenCheck', value=0) # 변수 0 초기화, 이 변수는 자쿰 몸통AI에서 자쿰손 소환할 때 이 변수 1로 만드는 신호를 보내서, 자쿰 손 마리수 체크 작업 시작하도록 함
        set_user_value(key='SummonZakumArmMany', value=0) # 변수 0 초기화, 이 변수 신호는 자쿰 몸통하고 싸울때 등장하는 소환몹 자쿰팔AI에서 보냄

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[199]):
            return 대기중()


class 대기중(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='SummonZakumArmRegenCheck', value=1):
            return 자쿰몸통무적버프로직_시작대기중()


class 자쿰몸통무적버프로직_시작대기중(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 자쿰몸통무적버프로직_작동()


class 자쿰몸통무적버프로직_작동(state.State):
    def on_enter(self):
        add_buff(boxIds=[2011], skillId=50000265, level=1, arg4=True, arg5=False) # 어려움 난이도 자쿰몸 스폰 ID가  arg1 = 2011    arg3="1" 은 애디셔널의 레벨, arg4="1" 은 대상이 몬스터라는 뜻 참고로 arg4="0"은 플레이어
        add_buff(boxIds=[2012], skillId=50000265, level=1, arg4=True, arg5=False) # 일반  난이도 자쿰몸 스폰 ID가  arg1 = 2012

    def on_tick(self) -> state.State:
        if user_value(key='SummonZakumArmMany', value=0):
            return 자쿰몸통무적버프_제거대기()


class 자쿰몸통무적버프_제거대기(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 자쿰몸통무적버프_제거작업()


class 자쿰몸통무적버프_제거작업(state.State):
    def on_enter(self):
        npc_remove_additional_effect(spawnId=2011, additionalEffectId=50000265) # 어려움 난이도 자쿰몸 스폰 ID가  2011
        npc_remove_additional_effect(spawnId=2012, additionalEffectId=50000265) # 일반  난이도 자쿰몸 스폰 ID가  2012
        set_user_value(key='SummonZakumArmRegenCheck', value=0) # 자쿰팔 제거되고 무적버프 제거되었으면 이 변수 0 초기화 시켜 "대기중" 상태가 되도록 함

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1200):
            return 대기중()


class 종료(state.State):
    pass


