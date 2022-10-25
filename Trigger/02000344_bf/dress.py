""" trigger/02000344_bf/dress.xml """
import common


# 플레이어 감지
# 60002 : 모든 영역
class idle(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[6701,6702,6703,6704,6705], visible=True, arg3=0, delay=0) # 가림막
        self.set_mesh(triggerIds=[6711,6712,6713,6714,6715], visible=False, arg3=0, delay=10) # 가림막
        self.set_interact_object(triggerIds=[10001066], state=1)

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=60002, boxId=1):
            return ready(self.ctx)


class ready(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20003441, textId=20003441, duration=5000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return start(self.ctx)


class start(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000344_BF__DRESS__0$', arg3='3000')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return start_02(self.ctx)


class start_02(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[6701,6702,6703,6704,6705], visible=False, arg3=0, delay=0) # 가림막
        self.set_mesh(triggerIds=[6711,6712,6713,6714,6715], visible=True, arg3=0, delay=10) # 가림막
        self.show_guide_summary(entityId=20003444, textId=20003444, duration=5000)


initial_state = idle
