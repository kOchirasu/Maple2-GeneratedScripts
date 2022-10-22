""" trigger/99999845/field_3.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000313], state=2)
        set_interact_object(triggerIds=[12000314], state=2)
        set_interact_object(triggerIds=[12000315], state=2)
        set_interact_object(triggerIds=[12000316], state=2)
        set_interact_object(triggerIds=[12000317], state=2)
        set_interact_object(triggerIds=[12000318], state=2)
        # <action name="SetVisibleBreakableObject" arg1="1001,1002,1003,1004,1005,1006,1007,1008,1009,1010" arg2="0" />

    def on_tick(self) -> state.State:
        if user_value(key='Block', value=1):
            set_user_value(triggerId=900004, key='Block', value=0)
            return Block_1()
        if user_value(key='Block', value=2):
            set_user_value(triggerId=900004, key='Block', value=0)
            return Block_2()
        if user_value(key='Block', value=3):
            set_user_value(triggerId=900004, key='Block', value=0)
            return Block_3()
        if user_value(key='Block', value=4):
            set_user_value(triggerId=900004, key='Block', value=0)
            return Block_4()


class Block_1(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1110]):
            set_visible_breakable_object(triggerIds=[1013], arg2=True)
            set_interact_object(triggerIds=[12000313], state=1)
            create_monster(spawnIds=[1114], arg2=False)
            create_monster(spawnIds=[1115], arg2=False)
            create_monster(spawnIds=[1116], arg2=False)
            return CableOn_13()


class Block_2(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1111]):
            set_visible_breakable_object(triggerIds=[1014], arg2=True)
            set_visible_breakable_object(triggerIds=[1015], arg2=True)
            set_interact_object(triggerIds=[12000314], state=1)
            set_interact_object(triggerIds=[12000315], state=1)
            create_monster(spawnIds=[1114], arg2=False)
            create_monster(spawnIds=[1115], arg2=False)
            create_monster(spawnIds=[1116], arg2=False)
            return CableOn_14_15()


class Block_3(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1112]):
            set_visible_breakable_object(triggerIds=[1016], arg2=True)
            set_visible_breakable_object(triggerIds=[1017], arg2=True)
            set_interact_object(triggerIds=[12000316], state=1)
            set_interact_object(triggerIds=[12000317], state=1)
            create_monster(spawnIds=[1114], arg2=False)
            create_monster(spawnIds=[1115], arg2=False)
            create_monster(spawnIds=[1116], arg2=False)
            return CableOn_16_17()


class Block_4(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1113]):
            set_visible_breakable_object(triggerIds=[1018], arg2=True)
            set_interact_object(triggerIds=[12000318], state=1)
            create_monster(spawnIds=[1114], arg2=False)
            create_monster(spawnIds=[1115], arg2=False)
            create_monster(spawnIds=[1116], arg2=False)
            return CableOn_18()


class CableOn_13(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000313], arg2=0):
            set_interact_object(triggerIds=[12000313], state=2)
            move_user_to_pos(pos=[-2514.072,3816.40259,1500], rot=[0,0,0])
            return CableDelay_13()


class CableOn_14_15(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000314], arg2=0):
            set_interact_object(triggerIds=[12000314], state=2)
            set_interact_object(triggerIds=[12000315], state=2)
            move_user_to_pos(pos=[-3524.431,-1479.53162,137], rot=[0,0,0])
            return CableDelay_14()
        if object_interacted(interactIds=[12000315], arg2=0):
            set_interact_object(triggerIds=[12000314], state=2)
            set_interact_object(triggerIds=[12000315], state=2)
            move_user_to_pos(pos=[-1478.22412,-4127.897,137], rot=[0,0,0])
            return CableDelay_15()


class CableOn_16_17(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000316], arg2=0):
            set_interact_object(triggerIds=[12000316], state=2)
            set_interact_object(triggerIds=[12000317], state=2)
            move_user_to_pos(pos=[-848.5522,-7473.63,2690], rot=[0,0,0])
            return CableDelay_16()
        if object_interacted(interactIds=[12000317], arg2=0):
            set_interact_object(triggerIds=[12000316], state=2)
            set_interact_object(triggerIds=[12000317], state=2)
            move_user_to_pos(pos=[1372.17615,-8612.513,2690], rot=[0,0,0])
            return CableDelay_17()


class CableOn_18(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000318], arg2=0):
            set_interact_object(triggerIds=[12000318], state=2)
            move_user_to_pos(pos=[-840.132935,6427.83936,1640], rot=[0,0,0])
            return CableDelay_18()


class CableDelay_13(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_breakable(triggerIds=[1013], enabled=True)
            return CableOff_13()


class CableDelay_14(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_breakable(triggerIds=[1014], enabled=True)
            return CableOff_14()


class CableDelay_15(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_breakable(triggerIds=[1015], enabled=True)
            return CableOff_15()


class CableDelay_16(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_breakable(triggerIds=[1016], enabled=True)
            return CableOff_16()


class CableDelay_17(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_breakable(triggerIds=[1017], enabled=True)
            return CableOff_17()


class CableDelay_18(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_breakable(triggerIds=[1018], enabled=True)
            return CableOff_18()


class CableOff_13(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            set_user_value(triggerId=900005, key='Block', value=1)
            return End_03()


class CableOff_14(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            set_user_value(triggerId=900005, key='Block', value=1)
            return End_03()


class CableOff_15(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            set_user_value(triggerId=900005, key='Block', value=2)
            return End_03()


class CableOff_16(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            set_user_value(triggerId=900005, key='Block', value=1)
            return End_03()


class CableOff_17(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            set_user_value(triggerId=900005, key='Block', value=2)
            return End_03()


class CableOff_18(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            set_user_value(triggerId=900005, key='Block', value=3)
            return End_03()


class End_03(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 대기()


