""" trigger/02010052_bf/torchlight_03.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=20499, visible=False, initialSequence='Closed')
        self.set_actor(triggerId=20501, visible=True, initialSequence='Closed') # 얼어붙은 문
        self.set_mesh(triggerIds=[20500], visible=True, arg3=1, delay=1, scale=1) # 철문
        self.set_effect(triggerIds=[7002], visible=False) # 횃불에 불이 붙는 이펙트
        self.set_effect(triggerIds=[7003], visible=False) # 횃불에 불이 붙는 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[102]):
            return burn_state_01(self.ctx)
        if self.monster_dead(boxIds=[103]):
            return burn_state_02(self.ctx)

    def on_exit(self):
        self.set_effect(triggerIds=[71001], visible=True)
        self.set_effect(triggerIds=[71002], visible=True)
        self.set_effect(triggerIds=[71003], visible=True)
        self.set_effect(triggerIds=[71004], visible=True)
        self.set_effect(triggerIds=[71005], visible=True)
        self.set_actor(triggerId=8001, visible=False, initialSequence='Dmg_A')
        self.set_actor(triggerId=8002, visible=False, initialSequence='Dmg_A')
        self.set_actor(triggerId=8003, visible=False, initialSequence='Dmg_A')
        self.set_actor(triggerId=8004, visible=False, initialSequence='Dmg_A')
        self.set_actor(triggerId=8005, visible=False, initialSequence='Dmg_A')
        self.create_monster(spawnIds=[301,302,303,304,305], animationEffect=False) # 기본 배치 될 몬스터 등장
        self.set_conversation(type=1, spawnId=993, script='$02010052_BF__TORCHLIGHT_03__0$', arg4=3) # 카나 말풍선 대사


class burn_state_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7002], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[103]):
            return burn_state_complete(self.ctx)

    def on_exit(self):
        self.set_effect(triggerIds=[7003], visible=True)


class burn_state_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7003], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[102]):
            return burn_state_complete(self.ctx)

    def on_exit(self):
        self.set_effect(triggerIds=[7002], visible=True)


class burn_state_complete(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7503], visible=True) # 얼음 녹는 소리
        self.set_mesh(triggerIds=[6021,6022,6023,6024,6025,6026,6027,6028,6029,6030,6031,6032], visible=False, arg3=800, delay=100, scale=8) # 벽 해제
        self.set_conversation(type=1, spawnId=9999, script='$02010052_BF__TORCHLIGHT_03__1$', arg4=3) # 카나 말풍선 대사
        self.hide_guide_summary(entityId=200)
        self.set_event_ui(type=1, arg2='$02010052_BF__TORCHLIGHT_03__2$', arg3='3000')
        self.set_timer(timerId='1', seconds=1, interval=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return spawn_state(self.ctx)


class spawn_state(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=299, textId=20105203) # 거대 다크 슬링을 처치하세요
        self.set_mesh(triggerIds=[5100,5101,5102,5103,5104,5105,5106,5107,5108,5109,5110], visible=False, arg3=800, delay=100, scale=8) # 카나 위에 있는 벽 해제
        self.set_effect(triggerIds=[7902], visible=True) # 카나 사라짐
        self.destroy_monster(spawnIds=[9999]) # 카나 사라짐
        self.set_actor(triggerId=8100, visible=False, initialSequence='Dmg_A')
        self.set_actor(triggerId=8006, visible=False, initialSequence='Dmg_A')
        self.set_actor(triggerId=8007, visible=False, initialSequence='Dmg_A')
        self.set_actor(triggerId=8008, visible=False, initialSequence='Dmg_A')
        self.set_actor(triggerId=8009, visible=False, initialSequence='Dmg_A')
        self.set_actor(triggerId=8010, visible=False, initialSequence='Dmg_A')
        self.create_monster(spawnIds=[199], animationEffect=True) # 얼음이 녹으며 등장하는 몬스터들 (중간)
        self.create_monster(spawnIds=[321,322,323,324,325], animationEffect=True) # 얼음이 녹으며 등장하는 몬스터들

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[199]):
            return monsterkill(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=299)


class monsterkill(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=20499, visible=True, initialSequence='Opening')
        self.set_actor(triggerId=20501, visible=False, initialSequence='Closed') # 얼어붙은 문
        self.set_mesh(triggerIds=[20500], visible=False, arg3=0, delay=0, scale=0) # 철문


initial_state = idle
