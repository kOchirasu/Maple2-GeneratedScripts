""" trigger/02000378_bf/1303_route_03roundfront.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_agent(triggerIds=[18031], visible=True)
        set_agent(triggerIds=[18032], visible=True)
        set_agent(triggerIds=[18033], visible=True)
        set_agent(triggerIds=[18034], visible=True)
        set_effect(triggerIds=[5003], visible=False) # 03Round_BridgeApp
        set_mesh(triggerIds=[130300,130301,130302,130303,130304,130305,130306,130307,130308,130309,130310,130311,130312,130313,130314,130315,130316,130317,130318,130319,130320,130321], visible=False, arg3=0, arg4=0, arg5=0) # Fake
        set_mesh(triggerIds=[330300,330301,330302,330303,330304,330305,330306,330307,330308,330309,330310,330311,330312,330313,330314,330315,330316,330317,330318,330319,330320,330321], visible=False, arg3=0, arg4=0, arg5=0) # Real
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
        set_random_mesh(triggerIds=[130300,130301,130302,130303,130304,130305,130306,130307,130308,130309,130310,130311,130312,130313,130314,130315,130316,130317,130318,130319,130320,130321], visible=True, meshCount=7, arg4=100, delay=500) # Fake

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return StartDazzlingRandom02()
        if user_value(key='MakeTrue', value=1):
            return MakeTrue()
        if user_value(key='MakeFalse', value=1):
            return MakeFalse()

    def on_exit(self):
        set_random_mesh(triggerIds=[130300,130301,130302,130303,130304,130305,130306,130307,130308,130309,130310,130311,130312,130313,130314,130315,130316,130317,130318,130319,130320,130321], visible=False, meshCount=22, arg4=0, delay=0) # Fake


class StartDazzlingRandom02(state.State):
    def on_enter(self):
        set_random_mesh(triggerIds=[130300,130301,130302,130303,130304,130305,130306,130307,130308,130309,130310,130311,130312,130313,130314,130315,130316,130317,130318,130319,130320,130321], visible=True, meshCount=7, arg4=100, delay=500) # Fake

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return StartDazzlingRandom01()
        if user_value(key='MakeTrue', value=1):
            return MakeTrue()
        if user_value(key='MakeFalse', value=1):
            return MakeFalse()

    def on_exit(self):
        set_random_mesh(triggerIds=[130300,130301,130302,130303,130304,130305,130306,130307,130308,130309,130310,130311,130312,130313,130314,130315,130316,130317,130318,130319,130320,130321], visible=False, meshCount=22, arg4=0, delay=0) # Fake


class MakeTrue(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5003], visible=True) # 03Round_BridgeApp
        set_mesh(triggerIds=[130300,130301,130302,130303,130304,130305,130306,130307,130308,130309,130310,130311,130312,130313,130314,130315,130316,130317,130318,130319,130320,130321], visible=False, arg3=0, arg4=0, arg5=5) # Fake
        set_random_mesh(triggerIds=[330300,330301,330302,330303,330304,330305,330306,330307,330308,330309,330310,330311,330312,330313,330314,330315,330316,330317,330318,330319,330320,330321], visible=True, meshCount=22, arg4=100, delay=50) # Real
        set_agent(triggerIds=[18031], visible=False)
        set_agent(triggerIds=[18032], visible=False)
        set_agent(triggerIds=[18033], visible=False)
        set_agent(triggerIds=[18034], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Quit()


class MakeFalse(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[130300,130301,130302,130303,130304,130305,130306,130307,130308,130309,130310,130311,130312,130313,130314,130315,130316,130317,130318,130319,130320,130321], visible=False, arg3=0, arg4=0, arg5=5) # Fake

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Quit()


class Quit(state.State):
    pass


