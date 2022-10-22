""" trigger/52000052_qd/1306_route_06roundleft.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_portal(portalId=13, visible=False, enabled=False, minimapVisible=False)
        set_mesh(triggerIds=[4013], visible=True, arg3=0, arg4=0, arg5=0) # PortalBarrier
        set_agent(triggerIds=[18061], visible=True)
        set_agent(triggerIds=[18062], visible=True)
        set_effect(triggerIds=[5006], visible=False) # 06Round_BridgeApp
        set_mesh(triggerIds=[130600,130601,130602,130603,130604,130605,130606,130607,130608,130609,130610,130611,130612,130613,130614,130615,130616,130617,130618,130619,130620,130621,130622,130623,130624,130625], visible=False, arg3=0, arg4=0, arg5=0) # Fake
        set_mesh(triggerIds=[330600,330601,330602,330603,330604,330605,330606,330607,330608,330609,330610,330611,330612,330613,330614,330615,330616,330617,330618,330619,330620,330621,330622,330623,330624,330625], visible=False, arg3=0, arg4=0, arg5=0) # Real
        set_user_value(key='RouteSelected', value=0)
        set_user_value(key='MakeTrue', value=0)
        set_user_value(key='MakeFalse', value=0)

    def on_tick(self) -> state.State:
        if count_users(boxId=9000, boxId=1):
            return StartDazzling01()


class StartDazzling01(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='RouteSelected', value=1):
            return StartDazzlingRandom01()


#  가짜 길이 깜빡이는 연출 
class StartDazzlingRandom01(state.State):
    def on_enter(self):
        set_random_mesh(triggerIds=[130600,130601,130602,130603,130604,130605,130606,130607,130608,130609,130610,130611,130612,130613,130614,130615,130616,130617,130618,130619,130620,130621,130622,130623,130624,130625], visible=True, meshCount=7, arg4=100, delay=500) # Fake

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return StartDazzlingRandom02()
        if user_value(key='MakeTrue', value=1):
            return MakeTrue()
        if user_value(key='MakeFalse', value=1):
            return MakeFalse()

    def on_exit(self):
        set_random_mesh(triggerIds=[130600,130601,130602,130603,130604,130605,130606,130607,130608,130609,130610,130611,130612,130613,130614,130615,130616,130617,130618,130619,130620,130621,130622,130623,130624,130625], visible=False, meshCount=26, arg4=0, delay=0) # Fake


class StartDazzlingRandom02(state.State):
    def on_enter(self):
        set_random_mesh(triggerIds=[130600,130601,130602,130603,130604,130605,130606,130607,130608,130609,130610,130611,130612,130613,130614,130615,130616,130617,130618,130619,130620,130621,130622,130623,130624,130625], visible=True, meshCount=7, arg4=100, delay=500) # Fake

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return StartDazzlingRandom01()
        if user_value(key='MakeTrue', value=1):
            return MakeTrue()
        if user_value(key='MakeFalse', value=1):
            return MakeFalse()

    def on_exit(self):
        set_random_mesh(triggerIds=[130600,130601,130602,130603,130604,130605,130606,130607,130608,130609,130610,130611,130612,130613,130614,130615,130616,130617,130618,130619,130620,130621,130622,130623,130624,130625], visible=False, meshCount=26, arg4=0, delay=0) # Fake


class MakeTrue(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5006], visible=True) # 06Round_BridgeApp
        set_mesh(triggerIds=[130600,130601,130602,130603,130604,130605,130606,130607,130608,130609,130610,130611,130612,130613,130614,130615,130616,130617,130618,130619,130620,130621,130622,130623,130624,130625], visible=False, arg3=0, arg4=0, arg5=5) # Fake
        set_random_mesh(triggerIds=[330600,330601,330602,330603,330604,330605,330606,330607,330608,330609,330610,330611,330612,330613,330614,330615,330616,330617,330618,330619,330620,330621,330622,330623,330624,330625], visible=True, meshCount=26, arg4=100, delay=50) # Real
        set_agent(triggerIds=[18061], visible=False)
        set_agent(triggerIds=[18062], visible=False)
        set_portal(portalId=13, visible=True, enabled=True, minimapVisible=False)
        set_mesh(triggerIds=[4013], visible=False, arg3=0, arg4=0, arg5=0) # PortalBarrier

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Quit()


class MakeFalse(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[130600,130601,130602,130603,130604,130605,130606,130607,130608,130609,130610,130611,130612,130613,130614,130615,130616,130617,130618,130619,130620,130621,130622,130623,130624,130625], visible=False, arg3=0, arg4=0, arg5=5) # Fake

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Quit()


class Quit(state.State):
    pass


