""" trigger/52000043_qd/50001451.xml """
import trigger_api


class 시작조건(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[601], visible=False)
        self.set_effect(triggerIds=[602], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[199], questIds=[50001451], questStates=[1]):
            return 연출시작(self.ctx)
        if self.quest_user_detected(boxIds=[199], questIds=[50001451], questStates=[2]):
            return NPC만배치(self.ctx)


class NPC만배치(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1001,2001], animationEffect=False)
        self.set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=301, enable=True)
        self.create_monster(spawnIds=[1001,2001], animationEffect=False)
        self.set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 카메라딜레이(self.ctx)


class 카메라딜레이(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=302, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 준타대사01(self.ctx)


class 준타대사01(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001557, script='$52000043_QD__50001451__0$', arg4=3)
        self.set_skip(state=준타대사01스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 틴차이대사01(self.ctx)


class 준타대사01스킵(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 틴차이대사01(self.ctx)


class 틴차이대사01(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001708, script='$52000043_QD__50001451__1$', arg4=4)
        self.set_skip(state=틴차이대사01스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 준타대사02(self.ctx)


class 틴차이대사01스킵(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 준타대사02(self.ctx)


class 준타대사02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001557, script='$52000043_QD__50001451__2$', arg4=3)
        self.set_skip(state=준타대사02스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 준타대사03(self.ctx)


class 준타대사02스킵(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 준타대사03(self.ctx)


class 준타대사03(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[601], visible=True)
        self.set_conversation(type=2, spawnId=11001557, script='$52000043_QD__50001451__3$', arg4=4)
        self.set_skip(state=준타대사03스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 틴차이대사02(self.ctx)


class 준타대사03스킵(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[601], visible=False)
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 틴차이대사02(self.ctx)


class 틴차이대사02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001708, script='$52000043_QD__50001451__4$', arg4=5)
        self.set_skip(state=틴차이대사02스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 준타대사04(self.ctx)


class 틴차이대사02스킵(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 준타대사04(self.ctx)


class 준타대사04(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[602], visible=True)
        self.set_conversation(type=2, spawnId=11001557, script='$52000043_QD__50001451__5$', arg4=2)
        self.set_skip(state=준타대사04스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 연출종료(self.ctx)


class 준타대사04스킵(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[602], visible=False)
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=302, enable=False)
        self.set_achievement(triggerId=199, type='trigger', achieve='gdworry')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작조건
