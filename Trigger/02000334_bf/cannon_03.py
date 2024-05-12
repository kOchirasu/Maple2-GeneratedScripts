""" trigger/02000334_bf/cannon_03.xml """
import trigger_api


class Idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[98012], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='cannon_03', value=1):
            return 마킹비표시(self.ctx)


class 마킹비표시(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[98012], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=90013, spawnIds=[190]):
            # 돼지왕 타보를 감지
            return 마킹표시(self.ctx)


class 마킹표시(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[98012], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(boxId=90013, spawnIds=[190]):
            return 마킹비표시(self.ctx)


initial_state = Idle
