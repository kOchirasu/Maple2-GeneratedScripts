""" trigger/63000038_cs/move.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_breakable(triggerIds=[7000,7001,7002,7003,7004,7005,7006,7007,7008,7009,7010,7011,7012,7013,7014,7015,7016,7017,7018,7019,7020,7021,7022,7023], enable=False)
        self.set_interact_object(triggerIds=[10001024], state=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Setlever', value=1):
            return 레버반응대기(self.ctx)


class 레버반응대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entityId=26300382, textId=26300382)
        self.set_interact_object(triggerIds=[10001024], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001024], stateValue=0):
            self.hide_guide_summary(entityId=26300382)
            return 이동(self.ctx)


class 이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_breakable(triggerIds=[7000,7001,7002,7003,7004,7005,7006,7007,7008,7009,7010,7011,7012,7013,7014,7015,7016,7017,7018,7019,7020,7021,7022,7023], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
