""" trigger/99999845/field_4.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000319], state=2)
        set_interact_object(triggerIds=[12000320], state=2)
        set_interact_object(triggerIds=[12000321], state=2)
        # <action name="SetVisibleBreakableObject" arg1="1001,1002,1003,1004,1005,1006,1007,1008,1009,1010" arg2="0" />

    def on_tick(self) -> state.State:
        if user_value(key='Block', value=1):
            set_user_value(triggerId=900005, key='Block', value=0)
            return Block_1()
        if user_value(key='Block', value=2):
            set_user_value(triggerId=900005, key='Block', value=0)
            return Block_2()
        if user_value(key='Block', value=3):
            set_user_value(triggerId=900005, key='Block', value=0)
            return Block_3()


class Block_1(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1114]):
            set_visible_breakable_object(triggerIds=[1019], arg2=True)
            set_interact_object(triggerIds=[12000319], state=1)
            create_monster(spawnIds=[1117], arg2=False)
            return CableOn_19()


class Block_2(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1115]):
            set_visible_breakable_object(triggerIds=[1020], arg2=True)
            set_interact_object(triggerIds=[12000320], state=1)
            create_monster(spawnIds=[1117], arg2=False)
            return CableOn_20()


class Block_3(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1116]):
            set_visible_breakable_object(triggerIds=[1021], arg2=True)
            set_interact_object(triggerIds=[12000321], state=1)
            create_monster(spawnIds=[1117], arg2=False)
            return CableOn_21()


class CableOn_19(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000319], arg2=0):
            set_interact_object(triggerIds=[12000319], state=2)
            move_user_to_pos(pos=[1974.56885,372.1966,289], rot=[0,0,0])
            return CableDelay_19()


class CableOn_20(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000320], arg2=0):
            set_interact_object(triggerIds=[12000320], state=2)
            move_user_to_pos(pos=[3971.3916,-4325.10742,1492], rot=[0,0,0])
            return CableDelay_20()


class CableOn_21(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000321], arg2=0):
            set_interact_object(triggerIds=[12000321], state=2)
            move_user_to_pos(pos=[3528.33643,2824.1394,2528], rot=[0,0,0])
            return CableDelay_21()


class CableDelay_19(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_breakable(triggerIds=[1019], enabled=True)
            return CableOff_19()


class CableDelay_20(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_breakable(triggerIds=[1020], enabled=True)
            return CableOff_20()


class CableDelay_21(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_breakable(triggerIds=[1021], enabled=True)
            return CableOff_21()


class CableOff_19(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            set_user_value(triggerId=900006, key='Block', value=1)
            return End_04()


class CableOff_20(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            set_user_value(triggerId=900006, key='Block', value=1)
            return End_04()


class CableOff_21(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            set_user_value(triggerId=900006, key='Block', value=1)
            return End_04()


class End_04(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 대기()


