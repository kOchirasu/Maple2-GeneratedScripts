""" trigger/63000029_cs/earthquake02.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5910], visible=False) # RumbleSound
        self.set_effect(trigger_ids=[5810], visible=False) # SandFlowdown
        self.set_effect(trigger_ids=[5811], visible=False) # SandFlowdown
        self.set_effect(trigger_ids=[5812], visible=False) # SandFlowdown
        self.set_effect(trigger_ids=[5813], visible=False) # SandFlowdown
        self.set_effect(trigger_ids=[5814], visible=False) # SandFlowdown
        self.set_effect(trigger_ids=[5815], visible=False) # SandFlowdown
        self.set_effect(trigger_ids=[5816], visible=False) # SandFlowdown
        self.set_effect(trigger_ids=[5817], visible=False) # SandFlowdown
        self.set_effect(trigger_ids=[5818], visible=False) # SandFlowdown
        self.set_effect(trigger_ids=[5802], visible=False) # EarthquakeVibrateLong
        self.set_mesh(trigger_ids=[3600,3601,3602,3603,3604,3605,3606,3607,3608,3609,3610,3611,3612,3613,3614,3615], visible=False, start_delay=0, interval=0, fade=0) # EarthquakeDebris
        self.set_user_value(key='EarthquakeStart', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='EarthquakeStart', value=1):
            return Delay01(self.ctx)


class Delay01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3600,3601,3602,3603,3604,3605,3606,3607,3608,3609,3610,3611,3612,3613,3614,3615], visible=True, start_delay=0, interval=0, fade=0) # EarthquakeDebris

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return Collapse00(self.ctx)


class Collapse00(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5910], visible=True) # RumbleSound
        self.set_effect(trigger_ids=[5802], visible=True) # EarthquakeVibrateLong
        self.set_effect(trigger_ids=[5810], visible=True) # SandFlowdown
        self.set_mesh(trigger_ids=[3600], visible=False, start_delay=0, interval=0, fade=0) # EarthquakeDebris
        self.set_mesh(trigger_ids=[3601], visible=False, start_delay=100, interval=0, fade=0) # EarthquakeDebris
        self.set_mesh(trigger_ids=[3602], visible=False, start_delay=250, interval=0, fade=0) # EarthquakeDebris
        self.set_mesh(trigger_ids=[3603], visible=False, start_delay=300, interval=0, fade=0) # EarthquakeDebris

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Collapse01(self.ctx)


class Collapse01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5817], visible=True) # SandFlowdown
        self.set_effect(trigger_ids=[5818], visible=True) # SandFlowdown
        self.set_mesh(trigger_ids=[3604], visible=False, start_delay=0, interval=0, fade=0) # EarthquakeDebris
        self.set_mesh(trigger_ids=[3605], visible=False, start_delay=150, interval=0, fade=0) # EarthquakeDebris

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return Collapse02(self.ctx)


class Collapse02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5814], visible=True) # SandFlowdown
        self.set_mesh(trigger_ids=[3606], visible=False, start_delay=0, interval=0, fade=0) # EarthquakeDebris
        self.set_mesh(trigger_ids=[3607], visible=False, start_delay=100, interval=0, fade=0) # EarthquakeDebris

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Collapse03(self.ctx)


class Collapse03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5816], visible=True) # SandFlowdown
        self.set_effect(trigger_ids=[5810], visible=True) # SandFlowdown
        self.set_mesh(trigger_ids=[3608], visible=False, start_delay=0, interval=0, fade=0) # EarthquakeDebris
        self.set_mesh(trigger_ids=[3609], visible=False, start_delay=100, interval=0, fade=0) # EarthquakeDebris
        self.set_mesh(trigger_ids=[3600], visible=True, start_delay=0, interval=0, fade=0) # EarthquakeDebris
        self.set_mesh(trigger_ids=[3601], visible=True, start_delay=0, interval=0, fade=0) # EarthquakeDebris
        self.set_mesh(trigger_ids=[3602], visible=True, start_delay=0, interval=0, fade=0) # EarthquakeDebris
        self.set_mesh(trigger_ids=[3603], visible=True, start_delay=0, interval=0, fade=0) # EarthquakeDebris

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return Collapse04(self.ctx)


class Collapse04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5910], visible=True) # RumbleSound
        self.set_effect(trigger_ids=[5811], visible=True) # SandFlowdown
        self.set_mesh(trigger_ids=[3600], visible=False, start_delay=0, interval=0, fade=0) # EarthquakeDebris
        self.set_mesh(trigger_ids=[3601], visible=False, start_delay=100, interval=0, fade=0) # EarthquakeDebris
        self.set_mesh(trigger_ids=[3602], visible=False, start_delay=250, interval=0, fade=0) # EarthquakeDebris
        self.set_mesh(trigger_ids=[3603], visible=False, start_delay=300, interval=0, fade=0) # EarthquakeDebris

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return Collapse05(self.ctx)


class Collapse05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3610], visible=False, start_delay=0, interval=0, fade=0) # EarthquakeDebris
        self.set_mesh(trigger_ids=[3611], visible=False, start_delay=500, interval=0, fade=0) # EarthquakeDebris
        self.set_effect(trigger_ids=[5815], visible=True) # SandFlowdown

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return Collapse06(self.ctx)


class Collapse06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5818], visible=True) # SandFlowdown
        self.set_effect(trigger_ids=[5812], visible=True) # SandFlowdown
        self.set_mesh(trigger_ids=[3612], visible=False, start_delay=500, interval=0, fade=0) # EarthquakeDebris

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Collapse07(self.ctx)


class Collapse07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5910], visible=True) # RumbleSound
        self.set_effect(trigger_ids=[5813], visible=True) # SandFlowdown
        self.set_mesh(trigger_ids=[3613], visible=False, start_delay=0, interval=0, fade=0) # EarthquakeDebris
        self.set_mesh(trigger_ids=[3614], visible=False, start_delay=300, interval=0, fade=0) # EarthquakeDebris
        self.set_mesh(trigger_ids=[3615], visible=False, start_delay=700, interval=0, fade=0) # EarthquakeDebris

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Collapse08(self.ctx)


class Collapse08(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9900]):
            return Delay01(self.ctx)
        if not self.user_detected(box_ids=[9900]):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5802], visible=False) # EarthquakeVibrateLong
        self.set_effect(trigger_ids=[5810], visible=False) # SandFlowdown
        self.set_effect(trigger_ids=[5811], visible=False) # SandFlowdown
        self.set_effect(trigger_ids=[5812], visible=False) # SandFlowdown
        self.set_effect(trigger_ids=[5813], visible=False) # SandFlowdown
        self.set_effect(trigger_ids=[5814], visible=False) # SandFlowdown
        self.set_effect(trigger_ids=[5815], visible=False) # SandFlowdown
        self.set_effect(trigger_ids=[5816], visible=False) # SandFlowdown
        self.set_effect(trigger_ids=[5817], visible=False) # SandFlowdown


initial_state = Wait
