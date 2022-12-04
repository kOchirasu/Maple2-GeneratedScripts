""" trigger/02010054_bf/star_02.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000860], state=2)
        self.set_effect(triggerIds=[605], visible=False)
        self.set_mesh(triggerIds=[3306,3307,3308,3309], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3125], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[102]):
            return 생성(self.ctx)


class 생성(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3306,3307,3308,3309], visible=True, arg3=0, delay=500, scale=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[103]):
            return 몬스터생성(self.ctx)


class 몬스터생성(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3306,3307,3308,3309], visible=False, arg3=0, delay=900, scale=3)
        self.set_mesh(triggerIds=[3125], visible=False, arg3=0, delay=0, scale=5)
        self.set_effect(triggerIds=[605], visible=True)
        self.create_monster(spawnIds=[2004], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2004]):
            self.set_interact_object(triggerIds=[10000860], state=1)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
