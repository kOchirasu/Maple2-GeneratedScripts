""" trigger/02000292_bf/npc6.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000625], state=1)
        destroy_monster(spawnIds=[1103])

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000625], arg2=0):
            return NPC대사()


class NPC대사(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000625], state=2)
        create_monster(spawnIds=[1103])
        set_conversation(type=1, spawnId=1103, script='$02000292_BF__NPC6__0$', arg4=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return NPC이동()


class NPC이동(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=1103, script='$02000292_BF__NPC6__1$', arg4=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return NPC소멸()


class NPC소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1103])


