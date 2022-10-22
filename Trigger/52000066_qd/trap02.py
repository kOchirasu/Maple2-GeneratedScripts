""" trigger/52000066_qd/trap02.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001071], state=0) # TrapLever
        set_mesh(triggerIds=[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029], visible=True, arg3=0, arg4=0, arg5=3) # TrapMesh
        set_effect(triggerIds=[5000], visible=False) # DownArrow
        set_user_value(key='TrapLeverOn', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='TrapLeverOn', value=1):
            return TrapLeverOn01()


class TrapLeverOn01(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001071], state=1) # TrapLever
        set_effect(triggerIds=[5000], visible=True) # DownArrow

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001071], arg2=0):
            return TrapFalse01()
        if user_value(key='TrapLeverOn', value=2):
            return Quit()


class TrapFalse01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=False) # DownArrow
        set_interact_object(triggerIds=[10001071], state=0) # TrapLever
        set_actor(triggerId=4000, visible=True, initialSequence='Closed') # TrapLever
        set_mesh(triggerIds=[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029], visible=True, arg3=500, arg4=50, arg5=1) # TrapMesh

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9300]):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=False) # DownArrow
        set_interact_object(triggerIds=[10001071], state=0) # TrapLever


