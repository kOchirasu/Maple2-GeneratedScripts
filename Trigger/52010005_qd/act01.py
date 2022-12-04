""" trigger/52010005_qd/act01.xml """
import trigger_api


class 퀘스트조건01(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101], animationEffect=True)
        self.set_interact_object(triggerIds=[10000872], state=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[10002820], questStates=[2]):
            return Q1_마샤르교체01(self.ctx)


# 1st Quest
class Q1_마샤르교체01(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.destroy_monster(spawnIds=[101])
        self.create_monster(spawnIds=[102], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return Q1_딜레이01(self.ctx)


class Q1_딜레이01(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return Q1_미카등장(self.ctx)


class Q1_미카등장(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[201], animationEffect=False)
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_2010')

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return Q1_마샤르이동01(self.ctx)


class Q1_마샤르이동01(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_1020')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=8001, spawnIds=[102]):
            return Q1_마샤르대화01(self.ctx)


class Q1_마샤르대화01(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=102, script='$52010005_QD__ACT01__0$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=8002, spawnIds=[102]):
            return Q1_마샤르대화02(self.ctx)


class Q1_마샤르대화02(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='4', seconds=3)
        self.set_conversation(type=1, spawnId=102, script='$52010005_QD__ACT01__1$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='4'):
            return Q1_카메라연출01(self.ctx)


class Q1_카메라연출01(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=3)
        self.destroy_monster(spawnIds=[102])
        self.create_monster(spawnIds=[104], animationEffect=False)
        self.select_camera(triggerId=1001, enable=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return Q1_카메라연출02(self.ctx)


class Q1_카메라연출02(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='6', seconds=5)
        self.destroy_monster(spawnIds=[201])
        self.create_monster(spawnIds=[202], animationEffect=False)
        self.set_conversation(type=2, spawnId=11001285, script='$52010005_QD__ACT01__2$', arg4=4)
        self.set_skip(state=Q1_카메라연출03)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='6'):
            return Q1_카메라연출03(self.ctx)

    def on_exit(self):
        self.remove_cinematic_talk()


class Q1_카메라연출03(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='7', seconds=1)
        self.select_camera(triggerId=1001, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='7'):
            return Q1_마샤르교체02(self.ctx)


class Q1_마샤르교체02(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[104])
        self.create_monster(spawnIds=[103], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[10002821], questStates=[2]):
            return Q1_퇴장(self.ctx)


class Q1_퇴장(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[103])
        self.destroy_monster(spawnIds=[202])
        self.create_monster(spawnIds=[101], animationEffect=True)


initial_state = 퀘스트조건01
