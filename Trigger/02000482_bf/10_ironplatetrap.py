""" trigger/02000482_bf/10_ironplatetrap.xml """
import common


class Setting(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3410,3411,3412,3413], visible=True, arg3=0, delay=0, scale=0) # IronPlateHold
        self.set_effect(triggerIds=[5100], visible=False) # CubeSkillNotice
        self.set_effect(triggerIds=[5101], visible=False) # CubeSkillNotice
        self.set_effect(triggerIds=[5102], visible=False) # CubeSkillNotice
        self.set_effect(triggerIds=[5103], visible=False) # CubeSkillNotice
        self.destroy_monster(spawnIds=[201,301])
        self.set_interact_object(triggerIds=[10002027], state=0, arg4=False) # LeverForTrap
        self.set_user_value(key='TrapOn', value=0)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='TrapOn', value=1):
            return LeverOnDelay(self.ctx)


class LeverOnDelay(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return LeverOn(self.ctx)


class LeverOn(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10002027], state=1) # LeverForTrap
        self.set_effect(triggerIds=[5100], visible=True) # CubeSkillNotice
        self.set_effect(triggerIds=[5101], visible=True) # CubeSkillNotice
        self.set_effect(triggerIds=[5102], visible=True) # CubeSkillNotice
        self.set_effect(triggerIds=[5103], visible=True) # CubeSkillNotice

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10002027], stateValue=0):
            return TrapOn(self.ctx)


class TrapOn(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[201,301], animationEffect=False)
        self.set_mesh(triggerIds=[3410,3411,3412,3413], visible=False, arg3=500, delay=0, scale=2) # IronPlateHold
        self.set_effect(triggerIds=[5100], visible=False) # CubeSkillNotice
        self.set_effect(triggerIds=[5101], visible=False) # CubeSkillNotice
        self.set_effect(triggerIds=[5102], visible=False) # CubeSkillNotice
        self.set_effect(triggerIds=[5103], visible=False) # CubeSkillNotice

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Remove(self.ctx)


class Remove(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[201,301])


initial_state = Setting
