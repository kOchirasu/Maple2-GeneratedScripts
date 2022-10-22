""" trigger/63000029_cs/earthquake02.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5910], visible=False) # RumbleSound
        set_effect(triggerIds=[5810], visible=False) # SandFlowdown
        set_effect(triggerIds=[5811], visible=False) # SandFlowdown
        set_effect(triggerIds=[5812], visible=False) # SandFlowdown
        set_effect(triggerIds=[5813], visible=False) # SandFlowdown
        set_effect(triggerIds=[5814], visible=False) # SandFlowdown
        set_effect(triggerIds=[5815], visible=False) # SandFlowdown
        set_effect(triggerIds=[5816], visible=False) # SandFlowdown
        set_effect(triggerIds=[5817], visible=False) # SandFlowdown
        set_effect(triggerIds=[5818], visible=False) # SandFlowdown
        set_effect(triggerIds=[5802], visible=False) # EarthquakeVibrateLong
        set_mesh(triggerIds=[3600,3601,3602,3603,3604,3605,3606,3607,3608,3609,3610,3611,3612,3613,3614,3615], visible=False, arg3=0, arg4=0, arg5=0) # EarthquakeDebris
        set_user_value(key='EarthquakeStart', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='EarthquakeStart', value=1):
            return Delay01()


class Delay01(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3600,3601,3602,3603,3604,3605,3606,3607,3608,3609,3610,3611,3612,3613,3614,3615], visible=True, arg3=0, arg4=0, arg5=0) # EarthquakeDebris

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return Collapse00()


class Collapse00(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5910], visible=True) # RumbleSound
        set_effect(triggerIds=[5802], visible=True) # EarthquakeVibrateLong
        set_effect(triggerIds=[5810], visible=True) # SandFlowdown
        set_mesh(triggerIds=[3600], visible=False, arg3=0, arg4=0, arg5=0) # EarthquakeDebris
        set_mesh(triggerIds=[3601], visible=False, arg3=100, arg4=0, arg5=0) # EarthquakeDebris
        set_mesh(triggerIds=[3602], visible=False, arg3=250, arg4=0, arg5=0) # EarthquakeDebris
        set_mesh(triggerIds=[3603], visible=False, arg3=300, arg4=0, arg5=0) # EarthquakeDebris

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Collapse01()


class Collapse01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5817], visible=True) # SandFlowdown
        set_effect(triggerIds=[5818], visible=True) # SandFlowdown
        set_mesh(triggerIds=[3604], visible=False, arg3=0, arg4=0, arg5=0) # EarthquakeDebris
        set_mesh(triggerIds=[3605], visible=False, arg3=150, arg4=0, arg5=0) # EarthquakeDebris

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return Collapse02()


class Collapse02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5814], visible=True) # SandFlowdown
        set_mesh(triggerIds=[3606], visible=False, arg3=0, arg4=0, arg5=0) # EarthquakeDebris
        set_mesh(triggerIds=[3607], visible=False, arg3=100, arg4=0, arg5=0) # EarthquakeDebris

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Collapse03()


class Collapse03(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5816], visible=True) # SandFlowdown
        set_effect(triggerIds=[5810], visible=True) # SandFlowdown
        set_mesh(triggerIds=[3608], visible=False, arg3=0, arg4=0, arg5=0) # EarthquakeDebris
        set_mesh(triggerIds=[3609], visible=False, arg3=100, arg4=0, arg5=0) # EarthquakeDebris
        set_mesh(triggerIds=[3600], visible=True, arg3=0, arg4=0, arg5=0) # EarthquakeDebris
        set_mesh(triggerIds=[3601], visible=True, arg3=0, arg4=0, arg5=0) # EarthquakeDebris
        set_mesh(triggerIds=[3602], visible=True, arg3=0, arg4=0, arg5=0) # EarthquakeDebris
        set_mesh(triggerIds=[3603], visible=True, arg3=0, arg4=0, arg5=0) # EarthquakeDebris

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return Collapse04()


class Collapse04(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5910], visible=True) # RumbleSound
        set_effect(triggerIds=[5811], visible=True) # SandFlowdown
        set_mesh(triggerIds=[3600], visible=False, arg3=0, arg4=0, arg5=0) # EarthquakeDebris
        set_mesh(triggerIds=[3601], visible=False, arg3=100, arg4=0, arg5=0) # EarthquakeDebris
        set_mesh(triggerIds=[3602], visible=False, arg3=250, arg4=0, arg5=0) # EarthquakeDebris
        set_mesh(triggerIds=[3603], visible=False, arg3=300, arg4=0, arg5=0) # EarthquakeDebris

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return Collapse05()


class Collapse05(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3610], visible=False, arg3=0, arg4=0, arg5=0) # EarthquakeDebris
        set_mesh(triggerIds=[3611], visible=False, arg3=500, arg4=0, arg5=0) # EarthquakeDebris
        set_effect(triggerIds=[5815], visible=True) # SandFlowdown

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return Collapse06()


class Collapse06(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5818], visible=True) # SandFlowdown
        set_effect(triggerIds=[5812], visible=True) # SandFlowdown
        set_mesh(triggerIds=[3612], visible=False, arg3=500, arg4=0, arg5=0) # EarthquakeDebris

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Collapse07()


class Collapse07(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5910], visible=True) # RumbleSound
        set_effect(triggerIds=[5813], visible=True) # SandFlowdown
        set_mesh(triggerIds=[3613], visible=False, arg3=0, arg4=0, arg5=0) # EarthquakeDebris
        set_mesh(triggerIds=[3614], visible=False, arg3=300, arg4=0, arg5=0) # EarthquakeDebris
        set_mesh(triggerIds=[3615], visible=False, arg3=700, arg4=0, arg5=0) # EarthquakeDebris

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Collapse08()


class Collapse08(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9900]):
            return Delay01()
        if not user_detected(boxIds=[9900]):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5802], visible=False) # EarthquakeVibrateLong
        set_effect(triggerIds=[5810], visible=False) # SandFlowdown
        set_effect(triggerIds=[5811], visible=False) # SandFlowdown
        set_effect(triggerIds=[5812], visible=False) # SandFlowdown
        set_effect(triggerIds=[5813], visible=False) # SandFlowdown
        set_effect(triggerIds=[5814], visible=False) # SandFlowdown
        set_effect(triggerIds=[5815], visible=False) # SandFlowdown
        set_effect(triggerIds=[5816], visible=False) # SandFlowdown
        set_effect(triggerIds=[5817], visible=False) # SandFlowdown


