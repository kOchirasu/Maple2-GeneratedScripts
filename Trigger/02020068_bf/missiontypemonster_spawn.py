""" trigger/02020068_bf/missiontypemonster_spawn.xml """
import common


class 루프1(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            self.start_combine_spawn(groupId=[521], isStart=True)
            return 루프2(self.ctx)


class 루프2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=150000):
            return 루프3(self.ctx)


class 루프3(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=150000):
            return 루프2(self.ctx)


initial_state = 루프1
