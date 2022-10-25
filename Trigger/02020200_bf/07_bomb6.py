""" trigger/02020200_bf/07_bomb6.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='BombOn', value=1):
            return 시작(self.ctx)


class 시작(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[213], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='BombOn', value=2):
            return 종료(self.ctx)
        if self.monster_dead(boxIds=[213]):
            return 폭탄_터짐(self.ctx)


class 폭탄_터짐(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[2006], visible=False, arg3=1500, scale=3)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='BombOn', value=2):
            return 종료(self.ctx)
        if self.true():
            return 대기시간(self.ctx)


class 대기시간(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='BombOn', value=2):
            return 종료(self.ctx)
        if self.wait_tick(waitTick=40000):
            self.set_mesh(triggerIds=[2006], visible=True, scale=3)
            return 시작(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[213])
        self.set_mesh(triggerIds=[2006], visible=False, arg3=1500, scale=3)


initial_state = 대기
