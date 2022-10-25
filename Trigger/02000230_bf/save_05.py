""" trigger/02000230_bf/save_05.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[500], animationEffect=False)
        self.set_actor(triggerId=501, visible=True, initialSequence='Emotion_Failure_Idle_A')
        self.set_actor(triggerId=50501, visible=True, initialSequence='Attack_Idle_A')
        self.set_actor(triggerId=50502, visible=True, initialSequence='Attack_02_A')
        self.set_actor(triggerId=50503, visible=True, initialSequence='Attack_02_A')
        self.set_actor(triggerId=50504, visible=True, initialSequence='Attack_Idle_A')
        self.set_actor(triggerId=50505, visible=True, initialSequence='Attack_02_A')

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 주민구출(self.ctx)


class 주민구출(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000357], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000357], stateValue=0):
            return 문열림(self.ctx)


class 문열림(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='10', seconds=3)
        self.set_conversation(type=1, spawnId=500, script='$02000230_BF__SAVE_05__0$', arg4=2, arg5=0)
        self.set_actor(triggerId=50501, visible=False, initialSequence='Attack_Idle_A')
        self.create_monster(spawnIds=[50511], animationEffect=True)
        self.set_actor(triggerId=50502, visible=False, initialSequence='Attack_02_A')
        self.create_monster(spawnIds=[50512], animationEffect=True)
        self.set_actor(triggerId=50503, visible=False, initialSequence='Attack_02_A')
        self.create_monster(spawnIds=[50513], animationEffect=True)
        self.set_actor(triggerId=50504, visible=False, initialSequence='Attack_Idle_A')
        self.create_monster(spawnIds=[50514], animationEffect=True)
        self.set_actor(triggerId=50505, visible=False, initialSequence='Attack_02_A')
        self.create_monster(spawnIds=[50515], animationEffect=True)
        self.set_conversation(type=1, spawnId=50511, script='$02000230_BF__SAVE_05__1$', arg4=2, arg5=1)
        self.set_conversation(type=1, spawnId=50513, script='$02000230_BF__SAVE_05__2$', arg4=2, arg5=2)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='10'):
            return 도망과공격(self.ctx)


class 도망과공격(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[500])
        self.set_actor(triggerId=501, visible=False, initialSequence='Emotion_Failure_Idle_A')
        self.create_monster(spawnIds=[511], animationEffect=False)
        self.set_conversation(type=1, spawnId=511, script='$02000230_BF__SAVE_05__3$', arg4=2, arg5=0)
        self.move_npc(spawnId=511, patrolName='MS2PatrolData_511_11000689')
        self.set_conversation(type=1, spawnId=511, script='$02000230_BF__SAVE_05__4$', arg4=2, arg5=2)

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=90511, spawnIds=[511]):
            return 도망완료(self.ctx)


class 도망완료(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[511])

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[50511,50512,50513,50514,50515]):
            return 트리거초기화(self.ctx)
        if not self.monster_in_combat(boxIds=[50511,50512,50513,50514,50515]):
            return 트리거초기화(self.ctx)


class 트리거초기화(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='11', seconds=10)
        self.destroy_monster(spawnIds=[50511,50512,50513,50514,50515])

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='11'):
            return 대기(self.ctx)


initial_state = 대기
