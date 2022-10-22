""" trigger/52000013_qd/patrol.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_actor(triggerId=6000, visible=False, initialSequence='Idle_A')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return 어린벨라등장()


class 어린벨라등장(state.State):
    def on_enter(self):
        set_timer(timerId='10', seconds=1)
        create_monster(spawnIds=[5000], arg2=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='10'):
            return 어린벨라패트롤01()


class 어린벨라패트롤01(state.State):
    def on_enter(self):
        move_npc(spawnId=5000, patrolName='MS2PatrolData_1001')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=9001, spawnIds=[5000]):
            return 어린벨라대화01()


class 어린벨라대화01(state.State):
    def on_enter(self):
        set_timer(timerId='11', seconds=3)
        set_conversation(type=1, spawnId=5000, script='$52000013_QD__MAIN__1$', arg4=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11'):
            return 어린벨라패트롤02()


class 어린벨라패트롤02(state.State):
    def on_enter(self):
        move_npc(spawnId=5000, patrolName='MS2PatrolData_1002')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=9002, spawnIds=[5000]):
            return 어린벨라대화02()


class 어린벨라대화02(state.State):
    def on_enter(self):
        set_timer(timerId='12', seconds=3)
        set_conversation(type=1, spawnId=5000, script='$52000013_QD__MAIN__2$', arg4=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='12'):
            return 어린벨라패트롤03()


class 어린벨라패트롤03(state.State):
    def on_enter(self):
        move_npc(spawnId=5000, patrolName='MS2PatrolData_1003')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=9003, spawnIds=[5000]):
            return 카메라연출01()


class 카메라연출01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_timer(timerId='12', seconds=6)
        select_camera_path(pathIds=[901], returnView=False)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=9004, spawnIds=[5000]):
            return 카메라연출02()


class 카메라연출02(state.State):
    def on_enter(self):
        set_timer(timerId='13', seconds=12)
        set_actor(triggerId=6000, visible=True, initialSequence='Idle_A')
        select_camera_path(pathIds=[902,903], returnView=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='13'):
            return 화면끄기()


class 화면끄기(state.State):
    def on_enter(self):
        set_timer(timerId='14', seconds=2)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if time_expired(timerId='14'):
            return 어린벨라소멸()


class 어린벨라소멸(state.State):
    def on_enter(self):
        set_timer(timerId='15', seconds=1)
        destroy_monster(spawnIds=[5000])
        set_actor(triggerId=6000, visible=False, initialSequence='Idle_A')
        create_monster(spawnIds=[6001], arg2=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='15'):
            return 벨라연출01()


class 벨라연출01(state.State):
    def on_enter(self):
        set_timer(timerId='16', seconds=8)
        set_cinematic_ui(type=4)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_npc(spawnId=6001, patrolName='MS2PatrolData_2001')
        select_camera_path(pathIds=[904,905], returnView=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='16'):
            return 벨라연출종료()


class 벨라연출종료(state.State):
    def on_enter(self):
        set_timer(timerId='17', seconds=8)
        select_camera(triggerId=905, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='17'):
            return 이동딜레이()


class 이동딜레이(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[10000], questIds=[10002611], questStates=[3]):
            return 강제이동()


class 강제이동(state.State):
    def on_enter(self):
        set_timer(timerId='19', seconds=10)
        move_user(mapId=3009017, portalId=50)

    def on_tick(self) -> state.State:
        if time_expired(timerId='19'):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_timer(timerId='20', seconds=10)
        destroy_monster(spawnIds=[6001])

    def on_tick(self) -> state.State:
        if time_expired(timerId='20'):
            return 대기()


