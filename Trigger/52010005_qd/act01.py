""" trigger/52010005_qd/act01.xml """
from common import *
import state


class 퀘스트조건01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=True)
        set_interact_object(triggerIds=[10000872], state=0)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[10002820], questStates=[2]):
            return Q1_마샤르교체01()


#   1st Quest 
class Q1_마샤르교체01(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        destroy_monster(spawnIds=[101])
        create_monster(spawnIds=[102], arg2=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return Q1_딜레이01()


class Q1_딜레이01(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return Q1_미카등장()


class Q1_미카등장(state.State):
    def on_enter(self):
        create_monster(spawnIds=[201], arg2=False)
        move_npc(spawnId=201, patrolName='MS2PatrolData_2010')

    def on_tick(self) -> state.State:
        if true():
            return Q1_마샤르이동01()


class Q1_마샤르이동01(state.State):
    def on_enter(self):
        move_npc(spawnId=102, patrolName='MS2PatrolData_1020')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=8001, spawnIds=[102]):
            return Q1_마샤르대화01()


class Q1_마샤르대화01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=102, script='$52010005_QD__ACT01__0$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=8002, spawnIds=[102]):
            return Q1_마샤르대화02()


class Q1_마샤르대화02(state.State):
    def on_enter(self):
        set_timer(timerId='4', seconds=3)
        set_conversation(type=1, spawnId=102, script='$52010005_QD__ACT01__1$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return Q1_카메라연출01()


class Q1_카메라연출01(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=3)
        destroy_monster(spawnIds=[102])
        create_monster(spawnIds=[104], arg2=False)
        select_camera(triggerId=1001, enable=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return Q1_카메라연출02()


class Q1_카메라연출02(state.State):
    def on_enter(self):
        set_timer(timerId='6', seconds=5)
        destroy_monster(spawnIds=[201])
        create_monster(spawnIds=[202], arg2=False)
        set_conversation(type=2, spawnId=11001285, script='$52010005_QD__ACT01__2$', arg4=4)
        set_skip(state=Q1_카메라연출03)

    def on_tick(self) -> state.State:
        if time_expired(timerId='6'):
            return Q1_카메라연출03()

    def on_exit(self):
        remove_cinematic_talk()


class Q1_카메라연출03(state.State):
    def on_enter(self):
        set_timer(timerId='7', seconds=1)
        select_camera(triggerId=1001, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='7'):
            return Q1_마샤르교체02()


class Q1_마샤르교체02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[104])
        create_monster(spawnIds=[103], arg2=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[10002821], questStates=[2]):
            return Q1_퇴장()


class Q1_퇴장(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[103])
        destroy_monster(spawnIds=[202])
        create_monster(spawnIds=[101], arg2=True)


