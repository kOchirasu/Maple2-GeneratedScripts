""" trigger/52100053_qd/3100_hidden_fireplace.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5001], visible=False) # PortalOn
        self.set_actor(triggerId=4000, visible=True, initialSequence='he_in_prop_fireplace_A01_Closed') # FireplaceActor
        self.set_ladder(triggerIds=[510], visible=False, animationEffect=False, animationDelay=0) # Ladder
        self.set_ladder(triggerIds=[511], visible=False, animationEffect=False, animationDelay=0) # Ladder
        self.set_ladder(triggerIds=[512], visible=False, animationEffect=False, animationDelay=0) # Ladder
        self.set_ladder(triggerIds=[513], visible=False, animationEffect=False, animationDelay=0) # Ladder
        self.set_ladder(triggerIds=[514], visible=False, animationEffect=False, animationDelay=0) # Ladder
        self.set_ladder(triggerIds=[515], visible=False, animationEffect=False, animationDelay=0) # Ladder
        self.set_mesh(triggerIds=[3100], visible=True, arg3=0, delay=0, scale=0) # Wall_BehindFirePlace
        self.set_mesh(triggerIds=[3101], visible=True, arg3=0, delay=0, scale=0) # BehindFirePlaceCover
        self.set_mesh(triggerIds=[3102], visible=True, arg3=0, delay=0, scale=0) # FireplaceInvisible
        self.set_interact_object(triggerIds=[10002091], state=0) # Fireplace
        self.set_user_value(key='HiddenRouteOpen', value=0)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='HiddenRouteOpen', value=1):
            return Opened(self.ctx)
        if self.user_value(key='HiddenRouteOpen', value=2):
            return Closed(self.ctx)


class Opened(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=4000, visible=False, initialSequence='he_in_prop_fireplace_A01_Closed') # FireplaceActor
        self.set_interact_object(triggerIds=[10002091], state=1) # Fireplace

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10002091], stateValue=0):
            return LadderOn(self.ctx)


class LadderOn(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5001], visible=True) # PortalOn
        self.set_mesh(triggerIds=[3102], visible=False, arg3=0, delay=0, scale=0) # FireplaceInvisible
        self.set_ladder(triggerIds=[510], visible=True, animationEffect=True, animationDelay=2) # Ladder
        self.set_ladder(triggerIds=[511], visible=True, animationEffect=True, animationDelay=2) # Ladder
        self.set_ladder(triggerIds=[512], visible=True, animationEffect=True, animationDelay=2) # Ladder
        self.set_ladder(triggerIds=[513], visible=True, animationEffect=True, animationDelay=2) # Ladder
        self.set_ladder(triggerIds=[514], visible=True, animationEffect=True, animationDelay=2) # Ladder
        self.set_ladder(triggerIds=[515], visible=True, animationEffect=True, animationDelay=2) # Ladder
        self.set_mesh(triggerIds=[3100], visible=False, arg3=0, delay=0, scale=3) # Wall_BehindFirePlace
        self.set_mesh(triggerIds=[3101], visible=False, arg3=0, delay=0, scale=3) # BehindFirePlaceCover


class Closed(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=4000, visible=False, initialSequence='he_in_prop_fireplace_A01_Closed') # FireplaceActor
        self.set_interact_object(triggerIds=[10002091], state=1) # Fireplace

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10002091], stateValue=0):
            return NothingHappened(self.ctx)


class NothingHappened(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=4000, visible=True, initialSequence='he_in_prop_fireplace_A01_Opened') # FireplaceActor


initial_state = Wait
