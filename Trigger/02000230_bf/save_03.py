""" trigger/02000230_bf/save_03.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[300], animationEffect=False)
        self.set_actor(triggerId=301, visible=True, initialSequence='Emotion_Failure_Idle_A')
        self.set_actor(triggerId=30301, visible=True, initialSequence='Attack_Idle_A')
        self.set_actor(triggerId=30302, visible=True, initialSequence='Attack_02_A')
        self.set_actor(triggerId=30303, visible=True, initialSequence='Attack_02_A')
        self.set_actor(triggerId=30304, visible=True, initialSequence='Attack_Idle_A')
        self.set_actor(triggerId=30305, visible=True, initialSequence='Attack_02_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 주민구출(self.ctx)


class 주민구출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000355], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000355], stateValue=0):
            return 문열림(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='10', seconds=3)
        self.set_conversation(type=1, spawnId=300, script='$02000230_BF__SAVE_03__0$', arg4=2, arg5=0)
        self.set_actor(triggerId=30301, visible=False, initialSequence='Attack_Idle_A')
        self.create_monster(spawnIds=[30311], animationEffect=True)
        self.set_actor(triggerId=30302, visible=False, initialSequence='Attack_02_A')
        self.create_monster(spawnIds=[30312], animationEffect=True)
        self.set_actor(triggerId=30303, visible=False, initialSequence='Attack_02_A')
        self.create_monster(spawnIds=[30313], animationEffect=True)
        self.set_actor(triggerId=30304, visible=False, initialSequence='Attack_Idle_A')
        self.create_monster(spawnIds=[30314], animationEffect=True)
        self.set_actor(triggerId=30305, visible=False, initialSequence='Attack_02_A')
        self.create_monster(spawnIds=[30315], animationEffect=True)
        self.set_conversation(type=1, spawnId=30311, script='$02000230_BF__SAVE_03__1$', arg4=2, arg5=1)
        self.set_conversation(type=1, spawnId=30313, script='$02000230_BF__SAVE_03__2$', arg4=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='10'):
            return 도망과공격(self.ctx)


class 도망과공격(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[300])
        self.set_actor(triggerId=301, visible=False, initialSequence='Emotion_Failure_Idle_A')
        self.create_monster(spawnIds=[311], animationEffect=False)
        self.set_conversation(type=1, spawnId=311, script='$02000230_BF__SAVE_03__3$', arg4=2, arg5=0)
        self.move_npc(spawnId=311, patrolName='MS2PatrolData_311_11000689')
        self.set_conversation(type=1, spawnId=311, script='$02000230_BF__SAVE_03__4$', arg4=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=90311, spawnIds=[311]):
            return 도망완료(self.ctx)


class 도망완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[311])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[30311,30312,30313,30314,30315]):
            return 트리거초기화(self.ctx)
        if not self.monster_in_combat(boxIds=[30311,30312,30313,30314,30315]):
            return 트리거초기화(self.ctx)


class 트리거초기화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='11', seconds=10)
        self.destroy_monster(spawnIds=[30311,30312,30313,30314,30315])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='11'):
            return 대기(self.ctx)


initial_state = 대기
