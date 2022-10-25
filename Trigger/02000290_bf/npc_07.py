""" trigger/02000290_bf/npc_07.xml """
import common


class 시작대기중(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6001], visible=False) # 요미공주음성01
        self.set_effect(triggerIds=[6002], visible=False) # 요미공주음성02
        self.set_interact_object(triggerIds=[10000464], state=1)
        self.set_actor(triggerId=9007, visible=True, initialSequence='Down_Idle_A')

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000464], stateValue=0):
            return NPC대사(self.ctx)

    def on_exit(self):
        self.set_actor(triggerId=9007, visible=False, initialSequence='Down_Idle_A')
        self.set_user_value(triggerId=9999995, key='dungeonclear', value=1)


class NPC대사(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[907])
        self.set_timer(timerId='2', seconds=2)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='2'):
            self.set_effect(triggerIds=[6001], visible=True)
            self.set_conversation(type=1, spawnId=907, script='$02000290_BF__NPC_07__0$', arg4=3)
            return NPC이동(self.ctx)


class NPC이동(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='4', seconds=4)
        self.move_npc(spawnId=907, patrolName='MS2PatrolData907')

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='4'):
            self.set_effect(triggerIds=[6002], visible=True)
            self.set_conversation(type=1, spawnId=907, script='$02000290_BF__NPC_07__1$', arg4=3)
            return NPC소멸(self.ctx)


class NPC소멸(common.Trigger):
    pass


initial_state = 시작대기중
