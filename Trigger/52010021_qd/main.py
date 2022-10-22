""" trigger/52010021_qd/main.xml """
from common import *
import state


class idle(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7001], visible=False)
        create_monster(spawnIds=[101,102,103])

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[40002540], questStates=[3]):
            return Event_01_Idle()


class Event_01_Idle(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_user(mapId=52010021, portalId=3, boxId=701)
        set_timer(timerId='2', seconds=2)
        set_effect(triggerIds=[7001], visible=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return Event_01()


class Event_01(state.State):
    def on_enter(self):
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)
        create_monster(spawnIds=[104])
        move_npc(spawnId=104, patrolName='MS2PatrolData_2001')
        move_npc(spawnId=101, patrolName='MS2PatrolData_2002')
        move_npc(spawnId=102, patrolName='MS2PatrolData_2004')
        move_npc(spawnId=103, patrolName='MS2PatrolData_2003')
        select_camera(triggerId=8001, enable=True)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return Event_05()

    def on_exit(self):
        select_camera(triggerId=8001, enable=True)


class Event_05(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001285, script='$52010021_QD__MAIN__0$', arg4=4)
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return Ending()


class Ending(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8001,8002], returnView=False) # 사이드뷰 카메라
        move_npc(spawnId=101, patrolName='MS2PatrolData_2012')
        move_npc(spawnId=102, patrolName='MS2PatrolData_2014')
        move_npc(spawnId=103, patrolName='MS2PatrolData_2013')
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return out()

    def on_exit(self):
        set_cinematic_ui(type=4)


class out(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return end()

    def on_exit(self):
        set_cinematic_ui(type=9, script='$52010021_QD__MAIN__1$', arg3=True)


class end(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return real_end2()

    def on_exit(self):
        set_cinematic_ui(type=9, script='$52010021_QD__MAIN__2$', arg3=True)
        play_system_sound_in_box(sound='System_Laugh_01')


class real_end2(state.State):
    def on_enter(self):
        set_timer(timerId='4', seconds=4)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return real_end3()

    def on_exit(self):
        set_cinematic_ui(type=9, script='$52010021_QD__MAIN__3$', arg3=True)


class real_end3(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return real_end4()

    def on_exit(self):
        play_system_sound_in_box(sound='System_Burp_01')


class real_end4(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return real_end()


class real_end(state.State):
    def on_enter(self):
        set_achievement(triggerId=701, type='trigger', achieve='mikaEpilogueEnd')
        move_user(mapId=2010002, portalId=1, boxId=701)


