""" trigger/02000313_bf/regionskill01.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=11, spawnIds=[2099]):
            return 스킬작동()


class 스킬작동(state.State):
    def on_enter(self):
        set_skill(triggerIds=[302], isEnable=True)
        set_skill(triggerIds=[303], isEnable=True)

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=11, spawnIds=[2099]):
            return 트리거초기화()


class 트리거초기화(state.State):
    def on_enter(self):
        set_skill(triggerIds=[302], isEnable=False)
        set_skill(triggerIds=[303], isEnable=False)
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 시작대기중()


