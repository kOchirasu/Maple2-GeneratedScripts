""" trigger/99999841/pc_move.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    pass


class 애디셔널체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(varId=2, value=1):
            return 종료(self.ctx)
        if self.check_any_user_additional_effect(boxId=9001, additionalEffectId=70002541, level=1):
            return 유저이동확률(self.ctx)


class 유저이동확률(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(varId=2, value=1):
            return 종료(self.ctx)
        if self.random_condition(rate=33):
            return 유저이동1(self.ctx)
        if self.random_condition(rate=34):
            return 유저이동2(self.ctx)
        if self.random_condition(rate=33):
            return 유저이동3(self.ctx)


class 유저이동1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(mapId=99999840, portalId=2, boxId=9102)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(varId=2, value=1):
            return 종료(self.ctx)
        if self.true():
            return 대기(self.ctx)


class 유저이동2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(mapId=99999840, portalId=3, boxId=9102)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(varId=2, value=1):
            return 종료(self.ctx)
        if self.true():
            return 대기(self.ctx)


class 유저이동3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(mapId=99999840, portalId=4, boxId=9102)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(varId=2, value=1):
            return 종료(self.ctx)
        if self.true():
            return 대기(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
