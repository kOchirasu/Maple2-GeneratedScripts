""" trigger/52000062_qd/guidescene_01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1001], arg2=False)
        create_monster(spawnIds=[1002], arg2=False)
        create_monster(spawnIds=[1003], arg2=False)
        create_monster(spawnIds=[1004], arg2=False)
        create_monster(spawnIds=[1007], arg2=False)
        set_effect(triggerIds=[601], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 유저감지()


class 유저감지(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[199], questIds=[90000561], questStates=[3]):
            return 종료()
        if quest_user_detected(boxIds=[199], questIds=[90000561], questStates=[2]):
            return 연퀘감지2()
        if quest_user_detected(boxIds=[199], questIds=[90000560,90000561], questStates=[1]):
            return 연퀘감지()
        if user_detected(boxIds=[199]):
            return 페르시카대사01()


class 페르시카대사01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=301, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 페르시카대사02()


class 페르시카대사02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001176, script='$52000062_QD__GUIDESCENE_01__0$', arg4=3, arg5=0)
        set_conversation(type=2, spawnId=11001176, script='$52000062_QD__GUIDESCENE_01__1$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=301, enable=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 연퀘감지()


class 연퀘감지(state.State):
    def on_enter(self):
        move_npc(spawnId=1001, patrolName='MS2PatrolData_Fercika')

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[199], questIds=[90000561], questStates=[2]):
            return PC이동()


class 연퀘감지2(state.State):
    def on_enter(self):
        move_npc(spawnId=1001, patrolName='MS2PatrolData_Fercika')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return PC이동()


class PC이동(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=301, enable=True)
        move_user_path(patrolName='MS2PatrolData_PC')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[198]):
            return 찬양NPC이동()


class 찬양NPC이동(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=True)
        move_npc(spawnId=1001, patrolName='MS2PatrolData_Fercika2')
        create_monster(spawnIds=[1005], arg2=False)
        destroy_monster(spawnIds=[1002], arg2=False)
        create_monster(spawnIds=[1006], arg2=False)
        destroy_monster(spawnIds=[1004], arg2=False)
        create_monster(spawnIds=[1008], arg2=False)
        destroy_monster(spawnIds=[1007], arg2=False)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=197, spawnIds=[1001]):
            return 찬양연출()


class 찬양연출(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=1008, script='$52000062_QD__GUIDESCENE_01__2$', arg4=2, arg5=1)
        set_conversation(type=1, spawnId=1005, script='$52000062_QD__GUIDESCENE_01__3$', arg4=2, arg5=3)
        set_conversation(type=1, spawnId=1006, script='$52000062_QD__GUIDESCENE_01__4$', arg4=2, arg5=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 연출종료2()


class 연출종료2(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=301, enable=False)
        set_effect(triggerIds=[601], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 종료()


class 종료(state.State):
    pass


