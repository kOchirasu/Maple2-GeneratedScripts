""" trigger/52020027_qd/52020027_boss.xml """
import trigger_api


class 감지(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Boss', value=1):
            return 페이즈1(self.ctx)


class 페이즈1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SerihaAI', value=1):
            # <AI에서 신호 쏴줌(AI_Seriha.xml)>
            return 도약(self.ctx)


class 도약(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=903, spawnIds=[111]):
            return 페이즈2(self.ctx)


class 페이즈2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=111, script='조심하는 게 좋을걸?', arg4=4)
        self.create_monster(spawnIds=[112], animationEffect=True)
        self.create_monster(spawnIds=[113], animationEffect=True)
        self.create_monster(spawnIds=[114], animationEffect=True)
        self.create_monster(spawnIds=[115], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return NPC애니세팅(self.ctx)


class NPC애니세팅(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawnId=114, sequenceName='Attack_01_A', duration=2000)
        self.set_npc_emotion_loop(spawnId=115, sequenceName='Attack_01_A', duration=2000)


initial_state = 감지
