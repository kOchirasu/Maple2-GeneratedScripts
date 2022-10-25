""" trigger/02000328_bf/event3.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[201], visible=False, arg3=0, delay=0, scale=0)

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
        self.set_mesh(triggerIds=[201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1301,1302,1303,1304,1305]):
            return 진행3(self.ctx)


class 진행3(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[201,202], visible=True, arg3=100, delay=50, scale=2)
        self.set_mesh(triggerIds=[203,204,205,206], visible=True, arg3=200, delay=50, scale=2)
        self.set_mesh(triggerIds=[207,208,209,210,211,212], visible=True, arg3=300, delay=50, scale=2)
        self.set_mesh(triggerIds=[213,214,215,216,217,218,219,220], visible=True, arg3=400, delay=50, scale=2)
        self.set_mesh(triggerIds=[221,222,223,224,225,226,227,228,229,230], visible=True, arg3=500, delay=50, scale=2)
        self.set_mesh(triggerIds=[231,232,233,234,235,236,237,238,239,240,241,242], visible=True, arg3=600, delay=50, scale=2)
        self.set_mesh(triggerIds=[243,244,245,246,247,248,249,250,251,252,253,254], visible=True, arg3=700, delay=50, scale=2)
        self.set_mesh(triggerIds=[255,256,257,258,259,260,261,262,263,264], visible=True, arg3=800, delay=50, scale=2)
        self.set_mesh(triggerIds=[265,266,267,268,269,270,271,272], visible=True, arg3=900, delay=50, scale=2)
        self.set_mesh(triggerIds=[273,274,275,276], visible=True, arg3=1000, delay=50, scale=2)
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
