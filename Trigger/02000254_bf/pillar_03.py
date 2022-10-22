""" trigger/02000254_bf/pillar_03.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000442], state=0)
        set_skill(triggerIds=[703], isEnable=False)
        set_effect(triggerIds=[446], visible=False)
        set_effect(triggerIds=[447], visible=False)
        set_effect(triggerIds=[462], visible=False)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=907, spawnIds=[105]):
            return 반응대기()


class 반응대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000442], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000442], arg2=0):
            return 스턴()
        if not npc_detected(boxId=907, spawnIds=[105]):
            return 시작대기중()


class 스턴(state.State):
    def on_enter(self):
        set_effect(triggerIds=[446], visible=True)
        set_effect(triggerIds=[447], visible=True)
        set_effect(triggerIds=[462], visible=True)
        set_skill(triggerIds=[703], isEnable=True)
        set_timer(timerId='1', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스턴2()


class 스턴2(state.State):
    def on_enter(self):
        set_skill(triggerIds=[703], isEnable=False)
        set_timer(timerId='1', seconds=10)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 시작대기중()


