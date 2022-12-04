""" trigger/99999843/objecttest.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000401], state=1)
        self.set_interact_object(triggerIds=[12000400], state=2)
        self.set_interact_object(triggerIds=[12000402], state=2)
        self.set_interact_object(triggerIds=[12000403], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.all_of():
            return PC_MOVE_01(self.ctx)


class PC_MOVE_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            self.patrol_condition_user(patrolName='MS2PatrolData0', patrolIndex=1, additionalEffectId=73000006)
            return PC_MOVE_02_Delay(self.ctx)


class PC_MOVE_02_Delay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return PC_MOVE_02(self.ctx)


class PC_MOVE_02(trigger_api.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[901], skillId=73000009, level=1, isPlayer=False, isSkillSet=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return PC_MOVE_02_Delay(self.ctx)


class RESET_DELAY(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 대기(self.ctx)


initial_state = 대기
