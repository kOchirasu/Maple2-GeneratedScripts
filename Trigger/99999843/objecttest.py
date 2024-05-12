""" trigger/99999843/objecttest.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[12000401], state=1)
        self.set_interact_object(triggerIds=[12000400], state=2)
        self.set_interact_object(triggerIds=[12000402], state=2)
        self.set_interact_object(triggerIds=[12000403], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[12000401], stateValue=0):
            return PC_MOVE_01(self.ctx)


# <state name="PC_01" >
# <onEnter>
# </onEnter>
# <condition name="WaitTick" waitTick="2000" >
# <transition state="PC_02"/>
# </condition>
# </state>
class PC_MOVE_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            self.patrol_condition_user(patrolName='MS2PatrolData0', patrolIndex=1, additionalEffectId=73000006)
            # self.patrol_condition_user(patrolName='MS2PatrolData2', patrolIndex=2, additionalEffectId=73000007)
            return PC_MOVE_02_Delay(self.ctx)


class PC_MOVE_02_Delay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return PC_MOVE_02(self.ctx)


class PC_MOVE_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(boxIds=[901], skillId=73000009, level=1, isPlayer=False, isSkillSet=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return PC_MOVE_02_Delay(self.ctx)


class RESET_DELAY(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 대기(self.ctx)


initial_state = 대기
