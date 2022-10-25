""" trigger/02020065_bf/message.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02020065_BF__MESSAGE__0$', arg3='5000')

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='FieldGameStart', value=1):
            return 체력공지_1(self.ctx)
        if self.user_value(key='FieldGameStart', value=2):
            return 체력공지_1(self.ctx)
        if self.wait_tick(waitTick=5000):
            return 대기(self.ctx)


class 체력공지_1(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.check_npc_hp(compare='lowerEqual', value=50, spawnId=801, isRelative=True):
            self.set_event_ui(type=1, arg2='$02020065_BF__MESSAGE__1$', arg3='5000')
            return 체력공지_2(self.ctx)


class 체력공지_2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.check_npc_hp(compare='lowerEqual', value=30, spawnId=801, isRelative=True):
            self.set_event_ui(type=1, arg2='$02020065_BF__MESSAGE__2$', arg3='5000')
            return 체력공지_3(self.ctx)


class 체력공지_3(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.check_npc_hp(compare='lowerEqual', value=10, spawnId=801, isRelative=True):
            self.set_event_ui(type=1, arg2='$02020065_BF__MESSAGE__3$', arg3='5000')
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
