""" trigger/02000375_bf/move.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_visible_breakable_object(triggerIds=[7000,7001,7002,7003,7004,7005,7006,7007,7008,7009,7010,7011,7012,7013,7014,7015,7016,7017,7018,7019,7020,7021,7022,7023], visible=True)
        self.set_breakable(triggerIds=[7000,7001,7002,7003,7004,7005,7006,7007,7008,7009,7010,7011,7012,7013,7014,7015,7016,7017,7018,7019,7020,7021,7022,7023], enable=False)
        self.set_interact_object(triggerIds=[10001024], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001024], stateValue=0):
            return 이동(self.ctx)


class 이동(trigger_api.Trigger):
    def on_enter(self):
        self.set_breakable(triggerIds=[7000,7001,7002,7003,7004,7005,7006,7007,7008,7009,7010,7011,7012,7013,7014,7015,7016,7017,7018,7019,7020,7021,7022,7023], enable=True)
        self.set_event_ui(type=1, arg2='$02000375_BF__move__0$', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=60000):
            return 레버삭제(self.ctx)


class 레버삭제(trigger_api.Trigger):
    def on_enter(self):
        self.set_visible_breakable_object(triggerIds=[7000,7001,7002,7003,7004,7005,7006,7007,7008,7009,7010,7011,7012,7013,7014,7015,7016,7017,7018,7019,7020,7021,7022,7023], visible=False)
        self.set_breakable(triggerIds=[7000,7001,7002,7003,7004,7005,7006,7007,7008,7009,7010,7011,7012,7013,7014,7015,7016,7017,7018,7019,7020,7021,7022,7023], enable=False)
        self.set_interact_object(triggerIds=[10001024], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BattleEnd', value=1):
            return 대기(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
