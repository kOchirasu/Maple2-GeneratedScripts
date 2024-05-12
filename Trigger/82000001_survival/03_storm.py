""" trigger/82000001_survival/03_storm.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SurvivalContents')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StormStart', value=1):
            return SetStorm(self.ctx)


class SetStorm(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # test용 수정 가능 지점 arg3="6,0" 10배 빠른 스톰
        self.widget_action(type='SurvivalContents', func='StormData', widgetArg='1,0')
        self.write_log(logName='Survival', event='Storm_Step_0') # 서바이벌 스톰 로그

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return Step01(self.ctx)


class Step01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.widget_action(type='SurvivalContents', func='EnterStep', widgetArg='1')
        self.write_log(logName='Survival', event='Storm_Step_1_start') # 서바이벌 스톰 로그

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='SurvivalContents', name='TimeOver'):
            return Step02(self.ctx)

    def on_exit(self) -> None:
        self.widget_action(type='SurvivalContents', func='ExitStep', widgetArg='1')
        self.write_log(logName='Survival', event='Storm_Step_1_end')
        # 서바이벌 스톰 로그


class Step02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.widget_action(type='SurvivalContents', func='EnterStep', widgetArg='2')
        self.write_log(logName='Survival', event='Storm_Step_2_start') # 서바이벌 스톰 로그

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='SurvivalContents', name='TimeOver'):
            return Step03(self.ctx)

    def on_exit(self) -> None:
        self.widget_action(type='SurvivalContents', func='ExitStep', widgetArg='1')
        self.write_log(logName='Survival', event='Storm_Step_2_end')
        # 서바이벌 스톰 로그


class Step03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.widget_action(type='SurvivalContents', func='EnterStep', widgetArg='3')
        self.write_log(logName='Survival', event='Storm_Step_3_start') # 서바이벌 스톰 로그

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='SurvivalContents', name='TimeOver'):
            return Step04(self.ctx)

    def on_exit(self) -> None:
        self.widget_action(type='SurvivalContents', func='ExitStep', widgetArg='1')
        self.write_log(logName='Survival', event='Storm_Step_3_end')
        # 서바이벌 스톰 로그


class Step04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.widget_action(type='SurvivalContents', func='EnterStep', widgetArg='4')
        self.write_log(logName='Survival', event='Storm_Step_4_start') # 서바이벌 스톰 로그

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='SurvivalContents', name='TimeOver'):
            return Step05(self.ctx)

    def on_exit(self) -> None:
        self.widget_action(type='SurvivalContents', func='ExitStep', widgetArg='1')
        self.write_log(logName='Survival', event='Storm_Step_4_end')
        # 서바이벌 스톰 로그


class Step05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.widget_action(type='SurvivalContents', func='EnterStep', widgetArg='5')
        self.write_log(logName='Survival', event='Storm_Step_5_start') # 서바이벌 스톰 로그

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='SurvivalContents', name='TimeOver'):
            return Step06(self.ctx)

    def on_exit(self) -> None:
        self.widget_action(type='SurvivalContents', func='ExitStep', widgetArg='1')
        self.write_log(logName='Survival', event='Storm_Step_5_end')
        # 서바이벌 스톰 로그


class Step06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.widget_action(type='SurvivalContents', func='EnterStep', widgetArg='6')
        self.write_log(logName='Survival', event='Storm_Step_6_start') # 서바이벌 스톰 로그

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='SurvivalContents', name='TimeOver'):
            return Step07(self.ctx)

    def on_exit(self) -> None:
        self.widget_action(type='SurvivalContents', func='ExitStep', widgetArg='1')
        self.write_log(logName='Survival', event='Storm_Step_6_end')
        # 서바이벌 스톰 로그


class Step07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.widget_action(type='SurvivalContents', func='EnterStep', widgetArg='7')
        self.write_log(logName='Survival', event='Storm_Step_7_start') # 서바이벌 스톰 로그

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='SurvivalContents', name='TimeOver'):
            return Step08(self.ctx)

    def on_exit(self) -> None:
        self.widget_action(type='SurvivalContents', func='ExitStep', widgetArg='1')
        self.write_log(logName='Survival', event='Storm_Step_7_end')
        # 서바이벌 스톰 로그


class Step08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.widget_action(type='SurvivalContents', func='EnterStep', widgetArg='8')
        self.write_log(logName='Survival', event='Storm_Step_8_start') # 서바이벌 스톰 로그

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='SurvivalContents', name='TimeOver'):
            return Quit(self.ctx)

    def on_exit(self) -> None:
        self.widget_action(type='SurvivalContents', func='ExitStep', widgetArg='1')
        self.write_log(logName='Survival', event='Storm_Step_8_end')
        # 서바이벌 스톰 로그


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
