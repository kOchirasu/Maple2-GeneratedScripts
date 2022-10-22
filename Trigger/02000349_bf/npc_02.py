""" trigger/02000349_bf/npc_02.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        create_monster(spawnIds=[902])

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000807], arg2=0):
            return NPC대사()


class NPC대사(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2)
        set_conversation(type=1, spawnId=902, script='$02000349_BF__NPC_02__0$', arg4=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return NPC이동()


class NPC이동(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)
        move_npc(spawnId=902, patrolName='MS2PatrolData902')

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return NPC소멸()


class NPC소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[902])


