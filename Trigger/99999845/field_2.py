""" trigger/99999845/field_2.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000307], state=2)
        set_interact_object(triggerIds=[12000308], state=2)
        set_interact_object(triggerIds=[12000309], state=2)
        set_interact_object(triggerIds=[12000310], state=2)
        set_interact_object(triggerIds=[12000311], state=2)
        set_interact_object(triggerIds=[12000312], state=2)
        # <action name="SetVisibleBreakableObject" arg1="1001,1002,1003,1004,1005,1006,1007,1008,1009,1010" arg2="0" />

    def on_tick(self) -> state.State:
        if user_value(key='Block', value=1):
            set_user_value(triggerId=900003, key='Block', value=0)
            return Block_1()
        if user_value(key='Block', value=2):
            set_user_value(triggerId=900003, key='Block', value=0)
            return Block_2()
        if user_value(key='Block', value=3):
            set_user_value(triggerId=900003, key='Block', value=0)
            return Block_3()


class Block_1(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1107]):
            set_visible_breakable_object(triggerIds=[1007], arg2=True)
            set_visible_breakable_object(triggerIds=[1008], arg2=True)
            set_interact_object(triggerIds=[12000307], state=1)
            set_interact_object(triggerIds=[12000308], state=1)
            create_monster(spawnIds=[1110], arg2=False)
            create_monster(spawnIds=[1111], arg2=False)
            create_monster(spawnIds=[1112], arg2=False)
            create_monster(spawnIds=[1113], arg2=False)
            return CableOn_07_08()


class Block_2(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1108]):
            set_visible_breakable_object(triggerIds=[1009], arg2=True)
            set_visible_breakable_object(triggerIds=[1010], arg2=True)
            set_interact_object(triggerIds=[12000309], state=1)
            set_interact_object(triggerIds=[12000310], state=1)
            create_monster(spawnIds=[1110], arg2=False)
            create_monster(spawnIds=[1111], arg2=False)
            create_monster(spawnIds=[1112], arg2=False)
            create_monster(spawnIds=[1113], arg2=False)
            return CableOn_09_10()


class Block_3(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1109]):
            set_visible_breakable_object(triggerIds=[1011], arg2=True)
            set_visible_breakable_object(triggerIds=[1012], arg2=True)
            set_interact_object(triggerIds=[12000311], state=1)
            set_interact_object(triggerIds=[12000312], state=1)
            create_monster(spawnIds=[1110], arg2=False)
            create_monster(spawnIds=[1111], arg2=False)
            create_monster(spawnIds=[1112], arg2=False)
            create_monster(spawnIds=[1113], arg2=False)
            return CableOn_11_12()


class CableOn_07_08(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000307], arg2=0):
            set_interact_object(triggerIds=[12000307], state=2)
            set_interact_object(triggerIds=[12000308], state=2)
            move_user_to_pos(pos=[-8476.297,-3480.99072,1343], rot=[0,0,0])
            return CableDelay_07()
        if object_interacted(interactIds=[12000308], arg2=0):
            set_interact_object(triggerIds=[12000307], state=2)
            set_interact_object(triggerIds=[12000308], state=2)
            move_user_to_pos(pos=[-6726.70264,-377.953552,1343], rot=[0,0,0])
            return CableDelay_08()


class CableOn_09_10(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000309], arg2=0):
            set_interact_object(triggerIds=[12000309], state=2)
            set_interact_object(triggerIds=[12000310], state=2)
            move_user_to_pos(pos=[-8321.446,-7475.03271,135], rot=[0,0,0])
            return CableDelay_09()
        if object_interacted(interactIds=[12000310], arg2=0):
            set_interact_object(triggerIds=[12000309], state=2)
            set_interact_object(triggerIds=[12000310], state=2)
            move_user_to_pos(pos=[-6576.207,-9063.119,135], rot=[0,0,0])
            return CableDelay_10()


class CableOn_11_12(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000311], arg2=0):
            set_interact_object(triggerIds=[12000311], state=2)
            set_interact_object(triggerIds=[12000312], state=2)
            move_user_to_pos(pos=[-7723.194,5673.29346,2690], rot=[0,0,0])
            return CableDelay_11()
        if object_interacted(interactIds=[12000312], arg2=0):
            set_interact_object(triggerIds=[12000311], state=2)
            set_interact_object(triggerIds=[12000312], state=2)
            move_user_to_pos(pos=[-6276.41748,8028.68164,2690], rot=[0,0,0])
            return CableDelay_12()


class CableDelay_07(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_breakable(triggerIds=[1007], enabled=True)
            return CableOff_07()


class CableDelay_08(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_breakable(triggerIds=[1008], enabled=True)
            return CableOff_08()


class CableDelay_09(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_breakable(triggerIds=[1009], enabled=True)
            return CableOff_09()


class CableDelay_10(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_breakable(triggerIds=[1010], enabled=True)
            return CableOff_10()


class CableDelay_11(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_breakable(triggerIds=[1011], enabled=True)
            return CableOff_11()


class CableDelay_12(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_breakable(triggerIds=[1012], enabled=True)
            return CableOff_12()


class CableOff_07(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            set_user_value(triggerId=900004, key='Block', value=2)
            return End_02()


class CableOff_08(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            set_user_value(triggerId=900004, key='Block', value=1)
            return End_02()


class CableOff_09(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            set_user_value(triggerId=900004, key='Block', value=2)
            return End_02()


class CableOff_10(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            set_user_value(triggerId=900004, key='Block', value=3)
            return End_02()


class CableOff_11(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            set_user_value(triggerId=900004, key='Block', value=1)
            return End_02()


class CableOff_12(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            set_user_value(triggerId=900004, key='Block', value=4)
            return End_02()


class End_02(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 대기()


