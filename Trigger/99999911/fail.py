""" trigger/99999911/fail.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=99999911, portalId=1, boxId=702)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=702, boxId=1):
            return fail_random(self.ctx)


class fail_random(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=1):
            return fail_01(self.ctx)
        if self.random_condition(rate=1):
            return fail_02(self.ctx)
        if self.random_condition(rate=1):
            return fail_03(self.ctx)
        if self.random_condition(rate=1):
            return fail_04(self.ctx)
        if self.random_condition(rate=5):
            return fail_04(self.ctx)


class fail_01(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=99999911, portalId=1, boxId=702)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return idle(self.ctx)


class fail_02(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=99999911, portalId=2, boxId=702)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return idle(self.ctx)


class fail_03(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=99999911, portalId=3, boxId=702)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return idle(self.ctx)


class fail_04(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=99999911, portalId=4, boxId=702)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return idle(self.ctx)


class fail_05(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=99999911, portalId=5, boxId=702)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return idle(self.ctx)


initial_state = idle
