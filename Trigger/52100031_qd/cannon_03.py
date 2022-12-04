""" trigger/52100031_qd/cannon_03.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[693], visible=False)
        self.set_mesh(triggerIds=[3903], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='cannon03', value=1):
            return 생성(self.ctx)


class 생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2903], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2903]):
            self.set_effect(triggerIds=[693], visible=True)
            self.set_mesh(triggerIds=[3903], visible=False, arg3=0, delay=0, scale=5)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
