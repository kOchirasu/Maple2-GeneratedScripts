""" trigger/52010018_qd/main_2.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3000], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3001], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3002], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3003], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3004], visible=False, arg3=0, delay=0, scale=0)
        self.set_actor(triggerId=201, visible=False, initialSequence='Eff_MassiveEvent_Door_Vanished')
        self.set_actor(triggerId=202, visible=False, initialSequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(triggerId=203, visible=False, initialSequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(triggerId=204, visible=False, initialSequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(triggerId=205, visible=False, initialSequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(triggerId=206, visible=False, initialSequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(triggerId=207, visible=False, initialSequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(triggerId=208, visible=False, initialSequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(triggerId=209, visible=False, initialSequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(triggerId=210, visible=False, initialSequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(triggerId=211, visible=False, initialSequence='Eff_MassiveEvent_Stair_Closed')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[100], questIds=[10002853], questStates=[1]):
            return 미카이동02(self.ctx)


class 미카이동02(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=302, enable=True)
        self.destroy_monster(spawnIds=[1005])
        self.create_monster(spawnIds=[1007], animationEffect=False)
        self.move_npc(spawnId=1007, patrolName='MS2PatrolData_1007_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=104, spawnIds=[1007]):
            return 다리생성대기(self.ctx)


class 다리생성대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            self.set_mesh(triggerIds=[3000], visible=False, arg3=0, delay=0, scale=0)
            self.set_mesh(triggerIds=[3001], visible=True, arg3=0, delay=0, scale=0)
            self.set_mesh(triggerIds=[3003], visible=False, arg3=0, delay=0, scale=0)
            self.set_mesh(triggerIds=[3004], visible=True, arg3=0, delay=0, scale=0)
            return 다리생성(self.ctx)


class 다리생성(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_actor(triggerId=201, visible=True, initialSequence='Eff_MassiveEvent_Door_Opened')
            self.set_actor(triggerId=202, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
            self.set_actor(triggerId=203, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
            self.set_actor(triggerId=204, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
            self.set_actor(triggerId=205, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
            self.set_actor(triggerId=206, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
            self.set_actor(triggerId=207, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
            self.set_actor(triggerId=208, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
            self.set_actor(triggerId=209, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
            self.set_actor(triggerId=210, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
            self.set_actor(triggerId=211, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
            return 미카대사02(self.ctx)


class 미카대사02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001285, script='$52010018_QD__MAIN_2__0$', arg4=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4500):
            return 에레브대사02(self.ctx)


class 에레브대사02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11000075, script='$52010018_QD__MAIN_2__1$', arg4=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4500):
            return 미카대사03(self.ctx)


class 미카대사03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001285, script='$52010018_QD__MAIN_2__2$', arg4=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            self.move_npc(spawnId=1007, patrolName='MS2PatrolData_1007_B')
            return 미카소멸(self.ctx)


class 미카소멸(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            self.set_cinematic_ui(type=0)
            self.set_cinematic_ui(type=2)
            self.select_camera(triggerId=302, enable=False)
            self.destroy_monster(spawnIds=[1007])
            self.set_achievement(triggerId=100, type='trigger', achieve='BacktoDrakenheim')
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            self.set_actor(triggerId=201, visible=False, initialSequence='Eff_MassiveEvent_Door_Vanished')
            self.set_actor(triggerId=202, visible=False, initialSequence='Eff_MassiveEvent_Stair_Closed')
            self.set_actor(triggerId=203, visible=False, initialSequence='Eff_MassiveEvent_Stair_Closed')
            self.set_actor(triggerId=204, visible=False, initialSequence='Eff_MassiveEvent_Stair_Closed')
            self.set_actor(triggerId=205, visible=False, initialSequence='Eff_MassiveEvent_Stair_Closed')
            self.set_actor(triggerId=206, visible=False, initialSequence='Eff_MassiveEvent_Stair_Closed')
            self.set_actor(triggerId=207, visible=False, initialSequence='Eff_MassiveEvent_Stair_Closed')
            self.set_actor(triggerId=208, visible=False, initialSequence='Eff_MassiveEvent_Stair_Closed')
            self.set_actor(triggerId=209, visible=False, initialSequence='Eff_MassiveEvent_Stair_Closed')
            self.set_actor(triggerId=210, visible=False, initialSequence='Eff_MassiveEvent_Stair_Closed')
            self.set_actor(triggerId=211, visible=False, initialSequence='Eff_MassiveEvent_Stair_Closed')
            return 종료2(self.ctx)


class 종료2(trigger_api.Trigger):
    pass


initial_state = 대기
