""" trigger/02000242_bf/trigger_04_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[707,708], visible=True)
        self.destroy_monster(spawnIds=[607,608])


class 차웨이브1(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[607,608], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[607,608]):
            return 차딜레이1(self.ctx)


class 차딜레이1(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 차웨이브2(self.ctx)


class 차웨이브2(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[607,608], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[607,608]):
            return 차딜레이2(self.ctx)


class 차딜레이2(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 차웨이브3(self.ctx)


class 차웨이브3(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[607,608], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[607,608]):
            return 차딜레이3(self.ctx)


class 차딜레이3(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=180)


initial_state = 대기
