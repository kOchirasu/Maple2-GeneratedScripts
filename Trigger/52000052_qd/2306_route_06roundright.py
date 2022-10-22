""" trigger/52000052_qd/2306_route_06roundright.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_portal(portalId=14, visible=False, enabled=False, minimapVisible=False)
        set_mesh(triggerIds=[4014], visible=True, arg3=0, arg4=0, arg5=0) # PortalBarrier
        set_agent(triggerIds=[28061], visible=True)
        set_agent(triggerIds=[28062], visible=True)
        set_mesh(triggerIds=[230600,230601,230602,230603,230604,230605,230606,230607,230608,230609,230610,230611,230612,230613,230614,230615,230616,230617,230618,230619], visible=False, arg3=0, arg4=0, arg5=0) # Fake
        set_mesh(triggerIds=[430600,430601,430602,430603,430604,430605,430606,430607,430608,430609,430610,430611,430612,430613,430614,430615,430616,430617,430618,430619], visible=False, arg3=0, arg4=0, arg5=0) # Real
        set_user_value(key='RouteSelected', value=0)
        set_user_value(key='MakeTrue', value=0)
        set_user_value(key='MakeFalse', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='RouteSelected', value=1):
            return StartDazzlingRandom01()


#  가짜 길이 깜빡이는 연출 
class StartDazzlingRandom01(state.State):
    def on_enter(self):
        set_random_mesh(triggerIds=[230600,230601,230602,230603,230604,230605,230606,230607,230608,230609,230610,230611,230612,230613,230614,230615,230616,230617,230618,230619], visible=True, meshCount=6, arg4=100, delay=500) # Fake

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return StartDazzlingRandom02()
        if user_value(key='MakeTrue', value=1):
            return MakeTrue()
        if user_value(key='MakeFalse', value=1):
            return MakeFalse()

    def on_exit(self):
        set_random_mesh(triggerIds=[230600,230601,230602,230603,230604,230605,230606,230607,230608,230609,230610,230611,230612,230613,230614,230615,230616,230617,230618,230619], visible=False, meshCount=20, arg4=0, delay=0) # Fake


class StartDazzlingRandom02(state.State):
    def on_enter(self):
        set_random_mesh(triggerIds=[230600,230601,230602,230603,230604,230605,230606,230607,230608,230609,230610,230611,230612,230613,230614,230615,230616,230617,230618,230619], visible=True, meshCount=6, arg4=100, delay=500) # Fake

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return StartDazzlingRandom01()
        if user_value(key='MakeTrue', value=1):
            return MakeTrue()
        if user_value(key='MakeFalse', value=1):
            return MakeFalse()

    def on_exit(self):
        set_random_mesh(triggerIds=[230600,230601,230602,230603,230604,230605,230606,230607,230608,230609,230610,230611,230612,230613,230614,230615,230616,230617,230618,230619], visible=False, meshCount=20, arg4=0, delay=0) # Fake


class MakeTrue(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5006], visible=True) # 06Round_BridgeApp
        set_mesh(triggerIds=[230600,230601,230602,230603,230604,230605,230606,230607,230608,230609,230610,230611,230612,230613,230614,230615,230616,230617,230618,230619], visible=False, arg3=0, arg4=0, arg5=5) # Fake
        set_random_mesh(triggerIds=[430600,430601,430602,430603,430604,430605,430606,430607,430608,430609,430610,430611,430612,430613,430614,430615,430616,430617,430618,430619], visible=True, meshCount=20, arg4=0, delay=50) # Real
        set_agent(triggerIds=[28061], visible=False)
        set_agent(triggerIds=[28062], visible=False)
        set_portal(portalId=14, visible=True, enabled=True, minimapVisible=False)
        set_mesh(triggerIds=[4014], visible=False, arg3=0, arg4=0, arg5=0) # PortalBarrier

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Quit()


class MakeFalse(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[230600,230601,230602,230603,230604,230605,230606,230607,230608,230609,230610,230611,230612,230613,230614,230615,230616,230617,230618,230619], visible=False, arg3=0, arg4=0, arg5=5) # Fake

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Quit()


class Quit(state.State):
    pass


