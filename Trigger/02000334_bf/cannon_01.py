""" trigger/02000334_bf/cannon_01.xml """
import trigger_api


class Idle(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[98010], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='cannon_01', value=1):
            return 마킹비표시(self.ctx)


class 마킹비표시(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[98010], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=90011, spawnIds=[190]):
            return 마킹표시(self.ctx)


class 마킹표시(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[98010], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(boxId=90011, spawnIds=[190]):
            return 마킹비표시(self.ctx)


initial_state = Idle
