""" trigger/02020142_bf/2phasetubeattackcheck.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_user_value(key='2PhaseTubeStep', value=0) # 변수 최초 초기화: 이 변수가 1이 되면 튜브 대미지 필드 1단계 진행,  이 변수가 2이 되면 튜브 대미지 필드 2단계 진행
        set_user_value(key='MarbleTurkaSupportMany', value=0) # 변수 최초 초기화: 마법 구슬 오브젝트가 등장하면, 이 오브젝트  AI_MarbleTurkaSupport.xml  AI로 부터 이 변수 +1 신호를 받고, 파괴되어 죽으면  AI_MarbleTurkaSupport.xml AI로 부터 이 변수 -1 신호를 받게 됨

    def on_tick(self) -> state.State:
        if check_user():
            return 트리거작동신호받기대기중()


class 트리거작동신호받기대기중(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='2PhaseTubeStep', value=1, operator='GreaterEqual'):
            return 트리거작동대기중()


class 트리거작동대기중(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 트리거작동시작()


class 트리거작동시작(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='2PhaseTubeStep', value=1):
            return 튜브대미지필드_1단계진행()
        if user_value(key='2PhaseTubeStep', value=2):
            return 튜브대미지필드_2단계전환_우선1단계제거()


class 튜브대미지필드_1단계진행(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='MarbleTurkaSupportMany', value=1, operator='GreaterEqual'):
            return 단계_튜브대미지필드_생성1()
        if wait_tick(waitTick=1000):
            return 단계_튜브대미지필드_제거1()


class 단계_튜브대미지필드_생성1(state.State):
    def on_enter(self):
        add_buff(boxIds=[102], skillId=50004566, level=1, arg4=True, arg5=True) # 1단계 튜브대미지필드 발동 , arg1 은 등장 몬스터의 스폰ID, arg2은 애디셔널 코드,  arg3은 애디셔널 레벨,   arg4 = 1 이면 플레이어가 아닌 NPC에게 적용,    arg5 = 1 하면 트리거 박스 영역 외의 모든 지점 체크

    def on_tick(self) -> state.State:
        if user_value(key='2PhaseTubeStep', value=2):
            return 튜브대미지필드_2단계전환_우선1단계제거()
        if user_value(key='MarbleTurkaSupportMany', value=0):
            return 단계_튜브대미지필드_제거1()


class 단계_튜브대미지필드_제거1(state.State):
    def on_enter(self):
        npc_remove_additional_effect(spawnId=102, additionalEffectId=50004566) # 1단계 튜브대미지필드 제거

    def on_tick(self) -> state.State:
        if user_value(key='2PhaseTubeStep', value=2):
            return 튜브대미지필드_2단계전환_우선1단계제거()
        if wait_tick(waitTick=1000):
            return 튜브대미지필드_1단계진행()


class 튜브대미지필드_2단계전환_우선1단계제거(state.State):
    def on_enter(self):
        npc_remove_additional_effect(spawnId=102, additionalEffectId=50004566) # 우선 1단계 튜브대미지필드  제거
        set_user_value(key='TubeLeveStep', value=0) # 이 변수 최초 초기화: 보스가 마법 구슬 오브제트로 인한 애디셔널에 계속 걸려 있으면, 이 변수 1씩 더하는데, 이 변수가 10씩 쌓일 수록 튜브대미지필드 1단계씩 상승시킴

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 단계_튜브대미지필드_처음단계2()


class 단계_튜브대미지필드_처음단계2(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='MarbleTurkaSupportMany', value=1, operator='GreaterEqual'):
            return 단계_튜브대미지필드_1Lv생성2()
        if wait_tick(waitTick=1000):
            return 단계_튜브대미지필드_제거2()


class 단계_튜브대미지필드_1Lv생성2(state.State):
    def on_enter(self):
        add_buff(boxIds=[102], skillId=50004563, level=1, arg4=True, arg5=True) # 튜브대미지필드 1Lv 발동 , arg1 은 등장 몬스터의 스폰ID, arg2은 애디셔널 코드,  arg3은 애디셔널 레벨,   arg4 = 1 이면 플레이어가 아닌 NPC에게 적용,    arg5 = 1 하면 트리거 박스 영역 외의 모든 지점 체크

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 단계_튜브대미지필드_TubeLeveStep_더하기2()


class 단계_튜브대미지필드_2Lv생성2(state.State):
    def on_enter(self):
        npc_remove_additional_effect(spawnId=102, additionalEffectId=50004563) # 2단계 튜브대미지필드 1Lv  제거
        add_buff(boxIds=[102], skillId=50004564, level=1, arg4=True, arg5=True) # 튜브대미지필드 2Lv 발동 , arg1 은 등장 몬스터의 스폰ID, arg2은 애디셔널 코드,  arg3은 애디셔널 레벨,   arg4 = 1 이면 플레이어가 아닌 NPC에게 적용,    arg5 = 1 하면 트리거 박스 영역 외의 모든 지점 체크

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 단계_튜브대미지필드_TubeLeveStep_더하기2()


class 단계_튜브대미지필드_3Lv생성2(state.State):
    def on_enter(self):
        npc_remove_additional_effect(spawnId=102, additionalEffectId=50004564) # 2단계 튜브대미지필드 2Lv 제거
        add_buff(boxIds=[102], skillId=50004565, level=1, arg4=True, arg5=True) # 튜브대미지필드 3Lv 발동 , arg1 은 등장 몬스터의 스폰ID, arg2은 애디셔널 코드,  arg3은 애디셔널 레벨,   arg4 = 1 이면 플레이어가 아닌 NPC에게 적용,    arg5 = 1 하면 트리거 박스 영역 외의 모든 지점 체크

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 단계_튜브대미지필드_TubeLeveStep_더하기2()


class 단계_튜브대미지필드_TubeLeveStep_더하기2(state.State):
    def on_enter(self):
        add_user_value(key='TubeLeveStep', value=1) # 이 변수 1씩 더하는데, 이 변수가 10씩 쌓일 수록 튜브대미지필드 1단계씩 상승시킴

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 단계_튜브대미지필드_TubeLeveStep_체크2()


class 단계_튜브대미지필드_TubeLeveStep_체크2(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='TubeLeveStep', value=10):
            return 단계_튜브대미지필드_2Lv생성2()
        if user_value(key='TubeLeveStep', value=20):
            return 단계_튜브대미지필드_3Lv생성2()
        if user_value(key='MarbleTurkaSupportMany', value=1, operator='GreaterEqual'):
            return 단계_튜브대미지필드_TubeLeveStep_더하기2()
        if wait_tick(waitTick=1000):
            return 단계_튜브대미지필드_제거2()


class 단계_튜브대미지필드_제거2(state.State):
    def on_enter(self):
        npc_remove_additional_effect(spawnId=102, additionalEffectId=50004563) # 2단계 튜브대미지필드 1Lv  제거
        npc_remove_additional_effect(spawnId=102, additionalEffectId=50004564) # 2단계 튜브대미지필드 2Lv 제거
        npc_remove_additional_effect(spawnId=102, additionalEffectId=50004565) # 2단계 튜브대미지필드 3Lv 제거
        set_user_value(key='TubeLeveStep', value=0) # 다시 처음부터 시작하니 이 변수  초기화: 보스가 마법 구슬 오브제트로 인한 애디셔널에 계속 걸려 있으면, 이 변수 1씩 더하는데, 이 변수가 10씩 쌓일 수록 튜브대미지필드 1단계씩 상승시킴

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 단계_튜브대미지필드_처음단계2()


class 종료(state.State):
    pass


