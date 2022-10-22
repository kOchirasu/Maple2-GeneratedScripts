""" trigger/52000004_qd/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=False)
        set_effect(triggerIds=[602], visible=False)
        destroy_monster(spawnIds=[2001])
        destroy_monster(spawnIds=[2099])
        destroy_monster(spawnIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016])
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[199]):
            return 던전시작()
        if not user_detected(boxIds=[199]):
            return 종료()


class 던전시작(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 차목표1()
        if not user_detected(boxIds=[199]):
            return 종료()


class 차목표1(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=True)
        set_timer(timerId='2', seconds=2)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3, script='$52000004_QD__MAIN__0$')
        set_skip(state=연출종료)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 카메라이동()


class 카메라이동(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)
        select_camera(triggerId=301, enable=True)
        set_skip(state=연출종료)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        set_effect(triggerIds=[602], visible=True)
        select_camera_path(pathIds=[301], returnView=True)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[100]):
            return 피자들기()
        if not user_detected(boxIds=[199]):
            return 종료()


class 피자들기(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)
        show_guide_summary(entityId=25200401, textId=25200401)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 엘리트스폰대기()
        if not user_detected(boxIds=[199]):
            return 종료()

    def on_exit(self):
        hide_guide_summary(entityId=25200401)


class 엘리트스폰대기(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016], arg2=False)
        set_effect(triggerIds=[602], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 엘리트스폰()
        if not user_detected(boxIds=[199]):
            return 종료()


class 엘리트스폰(state.State):
    def on_enter(self):
        show_guide_summary(entityId=25200402, textId=25200402)
        set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009], visible=True, arg3=0, arg4=0, arg5=2)
        create_monster(spawnIds=[2001], arg2=False)
        set_conversation(type=1, spawnId=2001, script='$52000004_QD__MAIN__3$', arg4=3)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 벽해제()
        if not user_detected(boxIds=[199]):
            return 종료()

    def on_exit(self):
        hide_guide_summary(entityId=25200402)


class 벽해제(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009], visible=False, arg3=0, arg4=0, arg5=2)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[102]):
            return NPC등장()
        if not user_detected(boxIds=[199]):
            return 종료()


class NPC등장(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=False)
        create_monster(spawnIds=[2099], arg2=False)
        set_conversation(type=1, spawnId=2099, script='$52000004_QD__MAIN__4$', arg4=3)
        move_npc(spawnId=2099, patrolName='MS2PatrolData_2099')
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[199]):
            return 종료()
        if time_expired(timerId='5'):
            return 미션성공()


class 미션성공(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[199], questIds=[10001852], questStates=[2]):
            set_event_ui(type=7, arg2='$52000004_QD__MAIN__5$', arg3='3000', arg4='0')
            return 포털생성()
        if quest_user_detected(boxIds=[199], questIds=[10001851], questStates=[2]):
            set_event_ui(type=7, arg2='$52000004_QD__MAIN__6$', arg3='3000', arg4='0')
            return 포털생성()
        if time_expired(timerId='3'):
            return 포털생성()
        if not user_detected(boxIds=[199]):
            return 종료()


class 포털생성(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)
            show_guide_summary(entityId=25200403, textId=25200403)
            return 종료대기()
        if not user_detected(boxIds=[199]):
            return 종료()


class 종료대기(state.State):
    def on_enter(self):
        set_timer(timerId='30', seconds=30)

    def on_tick(self) -> state.State:
        if time_expired(timerId='30'):
            move_user(mapId=2000166, portalId=30, boxId=199)
            return 종료()
        if not user_detected(boxIds=[199]):
            return 종료()

    def on_exit(self):
        hide_guide_summary(entityId=25200403)


class 종료(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[2001])
        destroy_monster(spawnIds=[2099])
        destroy_monster(spawnIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016])
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if true():
            return 대기()


