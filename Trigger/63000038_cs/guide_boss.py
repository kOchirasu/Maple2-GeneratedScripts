""" trigger/63000038_cs/guide_boss.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='BossGuide', value=1):
            return 가이드분기()


class 가이드분기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[199], jobCode=100):
            return 가이드출력()
        if user_detected(boxIds=[199], jobCode=110):
            return 퀘스트체크()


class 퀘스트체크(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[199], questIds=[40002651], questStates=[1]):
            return 가이드출력()


class 가이드출력(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26300384, textId=26300384)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[105]):
            hide_guide_summary(entityId=26300384)
            return 종료()


class 종료(state.State):
    pass


