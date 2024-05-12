""" trigger/02000328_bf/event4.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[301], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[999998]):
            return 진행1(self.ctx)


class 진행1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 진행2(self.ctx)


class 진행2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354,355,356,357,358,359,360,361,362,363,364,365,366,367,368,369,370,371,372,373,374,375,376], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[1401,1402,1403,1404,1405]):
            return 진행3(self.ctx)


class 진행3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[301,302], visible=True, arg3=100, delay=50, scale=2)
        self.set_mesh(triggerIds=[303,304,305,306], visible=True, arg3=200, delay=50, scale=2)
        self.set_mesh(triggerIds=[307,308,309,310,311,312], visible=True, arg3=300, delay=50, scale=2)
        self.set_mesh(triggerIds=[313,314,315,316,317,318,319,320], visible=True, arg3=400, delay=50, scale=2)
        self.set_mesh(triggerIds=[321,322,323,324,325,326,327,328,329,330], visible=True, arg3=500, delay=50, scale=2)
        self.set_mesh(triggerIds=[331,332,333,334,335,336,337,338,339,340,341,342], visible=True, arg3=600, delay=50, scale=2)
        self.set_mesh(triggerIds=[343,344,345,346,347,348,349,350,351,352,353,354], visible=True, arg3=700, delay=50, scale=2)
        self.set_mesh(triggerIds=[355,356,357,358,359,360,361,362,363,364], visible=True, arg3=800, delay=50, scale=2)
        self.set_mesh(triggerIds=[365,366,367,368,369,370,371,372], visible=True, arg3=900, delay=50, scale=2)
        self.set_mesh(triggerIds=[373,374,375,376], visible=True, arg3=1000, delay=50, scale=2)
        self.show_guide_summary(entityId=20003281, textId=20003281)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_timer(timerId='100', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='100'):
            return 종료2(self.ctx)


class 종료2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entityId=20003281)


initial_state = 대기
