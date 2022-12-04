""" trigger/02010054_bf/spawn_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000884], state=2)
        self.set_effect(triggerIds=[610], visible=False)
        self.set_mesh(triggerIds=[3127], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[105]):
            return 몬스터생성(self.ctx)


class 몬스터생성(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[610], visible=True)
        self.create_monster(spawnIds=[2022], animationEffect=False)
        self.set_mesh(triggerIds=[3127], visible=False, arg3=0, delay=0, scale=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2022]):
            self.set_interact_object(triggerIds=[10000884], state=1)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
