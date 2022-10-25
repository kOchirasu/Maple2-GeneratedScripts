""" trigger/02000350_bf/r11_02.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=103, spawnIds=[111001]):
            return 몹스폰(self.ctx)


class 몹스폰(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[111003], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[111001]):
            self.destroy_monster(spawnIds=[111003])
            return 종료(self.ctx)
        if self.monster_dead(boxIds=[111003]):
            return 몹스폰(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
