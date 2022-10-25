""" trigger/52000040_qd/main_02.xml """
import common


# 출연진 : 라오즈(401 : 11001760)
class ready(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=4, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=3, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[10003053], questStates=[1]):
            return end(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[10003053], questStates=[2]):
            return end(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[10003053], questStates=[3]):
            return end(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[10003052], questStates=[3]):
            return start_05(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[10003052], questStates=[2]):
            return start_05(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[10003052], questStates=[1]):
            self.set_effect(triggerIds=[6002], visible=True)
            self.create_monster(spawnIds=[401], animationEffect=False)
            return start(self.ctx)


class start(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return start_02(self.ctx)


class start_02(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=401, script='$52000040_QD__MAIN_02__0$', arg4=2, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return start_03(self.ctx)


class start_03(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=401, script='$52000040_QD__MAIN_02__1$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=401, script='$52000040_QD__MAIN_02__2$', arg4=2, arg5=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            self.move_npc(spawnId=401, patrolName='MS2PatrolData_4001')
            self.set_cinematic_ui(type=0)
            self.set_cinematic_ui(type=2)
            return start_04(self.ctx)


class start_04(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=702, spawnIds=[401]):
            return npc_exit_01(self.ctx)


class npc_exit_01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6001], visible=True)
        self.destroy_monster(spawnIds=[401])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return start_05(self.ctx)


class start_05(common.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=701, type='trigger', achieve='FollowingLaoz') # 퀘스트 목표 체크용 업적이벤트 발생
        self.create_monster(spawnIds=[501], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[10003053], questStates=[1]):
            return end(self.ctx)


class end(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[501])
        self.set_portal(portalId=3, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=4, visible=True, enable=False, minimapVisible=False)


initial_state = ready
