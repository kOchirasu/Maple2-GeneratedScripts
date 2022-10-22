""" trigger/02000254_bf/pillar_01.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000440], state=0)
        set_skill(triggerIds=[701], isEnable=False)
        set_effect(triggerIds=[440], visible=False)
        set_effect(triggerIds=[441], visible=False)
        set_effect(triggerIds=[442], visible=False)
        set_effect(triggerIds=[443], visible=False)
        set_effect(triggerIds=[460], visible=False)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=905, spawnIds=[103]):
            return 반응대기()


class 반응대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000440], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000440], arg2=0):
            return 스턴()
        if not npc_detected(boxId=905, spawnIds=[103]):
            return 시작대기중()


class 스턴(state.State):
    def on_enter(self):
        set_effect(triggerIds=[440], visible=True)
        set_effect(triggerIds=[441], visible=True)
        set_effect(triggerIds=[442], visible=True)
        set_effect(triggerIds=[443], visible=True)
        set_effect(triggerIds=[460], visible=True)
        set_skill(triggerIds=[701], isEnable=True)
        set_timer(timerId='1', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스턴2()


class 스턴2(state.State):
    def on_enter(self):
        set_skill(triggerIds=[701], isEnable=False)
        set_timer(timerId='1', seconds=10)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 시작대기중()


