""" trigger/52000043_qd/50001452.xml """
from common import *
import state


class 선행퀘스트체크(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001017], state=2)
        set_interact_object(triggerIds=[10001018], state=2)
        set_interact_object(triggerIds=[10001019], state=2)
        set_interact_object(triggerIds=[10001020], state=2)
        set_interact_object(triggerIds=[10001021], state=2)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[199], questIds=[50001451], questStates=[3]):
            destroy_monster(spawnIds=[1001,2001])
            return 시작조건()


class 시작조건(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1001,2001], arg2=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[199], questIds=[50001452], questStates=[1]):
            return 연출시작()
        if quest_user_detected(boxIds=[199], questIds=[50001452], questStates=[2]):
            destroy_monster(spawnIds=[1003,2003])
            return NPC만배치()
        if quest_user_detected(boxIds=[199], questIds=[50001452], questStates=[3]):
            destroy_monster(spawnIds=[1003,2003])
            return NPC만배치()


class NPC만배치(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1001,2001])
        create_monster(spawnIds=[1003,2003], arg2=False)
        set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[199], questIds=[50001454], questStates=[2]):
            destroy_monster(spawnIds=[1003,2003])
            return 종료()
        if quest_user_detected(boxIds=[199], questIds=[50001454], questStates=[3]):
            destroy_monster(spawnIds=[1003,2003])
            return 종료()
        if wait_tick(waitTick=1000):
            return 종료()


class 연출시작(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1001,2001])
        create_monster(spawnIds=[1002,2002], arg2=False)
        set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017], visible=True, arg3=0, arg4=0, arg5=0)
        select_camera(triggerId=304, enable=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return NPC이동01()


class NPC이동01(state.State):
    def on_enter(self):
        move_npc(spawnId=1002, patrolName='MS2PatrolData_1002A')
        move_npc(spawnId=2002, patrolName='MS2PatrolData_2002A')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=101, spawnIds=[2002]):
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        select_camera(triggerId=304, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        move_npc(spawnId=1002, patrolName='MS2PatrolData_1002B')
        move_npc(spawnId=2002, patrolName='MS2PatrolData_2002B')
        set_interact_object(triggerIds=[10001017], state=1)
        set_interact_object(triggerIds=[10001018], state=1)
        set_interact_object(triggerIds=[10001019], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001019], arg2=0):
            return 부서짐연출()


class 부서짐연출(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001017], state=2)
        set_interact_object(triggerIds=[10001018], state=2)
        set_interact_object(triggerIds=[10001020], state=1)
        set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017], visible=False, arg3=0, arg4=200, arg5=2)
        select_camera(triggerId=306, enable=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_skip(state=향로반응대기)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 향로반응대기()

    def on_exit(self):
        select_camera(triggerId=306, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class 향로반응대기(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[199], questIds=[50001452], questStates=[2]):
            return NPC이동02()


class NPC이동02(state.State):
    def on_enter(self):
        move_npc(spawnId=1002, patrolName='MS2PatrolData_1002C')
        move_npc(spawnId=2002, patrolName='MS2PatrolData_2002C')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=102, spawnIds=[1002]):
            return NPC교체01()


class NPC교체01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1002])
        create_monster(spawnIds=[1003], arg2=False)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=103, spawnIds=[2002]):
            return NPC교체02()


class NPC교체02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[2002])
        create_monster(spawnIds=[2003], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 종료()


class 종료(state.State):
    pass


