""" trigger/99999845/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000301], state=2)
        set_interact_object(triggerIds=[12000302], state=2)
        set_interact_object(triggerIds=[12000303], state=2)
        set_interact_object(triggerIds=[12000304], state=2)
        set_interact_object(triggerIds=[12000305], state=2)
        set_interact_object(triggerIds=[12000306], state=2)
        set_interact_object(triggerIds=[12000307], state=2)
        set_interact_object(triggerIds=[12000308], state=2)
        set_interact_object(triggerIds=[12000309], state=2)
        set_interact_object(triggerIds=[12000310], state=2)
        set_interact_object(triggerIds=[12000311], state=2)
        set_interact_object(triggerIds=[12000312], state=2)
        set_interact_object(triggerIds=[12000313], state=2)
        set_interact_object(triggerIds=[12000314], state=2)
        set_interact_object(triggerIds=[12000315], state=2)
        set_interact_object(triggerIds=[12000316], state=2)
        set_interact_object(triggerIds=[12000317], state=2)
        set_interact_object(triggerIds=[12000318], state=2)
        set_interact_object(triggerIds=[12000319], state=2)
        set_interact_object(triggerIds=[12000320], state=2)
        set_interact_object(triggerIds=[12000321], state=2)
        set_interact_object(triggerIds=[12000322], state=2)
        set_mesh(triggerIds=[1001], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[1002], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[1003], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[1004], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[1005], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[1006], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[2001], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[2002], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[2003], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[2004], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[2005], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[2006], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[2007], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[2008], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3001], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3002], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3003], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3004], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3005], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3006], visible=True, arg3=0, arg4=0, arg5=0)
        set_visible_breakable_object(triggerIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010], arg2=False)
        set_visible_breakable_object(triggerIds=[1011,1012,1013,1014,1015,1016,1017,1018,1019,1020], arg2=False)
        set_visible_breakable_object(triggerIds=[1021,1022], arg2=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[900]):
            return LineStart()


class LineStart(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1101], arg2=False)
        create_monster(spawnIds=[1102], arg2=False)
        create_monster(spawnIds=[1103], arg2=False)
        create_monster(spawnIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010], arg2=False)
        create_monster(spawnIds=[1011,1012,1013,1014,1015,1016,1017,1018,1019,1020], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1101,1103]):
            set_mesh(triggerIds=[1001], visible=False, arg3=0, arg4=0, arg5=0)
            set_mesh(triggerIds=[1002], visible=False, arg3=0, arg4=0, arg5=0)
            set_mesh(triggerIds=[1003], visible=False, arg3=0, arg4=0, arg5=0)
            set_mesh(triggerIds=[1004], visible=False, arg3=0, arg4=0, arg5=0)
            set_mesh(triggerIds=[1005], visible=False, arg3=0, arg4=0, arg5=0)
            set_mesh(triggerIds=[1006], visible=False, arg3=0, arg4=0, arg5=0)
            set_mesh(triggerIds=[2001], visible=False, arg3=0, arg4=0, arg5=0)
            set_mesh(triggerIds=[2002], visible=False, arg3=0, arg4=0, arg5=0)
            set_mesh(triggerIds=[2003], visible=False, arg3=0, arg4=0, arg5=0)
            set_mesh(triggerIds=[2004], visible=False, arg3=0, arg4=0, arg5=0)
            set_mesh(triggerIds=[2005], visible=False, arg3=0, arg4=0, arg5=0)
            set_mesh(triggerIds=[2006], visible=False, arg3=0, arg4=0, arg5=0)
            set_mesh(triggerIds=[2007], visible=False, arg3=0, arg4=0, arg5=0)
            set_mesh(triggerIds=[2008], visible=False, arg3=0, arg4=0, arg5=0)
            set_mesh(triggerIds=[3001], visible=False, arg3=0, arg4=0, arg5=0)
            set_mesh(triggerIds=[3002], visible=False, arg3=0, arg4=0, arg5=0)
            set_mesh(triggerIds=[3003], visible=False, arg3=0, arg4=0, arg5=0)
            set_mesh(triggerIds=[3004], visible=False, arg3=0, arg4=0, arg5=0)
            set_mesh(triggerIds=[3005], visible=False, arg3=0, arg4=0, arg5=0)
            set_mesh(triggerIds=[3006], visible=False, arg3=0, arg4=0, arg5=0)
            set_visible_breakable_object(triggerIds=[1001,1002,1003], arg2=True)
            set_interact_object(triggerIds=[12000301], state=1)
            set_interact_object(triggerIds=[12000302], state=1)
            set_interact_object(triggerIds=[12000303], state=1)
            create_monster(spawnIds=[1104], arg2=False)
            create_monster(spawnIds=[1105], arg2=False)
            create_monster(spawnIds=[1106], arg2=False)
            return CableOn_01()


class CableOn_01(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000302], arg2=0):
            set_interact_object(triggerIds=[12000301], state=2)
            set_interact_object(triggerIds=[12000302], state=2)
            set_interact_object(triggerIds=[12000303], state=2)
            move_user_to_pos(pos=[-15571.11,75.2856445,3600], rot=[0,0,0])
            return CableDelay_01_1()
        if object_interacted(interactIds=[12000303], arg2=0):
            set_interact_object(triggerIds=[12000301], state=2)
            set_interact_object(triggerIds=[12000302], state=2)
            set_interact_object(triggerIds=[12000303], state=2)
            move_user_to_pos(pos=[-15571.11,-1561.813,3600], rot=[0,0,0])
            return CableDelay_01_2()
        if object_interacted(interactIds=[12000301], arg2=0):
            set_interact_object(triggerIds=[12000301], state=2)
            set_interact_object(triggerIds=[12000302], state=2)
            set_interact_object(triggerIds=[12000303], state=2)
            move_user_to_pos(pos=[-15571.11,1730.293,3600], rot=[0,0,0])
            return CableDelay_01_3()


class CableDelay_01_1(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_breakable(triggerIds=[1002], enabled=True)
            return CableOff_01()


class CableDelay_01_2(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_breakable(triggerIds=[1003], enabled=True)
            return CableOff_02()


class CableDelay_01_3(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_breakable(triggerIds=[1001], enabled=True)
            return CableOff_03()


class CableOff_01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            set_user_value(triggerId=900002, key='Block', value=1)
            return End_01()


class CableOff_02(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            set_user_value(triggerId=900002, key='Block', value=2)
            return End_01()


class CableOff_03(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            set_user_value(triggerId=900002, key='Block', value=3)
            return End_01()


class End_01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return None


