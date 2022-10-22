""" trigger/02000535_bf/gamelogic_9002.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        create_widget(type='TypingGame') # 키입력 게임 선언
        create_widget(type='Round') # 라운드 관리 트리거위젯 선언
        widget_action(type='Round', func='SettingFinalRound', widgetArg='1')
        widget_action(type='Round', func='SettingAllowedFailCount', widgetArg='3')
        widget_action(type='Round', func='SettingRoundInitIfFail', widgetArg='0')
        lock_my_pc(isLock=False)

    def on_tick(self) -> state.State:
        if user_value(key='GameLogicStart', value=1):
            return 게임진입()


class 게임진입(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 새라운드시작가능체크()


class 새라운드시작가능체크(state.State):
    def on_tick(self) -> state.State:
        if widget_condition(type='Round', name='GameClear'):
            return 게임성공종료()
        if widget_condition(type='Round', name='GameFail'):
            return 게임실패종료()
        if wait_tick(waitTick=1000):
            return 라운드체크()


class 라운드체크(state.State):
    def on_tick(self) -> state.State:
        if widget_condition(type='Round', name='CurrentRound', condition='= 1'):
            return 라운드1시작전UI()
        if widget_condition(type='Round', name='CurrentRound', condition='= 2'):
            return 라운드2시작전UI()
        if widget_condition(type='Round', name='CurrentRound', condition='= 3'):
            return 라운드3시작전UI()


class 라운드1시작전UI(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000535_BF__GAMELOGIC_9002__0$', arg3='3000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            lock_my_pc(isLock=True)
            set_event_ui(type=1, arg2='$02000535_BF__GAMELOGIC_9002__1$', arg3='6000')
            widget_action(type='TypingGame', func='Start', widgetArgNum=7, widgetArg='6000')
            return 라운드1진행()


class 라운드1진행(state.State):
    def on_tick(self) -> state.State:
        if widget_condition(type='TypingGame', name='Result', condition='1'):
            widget_action(type='Round', func='RoundResult', widgetArg='1')
            set_event_ui(type=1, arg2='$02000535_BF__GAMELOGIC_9002__2$', arg3='3000')
            return 라운드종료()
        if widget_condition(type='TypingGame', name='Result', condition='0'):
            widget_action(type='Round', func='RoundResult', widgetArg='0')
            set_event_ui(type=1, arg2='$02000535_BF__GAMELOGIC_9002__3$', arg3='3000')
            return 라운드종료()


class 라운드2시작전UI(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000535_BF__GAMELOGIC_9002__4$', arg3='3000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            lock_my_pc(isLock=True)
            set_event_ui(type=1, arg2='$02000535_BF__GAMELOGIC_9002__5$', arg3='4000')
            widget_action(type='TypingGame', func='Start', widgetArgNum=6, widgetArg='4000')
            return 라운드2진행()


class 라운드2진행(state.State):
    def on_tick(self) -> state.State:
        if widget_condition(type='TypingGame', name='Result', condition='1'):
            set_event_ui(type=1, arg2='$02000535_BF__GAMELOGIC_9002__6$', arg3='3000')
            widget_action(type='Round', func='RoundResult', widgetArg='1')
            return 라운드종료()
        if widget_condition(type='TypingGame', name='Result', condition='0'):
            set_event_ui(type=1, arg2='$02000535_BF__GAMELOGIC_9002__7$', arg3='3000')
            widget_action(type='Round', func='RoundResult', widgetArg='0')
            return 라운드종료()


class 라운드3시작전UI(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000535_BF__GAMELOGIC_9002__8$', arg3='3000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            lock_my_pc(isLock=True)
            set_event_ui(type=1, arg2='$02000535_BF__GAMELOGIC_9002__9$', arg3='3000')
            widget_action(type='TypingGame', func='Start', widgetArgNum=7, widgetArg='3000')
            return 라운드3진행()


class 라운드3진행(state.State):
    def on_tick(self) -> state.State:
        if widget_condition(type='TypingGame', name='Result', condition='1'):
            lock_my_pc(isLock=True)
            set_event_ui(type=1, arg2='$02000535_BF__GAMELOGIC_9002__10$', arg3='3000')
            widget_action(type='Round', func='RoundResult', widgetArg='1')
            return 라운드종료()
        if widget_condition(type='TypingGame', name='Result', condition='0'):
            set_event_ui(type=1, arg2='$02000535_BF__GAMELOGIC_9002__11$', arg3='3000')
            widget_action(type='Round', func='RoundResult', widgetArg='0')
            return 라운드종료()


class 라운드종료(state.State):
    def on_tick(self) -> state.State:
        if true():
            lock_my_pc(isLock=False)
            return 새라운드시작가능체크()


class 게임성공종료(state.State):
    def on_enter(self):
        set_user_value(triggerId=1001, key='GameLogicEnd', value=1)
        set_user_value(key='GameLogicStart', value=999) # 코드는 테스트 후 지워주세요

    def on_tick(self) -> state.State:
        if true():
            return 대기()


class 게임실패종료(state.State):
    def on_enter(self):
        set_user_value(triggerId=1001, key='GameLogicEnd', value=2)
        set_user_value(key='GameLogicStart', value=999) # 코드는 테스트 후 지워주세요

    def on_tick(self) -> state.State:
        if true():
            return 대기()


