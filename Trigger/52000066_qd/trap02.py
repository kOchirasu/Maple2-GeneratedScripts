""" trigger/52000066_qd/trap02.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001071], state=0) # TrapLever
        self.set_mesh(triggerIds=[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029], visible=True, arg3=0, delay=0, scale=3) # TrapMesh
        self.set_effect(triggerIds=[5000], visible=False) # DownArrow
        self.set_user_value(key='TrapLeverOn', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TrapLeverOn', value=1):
            return TrapLeverOn01(self.ctx)


class TrapLeverOn01(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001071], state=1) # TrapLever
        self.set_effect(triggerIds=[5000], visible=True) # DownArrow

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001071], stateValue=0):
            return TrapFalse01(self.ctx)
        if self.user_value(key='TrapLeverOn', value=2):
            return Quit(self.ctx)


class TrapFalse01(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=False) # DownArrow
        self.set_interact_object(triggerIds=[10001071], state=0) # TrapLever
        self.set_actor(triggerId=4000, visible=True, initialSequence='Closed') # TrapLever
        self.set_mesh(triggerIds=[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029], visible=True, arg3=500, delay=50, scale=1) # TrapMesh

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9300]):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=False) # DownArrow
        self.set_interact_object(triggerIds=[10001071], state=0) # TrapLever


initial_state = Wait
