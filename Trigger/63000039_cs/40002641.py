""" trigger/63000039_cs/40002641.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_actor(triggerId=201, visible=True, initialSequence='sf_fi_funct_darkdoor_A01_off')
        set_mesh(triggerIds=[3000,3001,3002], visible=True)
        set_mesh(triggerIds=[3003,3004,3005], visible=False)
        set_interact_object(triggerIds=[10001025], state=0)
        create_monster(spawnIds=[1001,1002,1003,1004,1005], arg2=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[199], questIds=[40002641], questStates=[1]):
            return NPC말풍선()
        if quest_user_detected(boxIds=[199], questIds=[40002641], questStates=[2]):
            return 유저이동()


class NPC말풍선(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            set_conversation(type=1, spawnId=1002, script='$63000039_CS__40002641__0$', arg4=4, arg5=0)
            set_conversation(type=1, spawnId=1005, script='$63000039_CS__40002641__1$', arg4=4, arg5=2)
            return 오브젝트반응대기()


class 오브젝트반응대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001025], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001025], arg2=0):
            set_mesh(triggerIds=[3000,3001,3002], visible=False)
            set_mesh(triggerIds=[3003,3004,3005], visible=True)
            return NPC를이동()


class NPC를이동(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=301, enable=True)
        move_npc(spawnId=1001, patrolName='MS2PatrolData_1001')
        move_npc(spawnId=1002, patrolName='MS2PatrolData_1002')
        move_npc(spawnId=1003, patrolName='MS2PatrolData_1003')
        move_npc(spawnId=1004, patrolName='MS2PatrolData_1004')
        move_npc(spawnId=1005, patrolName='MS2PatrolData_1005')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return PC이동()


class PC이동(state.State):
    def on_enter(self):
        set_actor(triggerId=201, visible=True, initialSequence='sf_fi_funct_darkdoor_A01_on')
        move_user_path(patrolName='MS2PatrolData_PC')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4500):
            return PC말풍선()


class PC말풍선(state.State):
    def on_enter(self):
        select_camera(triggerId=302, enable=True)
        set_conversation(type=1, spawnId=0, script='$63000039_CS__40002641__2$', arg4=4, arg5=0)
        set_achievement(triggerId=199, type='trigger', achieve='SaveBackstreetPeople')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 유저이동조건()


class 유저이동조건(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[199], questIds=[40002641], questStates=[2]):
            return 유저이동()


class 유저이동(state.State):
    def on_enter(self):
        select_camera(triggerId=302, enable=False)
        move_user(mapId=2000275, portalId=30)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 종료()


class 종료(state.State):
    pass


