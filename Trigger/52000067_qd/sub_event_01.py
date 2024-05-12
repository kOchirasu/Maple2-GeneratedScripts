""" trigger/52000067_qd/sub_event_01.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[751], animationEffect=True) # 골두스

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=703, minUsers='1'):
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=751, script='$52000067_QD__SUB_EVENT_01__0$', arg4=3, arg5=0)
        self.set_conversation(type=1, spawnId=751, script='$52000067_QD__SUB_EVENT_01__1$', arg4=3, arg5=3)
        self.set_conversation(type=1, spawnId=751, script='$52000067_QD__SUB_EVENT_01__2$', arg4=3, arg5=6)
        self.set_conversation(type=1, spawnId=751, script='$52000067_QD__SUB_EVENT_01__3$', arg4=3, arg5=9)
        self.set_conversation(type=1, spawnId=751, script='$52000067_QD__SUB_EVENT_01__4$', arg4=3, arg5=12)
        self.set_conversation(type=1, spawnId=751, script='$52000067_QD__SUB_EVENT_01__5$', arg4=3, arg5=15)
        self.set_conversation(type=1, spawnId=751, script='$52000067_QD__SUB_EVENT_01__6$', arg4=3, arg5=18)
        self.set_conversation(type=1, spawnId=752, script='$52000067_QD__SUB_EVENT_01__7$', arg4=3, arg5=19)
        self.set_conversation(type=1, spawnId=753, script='$52000067_QD__SUB_EVENT_01__8$', arg4=3, arg5=19)
        self.set_conversation(type=1, spawnId=754, script='$52000067_QD__SUB_EVENT_01__9$', arg4=3, arg5=20)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return start(self.ctx)


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[757,758,761,762], animationEffect=True) # 시민
        self.set_conversation(type=1, spawnId=757, script='$52000067_QD__SUB_EVENT_01__10$', arg4=3, arg5=2)
        self.set_conversation(type=1, spawnId=758, script='$52000067_QD__SUB_EVENT_01__11$', arg4=3, arg5=3)
        self.set_conversation(type=1, spawnId=762, script='$52000067_QD__SUB_EVENT_01__12$', arg4=3, arg5=2)
        self.set_conversation(type=1, spawnId=761, script='$52000067_QD__SUB_EVENT_01__13$', arg4=3, arg5=2)


initial_state = idle
