""" trigger/02000378_bf/1305_route_05roundleft.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_portal(portalId=11, visible=False, enabled=False, minimapVisible=False)
        set_mesh(triggerIds=[4011], visible=True, arg3=0, arg4=0, arg5=0) # PortalBarrier
        set_agent(triggerIds=[18051], visible=True)
        set_agent(triggerIds=[18052], visible=True)
        set_effect(triggerIds=[5005], visible=False) # 05Round_BridgeApp
        set_mesh(triggerIds=[130500,130501,130502,130503,130504,130505,130506,130507,130508,130509,130510,130511,130512,130513,130514,130515,130516,130517,130518,130519], visible=False, arg3=0, arg4=0, arg5=0) # Fake
        set_mesh(triggerIds=[330500,330501,330502,330503,330504,330505,330506,330507,330508,330509,330510,330511,330512,330513,330514,330515,330516,330517,330518,330519], visible=False, arg3=0, arg4=0, arg5=0) # Real
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
        set_random_mesh(triggerIds=[130500,130501,130502,130503,130504,130505,130506,130507,130508,130509,130510,130511,130512,130513,130514,130515,130516,130517,130518,130519], visible=True, meshCount=6, arg4=100, delay=500) # Fake

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return StartDazzlingRandom02()
        if user_value(key='MakeTrue', value=1):
            return MakeTrue()
        if user_value(key='MakeFalse', value=1):
            return MakeFalse()

    def on_exit(self):
        set_random_mesh(triggerIds=[130500,130501,130502,130503,130504,130505,130506,130507,130508,130509,130510,130511,130512,130513,130514,130515,130516,130517,130518,130519], visible=False, meshCount=20, arg4=0, delay=0) # Fake


class StartDazzlingRandom02(state.State):
    def on_enter(self):
        set_random_mesh(triggerIds=[130500,130501,130502,130503,130504,130505,130506,130507,130508,130509,130510,130511,130512,130513,130514,130515,130516,130517,130518,130519], visible=True, meshCount=6, arg4=100, delay=500) # Fake

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return StartDazzlingRandom01()
        if user_value(key='MakeTrue', value=1):
            return MakeTrue()
        if user_value(key='MakeFalse', value=1):
            return MakeFalse()

    def on_exit(self):
        set_random_mesh(triggerIds=[130500,130501,130502,130503,130504,130505,130506,130507,130508,130509,130510,130511,130512,130513,130514,130515,130516,130517,130518,130519], visible=False, meshCount=20, arg4=0, delay=0) # Fake


class MakeTrue(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5005], visible=True) # 05Round_BridgeApp
        set_mesh(triggerIds=[130500,130501,130502,130503,130504,130505,130506,130507,130508,130509,130510,130511,130512,130513,130514,130515,130516,130517,130518,130519], visible=False, arg3=0, arg4=0, arg5=5) # Fake
        set_random_mesh(triggerIds=[330500,330501,330502,330503,330504,330505,330506,330507,330508,330509,330510,330511,330512,330513,330514,330515,330516,330517,330518,330519], visible=True, meshCount=20, arg4=100, delay=50) # Real
        set_agent(triggerIds=[18051], visible=False)
        set_agent(triggerIds=[18052], visible=False)
        set_portal(portalId=11, visible=True, enabled=True, minimapVisible=False)
        set_mesh(triggerIds=[4011], visible=False, arg3=0, arg4=0, arg5=0) # PortalBarrier

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Quit()


class MakeFalse(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[130500,130501,130502,130503,130504,130505,130506,130507,130508,130509,130510,130511,130512,130513,130514,130515,130516,130517,130518,130519], visible=False, arg3=0, arg4=0, arg5=5) # Fake

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Quit()


class Quit(state.State):
    pass


