""" trigger/02000492_bf/mob_01.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[1001]):
            return 전투01(self.ctx)
        if self.user_detected(boxIds=[1002]):
            return 전투01(self.ctx)


class 전투01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101,111], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[101,111]):
            return 전투02(self.ctx)


class 전투02(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[102], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[102]):
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
