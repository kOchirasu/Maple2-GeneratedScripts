""" trigger/63000038_cs/guide_boss.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='BossGuide', value=1):
            return 가이드분기(self.ctx)


class 가이드분기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[199], jobCode=100):
            return 가이드출력(self.ctx)
        if self.user_detected(boxIds=[199], jobCode=110):
            return 퀘스트체크(self.ctx)


class 퀘스트체크(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[199], questIds=[40002651], questStates=[1]):
            return 가이드출력(self.ctx)


class 가이드출력(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=26300384, textId=26300384)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[105]):
            self.hide_guide_summary(entityId=26300384)
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
