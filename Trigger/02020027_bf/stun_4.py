""" trigger/02020027_bf/stun_4.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[1001]):
            return 전투시작(self.ctx)


class 전투시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='summon_3_4', value=1):
            return 버프(self.ctx)


class 버프(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=11000):
            return 버프_2(self.ctx)


class 버프_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=401, script='$02020027_BF__stun_1__0$', arg4=3, arg5=0)
        self.set_conversation(type=1, spawnId=402, script='$02020027_BF__stun_1__1$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 버프_4(self.ctx)


class 버프_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=403, script='$02020027_BF__stun_1__2$', arg4=3, arg5=0)
        self.set_conversation(type=1, spawnId=404, script='$02020027_BF__stun_1__3$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 버프_5(self.ctx)


class 버프_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=405, script='$02020027_BF__stun_1__4$', arg4=3, arg5=0)
        self.set_conversation(type=1, spawnId=406, script='$02020027_BF__stun_1__5$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 버프_제거(self.ctx)


class 버프_제거(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(boxIds=[201], skillId=62000002, level=1, isPlayer=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            pass


initial_state = 시작
