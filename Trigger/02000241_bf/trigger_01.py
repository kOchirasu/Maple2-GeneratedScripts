""" trigger/02000241_bf/trigger_01.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[201]):
            return 벽삭제(self.ctx)


class 벽삭제(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199], visible=False)
        self.set_timer(timerId='5', seconds=5, startDelay=0)
        self.show_guide_summary(entityId=20002411, textId=20002411)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='5'):
            self.hide_guide_summary(entityId=20002411)
            return 벽재생(self.ctx)


class 벽재생(common.Trigger):
    pass


initial_state = 대기
