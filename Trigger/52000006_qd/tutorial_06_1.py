""" trigger/52000006_qd/tutorial_06_1.xml """
from common import *
import state


class 엔터대기중(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[100]):
            return 연출세팅()


class 연출세팅(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return PC대사1()


class PC대사1(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=2)
        set_cinematic_ui(type=3, script='$52000006_QD__TUTORIAL_06_1__0$')

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 양등장()


class 양등장(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=2)
        select_camera(triggerId=301, enable=True)
        create_monster(spawnIds=[201], arg2=False)
        set_cinematic_ui(type=3, script='$52000006_QD__TUTORIAL_06_1__1$')

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 양이동()


class 양이동(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=4)
        move_npc(spawnId=201, patrolName='PatrolData_Sheep_01')
        set_cinematic_ui(type=3, script='$52000006_QD__TUTORIAL_06_1__2$')

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 연출끝()


class 연출끝(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[201])
        select_camera(triggerId=302, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


