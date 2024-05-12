""" trigger/02000483_bf/3700_hidden_wardrope.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5004], visible=False) # PortalOn
        self.set_ladder(triggerIds=[540], visible=False, animationEffect=False, animationDelay=0) # Ladder
        self.set_ladder(triggerIds=[541], visible=False, animationEffect=False, animationDelay=0) # Ladder
        self.set_ladder(triggerIds=[542], visible=False, animationEffect=False, animationDelay=0) # Ladder
        self.set_ladder(triggerIds=[543], visible=False, animationEffect=False, animationDelay=0) # Ladder
        self.set_ladder(triggerIds=[544], visible=False, animationEffect=False, animationDelay=0) # Ladder
        self.set_ladder(triggerIds=[545], visible=False, animationEffect=False, animationDelay=0) # Ladder
        self.set_mesh(triggerIds=[3700], visible=True, arg3=0, delay=0, scale=0) # Wall_BehindWardrope
        self.set_mesh(triggerIds=[3701,3704], visible=True, arg3=0, delay=0, scale=0) # BehindWardropeCover01
        self.set_mesh(triggerIds=[3702], visible=True, arg3=0, delay=0, scale=0) # Wardrope
        self.set_mesh(triggerIds=[3703], visible=True, arg3=0, delay=0, scale=0) # WardropeInvisible
        self.set_interact_object(triggerIds=[10002044], state=0) # Wardrope
        self.set_user_value(key='HiddenRouteOpen', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='HiddenRouteOpen', value=1):
            return Opened(self.ctx)
        if self.user_value(key='HiddenRouteOpen', value=2):
            return Closed(self.ctx)


class Opened(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[3702], visible=False, arg3=100, delay=0, scale=2) # Wardrope
        self.set_interact_object(triggerIds=[10002044], state=1) # Wardrope

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10002044], stateValue=0):
            return LadderOn(self.ctx)


class LadderOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5004], visible=True) # PortalOn
        self.set_mesh(triggerIds=[3700], visible=False, arg3=0, delay=0, scale=3) # Wall_BehindWardrope
        self.set_mesh(triggerIds=[3701,3704], visible=False, arg3=0, delay=0, scale=3) # BehindWardropeCover
        self.set_mesh(triggerIds=[3703], visible=False, arg3=0, delay=0, scale=0) # WardropeInvisible
        self.set_ladder(triggerIds=[540], visible=True, animationEffect=True, animationDelay=2) # Ladder
        self.set_ladder(triggerIds=[541], visible=True, animationEffect=True, animationDelay=2) # Ladder
        self.set_ladder(triggerIds=[542], visible=True, animationEffect=True, animationDelay=2) # Ladder
        self.set_ladder(triggerIds=[543], visible=True, animationEffect=True, animationDelay=2) # Ladder
        self.set_ladder(triggerIds=[544], visible=True, animationEffect=True, animationDelay=2) # Ladder
        self.set_ladder(triggerIds=[545], visible=True, animationEffect=True, animationDelay=2) # Ladder


class Closed(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[3702], visible=False, arg3=100, delay=0, scale=2) # Wardrope
        self.set_interact_object(triggerIds=[10002044], state=1) # Wardrope

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10002044], stateValue=0):
            return NothingHappened(self.ctx)


class NothingHappened(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[3702], visible=True, arg3=0, delay=0, scale=0) # Wardrope


initial_state = Wait
