""" trigger/52020027_qd/52020027_boss.xml """
import common


class 감지(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Boss', value=1):
            return 페이즈1(self.ctx)


class 페이즈1(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='SerihaAI', value=1):
            return 도약(self.ctx)


class 도약(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=903, spawnIds=[111]):
            return 페이즈2(self.ctx)


class 페이즈2(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=111, script='조심하는 게 좋을걸?', arg4=4)
        self.create_monster(spawnIds=[112], animationEffect=True)
        self.create_monster(spawnIds=[113], animationEffect=True)
        self.create_monster(spawnIds=[114], animationEffect=True)
        self.create_monster(spawnIds=[115], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return NPC애니세팅(self.ctx)


class NPC애니세팅(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_loop(spawnId=114, sequenceName='Attack_01_A', duration=2000)
        self.set_npc_emotion_loop(spawnId=115, sequenceName='Attack_01_A', duration=2000)


initial_state = 감지
