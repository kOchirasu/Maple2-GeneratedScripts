""" trigger/80000012_bonus/wave_01.xml """
import common


class 시작(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=702, spawnIds=[199]):
            return 생성랜덤(self.ctx)


class 대기시간(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=702, spawnIds=[199]):
            return 차타이머1(self.ctx)


class 차타이머1(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return 생성랜덤(self.ctx)
        if not self.npc_detected(boxId=702, spawnIds=[199]):
            return 시작(self.ctx)


# 몬스터 랜덤 생성
class 생성랜덤(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=13):
            return 번생성1(self.ctx)
        if self.random_condition(rate=13):
            return 번생성2(self.ctx)
        if self.random_condition(rate=12):
            return 번생성3(self.ctx)
        if self.random_condition(rate=12):
            return 번생성4(self.ctx)
        if self.random_condition(rate=12):
            return 번생성5(self.ctx)
        if self.random_condition(rate=12):
            return 번생성6(self.ctx)
        if self.random_condition(rate=13):
            return 번생성7(self.ctx)
        if self.random_condition(rate=13):
            return 번생성8(self.ctx)


class 번생성1(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대기시간(self.ctx)


class 번생성2(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[102], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대기시간(self.ctx)


class 번생성3(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[103], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대기시간(self.ctx)


class 번생성4(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[104], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대기시간(self.ctx)


class 번생성5(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[105], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대기시간(self.ctx)


class 번생성6(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[106], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대기시간(self.ctx)


class 번생성7(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[107], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대기시간(self.ctx)


class 번생성8(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[108], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대기시간(self.ctx)


initial_state = 시작
