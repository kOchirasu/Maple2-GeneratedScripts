""" trigger/02020120_bf/dungeonmissioncheckskillbreakclear.xml """
import common


class Ready(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='SkillBreakSuccess', value=1):
            return 스킬브레이크성공_던전미션랭크(self.ctx)


class 스킬브레이크성공_던전미션랭크(common.Trigger):
    def on_enter(self):
        self.dungeon_mission_complete(missionId=23037005) # 스킬브레이크 막기 성공하면 SkillBreakSuccess = 1 신호를 받아서, DungeonMission.xml 에 등록된 숫자 코드 미션 완료 처리하기

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = Ready
