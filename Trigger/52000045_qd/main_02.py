""" trigger/52000045_qd/main_02.xml """
import trigger_api


class ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[701], jobCode=100):
            self.set_actor(triggerId=5001, visible=False, initialSequence='Idle_A')
            self.set_actor(triggerId=5002, visible=False, initialSequence='Idle_A')
            self.set_actor(triggerId=5003, visible=False, initialSequence='Idle_A')
            return ready_02(self.ctx)


class ready_02(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000045, portalId=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return start(self.ctx)


class start(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[902], animationEffect=False) # 로스트차일드
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user_path(patrolName='MS2PatrolData_2010') # 유저를 이동시킨다
        self.select_camera_path(pathIds=[8004], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return start_02(self.ctx)


class start_02(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=902, patrolName='MS2PatrolData_2004')
        self.move_user_path(patrolName='MS2PatrolData_2003') # 유저를 이동시킨다
        self.select_camera_path(pathIds=[8010], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return setup_userscript01(self.ctx)


class setup_userscript01(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$52000045_QD__MAIN_02__0$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return start_A_03(self.ctx)


class start_A_03(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8010,8013], returnView=False)
        self.set_conversation(type=1, spawnId=0, script='$52000045_QD__MAIN_02__3$', arg4=3)
        self.set_conversation(type=1, spawnId=902, script='$52000045_QD__MAIN_02__4$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return start_03(self.ctx)


class start_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=902, script='$52000045_QD__MAIN_02__1$', arg4=3, arg5=1)
        self.set_npc_emotion_loop(spawnId=902, sequenceName='Talk_A', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return start_04(self.ctx)


class start_04(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7003], visible=True)
        self.create_monster(spawnIds=[887,886,888], animationEffect=False)
        self.set_conversation(type=1, spawnId=902, script='$52000045_QD__MAIN_02__5$', arg4=1, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return start_05(self.ctx)


class start_05(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8014], returnView=False)
        self.set_conversation(type=1, spawnId=0, script='$52000045_QD__MAIN_02__6$', arg4=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2200):
            return start_06(self.ctx)


class start_06(trigger_api.Trigger):
    def on_enter(self):
        self.set_pc_emotion_sequence(sequenceNames=['Down2_A','Down_Idle_A','Down_Idle_A','Down_Idle_A','Down_Idle_A','Down_Idle_A'])
        self.set_effect(triggerIds=[7005], visible=True)
        self.set_effect(triggerIds=[7004], visible=True)
        self.create_monster(spawnIds=[872,873], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2050):
            return start_07(self.ctx)


class start_07(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8014,8015], returnView=False)
        self.create_monster(spawnIds=[871,876], animationEffect=False)
        self.set_pc_emotion_loop(sequenceName='Down_Idle_A', duration=80000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=900):
            return start_08(self.ctx)


class start_08(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[872,875,871,876], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return start_09(self.ctx)


class start_09(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7005], visible=False)
        self.create_monster(spawnIds=[874,873,872], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return start_10(self.ctx)


class start_10(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return end(self.ctx)


class end(trigger_api.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=701, type='trigger', achieve='InvestgatedScretroom') # 퀘스트 목표 체크용 업적이벤트 발생
        self.move_user(mapId=52000046, portalId=1)


initial_state = ready
