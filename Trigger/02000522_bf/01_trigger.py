""" trigger/02000522_bf/01_trigger.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=11, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[201]):
            return 몹생성(self.ctx)


class 몹생성(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[301], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[301]):
            return 클리어처리(self.ctx)


class 클리어처리(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            self.dungeon_clear()
            return 종료처리(self.ctx)


class 종료처리(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[-1])
        self.set_portal(portalId=11, visible=True, enable=True, minimapVisible=True)


initial_state = 대기
