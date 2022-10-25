""" trigger/51000001_dg/tutorial.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[100]):
            return 몬스터소환(self.ctx)


class 몬스터소환(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1000], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1000]):
            return 대기시간(self.ctx)
        if not self.user_detected(boxIds=[100]):
            return 종료(self.ctx)


class 대기시간(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 대기(self.ctx)
        if not self.user_detected(boxIds=[100]):
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
