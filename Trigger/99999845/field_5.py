""" trigger/99999845/field_5.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000322], state=2)
        # <action name="SetVisibleBreakableObject" arg1="1001,1002,1003,1004,1005,1006,1007,1008,1009,1010" arg2="0" />

    def on_tick(self) -> state.State:
        if user_value(key='Block', value=1):
            set_user_value(triggerId=900006, key='Block', value=0)
            return Block_1()


class Block_1(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1117]):
            set_visible_breakable_object(triggerIds=[1022], arg2=True)
            set_interact_object(triggerIds=[12000322], state=1)
            return None # Missing State: CableOn_04


class CableOn_22(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000322], arg2=0):
            set_interact_object(triggerIds=[12000322], state=2)
            move_user_to_pos(pos=[-12687.7676,-1071.39685,2530], rot=[0,0,0])
            return CableDelay_04()


class CableDelay_04(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_breakable(triggerIds=[1004], enabled=True)
            return CableOff_04()


class CableDelay_05(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_breakable(triggerIds=[1005], enabled=True)
            return CableOff_05()


class CableDelay_06(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_breakable(triggerIds=[1006], enabled=True)
            return CableOff_06()


class CableOff_04(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            move_user_to_pos(pos=[-9825,-1425,1350], rot=[0,0,0])
            set_user_value(triggerId=900003, key='Block', value=1)
            return End_01()


class CableOff_05(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            move_user_to_pos(pos=[-9375,-9225,150], rot=[0,0,0])
            set_user_value(triggerId=900003, key='Block', value=2)
            return End_01()


class CableOff_06(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            move_user_to_pos(pos=[-8475,7275,2700], rot=[0,0,0])
            set_user_value(triggerId=900003, key='Block', value=3)
            return End_01()


class End_01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            set_visible_breakable_object(triggerIds=[1004], arg2=False)
            set_visible_breakable_object(triggerIds=[1005], arg2=False)
            set_visible_breakable_object(triggerIds=[1006], arg2=False)
            return None


