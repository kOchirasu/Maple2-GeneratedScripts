""" trigger/02000334_bf/cannon_03.xml """
import common


class Idle(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[98012], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='cannon_03', value=1):
            return 마킹비표시(self.ctx)


class 마킹비표시(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[98012], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=90013, spawnIds=[190]):
            return 마킹표시(self.ctx)


class 마킹표시(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[98012], visible=True)

    def on_tick(self) -> common.Trigger:
        if not self.npc_detected(boxId=90013, spawnIds=[190]):
            return 마킹비표시(self.ctx)


initial_state = Idle
