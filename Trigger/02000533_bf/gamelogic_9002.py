""" trigger/02000533_bf/gamelogic_9002.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.create_widget(type='TypingGame') # 키입력 게임 선언
        self.create_widget(type='Round') # 라운드 관리 트리거위젯 선언
        self.widget_action(type='Round', func='SettingFinalRound', widgetArg='1')
        self.widget_action(type='Round', func='SettingAllowedFailCount', widgetArg='3')
        self.widget_action(type='Round', func='SettingRoundInitIfFail', widgetArg='0')
        self.lock_my_pc(isLock=False)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='GameLogicStart', value=1):
            return 게임진입(self.ctx)


class 게임진입(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 새라운드시작가능체크(self.ctx)


class 새라운드시작가능체크(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.widget_condition(type='Round', name='GameClear'):
            return 게임성공종료(self.ctx)
        if self.widget_condition(type='Round', name='GameFail'):
            return 게임실패종료(self.ctx)
        if self.wait_tick(waitTick=1000):
            return 라운드체크(self.ctx)


class 라운드체크(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.widget_condition(type='Round', name='CurrentRound', condition='= 1'):
            return 라운드1시작전UI(self.ctx)
        if self.widget_condition(type='Round', name='CurrentRound', condition='= 2'):
            return 라운드2시작전UI(self.ctx)
        if self.widget_condition(type='Round', name='CurrentRound', condition='= 3'):
            return 라운드3시작전UI(self.ctx)


class 라운드1시작전UI(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000533_BF__GAMELOGIC_9002__0$', arg3='3000')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            self.lock_my_pc(isLock=True)
            self.set_event_ui(type=1, arg2='$02000533_BF__GAMELOGIC_9002__1$', arg3='6000')
            self.widget_action(type='TypingGame', func='Start', widgetArgNum=7, widgetArg='6000')
            return 라운드1진행(self.ctx)


class 라운드1진행(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.widget_condition(type='TypingGame', name='Result', condition='1'):
            self.widget_action(type='Round', func='RoundResult', widgetArg='1')
            self.set_event_ui(type=1, arg2='$02000533_BF__GAMELOGIC_9002__2$', arg3='3000')
            return 라운드종료(self.ctx)
        if self.widget_condition(type='TypingGame', name='Result', condition='0'):
            self.widget_action(type='Round', func='RoundResult', widgetArg='0')
            self.set_event_ui(type=1, arg2='$02000533_BF__GAMELOGIC_9002__3$', arg3='3000')
            return 라운드종료(self.ctx)


class 라운드2시작전UI(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000533_BF__GAMELOGIC_9002__4$', arg3='3000')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            self.lock_my_pc(isLock=True)
            self.set_event_ui(type=1, arg2='$02000533_BF__GAMELOGIC_9002__5$', arg3='4000')
            self.widget_action(type='TypingGame', func='Start', widgetArgNum=6, widgetArg='4000')
            return 라운드2진행(self.ctx)


class 라운드2진행(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.widget_condition(type='TypingGame', name='Result', condition='1'):
            self.set_event_ui(type=1, arg2='$02000533_BF__GAMELOGIC_9002__6$', arg3='3000')
            self.widget_action(type='Round', func='RoundResult', widgetArg='1')
            return 라운드종료(self.ctx)
        if self.widget_condition(type='TypingGame', name='Result', condition='0'):
            self.set_event_ui(type=1, arg2='$02000533_BF__GAMELOGIC_9002__7$', arg3='3000')
            self.widget_action(type='Round', func='RoundResult', widgetArg='0')
            return 라운드종료(self.ctx)


class 라운드3시작전UI(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000533_BF__GAMELOGIC_9002__8$', arg3='3000')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            self.lock_my_pc(isLock=True)
            self.set_event_ui(type=1, arg2='$02000533_BF__GAMELOGIC_9002__9$', arg3='3000')
            self.widget_action(type='TypingGame', func='Start', widgetArgNum=7, widgetArg='3000')
            return 라운드3진행(self.ctx)


class 라운드3진행(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.widget_condition(type='TypingGame', name='Result', condition='1'):
            self.lock_my_pc(isLock=True)
            self.set_event_ui(type=1, arg2='$02000533_BF__GAMELOGIC_9002__10$', arg3='3000')
            self.widget_action(type='Round', func='RoundResult', widgetArg='1')
            return 라운드종료(self.ctx)
        if self.widget_condition(type='TypingGame', name='Result', condition='0'):
            self.set_event_ui(type=1, arg2='$02000533_BF__GAMELOGIC_9002__11$', arg3='3000')
            self.widget_action(type='Round', func='RoundResult', widgetArg='0')
            return 라운드종료(self.ctx)


class 라운드종료(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.true():
            self.lock_my_pc(isLock=False)
            return 새라운드시작가능체크(self.ctx)


class 게임성공종료(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=9001, key='GameLogicEnd', value=1)
        self.set_user_value(key='GameLogicStart', value=999) # 코드는 테스트 후 지워주세요

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대기(self.ctx)


class 게임실패종료(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=9001, key='GameLogicEnd', value=2)
        self.set_user_value(key='GameLogicStart', value=999) # 코드는 테스트 후 지워주세요

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대기(self.ctx)


initial_state = 대기
