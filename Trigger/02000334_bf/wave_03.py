""" trigger/02000334_bf/wave_03.xml """
import common


# 플레이어 감지
class 대기시간(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=90099, spawnIds=[152]):
            return 차타이머1(self.ctx)


class 차타이머1(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=5)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='5'):
            return 생성랜덤(self.ctx)


# 몬스터 랜덤 생성
class 생성랜덤(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=12):
            return 번생성1(self.ctx)
        if self.random_condition(rate=13):
            return 번생성2(self.ctx)
        if self.random_condition(rate=12):
            return 번생성3(self.ctx)
        if self.random_condition(rate=13):
            return 번생성4(self.ctx)
        if self.random_condition(rate=12):
            return 번생성5(self.ctx)
        if self.random_condition(rate=13):
            return 번생성6(self.ctx)
        if self.random_condition(rate=12):
            return 번생성7(self.ctx)
        if self.random_condition(rate=13):
            return 번생성8(self.ctx)


class 번생성1(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[131], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대기시간(self.ctx)


class 번생성2(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[132], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대기시간(self.ctx)


class 번생성3(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[133], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대기시간(self.ctx)


class 번생성4(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[134], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대기시간(self.ctx)


class 번생성5(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[131], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대기시간(self.ctx)


class 번생성6(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[132], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대기시간(self.ctx)


class 번생성7(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[133], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대기시간(self.ctx)


class 번생성8(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[134], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대기시간(self.ctx)


initial_state = 대기시간
