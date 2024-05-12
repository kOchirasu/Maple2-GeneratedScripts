""" trigger/52010005_qd/act02.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9000]):
            self.set_interact_object(triggerIds=[10000872], state=0)
            return 퀘스트조건02(self.ctx)


class 퀘스트조건02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[10002821], questStates=[2]):
            # 2nd Quest
            return Q2_미카등장01(self.ctx)


# 2nd Quest
class Q2_미카등장01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[401], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return Q2_딜레이01(self.ctx)


class Q2_딜레이01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='11', seconds=2)
        self.select_camera(triggerId=3001, enable=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='11'):
            return Q2_미카대화01(self.ctx)


class Q2_미카대화01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='12', seconds=3)
        self.set_conversation(type=2, spawnId=11001285, script='$52010005_QD__ACT02__0$', arg4=3)
        self.set_skip(state=Q2_미카대화02대기)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='12'):
            return Q2_미카대화02대기(self.ctx)


class Q2_미카대화02대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return Q2_미카대화02(self.ctx)


class Q2_미카대화02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='13', seconds=3)
        self.set_conversation(type=2, spawnId=11001285, script='$52010005_QD__ACT02__1$', arg4=3)
        self.set_skip(state=Q2_미카대화종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='13'):
            return Q2_미카대화종료(self.ctx)


class Q2_미카대화종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.select_camera(triggerId=3001, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = 대기
