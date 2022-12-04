""" trigger/02000396_bf/11_ironplatetrap.xml """
import trigger_api


class Setting(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3420,3421,3422,3423], visible=True, arg3=0, delay=0, scale=0) # IronPlateHold
        self.set_effect(triggerIds=[5200], visible=False) # CubeSkillNotice
        self.set_effect(triggerIds=[5201], visible=False) # CubeSkillNotice
        self.set_effect(triggerIds=[5202], visible=False) # CubeSkillNotice
        self.set_effect(triggerIds=[5203], visible=False) # CubeSkillNotice
        self.destroy_monster(spawnIds=[202,302])
        self.set_interact_object(triggerIds=[10001130], state=0, arg4=False) # LeverForTrap
        self.set_user_value(key='TrapOn', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TrapOn', value=1):
            return LeverOnDelay(self.ctx)


class LeverOnDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return LeverOn(self.ctx)


class LeverOn(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001130], state=1) # LeverForTrap
        self.set_effect(triggerIds=[5200], visible=True) # CubeSkillNotice
        self.set_effect(triggerIds=[5201], visible=True) # CubeSkillNotice
        self.set_effect(triggerIds=[5202], visible=True) # CubeSkillNotice
        self.set_effect(triggerIds=[5203], visible=True) # CubeSkillNotice

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001130], stateValue=0):
            return TrapOn(self.ctx)


class TrapOn(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[202,302], animationEffect=False)
        self.set_mesh(triggerIds=[3420,3421,3422,3423], visible=False, arg3=500, delay=0, scale=2) # IronPlateHold
        self.set_effect(triggerIds=[5200], visible=False) # CubeSkillNotice
        self.set_effect(triggerIds=[5201], visible=False) # CubeSkillNotice
        self.set_effect(triggerIds=[5202], visible=False) # CubeSkillNotice
        self.set_effect(triggerIds=[5203], visible=False) # CubeSkillNotice

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Remove(self.ctx)


class Remove(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[202,302])


initial_state = Setting
