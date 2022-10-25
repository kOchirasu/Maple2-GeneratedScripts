""" trigger/99999913/03_storm.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.create_widget(type='SurvivalContents')

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='StormStart', value=1):
            return SetStorm(self.ctx)


class SetStorm(common.Trigger):
    def on_enter(self):
        self.widget_action(type='SurvivalContents', func='StormData', widgetArg='1,0')
        self.write_log(logName='Survival', event='Storm_Step_0') # 서바이벌 스톰 로그

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Step01(self.ctx)


class Step01(common.Trigger):
    def on_enter(self):
        self.widget_action(type='SurvivalContents', func='EnterStep', widgetArg='1')
        self.write_log(logName='Survival', event='Storm_Step_1_start') # 서바이벌 스톰 로그

    def on_tick(self) -> common.Trigger:
        if self.widget_condition(type='SurvivalContents', name='TimeOver'):
            return Step02(self.ctx)

    def on_exit(self):
        self.widget_action(type='SurvivalContents', func='ExitStep', widgetArg='1')
        self.write_log(logName='Survival', event='Storm_Step_1_end') # 서바이벌 스톰 로그


class Step02(common.Trigger):
    def on_enter(self):
        self.widget_action(type='SurvivalContents', func='EnterStep', widgetArg='2')
        self.write_log(logName='Survival', event='Storm_Step_2_start') # 서바이벌 스톰 로그

    def on_tick(self) -> common.Trigger:
        if self.widget_condition(type='SurvivalContents', name='TimeOver'):
            return Step03(self.ctx)

    def on_exit(self):
        self.widget_action(type='SurvivalContents', func='ExitStep', widgetArg='1')
        self.write_log(logName='Survival', event='Storm_Step_2_end') # 서바이벌 스톰 로그


class Step03(common.Trigger):
    def on_enter(self):
        self.widget_action(type='SurvivalContents', func='EnterStep', widgetArg='3')
        self.write_log(logName='Survival', event='Storm_Step_3_start') # 서바이벌 스톰 로그

    def on_tick(self) -> common.Trigger:
        if self.widget_condition(type='SurvivalContents', name='TimeOver'):
            return Step04(self.ctx)

    def on_exit(self):
        self.widget_action(type='SurvivalContents', func='ExitStep', widgetArg='1')
        self.write_log(logName='Survival', event='Storm_Step_3_end') # 서바이벌 스톰 로그


class Step04(common.Trigger):
    def on_enter(self):
        self.widget_action(type='SurvivalContents', func='EnterStep', widgetArg='4')
        self.write_log(logName='Survival', event='Storm_Step_4_start') # 서바이벌 스톰 로그

    def on_tick(self) -> common.Trigger:
        if self.widget_condition(type='SurvivalContents', name='TimeOver'):
            return Step05(self.ctx)

    def on_exit(self):
        self.widget_action(type='SurvivalContents', func='ExitStep', widgetArg='1')
        self.write_log(logName='Survival', event='Storm_Step_4_end') # 서바이벌 스톰 로그


class Step05(common.Trigger):
    def on_enter(self):
        self.widget_action(type='SurvivalContents', func='EnterStep', widgetArg='5')
        self.write_log(logName='Survival', event='Storm_Step_5_start') # 서바이벌 스톰 로그

    def on_tick(self) -> common.Trigger:
        if self.widget_condition(type='SurvivalContents', name='TimeOver'):
            return Step06(self.ctx)

    def on_exit(self):
        self.widget_action(type='SurvivalContents', func='ExitStep', widgetArg='1')
        self.write_log(logName='Survival', event='Storm_Step_5_end') # 서바이벌 스톰 로그


class Step06(common.Trigger):
    def on_enter(self):
        self.widget_action(type='SurvivalContents', func='EnterStep', widgetArg='6')
        self.write_log(logName='Survival', event='Storm_Step_6_start') # 서바이벌 스톰 로그

    def on_tick(self) -> common.Trigger:
        if self.widget_condition(type='SurvivalContents', name='TimeOver'):
            return Step07(self.ctx)

    def on_exit(self):
        self.widget_action(type='SurvivalContents', func='ExitStep', widgetArg='1')
        self.write_log(logName='Survival', event='Storm_Step_6_end') # 서바이벌 스톰 로그


class Step07(common.Trigger):
    def on_enter(self):
        self.widget_action(type='SurvivalContents', func='EnterStep', widgetArg='7')
        self.write_log(logName='Survival', event='Storm_Step_7_start') # 서바이벌 스톰 로그

    def on_tick(self) -> common.Trigger:
        if self.widget_condition(type='SurvivalContents', name='TimeOver'):
            return Quit(self.ctx)

    def on_exit(self):
        self.widget_action(type='SurvivalContents', func='ExitStep', widgetArg='1')
        self.write_log(logName='Survival', event='Storm_Step_7_end') # 서바이벌 스톰 로그


class Quit(common.Trigger):
    pass


initial_state = Wait
