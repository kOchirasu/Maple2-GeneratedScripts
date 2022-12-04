""" trigger/02020200_bf/06_bomb5.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BombOn', value=1):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[212], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BombOn', value=2):
            return 종료(self.ctx)
        if self.monster_dead(boxIds=[212]):
            return 폭탄_터짐(self.ctx)


class 폭탄_터짐(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[2005], visible=False, arg3=1500, scale=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BombOn', value=2):
            return 종료(self.ctx)
        if self.true():
            return 대기시간(self.ctx)


class 대기시간(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BombOn', value=2):
            return 종료(self.ctx)
        if self.wait_tick(waitTick=40000):
            self.set_mesh(triggerIds=[2005], visible=True, scale=3)
            return 시작(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[212])
        self.set_mesh(triggerIds=[2005], visible=False, arg3=1500, scale=3)


initial_state = 대기
