""" trigger/99999840/badmob2.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=99990004, key='BadMob', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(varId=912, value=1):
            return 몬스터스폰(self.ctx)


class 몬스터스폰(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[992], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[991,992,993]):
            return 신호쏴주기(self.ctx)


class 신호쏴주기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=99990004, key='BadMob', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(varId=912, value=0):
            return 대기(self.ctx)


initial_state = 대기
