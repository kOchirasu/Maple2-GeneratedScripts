""" trigger/02000311_bf/ai.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=9999993, key='Buff_01', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Phase_02', value=1):
            return Phase_02(self.ctx)


class Phase_02(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_2001')
        self.move_npc(spawnId=202, patrolName='MS2PatrolData_2002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return Phase_02_b(self.ctx)


class Phase_02_b(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=201, script='$02000311_BF__AI__0$', arg4=2, arg5=2)
        self.set_conversation(type=1, spawnId=202, script='$02000311_BF__AI__1$', arg4=2, arg5=0)
        self.set_skill(triggerIds=[6001,6002,6003,6004,6005,6006,6007,6008,6009,6010], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Phase_02_c(self.ctx)


class Phase_02_c(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20003111, textId=20003111, duration=5000)
        self.set_effect(triggerIds=[7001], visible=True)
        self.set_effect(triggerIds=[7002], visible=True)
        self.set_user_value(triggerId=9999994, key='Buff_01', value=1)
        self.set_user_value(triggerId=9999995, key='Buff_02', value=1)


initial_state = idle
