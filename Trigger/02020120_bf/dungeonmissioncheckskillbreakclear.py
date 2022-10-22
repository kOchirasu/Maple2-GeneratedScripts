""" trigger/02020120_bf/dungeonmissioncheckskillbreakclear.xml """
from common import *
import state


class Ready(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='SkillBreakSuccess', value=1):
            return 스킬브레이크성공_던전미션랭크()


class 스킬브레이크성공_던전미션랭크(state.State):
    def on_enter(self):
        dungeon_mission_complete(missionId=23037005) # 스킬브레이크 막기 성공하면 SkillBreakSuccess = 1 신호를 받아서, DungeonMission.xml 에 등록된 숫자 코드 미션 완료 처리하기

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 종료()


class 종료(state.State):
    pass


