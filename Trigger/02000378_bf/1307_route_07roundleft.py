""" trigger/02000378_bf/1307_route_07roundleft.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_agent(triggerIds=[18071], visible=True)
        set_agent(triggerIds=[18072], visible=True)
        set_agent(triggerIds=[18073], visible=True)
        set_agent(triggerIds=[18074], visible=True)
        set_effect(triggerIds=[5007], visible=False) # 07Round_BridgeApp
        set_mesh(triggerIds=[130700,130701,130702,130703,130704,130705,130706,130707,130708,130709,130710,130711,130712,130713,130714,130715,130716,130717,130718,130719,130720,130721], visible=False, arg3=0, arg4=0, arg5=0) # Fake
        set_mesh(triggerIds=[330700,330701,330702,330703,330704,330705,330706,330707,330708,330709,330710,330711,330712,330713,330714,330715,330716,330717,330718,330719,330720,330721], visible=False, arg3=0, arg4=0, arg5=0) # Real
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
        set_random_mesh(triggerIds=[130700,130701,130702,130703,130704,130705,130706,130707,130708,130709,130710,130711,130712,130713,130714,130715,130716,130717,130718,130719,130720,130721], visible=True, meshCount=7, arg4=100, delay=500) # Fake

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return StartDazzlingRandom02()
        if user_value(key='MakeTrue', value=1):
            return MakeTrue()
        if user_value(key='MakeFalse', value=1):
            return MakeFalse()

    def on_exit(self):
        set_random_mesh(triggerIds=[130700,130701,130702,130703,130704,130705,130706,130707,130708,130709,130710,130711,130712,130713,130714,130715,130716,130717,130718,130719,130720,130721], visible=False, meshCount=22, arg4=0, delay=0) # Fake


class StartDazzlingRandom02(state.State):
    def on_enter(self):
        set_random_mesh(triggerIds=[130700,130701,130702,130703,130704,130705,130706,130707,130708,130709,130710,130711,130712,130713,130714,130715,130716,130717,130718,130719,130720,130721], visible=True, meshCount=7, arg4=100, delay=500) # Fake

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return StartDazzlingRandom01()
        if user_value(key='MakeTrue', value=1):
            return MakeTrue()
        if user_value(key='MakeFalse', value=1):
            return MakeFalse()

    def on_exit(self):
        set_random_mesh(triggerIds=[130700,130701,130702,130703,130704,130705,130706,130707,130708,130709,130710,130711,130712,130713,130714,130715,130716,130717,130718,130719,130720,130721], visible=False, meshCount=22, arg4=0, delay=0) # Fake


class MakeTrue(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5007], visible=True) # 07Round_BridgeApp
        set_mesh(triggerIds=[130700,130701,130702,130703,130704,130705,130706,130707,130708,130709,130710,130711,130712,130713,130714,130715,130716,130717,130718,130719,130720,130721], visible=False, arg3=0, arg4=0, arg5=5) # Fake
        set_random_mesh(triggerIds=[330700,330701,330702,330703,330704,330705,330706,330707,330708,330709,330710,330711,330712,330713,330714,330715,330716,330717,330718,330719,330720,330721], visible=True, meshCount=22, arg4=100, delay=50) # Real
        set_agent(triggerIds=[18071], visible=False)
        set_agent(triggerIds=[18072], visible=False)
        set_agent(triggerIds=[18073], visible=False)
        set_agent(triggerIds=[18074], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Quit()


class MakeFalse(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[130700,130701,130702,130703,130704,130705,130706,130707,130708,130709,130710,130711,130712,130713,130714,130715,130716,130717,130718,130719,130720,130721], visible=False, arg3=0, arg4=0, arg5=5) # Fake

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Quit()


class Quit(state.State):
    pass


