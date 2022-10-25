""" trigger/02100001_bf/99_barricade.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='CageDoorOpen', value=0)
        self.set_user_value(key='MissionStart', value=0)
        self.set_user_value(key='MissionComplete', value=0)
        self.set_actor(triggerId=4000, visible=True, initialSequence='Closed') # Cage
        self.set_mesh(triggerIds=[3100], visible=True, arg3=0, delay=0, scale=0) # Cage Door
        self.set_mesh(triggerIds=[3101,3102,3103], visible=True, arg3=0, delay=0, scale=0) # Cage Mesh
        self.set_effect(triggerIds=[5001], visible=False) # MetalDoorOpen 사운드 이펙트
        self.set_effect(triggerIds=[5002], visible=False) # MetalDoorClose 사운드 이펙트

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='CageDoorOpen', value=1):
            return CageDoorOpenDelay(self.ctx)


class CageDoorOpenDelay(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return CageDoorOpen(self.ctx)


class CageDoorOpen(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5001], visible=True) # MetalDoorOpen 사운드 이펙트
        self.set_actor(triggerId=4000, visible=True, initialSequence='Open') # Cage
        self.set_mesh(triggerIds=[3100], visible=False, arg3=300, delay=0, scale=0) # Cage Door

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='MissionStart', value=1):
            return CountDown(self.ctx)


class CountDown(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_event_ui(type=1, arg2='$02100001_BF__99_BARRICADE__0$', arg3='3000')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=30000):
            return ShutDown(self.ctx)


class ShutDown(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5002], visible=True) # MetalDoorClose 사운드 이펙트
        self.set_user_value(triggerId=5, key='GiveBuffSlowly', value=1)
        self.set_actor(triggerId=4000, visible=True, initialSequence='Closed') # Cage
        self.set_mesh(triggerIds=[3100], visible=True, arg3=0, delay=0, scale=0) # Cage Door

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='MissionComplete', value=1):
            return Release(self.ctx)


class Release(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5001], visible=True) # MetalDoorOpen 사운드 이펙트
        self.set_actor(triggerId=4000, visible=True, initialSequence='Open') # Cage
        self.set_mesh(triggerIds=[3100], visible=False, arg3=300, delay=0, scale=0) # Cage Door

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Quit(self.ctx)


class Quit(common.Trigger):
    pass


initial_state = Wait
