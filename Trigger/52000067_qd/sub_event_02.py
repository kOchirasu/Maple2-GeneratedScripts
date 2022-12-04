""" trigger/52000067_qd/sub_event_02.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7200], visible=False) # 폭발

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=704, boxId=1):
            return idle_02(self.ctx)


class idle_02(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[756,755], animationEffect=True) # 시민
        self.set_conversation(type=1, spawnId=102, script='$52000067_QD__SUB_EVENT_02__0$', arg4=3, arg5=0)
        self.set_conversation(type=1, spawnId=101, script='$52000067_QD__SUB_EVENT_02__1$', arg4=3, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    pass


initial_state = idle
