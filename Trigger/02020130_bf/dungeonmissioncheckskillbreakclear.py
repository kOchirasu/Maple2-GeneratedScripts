""" trigger/02020130_bf/dungeonmissioncheckskillbreakclear.xml """
from common import *
import state


class Ready(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[601]):
            return 보스스킬브레이크시작_대기중()


class 보스스킬브레이크시작_대기중(state.State):
    def on_tick(self) -> state.State:
        if check_npc_additional_effect(spawnId=701, additionalEffectId=50004546, level=2):
            return 던전미션_체크()
        if check_npc_additional_effect(spawnId=702, additionalEffectId=62100024, level=2):
            return 던전미션_체크()
        if check_npc_additional_effect(spawnId=703, additionalEffectId=62100016, level=2):
            return 던전미션_체크()


class 던전미션_체크(state.State):
    def on_tick(self) -> state.State:
        if check_npc_additional_effect(spawnId=701, additionalEffectId=70002171, level=1): # 유페리아 경우에만 스킬브레이크 클리어  체크하는 로직
            return 던전미션_스킬브레이크저지_성공()
        if check_npc_additional_effect(spawnId=702, additionalEffectId=70002171, level=1): # 렌듀비앙 경우에만 스킬브레이크 클리어  체크하는 로직
            return 던전미션_스킬브레이크저지_성공()
        if check_npc_additional_effect(spawnId=703, additionalEffectId=70002171, level=1): # 3마리 보스 중 하나라도 극 광역공격 실행하면 무조건 실패해서 트리거 처음으로 돌려놓기, 실패 체크 단계는 맨 마지막 쪽에 하는 것이 안정적임
            return 던전미션_스킬브레이크저지_성공()
        if check_npc_additional_effect(spawnId=701, additionalEffectId=50000264, level=1):
            return 보스스킬브레이크시작_대기중()
        if check_npc_additional_effect(spawnId=702, additionalEffectId=50000264, level=3):
            return 보스스킬브레이크시작_대기중()
        if check_npc_additional_effect(spawnId=703, additionalEffectId=50000264, level=2):
            return 보스스킬브레이크시작_대기중()


class 던전미션_스킬브레이크저지_성공(state.State):
    def on_enter(self):
        dungeon_mission_complete(missionId=23040005) # DungeonMission.xml 에 등록된 숫자 코드 미션 완료 처리하기,  스킬브레이크 한번이라도 막기 클리어 미션 달성임

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1100):
            return 종료()


class 종료(state.State):
    pass


