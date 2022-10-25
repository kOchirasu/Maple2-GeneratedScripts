""" trigger/02010050_bf/bossspawn01.xml """
import common


class 시작대기중(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9000]):
            return 보스등장(self.ctx)


class 보스등장(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[99], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[99]):
            return 보스처치(self.ctx)


class 보스처치(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[99])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 종료(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.dungeon_clear()
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)


initial_state = 시작대기중
