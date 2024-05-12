""" trigger/02000482_bf/10_ironplatetrap.xml """
import trigger_api


class Setting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3410,3411,3412,3413], visible=True, start_delay=0, interval=0, fade=0) # IronPlateHold
        self.set_effect(trigger_ids=[5100], visible=False) # CubeSkillNotice
        self.set_effect(trigger_ids=[5101], visible=False) # CubeSkillNotice
        self.set_effect(trigger_ids=[5102], visible=False) # CubeSkillNotice
        self.set_effect(trigger_ids=[5103], visible=False) # CubeSkillNotice
        self.destroy_monster(spawn_ids=[201,301])
        self.set_interact_object(trigger_ids=[10002027], state=0, arg4=False) # LeverForTrap
        self.set_user_value(key='TrapOn', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TrapOn') >= 1:
            return LeverOnDelay(self.ctx)


class LeverOnDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return LeverOn(self.ctx)


class LeverOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10002027], state=1) # LeverForTrap
        self.set_effect(trigger_ids=[5100], visible=True) # CubeSkillNotice
        self.set_effect(trigger_ids=[5101], visible=True) # CubeSkillNotice
        self.set_effect(trigger_ids=[5102], visible=True) # CubeSkillNotice
        self.set_effect(trigger_ids=[5103], visible=True) # CubeSkillNotice

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10002027], state=0):
            return TrapOn(self.ctx)


class TrapOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[201,301], auto_target=False)
        self.set_mesh(trigger_ids=[3410,3411,3412,3413], visible=False, start_delay=500, interval=0, fade=2) # IronPlateHold
        self.set_effect(trigger_ids=[5100], visible=False) # CubeSkillNotice
        self.set_effect(trigger_ids=[5101], visible=False) # CubeSkillNotice
        self.set_effect(trigger_ids=[5102], visible=False) # CubeSkillNotice
        self.set_effect(trigger_ids=[5103], visible=False) # CubeSkillNotice

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Remove(self.ctx)


class Remove(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[201,301])


initial_state = Setting
