""" trigger/99999925/laddercomplete.xml """
import trigger_api


class IsLadderComplete(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(trigger_ids=[311], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[312], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[313], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[314], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[315], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[316], visible=False, enable=False, fade=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ladderComp', value=1):
            return ladderComplete(self.ctx)


class ladderComplete(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(trigger_ids=[311], visible=True, enable=True, fade=0)
        self.set_ladder(trigger_ids=[312], visible=True, enable=True, fade=0)
        self.set_ladder(trigger_ids=[313], visible=True, enable=True, fade=0)
        self.set_ladder(trigger_ids=[314], visible=True, enable=True, fade=0)
        self.set_ladder(trigger_ids=[315], visible=True, enable=True, fade=0)
        self.set_ladder(trigger_ids=[316], visible=True, enable=True, fade=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return End(self.ctx)


class End(trigger_api.Trigger):
    pass


initial_state = IsLadderComplete
