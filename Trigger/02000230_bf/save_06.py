""" trigger/02000230_bf/save_06.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[600], animationEffect=False)
        self.set_actor(triggerId=601, visible=True, initialSequence='Emotion_Failure_Idle_A')
        self.set_actor(triggerId=60601, visible=True, initialSequence='Attack_Idle_A')
        self.set_actor(triggerId=60602, visible=True, initialSequence='Attack_02_A')
        self.set_actor(triggerId=60603, visible=True, initialSequence='Attack_02_A')
        self.set_actor(triggerId=60604, visible=True, initialSequence='Attack_Idle_A')
        self.set_actor(triggerId=60605, visible=True, initialSequence='Attack_02_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 주민구출(self.ctx)


class 주민구출(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000358], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000358], stateValue=0):
            return 문열림(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='10', seconds=3)
        self.set_conversation(type=1, spawnId=600, script='$02000230_BF__SAVE_06__0$', arg4=2, arg5=0)
        self.set_actor(triggerId=60601, visible=False, initialSequence='Attack_Idle_A')
        self.create_monster(spawnIds=[60611], animationEffect=True)
        self.set_actor(triggerId=60602, visible=False, initialSequence='Attack_02_A')
        self.create_monster(spawnIds=[60612], animationEffect=True)
        self.set_actor(triggerId=60603, visible=False, initialSequence='Attack_02_A')
        self.create_monster(spawnIds=[60613], animationEffect=True)
        self.set_actor(triggerId=60604, visible=False, initialSequence='Attack_Idle_A')
        self.create_monster(spawnIds=[60614], animationEffect=True)
        self.set_actor(triggerId=60605, visible=False, initialSequence='Attack_02_A')
        self.create_monster(spawnIds=[60615], animationEffect=True)
        self.set_conversation(type=1, spawnId=60611, script='$02000230_BF__SAVE_06__1$', arg4=2, arg5=1)
        self.set_conversation(type=1, spawnId=60613, script='$02000230_BF__SAVE_06__2$', arg4=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='10'):
            return 도망과공격(self.ctx)


class 도망과공격(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[600])
        self.set_actor(triggerId=601, visible=False, initialSequence='Emotion_Failure_Idle_A')
        self.create_monster(spawnIds=[611], animationEffect=False)
        self.set_conversation(type=1, spawnId=611, script='$02000230_BF__SAVE_06__3$', arg4=2, arg5=0)
        self.move_npc(spawnId=611, patrolName='MS2PatrolData_611_11000688')
        self.set_conversation(type=1, spawnId=611, script='$02000230_BF__SAVE_06__4$', arg4=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=90611, spawnIds=[611]):
            return 도망완료(self.ctx)


class 도망완료(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[611])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[60611,60612,60613,60614,60615]):
            return 트리거초기화(self.ctx)
        if not self.monster_in_combat(boxIds=[60611,60612,60613,60614,60615]):
            return 트리거초기화(self.ctx)


class 트리거초기화(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='11', seconds=10)
        self.destroy_monster(spawnIds=[60611,60612,60613,60614,60615])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='11'):
            return 대기(self.ctx)


initial_state = 대기
