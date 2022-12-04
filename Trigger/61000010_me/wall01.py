""" trigger/61000010_me/wall01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000042], state=1)
        self.set_mesh(triggerIds=[3201,3202,3203,3204,3205], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[12000042], stateValue=0):
            self.set_mesh(triggerIds=[3201,3202,3203,3204,3205], visible=True, arg3=0, delay=0, scale=0)
            return 쿨타임(self.ctx)


class 쿨타임(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 대기(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
