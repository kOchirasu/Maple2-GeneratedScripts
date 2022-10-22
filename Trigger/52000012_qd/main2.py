""" trigger/52000012_qd/main2.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_actor(triggerId=10001, visible=True, initialSequence='Closed')
        set_actor(triggerId=10002, visible=True, initialSequence='Closed')
        set_mesh(triggerIds=[10011], visible=True)
        set_mesh(triggerIds=[10012], visible=True)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[10002610], questStates=[2]):
            return 문열림1()
        if quest_user_detected(boxIds=[9000], questIds=[10002610], questStates=[3]):
            return 문열림1()

    def on_exit(self):
        create_monster(spawnIds=[2000], arg2=False)
        destroy_monster(spawnIds=[5000])
        destroy_monster(spawnIds=[101])
        destroy_monster(spawnIds=[102])
        destroy_monster(spawnIds=[103])


class 문열림1(state.State):
    def on_enter(self):
        set_timer(timerId='19', seconds=1)
        set_actor(triggerId=10001, visible=True, initialSequence='Opened')
        set_mesh(triggerIds=[10011], visible=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='19'):
            return 문열림2()


class 문열림2(state.State):
    def on_enter(self):
        set_actor(triggerId=10002, visible=True, initialSequence='Opened')
        set_mesh(triggerIds=[10012], visible=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9001], questIds=[10002611], questStates=[2]):
            return 포털생성()
        if quest_user_detected(boxIds=[9001], questIds=[10002611], questStates=[3]):
            return 포털생성()


class 포털생성(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[9001]):
            return 종료()


class 종료(state.State):
    def on_tick(self) -> state.State:
        if true():
            return 대기()


