""" trigger/02000495_bf/main.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[101]):
            return 레이드(self.ctx)


class 레이드(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2001], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[2001]):
            return 초대기2(self.ctx)


class 초대기2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 던전클리어(self.ctx)


class 던전클리어(common.Trigger):
    def on_enter(self):
        self.dungeon_clear()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 포털개방(self.ctx)


class 포털개방(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
