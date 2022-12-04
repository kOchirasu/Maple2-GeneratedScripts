""" trigger/02000298_bf/door_01.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=201, visible=True, initialSequence='Closed')
        self.set_mesh(triggerIds=[3011], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3012], visible=True, arg3=0, delay=0, scale=0)
        self.set_agent(triggerIds=[9011], visible=True)
        self.set_agent(triggerIds=[9012], visible=True)
        self.set_agent(triggerIds=[9013], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[101]):
            return 문열림(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=201, visible=True, initialSequence='Opened')
        self.create_monster(spawnIds=[1001], animationEffect=False)
        self.create_monster(spawnIds=[1002], animationEffect=False)
        self.create_monster(spawnIds=[1003], animationEffect=False)
        self.create_monster(spawnIds=[1004], animationEffect=False)
        self.set_mesh(triggerIds=[3011], visible=False, arg3=0, delay=0, scale=5)
        self.set_mesh(triggerIds=[3012], visible=False, arg3=0, delay=0, scale=5)
        self.set_agent(triggerIds=[9011], visible=False)
        self.set_agent(triggerIds=[9012], visible=False)
        self.set_agent(triggerIds=[9013], visible=False)


initial_state = 시작
