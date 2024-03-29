""" trigger/52020016_qd/monster_spawn_1_4.xml """
import trigger_api


class 체력조건(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='respawn_phase_1', value=1):
            return 전투페이즈(self.ctx)


class 전투페이즈(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[4000006], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[4000006]):
            return 몬스터리젠(self.ctx)
        if self.user_value(key='respawn_phase_1_end', value=1):
            return 끝(self.ctx)


class 몬스터리젠(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[4000008], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[4000008]):
            return 전투페이즈(self.ctx)
        if self.user_value(key='respawn_phase_1_end', value=1):
            return 끝(self.ctx)


class 끝(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[4000006], arg2=False)
        self.destroy_monster(spawnIds=[4000008], arg2=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return None


initial_state = 체력조건
