""" trigger/02000334_bf/gameover.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[200,999], animationEffect=True) # 성벽

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[200]):
            return 게임오버(self.ctx)


class 게임오버(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[999]) # 게임오버용몬스터 소멸


initial_state = 시작
