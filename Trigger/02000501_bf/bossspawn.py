""" trigger/02000501_bf/bossspawn.xml """
import common


class 시작대기중(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[101]):
            return 보스등장(self.ctx)


class 보스등장(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[99], animationEffect=False) # arg2="0" 을 넣으면 보스 등장하자마자 바로 공격 상태가 되는 것을 막을 수 있음

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[99]):
            return 종료체크(self.ctx)


class 종료체크(common.Trigger):
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
