""" trigger/52100053_qd/3200_hidden_bookcase.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5002], visible=False) # PortalOn
        self.set_ladder(triggerIds=[520], visible=False, animationEffect=False, animationDelay=0) # Ladder
        self.set_ladder(triggerIds=[521], visible=False, animationEffect=False, animationDelay=0) # Ladder
        self.set_ladder(triggerIds=[522], visible=False, animationEffect=False, animationDelay=0) # Ladder
        self.set_ladder(triggerIds=[523], visible=False, animationEffect=False, animationDelay=0) # Ladder
        self.set_ladder(triggerIds=[524], visible=False, animationEffect=False, animationDelay=0) # Ladder
        self.set_mesh(triggerIds=[3200], visible=True, arg3=0, delay=0, scale=0) # Wall_BehindBookcase
        self.set_mesh(triggerIds=[3201], visible=True, arg3=0, delay=0, scale=0) # BehindBookcaseCover
        self.set_mesh(triggerIds=[3202], visible=True, arg3=0, delay=0, scale=0) # Bookcase
        self.set_mesh(triggerIds=[3203], visible=True, arg3=0, delay=0, scale=0) # BookcaseInvisible
        self.set_interact_object(triggerIds=[10002092], state=0) # Bookcase
        self.set_user_value(key='HiddenRouteOpen', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='HiddenRouteOpen', value=1):
            return Opened(self.ctx)
        if self.user_value(key='HiddenRouteOpen', value=2):
            return Closed(self.ctx)


class Opened(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[3202], visible=False, arg3=0, delay=0, scale=0) # Bookcase
        self.set_interact_object(triggerIds=[10002092], state=1) # Bookcase

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10002092], stateValue=0):
            return LadderOn(self.ctx)


class LadderOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5002], visible=True) # PortalOn
        self.set_mesh(triggerIds=[3203], visible=False, arg3=0, delay=0, scale=0) # BookcaseInvisible
        self.set_ladder(triggerIds=[520], visible=True, animationEffect=True, animationDelay=2) # Ladder
        self.set_ladder(triggerIds=[521], visible=True, animationEffect=True, animationDelay=2) # Ladder
        self.set_ladder(triggerIds=[522], visible=True, animationEffect=True, animationDelay=2) # Ladder
        self.set_ladder(triggerIds=[523], visible=True, animationEffect=True, animationDelay=2) # Ladder
        self.set_ladder(triggerIds=[524], visible=True, animationEffect=True, animationDelay=2) # Ladder
        self.set_mesh(triggerIds=[3200], visible=False, arg3=0, delay=0, scale=3) # Wall_BehindBookcase
        self.set_mesh(triggerIds=[3201], visible=False, arg3=0, delay=0, scale=3) # BehindBookcaseCover


class Closed(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[3202], visible=False, arg3=0, delay=0, scale=0) # Bookcase
        self.set_interact_object(triggerIds=[10002092], state=1) # Bookcase

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10002092], stateValue=0):
            return NothingHappened(self.ctx)


class NothingHappened(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[3202], visible=True, arg3=0, delay=0, scale=0) # Bookcase


initial_state = Wait
