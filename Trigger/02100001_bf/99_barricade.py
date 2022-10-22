""" trigger/02100001_bf/99_barricade.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_user_value(key='CageDoorOpen', value=0)
        set_user_value(key='MissionStart', value=0)
        set_user_value(key='MissionComplete', value=0)
        set_actor(triggerId=4000, visible=True, initialSequence='Closed') # Cage
        set_mesh(triggerIds=[3100], visible=True, arg3=0, arg4=0, arg5=0) # Cage Door
        set_mesh(triggerIds=[3101,3102,3103], visible=True, arg3=0, arg4=0, arg5=0) # Cage Mesh
        set_effect(triggerIds=[5001], visible=False) # MetalDoorOpen 사운드 이펙트
        set_effect(triggerIds=[5002], visible=False) # MetalDoorClose 사운드 이펙트

    def on_tick(self) -> state.State:
        if user_value(key='CageDoorOpen', value=1):
            return CageDoorOpenDelay()


class CageDoorOpenDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CageDoorOpen()


class CageDoorOpen(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=True) # MetalDoorOpen 사운드 이펙트
        set_actor(triggerId=4000, visible=True, initialSequence='Open') # Cage
        set_mesh(triggerIds=[3100], visible=False, arg3=300, arg4=0, arg5=0) # Cage Door

    def on_tick(self) -> state.State:
        if user_value(key='MissionStart', value=1):
            return CountDown()


class CountDown(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_event_ui(type=1, arg2='$02100001_BF__99_BARRICADE__0$', arg3='3000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=30000):
            return ShutDown()


class ShutDown(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5002], visible=True) # MetalDoorClose 사운드 이펙트
        set_user_value(triggerId=5, key='GiveBuffSlowly', value=1)
        set_actor(triggerId=4000, visible=True, initialSequence='Closed') # Cage
        set_mesh(triggerIds=[3100], visible=True, arg3=0, arg4=0, arg5=0) # Cage Door

    def on_tick(self) -> state.State:
        if user_value(key='MissionComplete', value=1):
            return Release()


class Release(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=True) # MetalDoorOpen 사운드 이펙트
        set_actor(triggerId=4000, visible=True, initialSequence='Open') # Cage
        set_mesh(triggerIds=[3100], visible=False, arg3=300, arg4=0, arg5=0) # Cage Door

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Quit()


class Quit(state.State):
    pass


