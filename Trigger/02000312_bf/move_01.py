""" trigger/02000312_bf/move_01.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3001], visible=True, arg3=0, arg4=0, arg5=0) # Invisible_Barrier
        set_mesh(triggerIds=[3100,3101,3102,3103], visible=True, arg3=0, arg4=0, arg5=0) # Move_OnWater
        set_mesh(triggerIds=[3200,3201,3202,3203], visible=False, arg3=0, arg4=0, arg5=0) # Move_onTop
        set_agent(triggerIds=[8000], visible=True)
        set_agent(triggerIds=[8001], visible=True)
        set_agent(triggerIds=[8002], visible=True)
        set_agent(triggerIds=[8003], visible=True)
        set_agent(triggerIds=[8004], visible=True)
        set_agent(triggerIds=[8005], visible=True)
        set_agent(triggerIds=[8006], visible=True)
        set_agent(triggerIds=[8007], visible=True)
        set_breakable(triggerIds=[4000], enabled=False) # Move_GoUp
        set_breakable(triggerIds=[4001], enabled=False) # Move_GoUp
        set_breakable(triggerIds=[4002], enabled=False) # Move_GoUp
        set_breakable(triggerIds=[4003], enabled=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4000], arg2=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4001], arg2=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4002], arg2=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4003], arg2=False) # Move_GoUp
        set_effect(triggerIds=[5003], visible=False) # LeverHear
        set_effect(triggerIds=[5002], visible=False) # Wheel
        set_interact_object(triggerIds=[10001034], state=2) # Lever
        set_user_value(key='BoardApp', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='BoardApp', value=1):
            return BoardApp01()


class BoardApp01(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3001], visible=False, arg3=0, arg4=0, arg5=0) # Invisible_Barrier

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return BoardApp02()


class BoardApp02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # UI
        show_guide_summary(entityId=20031204, textId=20031204) # 레버를 당겨 이동 장치 작동시키기
        set_effect(triggerIds=[5003], visible=True) # LeverHear
        set_interact_object(triggerIds=[10001034], state=1) # Lever

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001034], arg2=0):
            return BoardGoUp01()


class BoardGoUp01(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=20031204)
        set_effect(triggerIds=[5002], visible=True) # Wheel
        set_mesh(triggerIds=[3100,3101,3102,3103], visible=False, arg3=100, arg4=0, arg5=2) # Move_OnWater
        set_interact_object(triggerIds=[10001034], state=2) # Lever
        set_breakable(triggerIds=[4000], enabled=True) # Move_GoUp
        set_breakable(triggerIds=[4001], enabled=True) # Move_GoUp
        set_breakable(triggerIds=[4002], enabled=True) # Move_GoUp
        set_breakable(triggerIds=[4003], enabled=True) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4000], arg2=True) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4001], arg2=True) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4002], arg2=True) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4003], arg2=True) # Move_GoUp

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return BoardGoUp02()


class BoardGoUp02(state.State):
    def on_enter(self):
        set_agent(triggerIds=[8000], visible=False)
        set_agent(triggerIds=[8001], visible=False)
        set_agent(triggerIds=[8002], visible=False)
        set_agent(triggerIds=[8003], visible=False)
        set_agent(triggerIds=[8004], visible=False)
        set_agent(triggerIds=[8005], visible=False)
        set_agent(triggerIds=[8006], visible=False)
        set_agent(triggerIds=[8007], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return BoardDisApp01()


class BoardDisApp01(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3200,3201,3202,3203], visible=True, arg3=100, arg4=0, arg5=2) # Move_onTop

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return BoardDisApp02()


class BoardDisApp02(state.State):
    def on_enter(self):
        set_breakable(triggerIds=[4000], enabled=False) # Move_GoUp
        set_breakable(triggerIds=[4001], enabled=False) # Move_GoUp
        set_breakable(triggerIds=[4002], enabled=False) # Move_GoUp
        set_breakable(triggerIds=[4003], enabled=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4000], arg2=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4001], arg2=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4002], arg2=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4003], arg2=False) # Move_GoUp

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return BoardReset01()


class BoardReset01(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3100,3101,3102,3103], visible=True, arg3=0, arg4=0, arg5=0) # Move_OnWater

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return BoardReset02()


class BoardReset02(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001034], state=1) # Lever

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001034], arg2=0):
            return BoardReset03()


class BoardReset03(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3200,3201,3202,3203], visible=False, arg3=100, arg4=0, arg5=2) # Move_onTop

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return BoardGoUp01()


