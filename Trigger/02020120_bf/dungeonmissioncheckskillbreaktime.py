""" trigger/02020120_bf/dungeonmissioncheckskillbreaktime.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[199]):
            return 보스스킬브레이크시작_대기중()


class 보스스킬브레이크시작_대기중(state.State):
    def on_tick(self) -> state.State:
        if check_npc_additional_effect(spawnId=99, additionalEffectId=50004546, level=1):
            return 던전미션_체크()


class 던전미션_체크(state.State):
    def on_tick(self) -> state.State:
        if all_of():
            return 던전미션_스킬브레이크저지_성공()
        if check_npc_additional_effect(spawnId=99, additionalEffectId=50000367, level=1):
            return 던전미션_스킬브레이크저지_실패()


class 던전미션_스킬브레이크저지_성공(state.State):
    def on_enter(self):
        dungeon_mission_complete(missionId=23037004) # DungeonMission.xml 에 등록된 숫자 코드 미션 완료 처리하기

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 종료()


class 던전미션_스킬브레이크저지_실패(state.State):
    def on_tick(self) -> state.State:
        if not check_npc_additional_effect(spawnId=99, additionalEffectId=50004546, level=1):
            return 시작대기중()


class 종료(state.State):
    pass


