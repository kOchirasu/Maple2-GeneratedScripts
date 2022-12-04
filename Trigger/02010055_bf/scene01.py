""" trigger/02010055_bf/scene01.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[699], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[105]):
            return 바르칸트대사(self.ctx)


class 바르칸트대사(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=301, enable=True)
        self.set_effect(triggerIds=[699], visible=True)
        self.set_conversation(type=2, spawnId=23000068, script='$02010055_BF__SCENE01__0$', arg4=4)
        self.set_skip(state=바르칸트대사2스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 바르칸트대사2(self.ctx)


class 바르칸트대사2스킵(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 바르칸트대사2(self.ctx)


class 바르칸트대사2(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=301, enable=True)
        self.set_effect(triggerIds=[699], visible=True)
        self.set_conversation(type=2, spawnId=23000068, script='$02010055_BF__SCENE01__1$', arg4=4)
        self.set_skip(state=종료준비)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4500):
            return 종료(self.ctx)


class 종료준비(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=301, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = 시작대기중
