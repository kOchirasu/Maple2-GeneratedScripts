""" trigger/02000345_bf/dress.xml """
import trigger_api


# 플레이어 감지
# 60002 : 모든 영역
class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[2001,2002], visible=True, arg3=0, delay=0)
        self.set_interact_object(triggerIds=[10001067], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=60002, minUsers='1'):
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entityId=20003441, textId=20003441, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return start(self.ctx)


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000345_BF__DRESS__0$', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return start_02(self.ctx)


class start_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[2001,2002], visible=False, arg3=0, delay=200)
        self.show_guide_summary(entityId=20003444, textId=20003444, duration=5000)


initial_state = idle
