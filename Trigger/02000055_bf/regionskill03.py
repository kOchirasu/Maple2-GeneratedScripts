""" trigger/02000055_bf/regionskill03.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=13, spawnIds=[91]):
            return 스킬작동()


class 스킬작동(state.State):
    def on_enter(self):
        set_skill(triggerIds=[301], isEnable=True)
        set_skill(triggerIds=[302], isEnable=True)

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=13, spawnIds=[91]):
            return 트리거초기화()


class 트리거초기화(state.State):
    def on_enter(self):
        set_skill(triggerIds=[301], isEnable=False)
        set_skill(triggerIds=[302], isEnable=False)
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 시작대기중()


