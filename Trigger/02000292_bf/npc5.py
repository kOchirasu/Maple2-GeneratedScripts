""" trigger/02000292_bf/npc5.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000624], state=1)
        destroy_monster(spawnIds=[1105])

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000624], arg2=0):
            return NPC대사()


class NPC대사(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000624], state=2)
        create_monster(spawnIds=[1105])
        set_conversation(type=1, spawnId=1105, script='$02000292_BF__NPC5__0$', arg4=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return NPC이동()


class NPC이동(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=1105, script='$02000292_BF__NPC5__1$', arg4=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return NPC소멸()


class NPC소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1105])


