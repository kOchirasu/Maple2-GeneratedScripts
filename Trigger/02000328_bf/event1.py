""" trigger/02000328_bf/event1.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[1], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[999998]):
            return 진행1(self.ctx)


class 진행1(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=5)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 진행2(self.ctx)


class 진행2(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1101,1102,1103,1104,1105]):
            return 진행3(self.ctx)


class 진행3(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[1,2], visible=True, arg3=100, delay=50, scale=2)
        self.set_mesh(triggerIds=[3,4,5,6], visible=True, arg3=200, delay=50, scale=2)
        self.set_mesh(triggerIds=[7,8,9,10,11,12], visible=True, arg3=300, delay=50, scale=2)
        self.set_mesh(triggerIds=[13,14,15,16,17,18,19,20], visible=True, arg3=400, delay=50, scale=2)
        self.set_mesh(triggerIds=[21,22,23,24,25,26,27,28,29,30], visible=True, arg3=500, delay=50, scale=2)
        self.set_mesh(triggerIds=[31,32,33,34,35,36,37,38,39,40,41,42], visible=True, arg3=600, delay=50, scale=2)
        self.set_mesh(triggerIds=[43,44,45,46,47,48,49,50,51,52,53,54], visible=True, arg3=700, delay=50, scale=2)
        self.set_mesh(triggerIds=[55,56,57,58,59,60,61,62,63,64], visible=True, arg3=800, delay=50, scale=2)
        self.set_mesh(triggerIds=[65,66,67,68,69,70,71,72], visible=True, arg3=900, delay=50, scale=2)
        self.set_mesh(triggerIds=[73,74,75,76], visible=True, arg3=1000, delay=50, scale=2)
        self.show_guide_summary(entityId=20003281, textId=20003281)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_timer(timerId='100', seconds=5)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='100'):
            return 종료2(self.ctx)


class 종료2(common.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=20003281)


initial_state = 대기
