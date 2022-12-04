""" trigger/02000328_bf/event2.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[101], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[999998]):
            return 진행1(self.ctx)


class 진행1(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 진행2(self.ctx)


class 진행2(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[1201,1202,1203,1204,1205]):
            return 진행3(self.ctx)


class 진행3(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[101,102], visible=True, arg3=100, delay=50, scale=2)
        self.set_mesh(triggerIds=[103,104,105,106], visible=True, arg3=200, delay=50, scale=2)
        self.set_mesh(triggerIds=[107,108,109,110,111,112], visible=True, arg3=300, delay=50, scale=2)
        self.set_mesh(triggerIds=[113,114,115,116,117,118,119,120], visible=True, arg3=400, delay=50, scale=2)
        self.set_mesh(triggerIds=[121,122,123,124,125,126,127,128,129,130], visible=True, arg3=500, delay=50, scale=2)
        self.set_mesh(triggerIds=[131,132,133,134,135,136,137,138,139,140,141,142], visible=True, arg3=600, delay=50, scale=2)
        self.set_mesh(triggerIds=[143,144,145,146,147,148,149,150,151,152,153,154], visible=True, arg3=700, delay=50, scale=2)
        self.set_mesh(triggerIds=[155,156,157,158,159,160,161,162,163,164], visible=True, arg3=800, delay=50, scale=2)
        self.set_mesh(triggerIds=[165,166,167,168,169,170,171,172], visible=True, arg3=900, delay=50, scale=2)
        self.set_mesh(triggerIds=[173,174,175,176], visible=True, arg3=1000, delay=50, scale=2)
        self.show_guide_summary(entityId=20003281, textId=20003281)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_timer(timerId='100', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='100'):
            return 종료2(self.ctx)


class 종료2(trigger_api.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=20003281)


initial_state = 대기
