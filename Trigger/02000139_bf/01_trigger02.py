""" trigger/02000139_bf/01_trigger02.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[701,702,703,704,705,706,707,708,709,710,711,712], visible=False)
        self.set_interact_object(triggerIds=[10000160], state=1)
        self.set_ladder(triggerIds=[601], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[602], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[603], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[604], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[605], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[606], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[607], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[608], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[609], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[610], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[611], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[612], visible=False, animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000160], stateValue=0):
            return 사다리등장(self.ctx)


class 사다리등장(trigger_api.Trigger):
    def on_enter(self):
        self.set_ladder(triggerIds=[601], visible=True, animationEffect=True)
        self.set_effect(triggerIds=[701], visible=True)
        self.set_ladder(triggerIds=[602], visible=True, animationEffect=True)
        self.set_effect(triggerIds=[702], visible=True)
        self.set_ladder(triggerIds=[603], visible=True, animationEffect=True)
        self.set_effect(triggerIds=[703], visible=True)
        self.set_ladder(triggerIds=[604], visible=True, animationEffect=True)
        self.set_effect(triggerIds=[704], visible=True)
        self.set_ladder(triggerIds=[605], visible=True, animationEffect=True)
        self.set_effect(triggerIds=[705], visible=True)
        self.set_ladder(triggerIds=[606], visible=True, animationEffect=True)
        self.set_effect(triggerIds=[706], visible=True)
        self.set_ladder(triggerIds=[607], visible=True, animationEffect=True)
        self.set_effect(triggerIds=[707], visible=True)
        self.set_ladder(triggerIds=[608], visible=True, animationEffect=True)
        self.set_effect(triggerIds=[708], visible=True)
        self.set_ladder(triggerIds=[609], visible=True, animationEffect=True)
        self.set_effect(triggerIds=[709], visible=True)
        self.set_ladder(triggerIds=[610], visible=True, animationEffect=True)
        self.set_effect(triggerIds=[710], visible=True)
        self.set_ladder(triggerIds=[611], visible=True, animationEffect=True)
        self.set_effect(triggerIds=[711], visible=True)
        self.set_ladder(triggerIds=[612], visible=True, animationEffect=True)
        self.set_effect(triggerIds=[713], visible=True)
        self.set_timer(timerId='4', seconds=18)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='4'):
            return 대기(self.ctx)


initial_state = 대기
