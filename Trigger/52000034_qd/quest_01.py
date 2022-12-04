""" trigger/52000034_qd/quest_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[101], questIds=[40002600], questStates=[3]):
            return 기본NPC배치(self.ctx)
        if not self.quest_user_detected(boxIds=[101], questIds=[40002600], questStates=[3]):
            return 제이시추가배치(self.ctx)


class 제이시추가배치(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2001,2002,2003], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[101], questIds=[40002603], questStates=[2]):
            return 연출01시작(self.ctx)
        if not self.quest_user_detected(boxIds=[101], questIds=[40002603], questStates=[2]):
            return 종료(self.ctx)


class 기본NPC배치(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2001,2002], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 종료(self.ctx)


class 연출01시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=301, enable=True)
        self.destroy_monster(spawnIds=[2001,2002,2003])
        self.create_monster(spawnIds=[1001,1002,1003], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 자베스대사01(self.ctx)


class 자베스대사01(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001546, script='$52000034_QD__QUEST_01__0$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 자베스대사02(self.ctx)


class 자베스대사02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001546, script='$52000034_QD__QUEST_01__1$', arg4=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 브라보대사01(self.ctx)


class 브라보대사01(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001545, script='$52000034_QD__QUEST_01__2$', arg4=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 브라보대사02(self.ctx)


class 브라보대사02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001545, script='$52000034_QD__QUEST_01__3$', arg4=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 브라보대사03(self.ctx)


class 브라보대사03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001545, script='$52000034_QD__QUEST_01__4$', arg4=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 자베스대사03(self.ctx)


class 자베스대사03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001546, script='$52000034_QD__QUEST_01__5$', arg4=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 자베스대사04(self.ctx)


class 자베스대사04(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001546, script='$52000034_QD__QUEST_01__6$', arg4=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 브라보대사04(self.ctx)


class 브라보대사04(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001545, script='$52000034_QD__QUEST_01__7$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 브라보대사05(self.ctx)


class 브라보대사05(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001545, script='$52000034_QD__QUEST_01__8$', arg4=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 자베스대사05(self.ctx)


class 자베스대사05(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001546, script='$52000034_QD__QUEST_01__9$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 자베스대사06(self.ctx)


class 자베스대사06(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001546, script='$52000034_QD__QUEST_01__10$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 브라보대사06(self.ctx)


class 브라보대사06(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001545, script='$52000034_QD__QUEST_01__11$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 브라보대사07(self.ctx)


class 브라보대사07(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001545, script='$52000034_QD__QUEST_01__12$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 잠시대기(self.ctx)


class 잠시대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 제이시대사01(self.ctx)


class 제이시대사01(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001690, script='$52000034_QD__QUEST_01__13$', arg4=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 연출01종료(self.ctx)


class 연출01종료(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.select_camera(triggerId=301, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.destroy_monster(spawnIds=[1003])
        self.create_monster(spawnIds=[2003], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
