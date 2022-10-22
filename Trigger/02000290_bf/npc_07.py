""" trigger/02000290_bf/npc_07.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6001], visible=False) # 요미공주음성01
        set_effect(triggerIds=[6002], visible=False) # 요미공주음성02
        set_interact_object(triggerIds=[10000464], state=1)
        set_actor(triggerId=9007, visible=True, initialSequence='Down_Idle_A')

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000464], arg2=0):
            return NPC대사()

    def on_exit(self):
        set_actor(triggerId=9007, visible=False, initialSequence='Down_Idle_A')
        set_user_value(triggerId=9999995, key='dungeonclear', value=1)


class NPC대사(state.State):
    def on_enter(self):
        create_monster(spawnIds=[907])
        set_timer(timerId='2', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            set_effect(triggerIds=[6001], visible=True)
            set_conversation(type=1, spawnId=907, script='$02000290_BF__NPC_07__0$', arg4=3)
            return NPC이동()


class NPC이동(state.State):
    def on_enter(self):
        set_timer(timerId='4', seconds=4)
        move_npc(spawnId=907, patrolName='MS2PatrolData907')

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            set_effect(triggerIds=[6002], visible=True)
            set_conversation(type=1, spawnId=907, script='$02000290_BF__NPC_07__1$', arg4=3)
            return NPC소멸()


class NPC소멸(state.State):
    pass


