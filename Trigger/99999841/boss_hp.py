""" trigger/99999841/boss_hp.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.dungeon_variable(varId=200, value=1):
            return 시작(self.ctx)


class 시작(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.check_npc_hp(compare='lowerEqual', value=70, spawnId=911, isRelative=True):
            return 프로70(self.ctx)


class 프로70(common.Trigger):
    def on_enter(self):
        self.dungeon_variable(varId=210, value=1)

    def on_tick(self) -> common.Trigger:
        if self.check_npc_hp(compare='lowerEqual', value=50, spawnId=911, isRelative=True):
            return 프로50(self.ctx)


class 프로50(common.Trigger):
    def on_enter(self):
        self.dungeon_variable(varId=220, value=1)

    def on_tick(self) -> common.Trigger:
        if self.check_npc_hp(compare='lowerEqual', value=30, spawnId=911, isRelative=True):
            return 프로30(self.ctx)


class 프로30(common.Trigger):
    def on_enter(self):
        self.dungeon_variable(varId=230, value=1)

    def on_tick(self) -> common.Trigger:
        if self.check_npc_hp(compare='lowerEqual', value=10, spawnId=911, isRelative=True):
            return 프로10(self.ctx)


class 프로10(common.Trigger):
    def on_enter(self):
        self.dungeon_variable(varId=240, value=1)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
