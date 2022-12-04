""" trigger/99999925/laddercomplete.xml """
import trigger_api


class IsLadderComplete(trigger_api.Trigger):
    def on_enter(self):
        self.set_ladder(triggerIds=[311], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[312], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[313], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[314], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[315], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[316], visible=False, animationEffect=False, animationDelay=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ladderComp', value=1):
            return ladderComplete(self.ctx)


class ladderComplete(trigger_api.Trigger):
    def on_enter(self):
        self.set_ladder(triggerIds=[311], visible=True, animationEffect=True, animationDelay=0)
        self.set_ladder(triggerIds=[312], visible=True, animationEffect=True, animationDelay=0)
        self.set_ladder(triggerIds=[313], visible=True, animationEffect=True, animationDelay=0)
        self.set_ladder(triggerIds=[314], visible=True, animationEffect=True, animationDelay=0)
        self.set_ladder(triggerIds=[315], visible=True, animationEffect=True, animationDelay=0)
        self.set_ladder(triggerIds=[316], visible=True, animationEffect=True, animationDelay=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return End(self.ctx)


class End(trigger_api.Trigger):
    pass


initial_state = IsLadderComplete
