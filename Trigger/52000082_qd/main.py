""" trigger/52000082_qd/main.xml """
import common


class mapskill(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[701]):
            return mapskill_start(self.ctx)


class mapskill_start(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[701], skillId=70000114, level=1, isPlayer=False, isSkillSet=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return mapskill(self.ctx)


initial_state = mapskill
