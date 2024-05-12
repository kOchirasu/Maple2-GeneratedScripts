""" trigger/02000312_bf/move_01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[3001], visible=True, arg3=0, delay=0, scale=0) # Invisible_Barrier
        self.set_mesh(triggerIds=[3100,3101,3102,3103], visible=True, arg3=0, delay=0, scale=0) # Move_OnWater
        self.set_mesh(triggerIds=[3200,3201,3202,3203], visible=False, arg3=0, delay=0, scale=0) # Move_onTop
        self.set_agent(triggerIds=[8000], visible=True)
        self.set_agent(triggerIds=[8001], visible=True)
        self.set_agent(triggerIds=[8002], visible=True)
        self.set_agent(triggerIds=[8003], visible=True)
        self.set_agent(triggerIds=[8004], visible=True)
        self.set_agent(triggerIds=[8005], visible=True)
        self.set_agent(triggerIds=[8006], visible=True)
        self.set_agent(triggerIds=[8007], visible=True)
        self.set_breakable(triggerIds=[4000], enable=False) # Move_GoUp
        self.set_breakable(triggerIds=[4001], enable=False) # Move_GoUp
        self.set_breakable(triggerIds=[4002], enable=False) # Move_GoUp
        self.set_breakable(triggerIds=[4003], enable=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4000], visible=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4001], visible=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4002], visible=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4003], visible=False) # Move_GoUp
        self.set_effect(triggerIds=[5003], visible=False) # LeverHear
        self.set_effect(triggerIds=[5002], visible=False) # Wheel
        self.set_interact_object(triggerIds=[10001034], state=2) # Lever
        self.set_user_value(key='BoardApp', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BoardApp', value=1):
            return BoardApp01(self.ctx)


class BoardApp01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[3001], visible=False, arg3=0, delay=0, scale=0) # Invisible_Barrier

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return BoardApp02(self.ctx)


class BoardApp02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5000], visible=True) # UI
        self.show_guide_summary(entityId=20031204, textId=20031204) # 레버를 당겨 이동 장치 작동시키기
        self.set_effect(triggerIds=[5003], visible=True) # LeverHear
        self.set_interact_object(triggerIds=[10001034], state=1) # Lever

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001034], stateValue=0):
            return BoardGoUp01(self.ctx)


class BoardGoUp01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entityId=20031204)
        self.set_effect(triggerIds=[5002], visible=True) # Wheel
        self.set_mesh(triggerIds=[3100,3101,3102,3103], visible=False, arg3=100, delay=0, scale=2) # Move_OnWater
        self.set_interact_object(triggerIds=[10001034], state=2) # Lever
        self.set_breakable(triggerIds=[4000], enable=True) # Move_GoUp
        self.set_breakable(triggerIds=[4001], enable=True) # Move_GoUp
        self.set_breakable(triggerIds=[4002], enable=True) # Move_GoUp
        self.set_breakable(triggerIds=[4003], enable=True) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4000], visible=True) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4001], visible=True) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4002], visible=True) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4003], visible=True) # Move_GoUp

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return BoardGoUp02(self.ctx)


class BoardGoUp02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(triggerIds=[8000], visible=False)
        self.set_agent(triggerIds=[8001], visible=False)
        self.set_agent(triggerIds=[8002], visible=False)
        self.set_agent(triggerIds=[8003], visible=False)
        self.set_agent(triggerIds=[8004], visible=False)
        self.set_agent(triggerIds=[8005], visible=False)
        self.set_agent(triggerIds=[8006], visible=False)
        self.set_agent(triggerIds=[8007], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return BoardDisApp01(self.ctx)


class BoardDisApp01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[3200,3201,3202,3203], visible=True, arg3=100, delay=0, scale=2) # Move_onTop

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=200):
            return BoardDisApp02(self.ctx)


class BoardDisApp02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_breakable(triggerIds=[4000], enable=False) # Move_GoUp
        self.set_breakable(triggerIds=[4001], enable=False) # Move_GoUp
        self.set_breakable(triggerIds=[4002], enable=False) # Move_GoUp
        self.set_breakable(triggerIds=[4003], enable=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4000], visible=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4001], visible=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4002], visible=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4003], visible=False) # Move_GoUp

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return BoardReset01(self.ctx)


class BoardReset01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[3100,3101,3102,3103], visible=True, arg3=0, delay=0, scale=0) # Move_OnWater

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return BoardReset02(self.ctx)


class BoardReset02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10001034], state=1) # Lever

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001034], stateValue=0):
            return BoardReset03(self.ctx)


class BoardReset03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[3200,3201,3202,3203], visible=False, arg3=100, delay=0, scale=2) # Move_onTop

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return BoardGoUp01(self.ctx)


initial_state = Wait
