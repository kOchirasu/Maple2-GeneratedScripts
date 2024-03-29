""" trigger/52100052_qd/12_ironplatetrap.xml """
import trigger_api


class Setting(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3430,3431,3432,3433], visible=True, arg3=0, delay=0, scale=0) # IronPlateHold
        self.set_effect(triggerIds=[5300], visible=False) # CubeSkillNotice
        self.set_effect(triggerIds=[5301], visible=False) # CubeSkillNotice
        self.set_effect(triggerIds=[5302], visible=False) # CubeSkillNotice
        self.set_effect(triggerIds=[5303], visible=False) # CubeSkillNotice
        self.destroy_monster(spawnIds=[203,303])
        self.set_interact_object(triggerIds=[10002082], state=0, arg4=False) # LeverForTrap
        self.set_user_value(key='TrapOn', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TrapOn', value=1):
            return LeverOnDelay(self.ctx)


class LeverOnDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return LeverOn(self.ctx)


class LeverOn(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10002082], state=1) # LeverForTrap
        self.set_effect(triggerIds=[5300], visible=True) # CubeSkillNotice
        self.set_effect(triggerIds=[5301], visible=True) # CubeSkillNotice
        self.set_effect(triggerIds=[5302], visible=True) # CubeSkillNotice
        self.set_effect(triggerIds=[5303], visible=True) # CubeSkillNotice

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10002082], stateValue=0):
            return TrapOn(self.ctx)


class TrapOn(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[203,303], animationEffect=False)
        self.set_mesh(triggerIds=[3430,3431,3432,3433], visible=False, arg3=500, delay=0, scale=2) # IronPlateHold
        self.set_effect(triggerIds=[5300], visible=False) # CubeSkillNotice
        self.set_effect(triggerIds=[5301], visible=False) # CubeSkillNotice
        self.set_effect(triggerIds=[5302], visible=False) # CubeSkillNotice
        self.set_effect(triggerIds=[5303], visible=False) # CubeSkillNotice

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Remove(self.ctx)


class Remove(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[203,303])


initial_state = Setting
