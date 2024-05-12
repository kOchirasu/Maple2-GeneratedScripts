""" trigger/02000482_bf/11_ironplatetrap.xml """
import trigger_api


class Setting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3420,3421,3422,3423], visible=True, start_delay=0, interval=0, fade=0) # IronPlateHold
        self.set_effect(trigger_ids=[5200], visible=False) # CubeSkillNotice
        self.set_effect(trigger_ids=[5201], visible=False) # CubeSkillNotice
        self.set_effect(trigger_ids=[5202], visible=False) # CubeSkillNotice
        self.set_effect(trigger_ids=[5203], visible=False) # CubeSkillNotice
        self.destroy_monster(spawn_ids=[202,302])
        self.set_interact_object(trigger_ids=[10002028], state=0, arg4=False) # LeverForTrap
        self.set_user_value(key='TrapOn', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TrapOn', value=1):
            return LeverOnDelay(self.ctx)


class LeverOnDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return LeverOn(self.ctx)


class LeverOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10002028], state=1) # LeverForTrap
        self.set_effect(trigger_ids=[5200], visible=True) # CubeSkillNotice
        self.set_effect(trigger_ids=[5201], visible=True) # CubeSkillNotice
        self.set_effect(trigger_ids=[5202], visible=True) # CubeSkillNotice
        self.set_effect(trigger_ids=[5203], visible=True) # CubeSkillNotice

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10002028], state=0):
            return TrapOn(self.ctx)


class TrapOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[202,302], auto_target=False)
        self.set_mesh(trigger_ids=[3420,3421,3422,3423], visible=False, start_delay=500, interval=0, fade=2) # IronPlateHold
        self.set_effect(trigger_ids=[5200], visible=False) # CubeSkillNotice
        self.set_effect(trigger_ids=[5201], visible=False) # CubeSkillNotice
        self.set_effect(trigger_ids=[5202], visible=False) # CubeSkillNotice
        self.set_effect(trigger_ids=[5203], visible=False) # CubeSkillNotice

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Remove(self.ctx)


class Remove(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[202,302])


initial_state = Setting
