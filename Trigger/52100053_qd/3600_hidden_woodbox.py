""" trigger/52100053_qd/3600_hidden_woodbox.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5003], visible=False) # PortalOn
        self.set_ladder(trigger_ids=[530], visible=False, enable=False, fade=0) # Ladder
        self.set_ladder(trigger_ids=[531], visible=False, enable=False, fade=0) # Ladder
        self.set_ladder(trigger_ids=[532], visible=False, enable=False, fade=0) # Ladder
        self.set_ladder(trigger_ids=[533], visible=False, enable=False, fade=0) # Ladder
        self.set_ladder(trigger_ids=[534], visible=False, enable=False, fade=0) # Ladder
        self.set_ladder(trigger_ids=[535], visible=False, enable=False, fade=0) # Ladder
        self.set_mesh(trigger_ids=[3600], visible=True, start_delay=0, interval=0, fade=0) # Wall_BehindWoodBox
        self.set_mesh(trigger_ids=[3601], visible=True, start_delay=0, interval=0, fade=0) # BehindWoodBoxCover
        self.set_mesh(trigger_ids=[3602], visible=True, start_delay=0, interval=0, fade=0) # WoodBox
        self.set_mesh(trigger_ids=[3603], visible=True, start_delay=0, interval=0, fade=0) # WoodBoxInvisible
        self.set_interact_object(trigger_ids=[10002096], state=0) # WoodBox
        self.set_user_value(key='HiddenRouteOpen', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='HiddenRouteOpen', value=1):
            return Opened(self.ctx)
        if self.user_value(key='HiddenRouteOpen', value=2):
            return Closed(self.ctx)


class Opened(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3602], visible=False, start_delay=100, interval=0, fade=2) # WoodBox
        self.set_interact_object(trigger_ids=[10002096], state=1) # WoodBox

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10002096], state=0):
            return LadderOn(self.ctx)


class LadderOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5003], visible=True) # PortalOn
        self.set_mesh(trigger_ids=[3600], visible=False, start_delay=0, interval=0, fade=3) # Wall_BehindWoodBox
        self.set_mesh(trigger_ids=[3601], visible=False, start_delay=0, interval=0, fade=3) # BehindWoodBoxCover
        self.set_mesh(trigger_ids=[3603], visible=False, start_delay=0, interval=0, fade=0) # WoodBoxInvisible
        self.set_ladder(trigger_ids=[530], visible=True, enable=True, fade=2) # Ladder
        self.set_ladder(trigger_ids=[531], visible=True, enable=True, fade=2) # Ladder
        self.set_ladder(trigger_ids=[532], visible=True, enable=True, fade=2) # Ladder
        self.set_ladder(trigger_ids=[533], visible=True, enable=True, fade=2) # Ladder
        self.set_ladder(trigger_ids=[534], visible=True, enable=True, fade=2) # Ladder
        self.set_ladder(trigger_ids=[535], visible=True, enable=True, fade=2) # Ladder


class Closed(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3602], visible=False, start_delay=100, interval=0, fade=2) # WoodBox
        self.set_interact_object(trigger_ids=[10002096], state=1) # WoodBox

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10002096], state=0):
            return NothingHappened(self.ctx)


class NothingHappened(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3602], visible=True, start_delay=0, interval=0, fade=0) # WoodBox


initial_state = Wait
