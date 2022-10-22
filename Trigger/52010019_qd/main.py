""" trigger/52010019_qd/main.xml """
from common import *
import state


class idle(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101,102,103])


class Event_01(state.State):
    def on_enter(self):
        select_camera(triggerId=8001, enable=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_timer(timerId='3', seconds=3)
        set_conversation(type=2, spawnId=11001292, script='$52010014_QD__MAIN__0$', arg4=3)
        set_skip(state=Event_02)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return Event_02()

    def on_exit(self):
        remove_cinematic_talk()


class Event_02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001285, script='$52010014_QD__MAIN__1$', arg4=3)
        set_skip(state=Event_03)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return Event_03()

    def on_exit(self):
        remove_cinematic_talk()


class Event_03(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001285, script='$52010014_QD__MAIN__2$', arg4=3)
        set_skip(state=Event_04)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return Event_04()

    def on_exit(self):
        remove_cinematic_talk()


class Event_04(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001292, script='$52010014_QD__MAIN__3$', arg4=3)
        set_timer(timerId='3', seconds=3)
        set_skip(state=Event_05)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return Event_05()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=7)


class Event_05(state.State):
    def on_enter(self):
        select_camera(triggerId=8001, enable=False)


