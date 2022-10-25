""" trigger/02000401_bf/cannon_05.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[695], visible=False)
        self.set_mesh(triggerIds=[3905], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='cannon05', value=1):
            return 생성(self.ctx)


class 생성(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2905], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[2905]):
            self.set_effect(triggerIds=[695], visible=True)
            self.set_mesh(triggerIds=[3905], visible=False, arg3=0, delay=0, scale=5)
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
