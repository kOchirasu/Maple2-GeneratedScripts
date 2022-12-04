""" trigger/63000033_cs/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001009], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001009], stateValue=0):
            return 번아이템1(self.ctx)


class 번아이템1(trigger_api.Trigger):
    def on_enter(self):
        self.create_item(spawnIds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14])
        self.create_item(spawnIds=[15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41])
        self.create_item(spawnIds=[42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70])
        self.create_item(spawnIds=[71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87])
        self.set_timer(timerId='181', seconds=19)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='181'):
            return 대기(self.ctx)


initial_state = 대기
