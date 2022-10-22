""" trigger/82000012_survival/03_storm.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        create_widget(type='SurvivalContents')

    def on_tick(self) -> state.State:
        if user_value(key='StormStart', value=1):
            return SetStorm()


class SetStorm(state.State):
    def on_enter(self):
        widget_action(type='SurvivalContents', func='StormData', widgetArg='1,0')
        write_log(logName='Survival', arg3='Storm_Step_0') # 서바이벌 스톰 로그

    def on_tick(self) -> state.State:
        if true():
            return Step01()


class Step01(state.State):
    def on_enter(self):
        widget_action(type='SurvivalContents', func='EnterStep', widgetArg='1')
        write_log(logName='Survival', arg3='Storm_Step_1_start') # 서바이벌 스톰 로그

    def on_tick(self) -> state.State:
        if widget_condition(type='SurvivalContents', name='TimeOver'):
            return Step02()

    def on_exit(self):
        widget_action(type='SurvivalContents', func='ExitStep', widgetArg='1')
        write_log(logName='Survival', arg3='Storm_Step_1_end') # 서바이벌 스톰 로그


class Step02(state.State):
    def on_enter(self):
        widget_action(type='SurvivalContents', func='EnterStep', widgetArg='2')
        write_log(logName='Survival', arg3='Storm_Step_2_start') # 서바이벌 스톰 로그

    def on_tick(self) -> state.State:
        if widget_condition(type='SurvivalContents', name='TimeOver'):
            return Step03()

    def on_exit(self):
        widget_action(type='SurvivalContents', func='ExitStep', widgetArg='1')
        write_log(logName='Survival', arg3='Storm_Step_2_end') # 서바이벌 스톰 로그


class Step03(state.State):
    def on_enter(self):
        widget_action(type='SurvivalContents', func='EnterStep', widgetArg='3')
        write_log(logName='Survival', arg3='Storm_Step_3_start') # 서바이벌 스톰 로그

    def on_tick(self) -> state.State:
        if widget_condition(type='SurvivalContents', name='TimeOver'):
            return Step04()

    def on_exit(self):
        widget_action(type='SurvivalContents', func='ExitStep', widgetArg='1')
        write_log(logName='Survival', arg3='Storm_Step_3_end') # 서바이벌 스톰 로그


class Step04(state.State):
    def on_enter(self):
        widget_action(type='SurvivalContents', func='EnterStep', widgetArg='4')
        write_log(logName='Survival', arg3='Storm_Step_4_start') # 서바이벌 스톰 로그

    def on_tick(self) -> state.State:
        if widget_condition(type='SurvivalContents', name='TimeOver'):
            return Step05()

    def on_exit(self):
        widget_action(type='SurvivalContents', func='ExitStep', widgetArg='1')
        write_log(logName='Survival', arg3='Storm_Step_4_end') # 서바이벌 스톰 로그


class Step05(state.State):
    def on_enter(self):
        widget_action(type='SurvivalContents', func='EnterStep', widgetArg='5')
        write_log(logName='Survival', arg3='Storm_Step_5_start') # 서바이벌 스톰 로그

    def on_tick(self) -> state.State:
        if widget_condition(type='SurvivalContents', name='TimeOver'):
            return Step06()

    def on_exit(self):
        widget_action(type='SurvivalContents', func='ExitStep', widgetArg='1')
        write_log(logName='Survival', arg3='Storm_Step_5_end') # 서바이벌 스톰 로그


class Step06(state.State):
    def on_enter(self):
        widget_action(type='SurvivalContents', func='EnterStep', widgetArg='6')
        write_log(logName='Survival', arg3='Storm_Step_6_start') # 서바이벌 스톰 로그

    def on_tick(self) -> state.State:
        if widget_condition(type='SurvivalContents', name='TimeOver'):
            return Step07()

    def on_exit(self):
        widget_action(type='SurvivalContents', func='ExitStep', widgetArg='1')
        write_log(logName='Survival', arg3='Storm_Step_6_end') # 서바이벌 스톰 로그


class Step07(state.State):
    def on_enter(self):
        widget_action(type='SurvivalContents', func='EnterStep', widgetArg='7')
        write_log(logName='Survival', arg3='Storm_Step_7_start') # 서바이벌 스톰 로그

    def on_tick(self) -> state.State:
        if widget_condition(type='SurvivalContents', name='TimeOver'):
            return Step08()

    def on_exit(self):
        widget_action(type='SurvivalContents', func='ExitStep', widgetArg='1')
        write_log(logName='Survival', arg3='Storm_Step_7_end') # 서바이벌 스톰 로그


class Step08(state.State):
    def on_enter(self):
        widget_action(type='SurvivalContents', func='EnterStep', widgetArg='8')
        write_log(logName='Survival', arg3='Storm_Step_8_start') # 서바이벌 스톰 로그

    def on_tick(self) -> state.State:
        if widget_condition(type='SurvivalContents', name='TimeOver'):
            return Quit()

    def on_exit(self):
        widget_action(type='SurvivalContents', func='ExitStep', widgetArg='1')
        write_log(logName='Survival', arg3='Storm_Step_8_end') # 서바이벌 스톰 로그


class Quit(state.State):
    pass


