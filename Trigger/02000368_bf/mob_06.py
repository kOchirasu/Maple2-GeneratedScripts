""" trigger/02000368_bf/mob_06.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[1001]):
            return 전투01(self.ctx)
        if self.user_detected(boxIds=[1002]):
            return 전투01(self.ctx)


class 전투01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[601,611], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[601,611]):
            return 전투02(self.ctx)


class 전투02(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[602], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[602]):
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
