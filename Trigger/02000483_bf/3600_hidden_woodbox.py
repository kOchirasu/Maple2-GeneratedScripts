""" trigger/02000483_bf/3600_hidden_woodbox.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5003], visible=False) # PortalOn
        self.set_ladder(triggerIds=[530], visible=False, animationEffect=False, animationDelay=0) # Ladder
        self.set_ladder(triggerIds=[531], visible=False, animationEffect=False, animationDelay=0) # Ladder
        self.set_ladder(triggerIds=[532], visible=False, animationEffect=False, animationDelay=0) # Ladder
        self.set_ladder(triggerIds=[533], visible=False, animationEffect=False, animationDelay=0) # Ladder
        self.set_ladder(triggerIds=[534], visible=False, animationEffect=False, animationDelay=0) # Ladder
        self.set_ladder(triggerIds=[535], visible=False, animationEffect=False, animationDelay=0) # Ladder
        self.set_mesh(triggerIds=[3600], visible=True, arg3=0, delay=0, scale=0) # Wall_BehindWoodBox
        self.set_mesh(triggerIds=[3601], visible=True, arg3=0, delay=0, scale=0) # BehindWoodBoxCover
        self.set_mesh(triggerIds=[3602], visible=True, arg3=0, delay=0, scale=0) # WoodBox
        self.set_mesh(triggerIds=[3603], visible=True, arg3=0, delay=0, scale=0) # WoodBoxInvisible
        self.set_interact_object(triggerIds=[10002043], state=0) # WoodBox
        self.set_user_value(key='HiddenRouteOpen', value=0)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='HiddenRouteOpen', value=1):
            return Opened(self.ctx)
        if self.user_value(key='HiddenRouteOpen', value=2):
            return Closed(self.ctx)


class Opened(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3602], visible=False, arg3=100, delay=0, scale=2) # WoodBox
        self.set_interact_object(triggerIds=[10002043], state=1) # WoodBox

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10002043], stateValue=0):
            return LadderOn(self.ctx)


class LadderOn(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5003], visible=True) # PortalOn
        self.set_mesh(triggerIds=[3600], visible=False, arg3=0, delay=0, scale=3) # Wall_BehindWoodBox
        self.set_mesh(triggerIds=[3601], visible=False, arg3=0, delay=0, scale=3) # BehindWoodBoxCover
        self.set_mesh(triggerIds=[3603], visible=False, arg3=0, delay=0, scale=0) # WoodBoxInvisible
        self.set_ladder(triggerIds=[530], visible=True, animationEffect=True, animationDelay=2) # Ladder
        self.set_ladder(triggerIds=[531], visible=True, animationEffect=True, animationDelay=2) # Ladder
        self.set_ladder(triggerIds=[532], visible=True, animationEffect=True, animationDelay=2) # Ladder
        self.set_ladder(triggerIds=[533], visible=True, animationEffect=True, animationDelay=2) # Ladder
        self.set_ladder(triggerIds=[534], visible=True, animationEffect=True, animationDelay=2) # Ladder
        self.set_ladder(triggerIds=[535], visible=True, animationEffect=True, animationDelay=2) # Ladder


class Closed(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3602], visible=False, arg3=100, delay=0, scale=2) # WoodBox
        self.set_interact_object(triggerIds=[10002043], state=1) # WoodBox

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10002043], stateValue=0):
            return NothingHappened(self.ctx)


class NothingHappened(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3602], visible=True, arg3=0, delay=0, scale=0) # WoodBox


initial_state = Wait
