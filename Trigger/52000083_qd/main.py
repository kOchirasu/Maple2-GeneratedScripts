""" trigger/52000083_qd/main.xml """
import trigger_api


"""
class start(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001536], questStates=[1]):
            return None # Missing State: 연출대기

"""


class 연출출력체크50001536(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001536], questStates=[1]):
            return 연출시작(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50100260], questStates=[1]):
            return 연출시작(self.ctx)
        if not self.quest_user_detected(boxIds=[9000], questIds=[50001536], questStates=[1]):
            return 조건체크01(self.ctx)
        if not self.quest_user_detected(boxIds=[9000], questIds=[50100260], questStates=[1]):
            return 조건체크01(self.ctx)


class 조건체크01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001536], questStates=[2]):
            return 연출이후(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50100260], questStates=[2]):
            return 연출이후(self.ctx)
        if not self.quest_user_detected(boxIds=[9000], questIds=[50001536], questStates=[2]):
            return 조건체크02(self.ctx)
        if not self.quest_user_detected(boxIds=[9000], questIds=[50100260], questStates=[2]):
            return 조건체크02(self.ctx)


class 조건체크02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001536], questStates=[3]):
            return 조건체크03(self.ctx)
        if not self.quest_user_detected(boxIds=[9000], questIds=[50001536], questStates=[3]):
            return 전투종료후(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50100260], questStates=[3]):
            return 조건체크03(self.ctx)
        if not self.quest_user_detected(boxIds=[9000], questIds=[50100260], questStates=[3]):
            return 조건체크03(self.ctx)


class 조건체크03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001537], questStates=[1]):
            return 연출이후(self.ctx)
        if not self.quest_user_detected(boxIds=[9000], questIds=[50001537], questStates=[1]):
            return 연출이후(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50100270], questStates=[1]):
            return 연출이후(self.ctx)
        if not self.quest_user_detected(boxIds=[9000], questIds=[50100270], questStates=[1]):
            return 연출이후(self.ctx)


"""
class 조건체크04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001537], questStates=[2]):
            return 연출이후(self.ctx)
        if not self.quest_user_detected(boxIds=[9000], questIds=[50001537], questStates=[2]):
            return None # Missing State: 빈방

"""


class 연출이후(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[1002], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 종료(self.ctx)


class 전투종료후(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 연출종료(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[1001], animationEffect=False) # 스턴당한 디나
        # self.set_npc_emotion_loop(spawnId=1001, sequenceName='Stun_A')
        self.create_monster(spawnIds=[1011], animationEffect=False) # 싸우고 있는 의문의 검사
        self.create_monster(spawnIds=[1021], animationEffect=False) # 연출용 어둠의 세력 몬스터 스폰포인트 1
        self.create_monster(spawnIds=[1022], animationEffect=False) # 연출용 어둠의 세력 몬스터 스폰포인트 2
        self.create_monster(spawnIds=[1023], animationEffect=False) # 연출용 어둠의 세력 몬스터 스폰포인트 3
        self.create_monster(spawnIds=[1024], animationEffect=False) # 연출용 어둠의 세력 몬스터 스폰포인트 4
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 몬스터처치(self.ctx)


class 몬스터처치(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[1021,1022,1023,1024]):
            return 경로이동01(self.ctx)


class 경로이동01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user_path(patrolName='MS2PatrolData_PC_01')
        self.move_npc(spawnId=1011, patrolName='MS2PatrolData_blader_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 경로이동02(self.ctx)


class 경로이동02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrolName='MS2PatrolData_PC_02')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            self.destroy_monster(spawnIds=[1011])
            self.create_monster(spawnIds=[1012], animationEffect=False)
            return PC말풍선01(self.ctx)


class PC말풍선01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=0, script='$52000083_QD__MAIN__0$', arg4=3, arg5=0)
        # self.set_npc_emotion_loop(spawnId=1012, sequenceName='Idle_A', duration=30000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 검사시네마틱대사(self.ctx)


class 검사시네마틱대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11004022, illustId='11004022', msg='$52000083_QD__MAIN__1$', align='left', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return PC말풍선02(self.ctx)


class PC말풍선02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=0, script='$52000083_QD__MAIN__2$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return PC말풍선03(self.ctx)


class PC말풍선03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=0, script='$52000083_QD__MAIN__3$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 디나말풍선01(self.ctx)


class 디나말풍선01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=1001, script='$52000083_QD__MAIN__4$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 디나기상(self.ctx)


class 디나기상(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawnId=1001, sequenceName='Idle_A', duration=69000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 검사대화01(self.ctx)


class 검사대화01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8001,8002], returnView=False)
        self.set_npc_emotion_loop(spawnId=1012, sequenceName='Talk_A', duration=3000)
        self.add_cinematic_talk(npcId=11004022, illustId='11004022', msg='$52000083_QD__MAIN__5$', align='left', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 디나대화01(self.ctx)


class 디나대화01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11003065, script='$52000083_QD__MAIN__6$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 검사대화02(self.ctx)


class 검사대화02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11004022, illustId='11004022', msg='$52000083_QD__MAIN__7$', align='left', duration=3000)
        self.set_npc_emotion_loop(spawnId=1012, sequenceName='Talk_A', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 디나대화02(self.ctx)


class 디나대화02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11003065, script='$52000083_QD__MAIN__8$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 검사대화03(self.ctx)


class 검사대화03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11004022, illustId='11004022', msg='$52000083_QD__MAIN__9$', align='left', duration=3000)
        self.set_npc_emotion_loop(spawnId=1012, sequenceName='Talk_A', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 디나대화03(self.ctx)


class 디나대화03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11003065, script='$52000083_QD__MAIN__10$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 디나대화04(self.ctx)


class 디나대화04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11003065, script='$52000083_QD__MAIN__11$', arg4=4, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 디나대화05(self.ctx)


class 디나대화05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11003065, script='$52000083_QD__MAIN__12$', arg4=4, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 디나대화05To1(self.ctx)


class 디나대화05To1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11003065, script='$52000083_QD__MAIN__13$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 검사대화04(self.ctx)


class 검사대화04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11004022, illustId='11004022', msg='$52000083_QD__MAIN__14$', align='left', duration=3000)
        self.set_npc_emotion_loop(spawnId=1012, sequenceName='Talk_A', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 디나대화06(self.ctx)


class 디나대화06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11003065, script='$52000083_QD__MAIN__15$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 검사대화06(self.ctx)


class 검사대화06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11004022, illustId='11004022', msg='$52000083_QD__MAIN__16$', align='left', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 시점이동(self.ctx)


class 시점이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8003], returnView=False)
        self.set_npc_emotion_loop(spawnId=1012, sequenceName='Bore_B', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 검사퇴장01(self.ctx)


class 검사퇴장01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=1012, patrolName='MS2PatrolData_blader_02')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return PC따라감(self.ctx)


class PC따라감(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrolName='MS2PatrolData_PC_03')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return PC말풍선04(self.ctx)


class PC말풍선04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=0, script='$52000083_QD__MAIN__17$', arg4=3, arg5=0)
        self.set_pc_emotion_loop(sequenceName='Talk_B', duration=2500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return PC말풍선05(self.ctx)


class PC말풍선05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=0, script='$52000083_QD__MAIN__18$', arg4=3, arg5=0)
        self.set_pc_emotion_loop(sequenceName='Talk_B', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 검사시네마틱대사02(self.ctx)


class 검사시네마틱대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11004022, illustId='11004022', msg='$52000083_QD__MAIN__19$', align='left', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 검사말풍선03(self.ctx)


class 검사말풍선03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11004022, illustId='11004022', msg='$52000083_QD__MAIN__20$', align='left', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 검사퇴장02(self.ctx)


class 검사퇴장02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolationTime=3)
        self.move_npc(spawnId=1012, patrolName='MS2PatrolData_blader_03')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.destroy_monster(spawnIds=[1012])
        self.destroy_monster(spawnIds=[1001])
        self.create_monster(spawnIds=[1002], animationEffect=False)
        self.set_achievement(triggerId=9000, type='trigger', achieve='meetarcaneblader2nd')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = start
