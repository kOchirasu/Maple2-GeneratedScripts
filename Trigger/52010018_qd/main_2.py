""" trigger/52010018_qd/main_2.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3000], visible=True, start_delay=0, interval=0, fade=0)
        self.set_mesh(trigger_ids=[3001], visible=False, start_delay=0, interval=0, fade=0)
        self.set_mesh(trigger_ids=[3002], visible=True, start_delay=0, interval=0, fade=0)
        self.set_mesh(trigger_ids=[3003], visible=True, start_delay=0, interval=0, fade=0)
        self.set_mesh(trigger_ids=[3004], visible=False, start_delay=0, interval=0, fade=0)
        self.set_actor(trigger_id=201, visible=False, initial_sequence='Eff_MassiveEvent_Door_Vanished')
        self.set_actor(trigger_id=202, visible=False, initial_sequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(trigger_id=203, visible=False, initial_sequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(trigger_id=204, visible=False, initial_sequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(trigger_id=205, visible=False, initial_sequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(trigger_id=206, visible=False, initial_sequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(trigger_id=207, visible=False, initial_sequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(trigger_id=208, visible=False, initial_sequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(trigger_id=209, visible=False, initial_sequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(trigger_id=210, visible=False, initial_sequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(trigger_id=211, visible=False, initial_sequence='Eff_MassiveEvent_Stair_Closed')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[100], quest_ids=[10002853], quest_states=[1]):
            return 미카이동02(self.ctx)


class 미카이동02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=302, enable=True)
        self.destroy_monster(spawn_ids=[1005])
        self.spawn_monster(spawn_ids=[1007], auto_target=False)
        self.move_npc(spawn_id=1007, patrol_name='MS2PatrolData_1007_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=104, spawn_ids=[1007]):
            return 다리생성대기(self.ctx)


class 다리생성대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            self.set_mesh(trigger_ids=[3000], visible=False, start_delay=0, interval=0, fade=0)
            self.set_mesh(trigger_ids=[3001], visible=True, start_delay=0, interval=0, fade=0)
            self.set_mesh(trigger_ids=[3003], visible=False, start_delay=0, interval=0, fade=0)
            self.set_mesh(trigger_ids=[3004], visible=True, start_delay=0, interval=0, fade=0)
            return 다리생성(self.ctx)


class 다리생성(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_actor(trigger_id=201, visible=True, initial_sequence='Eff_MassiveEvent_Door_Opened')
            self.set_actor(trigger_id=202, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
            self.set_actor(trigger_id=203, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
            self.set_actor(trigger_id=204, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
            self.set_actor(trigger_id=205, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
            self.set_actor(trigger_id=206, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
            self.set_actor(trigger_id=207, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
            self.set_actor(trigger_id=208, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
            self.set_actor(trigger_id=209, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
            self.set_actor(trigger_id=210, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
            self.set_actor(trigger_id=211, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
            return 미카대사02(self.ctx)


class 미카대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001285, script='$52010018_QD__MAIN_2__0$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4500):
            return 에레브대사02(self.ctx)


class 에레브대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000075, script='$52010018_QD__MAIN_2__1$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4500):
            return 미카대사03(self.ctx)


class 미카대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001285, script='$52010018_QD__MAIN_2__2$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            self.move_npc(spawn_id=1007, patrol_name='MS2PatrolData_1007_B')
            return 미카소멸(self.ctx)


class 미카소멸(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            self.set_cinematic_ui(type=0)
            self.set_cinematic_ui(type=2)
            self.select_camera(trigger_id=302, enable=False)
            self.destroy_monster(spawn_ids=[1007])
            self.set_achievement(trigger_id=100, type='trigger', achieve='BacktoDrakenheim')
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.set_actor(trigger_id=201, visible=False, initial_sequence='Eff_MassiveEvent_Door_Vanished')
            self.set_actor(trigger_id=202, visible=False, initial_sequence='Eff_MassiveEvent_Stair_Closed')
            self.set_actor(trigger_id=203, visible=False, initial_sequence='Eff_MassiveEvent_Stair_Closed')
            self.set_actor(trigger_id=204, visible=False, initial_sequence='Eff_MassiveEvent_Stair_Closed')
            self.set_actor(trigger_id=205, visible=False, initial_sequence='Eff_MassiveEvent_Stair_Closed')
            self.set_actor(trigger_id=206, visible=False, initial_sequence='Eff_MassiveEvent_Stair_Closed')
            self.set_actor(trigger_id=207, visible=False, initial_sequence='Eff_MassiveEvent_Stair_Closed')
            self.set_actor(trigger_id=208, visible=False, initial_sequence='Eff_MassiveEvent_Stair_Closed')
            self.set_actor(trigger_id=209, visible=False, initial_sequence='Eff_MassiveEvent_Stair_Closed')
            self.set_actor(trigger_id=210, visible=False, initial_sequence='Eff_MassiveEvent_Stair_Closed')
            self.set_actor(trigger_id=211, visible=False, initial_sequence='Eff_MassiveEvent_Stair_Closed')
            return 종료2(self.ctx)


class 종료2(trigger_api.Trigger):
    pass


initial_state = 대기
