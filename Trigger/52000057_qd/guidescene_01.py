""" trigger/52000057_qd/guidescene_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[1003], animationEffect=False)
        self.set_effect(triggerIds=[601], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[199], questIds=[90000611], questStates=[2]):
            return 오필리아리젠(self.ctx)
        if self.quest_user_detected(boxIds=[199], questIds=[90000611], questStates=[1]):
            return 오필리아리젠(self.ctx)
        if self.quest_user_detected(boxIds=[199], questIds=[90000610], questStates=[3]):
            return 오필리아리젠상시(self.ctx)
        if self.quest_user_detected(boxIds=[199], questIds=[90000610], questStates=[2]):
            return 오필리아리젠상시(self.ctx)
        if self.quest_user_detected(boxIds=[199], questIds=[90000610], questStates=[1]):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=301, enable=True)
        self.create_monster(spawnIds=[1001], animationEffect=False)
        self.set_effect(triggerIds=[601], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 말풍선대사01(self.ctx)


class 말풍선대사01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=198, spawnIds=[1001]):
            return 시네마틱대사01(self.ctx)


class 시네마틱대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11001871, script='$52000057_QD__GUIDESCENE_01__0$', arg4=2, arg5=0)
        self.set_conversation(type=2, spawnId=11001871, script='$52000057_QD__GUIDESCENE_01__1$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=301, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 연퀘감지(self.ctx)


class 연퀘감지(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[199], questIds=[90000611], questStates=[1]):
            return 오필리아대사연출01(self.ctx)


class 오필리아리젠(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[1002], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 오필리아대사연출01(self.ctx)


class 오필리아대사연출01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_conversation(type=2, spawnId=11001871, script='$52000057_QD__GUIDESCENE_01__2$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return SendSignalToGuide01(self.ctx)


# 트리거 To가이드
class SendSignalToGuide01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.guide_event(eventId=60660)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 종료(self.ctx)


class 오필리아리젠상시(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[1002], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[199], questIds=[90000611], questStates=[1]):
            return 오필리아대사연출01(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = 대기
