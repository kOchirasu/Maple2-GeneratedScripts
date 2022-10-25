""" trigger/52100022_qd/04_breakwall.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[7000], enable=False) # CubeBreak
        self.set_user_value(key='BossKill', value=0)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9100]):
            return BreakWall(self.ctx)
        if self.user_value(key='BossKill', value=1):
            return BreakWall(self.ctx)


class BreakWall(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[7000], enable=True) # CubeBreak


initial_state = Wait
