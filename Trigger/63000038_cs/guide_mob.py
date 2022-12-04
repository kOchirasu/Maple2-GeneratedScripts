""" trigger/63000038_cs/guide_mob.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(boxIds=[2101]):
            return 가이드출력(self.ctx)
        if self.monster_in_combat(boxIds=[2102]):
            return 가이드출력(self.ctx)


class 가이드출력(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=26300383, textId=26300383)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[102]):
            return 가이드삭제대기(self.ctx)


class 가이드삭제대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 가이드삭제(self.ctx)


class 가이드삭제(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2103]):
            self.hide_guide_summary(entityId=26300383)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
