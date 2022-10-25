""" trigger/51000003_dg/hidden.xml """
import common


# 여기서 부터 시작
class Start(common.Trigger):
    pass


class Hidden_ready_01(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=99, visible=False, enable=False, minimapVisible=False) # 임시 히든포탈
        self.set_event_ui(type=1, arg2='$51000003_DG__HIDDEN__0$', arg3='4000', arg4='0')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Hidden_ready_02(self.ctx)


class Hidden_ready_02(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$51000003_DG__HIDDEN__1$', arg3='4000', arg4='0')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Hidden_ready_03(self.ctx)


class Hidden_ready_03(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=0, arg2='6,6', arg3='0', arg4='0')
        self.select_camera(triggerId=8002, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return Hidden_ready_04(self.ctx)


class Hidden_ready_04(common.Trigger):
    def on_enter(self):
        self.show_count_ui(text='$61000004_ME__TRIGGER_01__1$', stage=0, count=5)
        self.set_achievement(triggerId=710, type='trigger', achieve='boomboombeach_hidden_start')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return Hidden_Start(self.ctx)


class Hidden_Start(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=991104, key='Round_06', value=1)
        self.set_user_value(triggerId=991105, key='Round_06', value=1)
        self.set_user_value(triggerId=991106, key='Round_06', value=1)
        self.set_user_value(triggerId=991107, key='Round_06', value=1)
        self.set_user_value(triggerId=991108, key='Round_06', value=1)
        self.set_timer(timerId='150', seconds=150, interval=1)


initial_state = Start
