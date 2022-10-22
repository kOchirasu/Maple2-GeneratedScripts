""" trigger/99999845/field_1.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000304], state=2)
        set_interact_object(triggerIds=[12000305], state=2)
        set_interact_object(triggerIds=[12000306], state=2)
        # <action name="SetVisibleBreakableObject" arg1="1001,1002,1003,1004,1005,1006,1007,1008,1009,1010" arg2="0" />

    def on_tick(self) -> state.State:
        if user_value(key='Block', value=1):
            set_user_value(triggerId=900002, key='Block', value=0)
            return Block_1()
        if user_value(key='Block', value=2):
            set_user_value(triggerId=900002, key='Block', value=0)
            return Block_2()
        if user_value(key='Block', value=3):
            set_user_value(triggerId=900002, key='Block', value=0)
            return Block_3()


class Block_1(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1104]):
            set_visible_breakable_object(triggerIds=[1004], arg2=True)
            set_interact_object(triggerIds=[12000304], state=1)
            create_monster(spawnIds=[1107], arg2=False)
            create_monster(spawnIds=[1108], arg2=False)
            create_monster(spawnIds=[1109], arg2=False)
            return CableOn_04()


class Block_2(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1105]):
            set_visible_breakable_object(triggerIds=[1005], arg2=True)
            set_interact_object(triggerIds=[12000305], state=1)
            create_monster(spawnIds=[1107], arg2=False)
            create_monster(spawnIds=[1108], arg2=False)
            create_monster(spawnIds=[1109], arg2=False)
            return CableOn_05()


class Block_3(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1106]):
            set_visible_breakable_object(triggerIds=[1006], arg2=True)
            set_interact_object(triggerIds=[12000306], state=1)
            create_monster(spawnIds=[1107], arg2=False)
            create_monster(spawnIds=[1108], arg2=False)
            create_monster(spawnIds=[1109], arg2=False)
            return CableOn_06()


class CableOn_04(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000304], arg2=0):
            set_interact_object(triggerIds=[12000304], state=2)
            move_user_to_pos(pos=[-12687.7676,-1071.39685,2530], rot=[0,0,0])
            return CableDelay_04()


class CableOn_05(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000305], arg2=0):
            set_interact_object(triggerIds=[12000305], state=2)
            move_user_to_pos(pos=[-11673.0137,-6377.65674,1639], rot=[0,0,0])
            return CableDelay_05()


class CableOn_06(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000306], arg2=0):
            set_interact_object(triggerIds=[12000306], state=2)
            move_user_to_pos(pos=[-11221.6494,6215.7334,433], rot=[0,0,0])
            return CableDelay_06()


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
            set_user_value(triggerId=900003, key='Block', value=1)
            return End_01()


class CableOff_05(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            set_user_value(triggerId=900003, key='Block', value=2)
            return End_01()


class CableOff_06(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            set_user_value(triggerId=900003, key='Block', value=3)
            return End_01()


class End_01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 대기()


