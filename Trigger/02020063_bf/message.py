""" trigger/02020063_bf/message.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02020063_BF__MESSAGE__0$', arg3='5000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='FieldGameStart', value=1):
            # <게임 시작 결정>
            return 체력공지_1(self.ctx)
        if self.user_value(key='FieldGameStart', value=2):
            # <방폭 결정>
            return 체력공지_1(self.ctx)
        if self.wait_tick(waitTick=5000):
            return 대기(self.ctx)


class 체력공지_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_npc_hp(compare='lowerEqual', value=50, spawnId=801, isRelative=True):
            # <게임 시작 결정>
            self.set_event_ui(type=1, arg2='$02020063_BF__MESSAGE__1$', arg3='5000')
            return 체력공지_2(self.ctx)


class 체력공지_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_npc_hp(compare='lowerEqual', value=30, spawnId=801, isRelative=True):
            # <게임 시작 결정>
            self.set_event_ui(type=1, arg2='$02020063_BF__MESSAGE__2$', arg3='5000')
            return 체력공지_3(self.ctx)


class 체력공지_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_npc_hp(compare='lowerEqual', value=10, spawnId=801, isRelative=True):
            # <게임 시작 결정>
            self.set_event_ui(type=1, arg2='$02020063_BF__MESSAGE__3$', arg3='5000')
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
