""" trigger/52010013_qd/main.xml """
from common import *
import state


class idle(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101,102,103])

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[10002797], questStates=[1]):
            return Event_01()


class Event_01(state.State):
    def on_enter(self):
        select_camera(triggerId=8001, enable=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        create_monster(spawnIds=[104])
        set_timer(timerId='3', seconds=3)
        set_conversation(type=2, spawnId=11001217, script='$52010013_QD__MAIN__0$', arg4=3)
        move_npc(spawnId=104, patrolName='MS2PatrolData_1001')

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return Event_02_IDLE()

    def on_exit(self):
        remove_cinematic_talk()


class Event_02_IDLE(state.State):
    def on_tick(self) -> state.State:
        if true():
            return Event_02()


class Event_02(state.State):
    def on_enter(self):
        select_camera(triggerId=8002, enable=True)
        set_conversation(type=2, spawnId=11001292, script='$52010013_QD__MAIN__1$', arg4=5)
        set_skip(state=Event_03_IDLE)
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return Event_03_IDLE()

    def on_exit(self):
        remove_cinematic_talk()


class Event_03_IDLE(state.State):
    def on_tick(self) -> state.State:
        if true():
            return Event_03()


class Event_03(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001285, script='$52010013_QD__MAIN__2$', arg4=4)
        set_skip(state=Event_04_IDLE)
        set_timer(timerId='4', seconds=4)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return Event_04_IDLE()

    def on_exit(self):
        remove_cinematic_talk()


class Event_04_IDLE(state.State):
    def on_tick(self) -> state.State:
        if true():
            return Event_04()


class Event_04(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001292, script='$52010013_QD__MAIN__3$', arg4=4)
        set_timer(timerId='4', seconds=4)
        set_skip(state=Event_05_IDLE)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return Event_05_IDLE()

    def on_exit(self):
        remove_cinematic_talk()


class Event_05_IDLE(state.State):
    def on_tick(self) -> state.State:
        if true():
            return Event_05()


class Event_05(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001292, script='$52010013_QD__MAIN__4$', arg4=4)
        set_timer(timerId='4', seconds=4)
        set_skip(state=Event_06_IDLE)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return Event_06_IDLE()

    def on_exit(self):
        remove_cinematic_talk()


class Event_06_IDLE(state.State):
    def on_tick(self) -> state.State:
        if true():
            return Event_06()


class Event_06(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001285, script='$52010013_QD__MAIN__5$', arg4=5)
        set_timer(timerId='5', seconds=5)
        set_skip(state=Event_07_IDLE)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return Event_07_IDLE()

    def on_exit(self):
        remove_cinematic_talk()


class Event_07_IDLE(state.State):
    def on_tick(self) -> state.State:
        if true():
            return Event_07()


class Event_07(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001292, script='$52010013_QD__MAIN__6$', arg4=4)
        set_timer(timerId='3', seconds=3)
        set_skip(state=Event_08_IDLE)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return Event_08_IDLE()

    def on_exit(self):
        remove_cinematic_talk()


class Event_08_IDLE(state.State):
    def on_tick(self) -> state.State:
        if true():
            return Event_08()


class Event_08(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001285, script='$52010013_QD__MAIN__7$', arg4=4)
        set_timer(timerId='4', seconds=4)
        set_skip(state=Event_09_IDLE)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return Event_09_IDLE()

    def on_exit(self):
        remove_cinematic_talk()


class Event_09_IDLE(state.State):
    def on_tick(self) -> state.State:
        if true():
            return Event_09()


class Event_09(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001292, script='$52010013_QD__MAIN__8$', arg4=3)
        set_timer(timerId='3', seconds=3)
        set_skip(state=Event_10)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return Event_10()

    def on_exit(self):
        remove_cinematic_talk()


class Event_10(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001292, script='$52010013_QD__MAIN__9$', arg4=4)
        set_timer(timerId='4', seconds=4)
        set_skip(state=End)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return End()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=7)
        select_camera(triggerId=8001, enable=False)
        select_camera(triggerId=8002, enable=False)


class End(state.State):
    def on_enter(self):
        set_achievement(triggerId=701, type='trigger', achieve='DragonMika')
        move_user(mapId=2010002, portalId=13, boxId=701)


