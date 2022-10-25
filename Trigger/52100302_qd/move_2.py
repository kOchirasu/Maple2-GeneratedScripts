""" trigger/52100302_qd/move_2.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Archeon2', value=1):
            self.set_user_value(triggerId=900008, key='Archeon2', value=0)
            return Archeon_Ready(self.ctx)


class Archeon_Ready(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.check_any_user_additional_effect(boxId=10001, additionalEffectId=73000006, level=1):
            self.move_user_to_pos(pos=[8700,-4800,2750], rot=[0,0,0])
            return Archeon_On(self.ctx)


class Archeon_On(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 대기(self.ctx)


initial_state = 대기
