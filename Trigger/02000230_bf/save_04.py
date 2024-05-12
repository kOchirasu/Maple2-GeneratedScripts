""" trigger/02000230_bf/save_04.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[400], animationEffect=False)
        self.set_actor(triggerId=401, visible=True, initialSequence='Emotion_Failure_Idle_A')
        self.set_actor(triggerId=40401, visible=True, initialSequence='Attack_Idle_A')
        self.set_actor(triggerId=40402, visible=True, initialSequence='Attack_02_A')
        self.set_actor(triggerId=40403, visible=True, initialSequence='Attack_02_A')
        self.set_actor(triggerId=40404, visible=True, initialSequence='Attack_Idle_A')
        self.set_actor(triggerId=40405, visible=True, initialSequence='Attack_02_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 주민구출(self.ctx)


class 주민구출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000356], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000356], stateValue=0):
            return 문열림(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='10', seconds=3)
        self.set_conversation(type=1, spawnId=400, script='$02000230_BF__SAVE_04__0$', arg4=2, arg5=0)
        self.set_actor(triggerId=40401, visible=False, initialSequence='Attack_Idle_A')
        self.create_monster(spawnIds=[40411], animationEffect=True)
        self.set_actor(triggerId=40402, visible=False, initialSequence='Attack_02_A')
        self.create_monster(spawnIds=[40412], animationEffect=True)
        self.set_actor(triggerId=40403, visible=False, initialSequence='Attack_02_A')
        self.create_monster(spawnIds=[40413], animationEffect=True)
        self.set_actor(triggerId=40404, visible=False, initialSequence='Attack_Idle_A')
        self.create_monster(spawnIds=[40414], animationEffect=True)
        self.set_actor(triggerId=40405, visible=False, initialSequence='Attack_02_A')
        self.create_monster(spawnIds=[40415], animationEffect=True)
        self.set_conversation(type=1, spawnId=40411, script='$02000230_BF__SAVE_04__1$', arg4=2, arg5=1)
        self.set_conversation(type=1, spawnId=40413, script='$02000230_BF__SAVE_04__2$', arg4=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='10'):
            return 도망과공격(self.ctx)


class 도망과공격(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[400])
        self.set_actor(triggerId=401, visible=False, initialSequence='Emotion_Failure_Idle_A')
        self.create_monster(spawnIds=[411], animationEffect=False)
        self.set_conversation(type=1, spawnId=411, script='$02000230_BF__SAVE_04__3$', arg4=2, arg5=0)
        self.move_npc(spawnId=411, patrolName='MS2PatrolData_411_11000687')
        self.set_conversation(type=1, spawnId=411, script='$02000230_BF__SAVE_04__4$', arg4=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=90411, spawnIds=[411]):
            return 도망완료(self.ctx)


class 도망완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[411])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[40411,40412,40413,40414,40415]):
            return 트리거초기화(self.ctx)
        if not self.monster_in_combat(boxIds=[40411,40412,40413,40414,40415]):
            return 트리거초기화(self.ctx)


class 트리거초기화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='11', seconds=10)
        self.destroy_monster(spawnIds=[40411,40412,40413,40414,40415])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='11'):
            return 대기(self.ctx)


initial_state = 대기
