""" trigger/52000045_qd/main_01.xml """
import trigger_api


class ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[701], jobCode=110):
            self.set_effect(triggerIds=[7001], visible=True)
            return start(self.ctx)


class start(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.create_monster(spawnIds=[101], animationEffect=False) # 비전
        self.add_buff(boxIds=[701], skillId=70000105, level=1) # 투명 버프를 걸어준다
        self.set_conversation(type=2, spawnId=11001560, script='$52000045_QD__MAIN_01__0$', arg4=5)
        self.create_monster(spawnIds=[201,202,203,204,205,206], animationEffect=False)
        self.create_monster(spawnIds=[301,302,303,304,305,306], animationEffect=False)
        self.create_monster(spawnIds=[401,402,403,404,405], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return start_02(self.ctx)


class start_02(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_2001')
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_2001')
        self.move_npc(spawnId=202, patrolName='MS2PatrolData_2001')
        self.move_npc(spawnId=203, patrolName='MS2PatrolData_2001')
        self.move_npc(spawnId=204, patrolName='MS2PatrolData_2001')
        self.move_npc(spawnId=205, patrolName='MS2PatrolData_2001')
        self.move_npc(spawnId=206, patrolName='MS2PatrolData_2001')
        self.move_npc(spawnId=301, patrolName='MS2PatrolData_2001')
        self.move_npc(spawnId=302, patrolName='MS2PatrolData_2001')
        self.move_npc(spawnId=303, patrolName='MS2PatrolData_2001')
        self.move_npc(spawnId=304, patrolName='MS2PatrolData_2001')
        self.move_npc(spawnId=305, patrolName='MS2PatrolData_2001')
        self.move_npc(spawnId=306, patrolName='MS2PatrolData_2001')
        self.select_camera_path(pathIds=[8001,8002,8003], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return start_03(self.ctx)


class start_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001560, script='$52000045_QD__MAIN_01__1$', arg4=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            self.create_monster(spawnIds=[101], animationEffect=False)
            self.remove_buff(boxId=701, skillId=70000105)
            self.select_camera_path(pathIds=[8004], returnView=True)
            self.destroy_monster(spawnIds=[101])
            self.destroy_monster(spawnIds=[401,402,403,404,405])
            self.set_actor(triggerId=5001, visible=False, initialSequence='Idle_A')
            self.set_actor(triggerId=5002, visible=False, initialSequence='Idle_A')
            self.set_actor(triggerId=5003, visible=False, initialSequence='Idle_A')
            self.set_cinematic_ui(type=4)
            return start_04(self.ctx)


class start_04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            self.set_effect(triggerIds=[7001], visible=False)
            self.add_buff(boxIds=[701], skillId=70000094, level=1)
            self.set_pc_emotion_loop(sequenceName='Down_Idle_A', duration=4000)
            self.set_cinematic_ui(type=1)
            self.set_cinematic_ui(type=3)
            return start_05(self.ctx)


class start_05(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4500):
            self.set_pc_emotion_sequence(sequenceNames=['Emotion_Failure_Idle_A'])
            return start_06(self.ctx)


class start_06(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_effect(triggerIds=[7002], visible=True)
            self.move_user_path(patrolName='MS2PatrolData_2002')
            return start_07(self.ctx)


class start_07(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return start_08(self.ctx)


class start_08(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8005], returnView=False)
        self.create_monster(spawnIds=[901], animationEffect=False) # 스커
        self.move_user_path(patrolName='MS2PatrolData_2004') # 유저를 이동시킨다
        self.move_npc(spawnId=901, patrolName='MS2PatrolData_2003')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return start_09(self.ctx)


class start_09(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=901, script='$52000045_QD__MAIN_01__2$', arg4=4, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return start_A_10(self.ctx)


class start_A_10(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=901, script='$52000045_QD__MAIN_01__11$', arg4=3)
        self.set_conversation(type=1, spawnId=0, script='$52000045_QD__MAIN_01__12$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return start_10(self.ctx)


class start_10(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$52000045_QD__MAIN_01__3$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            self.set_effect(triggerIds=[7003], visible=True)
            self.move_npc(spawnId=901, patrolName='MS2PatrolData_2005')
            return start_11(self.ctx)


class start_11(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[801,802,803,804,805,806], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return start_12(self.ctx)


class start_12(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8004], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return start_13(self.ctx)


class start_13(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7004], visible=True)
        self.select_camera_path(pathIds=[8004], returnView=True)
        self.create_monster(spawnIds=[809], animationEffect=False)
        self.set_npc_emotion_loop(spawnId=901, sequenceName='Down_Idle_A', duration=300000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            self.show_guide_summary(entityId=25200473, textId=25200473)
            self.set_cinematic_ui(type=0)
            self.set_cinematic_ui(type=2)
            return start_14(self.ctx)


class start_14(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[801,802,803,804,805,806,809]):
            self.hide_guide_summary(entityId=25200473)
            return start_15(self.ctx)


class start_15(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return start_16(self.ctx)


class start_16(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[7701,7702], animationEffect=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            self.select_camera_path(pathIds=[8004], returnView=False)
            return start_17(self.ctx)


class start_17(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_loop(spawnId=7702, sequenceName='Talk_A', duration=3000)
        self.set_conversation(type=2, spawnId=11001545, script='$52000045_QD__MAIN_01__4$', arg4=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return start_18(self.ctx)


class start_18(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_loop(spawnId=7701, sequenceName='Talk_A', duration=3000)
        self.set_conversation(type=2, spawnId=11001546, script='$52000045_QD__MAIN_01__5$', arg4=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            self.move_user_path(patrolName='MS2PatrolData_2006')
            self.move_npc(spawnId=7701, patrolName='MS2PatrolData_7003')
            self.move_npc(spawnId=7702, patrolName='MS2PatrolData_7004')
            return start_19(self.ctx)


class start_19(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            self.select_camera_path(pathIds=[8005], returnView=False)
            return start_20(self.ctx)


class start_20(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=7701, script='$52000045_QD__MAIN_01__6$', arg4=3, arg5=0)
        self.set_conversation(type=1, spawnId=7702, script='$52000045_QD__MAIN_01__7$', arg4=3, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return start_21(self.ctx)


class start_21(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$52000045_QD__MAIN_01__8$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=0, script='$52000045_QD__MAIN_01__9$', arg4=3, arg5=2)
        self.set_conversation(type=1, spawnId=0, script='$52000045_QD__MAIN_01__10$', arg4=3, arg5=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return start_22(self.ctx)


class start_22(trigger_api.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_2007') # 유저를 이동시킨다

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_achievement(triggerId=701, type='trigger', achieve='MeetAgainStriker')
            self.move_user(mapId=2000138, portalId=103)
            return start_22(self.ctx)


initial_state = ready
