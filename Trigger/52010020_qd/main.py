""" trigger/52010020_qd/main.xml """
from common import *
import state


class idle(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7001], visible=False)
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=4)
        create_monster(spawnIds=[101,102])

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[701]):
            return Event_Ready()


class Event_Ready(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return Event_01()


class Event_01(state.State):
    def on_enter(self):
        move_npc(spawnId=102, patrolName='MS2PatrolData_2001')
        set_conversation(type=1, spawnId=102, script='$52010020_QD__MAIN__0$', arg4=5)
        set_timer(timerId='2', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return Event_02()


class Event_02(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_2002')
        set_conversation(type=1, spawnId=101, script='$52010020_QD__MAIN__1$', arg4=5)
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return Event_03()


class Event_03(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7001], visible=True)
        move_npc(spawnId=101, patrolName='MS2PatrolData_2004')
        move_npc(spawnId=102, patrolName='MS2PatrolData_2001')
        move_user(mapId=52010020, portalId=1, boxId=701)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)
        create_monster(spawnIds=[103])
        move_npc(spawnId=103, patrolName='MS2PatrolData_2003')
        select_camera_path(pathIds=[8001,8002], returnView=False) # 사이드뷰 카메라
        set_timer(timerId='4', seconds=4)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return Event_04()


class Event_04(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001502, script='$52010020_QD__MAIN__2$', arg4=4)
        move_npc(spawnId=102, patrolName='MS2PatrolData_2001')
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return Event_05()

    def on_exit(self):
        set_cinematic_ui(type=4)


class Event_05(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return end()

    def on_exit(self):
        set_achievement(triggerId=701, type='trigger', achieve='luanDialogue')
        select_camera(triggerId=8001, enable=False)
        move_user(mapId=52010019, portalId=2, boxId=701)


class end(state.State):
    pass


