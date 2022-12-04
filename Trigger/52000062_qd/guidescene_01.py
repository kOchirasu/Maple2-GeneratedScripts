""" trigger/52000062_qd/guidescene_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1001], animationEffect=False)
        self.create_monster(spawnIds=[1002], animationEffect=False)
        self.create_monster(spawnIds=[1003], animationEffect=False)
        self.create_monster(spawnIds=[1004], animationEffect=False)
        self.create_monster(spawnIds=[1007], animationEffect=False)
        self.set_effect(triggerIds=[601], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 유저감지(self.ctx)


class 유저감지(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[199], questIds=[90000561], questStates=[3]):
            return 종료(self.ctx)
        if self.quest_user_detected(boxIds=[199], questIds=[90000561], questStates=[2]):
            return 연퀘감지2(self.ctx)
        if self.quest_user_detected(boxIds=[199], questIds=[90000560,90000561], questStates=[1]):
            return 연퀘감지(self.ctx)
        if self.user_detected(boxIds=[199]):
            return 페르시카대사01(self.ctx)


class 페르시카대사01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=301, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 페르시카대사02(self.ctx)


class 페르시카대사02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001176, script='$52000062_QD__GUIDESCENE_01__0$', arg4=3, arg5=0)
        self.set_conversation(type=2, spawnId=11001176, script='$52000062_QD__GUIDESCENE_01__1$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=301, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 연퀘감지(self.ctx)


class 연퀘감지(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=1001, patrolName='MS2PatrolData_Fercika')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[199], questIds=[90000561], questStates=[2]):
            return PC이동(self.ctx)


class 연퀘감지2(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=1001, patrolName='MS2PatrolData_Fercika')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return PC이동(self.ctx)


class PC이동(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=301, enable=True)
        self.move_user_path(patrolName='MS2PatrolData_PC')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[198]):
            return 찬양NPC이동(self.ctx)


class 찬양NPC이동(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[601], visible=True)
        self.move_npc(spawnId=1001, patrolName='MS2PatrolData_Fercika2')
        self.create_monster(spawnIds=[1005], animationEffect=False)
        self.destroy_monster(spawnIds=[1002], arg2=False)
        self.create_monster(spawnIds=[1006], animationEffect=False)
        self.destroy_monster(spawnIds=[1004], arg2=False)
        self.create_monster(spawnIds=[1008], animationEffect=False)
        self.destroy_monster(spawnIds=[1007], arg2=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=197, spawnIds=[1001]):
            return 찬양연출(self.ctx)


class 찬양연출(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=1008, script='$52000062_QD__GUIDESCENE_01__2$', arg4=2, arg5=1)
        self.set_conversation(type=1, spawnId=1005, script='$52000062_QD__GUIDESCENE_01__3$', arg4=2, arg5=3)
        self.set_conversation(type=1, spawnId=1006, script='$52000062_QD__GUIDESCENE_01__4$', arg4=2, arg5=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=7000):
            return 연출종료2(self.ctx)


class 연출종료2(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=301, enable=False)
        self.set_effect(triggerIds=[601], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
