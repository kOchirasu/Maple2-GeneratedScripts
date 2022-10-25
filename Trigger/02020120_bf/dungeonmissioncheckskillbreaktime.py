""" trigger/02020120_bf/dungeonmissioncheckskillbreaktime.xml """
import common


class 시작대기중(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[199]):
            return 보스스킬브레이크시작_대기중(self.ctx)


class 보스스킬브레이크시작_대기중(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.check_npc_additional_effect(spawnId=99, additionalEffectId=50004546, level=1):
            return 던전미션_체크(self.ctx)


class 던전미션_체크(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.all_of():
            return 던전미션_스킬브레이크저지_성공(self.ctx)
        if self.check_npc_additional_effect(spawnId=99, additionalEffectId=50000367, level=1):
            return 던전미션_스킬브레이크저지_실패(self.ctx)


class 던전미션_스킬브레이크저지_성공(common.Trigger):
    def on_enter(self):
        self.dungeon_mission_complete(missionId=23037004) # DungeonMission.xml 에 등록된 숫자 코드 미션 완료 처리하기

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 종료(self.ctx)


class 던전미션_스킬브레이크저지_실패(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if not self.check_npc_additional_effect(spawnId=99, additionalEffectId=50004546, level=1):
            return 시작대기중(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 시작대기중
