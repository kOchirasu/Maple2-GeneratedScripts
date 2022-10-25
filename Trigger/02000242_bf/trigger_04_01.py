""" trigger/02000242_bf/trigger_04_01.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[707,708], visible=True)
        self.destroy_monster(spawnIds=[607,608])


class 차웨이브1(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[607,608], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[607,608]):
            return 차딜레이1(self.ctx)


class 차딜레이1(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=10)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 차웨이브2(self.ctx)


class 차웨이브2(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[607,608], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[607,608]):
            return 차딜레이2(self.ctx)


class 차딜레이2(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=10)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 차웨이브3(self.ctx)


class 차웨이브3(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[607,608], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[607,608]):
            return 차딜레이3(self.ctx)


class 차딜레이3(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=180)


initial_state = 대기
