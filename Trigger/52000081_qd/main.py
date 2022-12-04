""" trigger/52000081_qd/main.xml """
import trigger_api


class start(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[601], visible=False)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001532], questStates=[1]):
            return 연출01시작(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50100230], questStates=[1]):
            return 연출01시작(self.ctx)


class 연출01시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            self.move_user_path(patrolName='MS2PatrolData_PC_01')
            return PC말풍선01(self.ctx)


class PC말풍선01(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$52000081_QD__MAIN__0$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return PC말풍선02(self.ctx)


class PC말풍선02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$52000081_QD__MAIN__1$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return PC말풍선03(self.ctx)


class PC말풍선03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$52000081_QD__MAIN__2$', arg4=1, arg5=0)
        self.set_pc_emotion_loop(sequenceName='Push_A', duration=10000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 감옥이펙트(self.ctx)


class 감옥이펙트(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[601], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몹소환(self.ctx)


class 몹소환(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$52000081_QD__MAIN__3$', arg4=2, arg5=0)
        self.set_pc_emotion_loop(sequenceName='Push_A', duration=15000)
        self.create_monster(spawnIds=[1001,1003,1004], animationEffect=False) # 연출용 어둠의 세력 몬스터

    def on_tick(self) -> trigger_api.Trigger:
        if not self.monster_dead(boxIds=[1001,1003,1004]):
            return 검사등장(self.ctx)
        if self.monster_dead(boxIds=[1001,1003,1004]):
            return PC구출01(self.ctx)


class 검사등장(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8001], returnView=False)
        self.create_monster(spawnIds=[1002], animationEffect=False) # 연출용 의문의 검사
        self.move_npc(spawnId=1002, patrolName='MS2PatrolData_NPC_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[1001]):
            return PC구출01(self.ctx)
        if self.wait_tick(waitTick=15000):
            return 예비용00(self.ctx)


class 예비용00(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1001,1003,1004])
        self.move_npc(spawnId=1002, patrolName='MS2PatrolData_NPC_02')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return PC구출01(self.ctx)


class PC구출01(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=1002, patrolName='MS2PatrolData_NPC_02')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return PC구출02(self.ctx)


class PC구출02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8002], returnView=False)
        self.move_npc(spawnId=1002, patrolName='MS2PatrolData_NPC_02_1')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return PC구출03(self.ctx)


class PC구출03(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_loop(spawnId=1002, sequenceName='Attack_01_D', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return PC구출04(self.ctx)


class PC구출04(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[601], visible=False)
        self.set_pc_emotion_loop(sequenceName='Idle_A', duration=10000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 검사대화01(self.ctx)


class 검사대화01(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_loop(spawnId=1002, sequenceName='Bore_A', duration=1500)
        self.add_cinematic_talk(npcId=11004022, illustId='11004022', msg='$52000081_QD__MAIN__4$', align='left', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 검사대화02(self.ctx)


class 검사대화02(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11004022, illustId='11004022', msg='$52000081_QD__MAIN__5$', align='left', duration=3000)
        self.move_npc(spawnId=1002, patrolName='MS2PatrolData_NPC_03')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return PC말풍선04(self.ctx)


class PC말풍선04(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8004,8005], returnView=False)
        self.set_conversation(type=1, spawnId=0, script='$52000081_QD__MAIN__6$', arg4=3, arg5=0)
        self.move_user_path(patrolName='MS2PatrolData_PC_02')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return PC말풍선05(self.ctx)


class PC말풍선05(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$52000081_QD__MAIN__7$', arg4=3, arg5=0)
        self.move_npc(spawnId=1002, patrolName='MS2PatrolData_NPC_04')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 검사대화03(self.ctx)


class 검사대화03(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11004022, illustId='11004022', msg='$52000081_QD__MAIN__17$', align='left', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return PC말풍선06(self.ctx)


class PC말풍선06(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$52000081_QD__MAIN__8$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return PC말풍선07(self.ctx)


class PC말풍선07(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$52000081_QD__MAIN__9$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return PC말풍선08(self.ctx)


class PC말풍선08(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$52000081_QD__MAIN__10$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 검사대화04(self.ctx)


class 검사대화04(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11004022, illustId='11004022', msg='$52000081_QD__MAIN__11$', align='left', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 검사대화05(self.ctx)


class 검사대화05(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11004022, illustId='11004022', msg='$52000081_QD__MAIN__12$', align='left', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 검사대화06(self.ctx)


class 검사대화06(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11004022, illustId='11004022', msg='$52000081_QD__MAIN__13$', align='left', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 검사퇴장01(self.ctx)


class 검사퇴장01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8003], returnView=False)
        self.move_npc(spawnId=1002, patrolName='MS2PatrolData_NPC_05')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 검사대화07(self.ctx)


class 검사대화07(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11004022, illustId='11004022', msg='$52000081_QD__MAIN__14$', align='left', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 검사대화08(self.ctx)


class 검사대화08(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11004022, illustId='11004022', msg='$52000081_QD__MAIN__15$', align='left', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 검사대화09(self.ctx)


class 검사대화09(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11004022, illustId='11004022', msg='$52000081_QD__MAIN__16$', align='left', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 검사퇴장02(self.ctx)


class 검사퇴장02(trigger_api.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=3)
        self.move_npc(spawnId=1002, patrolName='MS2PatrolData_NPC_06')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1002])
        self.set_achievement(triggerId=9000, type='trigger', achieve='meetarcaneblader1st')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = start
