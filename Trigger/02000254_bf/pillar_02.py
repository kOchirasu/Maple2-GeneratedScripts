""" trigger/02000254_bf/pillar_02.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000441], state=0)
        set_skill(triggerIds=[702], isEnable=False)
        set_effect(triggerIds=[444], visible=False)
        set_effect(triggerIds=[445], visible=False)
        set_effect(triggerIds=[461], visible=False)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=906, spawnIds=[104]):
            return 반응대기()


class 반응대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000441], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000441], arg2=0):
            return 스턴()
        if not npc_detected(boxId=906, spawnIds=[104]):
            return 시작대기중()


class 스턴(state.State):
    def on_enter(self):
        set_effect(triggerIds=[444], visible=True)
        set_effect(triggerIds=[445], visible=True)
        set_effect(triggerIds=[461], visible=True)
        set_skill(triggerIds=[702], isEnable=True)
        set_timer(timerId='1', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스턴2()


class 스턴2(state.State):
    def on_enter(self):
        set_skill(triggerIds=[702], isEnable=False)
        set_timer(timerId='1', seconds=10)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 시작대기중()


