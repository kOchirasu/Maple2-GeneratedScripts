""" trigger/52000050_qd/main_03.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1001,1002,2001], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[199], questIds=[10003042], questStates=[2]):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=301, enable=True)
        self.add_buff(boxIds=[199], skillId=70000095, level=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 자베스대사01(self.ctx)


class 자베스대사01(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001546, script='$52000050_QD__MAIN_03__0$', arg4=3)
        self.set_skip(state=자베스대사01스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 브라보대사01(self.ctx)


class 자베스대사01스킵(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 브라보대사01(self.ctx)


class 브라보대사01(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001545, script='$52000050_QD__MAIN_03__1$', arg4=3)
        self.set_skip(state=브라보대사01스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 제이시대사01(self.ctx)


class 브라보대사01스킵(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 제이시대사01(self.ctx)


class 제이시대사01(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11000515, script='$52000050_QD__MAIN_03__2$', arg4=5)
        self.set_skip(state=제이시대사01스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 연출종료(self.ctx)


class 제이시대사01스킵(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[2001])
        self.create_monster(spawnIds=[2002], animationEffect=False)
        self.add_buff(boxIds=[199], skillId=70000096, level=1)
        self.move_user(mapId=52000046, portalId=2)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=301, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10):
            self.move_user_path(patrolName='MS2PatrolData_9000')
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
