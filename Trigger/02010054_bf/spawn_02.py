""" trigger/02010054_bf/spawn_02.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000885], state=2)
        self.set_effect(triggerIds=[611], visible=False)
        self.set_mesh(triggerIds=[3128], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[106]):
            return 몬스터생성(self.ctx)


class 몬스터생성(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[611], visible=True)
        self.set_mesh(triggerIds=[3128], visible=False, arg3=0, delay=0, scale=5)
        self.create_monster(spawnIds=[2023], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2023]):
            self.set_interact_object(triggerIds=[10000885], state=1)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
