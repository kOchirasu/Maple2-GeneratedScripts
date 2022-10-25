""" trigger/02020025_bf/dungeonmission.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[901]):
            return 던전미션체크대기(self.ctx)


class 던전미션체크대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=904, spawnIds=[201]):
            return 체력90이하체크(self.ctx)


class 체력90이하체크(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.check_npc_hp(compare='lowerEqual', value=90, spawnId=201, isRelative=True):
            return 지하1층(self.ctx)


class 지하1층(common.Trigger):
    def on_enter(self):
        self.dungeon_mission_complete(missionId=24092001)

    def on_tick(self) -> common.Trigger:
        if self.check_npc_hp(compare='lowerEqual', value=70, spawnId=201, isRelative=True):
            return 지하2층(self.ctx)


class 지하2층(common.Trigger):
    def on_enter(self):
        self.dungeon_mission_complete(missionId=24092002)

    def on_tick(self) -> common.Trigger:
        if self.check_npc_hp(compare='lowerEqual', value=55, spawnId=201, isRelative=True):
            return 지하3층(self.ctx)


class 지하3층(common.Trigger):
    def on_enter(self):
        self.dungeon_mission_complete(missionId=24092003)

    def on_tick(self) -> common.Trigger:
        if self.check_npc_hp(compare='lowerEqual', value=40, spawnId=201, isRelative=True):
            return 지하4층(self.ctx)


class 지하4층(common.Trigger):
    def on_enter(self):
        self.dungeon_mission_complete(missionId=24092004)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
