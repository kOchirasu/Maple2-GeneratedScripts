""" trigger/02000351_bf/lever_check.xml """
import common


class 레버체크(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000819], state=0)
        self.set_interact_object(triggerIds=[10000820], state=0)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000819], stateValue=1):
            return 레버체크2(self.ctx)
        if self.object_interacted(interactIds=[10000820], stateValue=1):
            return 레버체크2(self.ctx)


class 레버체크2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000820], stateValue=0):
            return 레버체크3_1개(self.ctx)
        if self.object_interacted(interactIds=[10000819], stateValue=0):
            return 레버체크4_1개(self.ctx)


class 레버체크3_1개(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000819], stateValue=0):
            return 레버체크완료(self.ctx)


class 레버체크4_1개(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000820], stateValue=0):
            return 레버체크완료(self.ctx)


class 레버체크완료(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='3'):
            return 열림(self.ctx)


class 열림(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=2)
        self.set_mesh(triggerIds=[6005], visible=False, delay=0, scale=10) # 벽 해제

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='2'):
            return 열림_끝(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)


class 열림_끝(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3)
        # <action name="이벤트UI를설정한다" arg1="1" arg2="관문이 개방되었습니다. \n다음 지역으로 이동하십시오." arg3="3000"/>

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='3'):
            return 종료(self.ctx)
        if self.count_users(boxId=704, boxId=1):
            return 종료(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=113)


class 종료(common.Trigger):
    pass


initial_state = 레버체크
