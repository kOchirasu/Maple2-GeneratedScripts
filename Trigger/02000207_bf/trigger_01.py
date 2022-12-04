""" trigger/02000207_bf/trigger_01.xml """
import trigger_api


class 이동(trigger_api.Trigger):
    def on_enter(self):
        self.set_breakable(triggerIds=[7001,7002,7003,7004,7005,7006,7007,7008,7009,7010,7011,7012,7013,7014,7015,7016,7017,7018,7019,7020,7021,7022,7023,7024,7025,7026,7027,7028,7029,7030,7031,7032,7033,7034,7035,7036,7037,7038,7039], enable=False)
        self.set_interact_object(triggerIds=[10000063], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000063], stateValue=0):
            self.set_breakable(triggerIds=[7001,7002,7003,7004,7005,7006,7007,7008,7009,7010,7011,7012,7013,7014,7015,7016,7017,7018,7019,7020,7021,7022,7023,7024,7025,7026,7027,7028,7029,7030,7031,7032,7033,7034,7035,7036,7037,7038,7039], enable=True)
            return 이동(self.ctx)


initial_state = 이동
