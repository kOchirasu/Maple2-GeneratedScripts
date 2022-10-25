""" trigger/99999840/pc_move.xml """
import common


class 대기(common.Trigger):
    pass


class 애디셔널체크(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.dungeon_variable(varId=3, value=1):
            return 종료(self.ctx)
        if self.check_any_user_additional_effect(boxId=9001, additionalEffectId=70002541, level=1):
            return 유저이동확률(self.ctx)


class 유저이동확률(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.dungeon_variable(varId=3, value=1):
            return 종료(self.ctx)
        if self.random_condition(rate=33):
            return 유저이동1(self.ctx)
        if self.random_condition(rate=34):
            return 유저이동2(self.ctx)
        if self.random_condition(rate=33):
            return 유저이동3(self.ctx)


class 유저이동1(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=99999841, portalId=2, boxId=9202)

    def on_tick(self) -> common.Trigger:
        if self.dungeon_variable(varId=3, value=1):
            return 종료(self.ctx)
        if self.true():
            return 대기(self.ctx)


class 유저이동2(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=99999841, portalId=3, boxId=9202)

    def on_tick(self) -> common.Trigger:
        if self.dungeon_variable(varId=3, value=1):
            return 종료(self.ctx)
        if self.true():
            return 대기(self.ctx)


class 유저이동3(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=99999841, portalId=4, boxId=9202)

    def on_tick(self) -> common.Trigger:
        if self.dungeon_variable(varId=3, value=1):
            return 종료(self.ctx)
        if self.true():
            return 대기(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
