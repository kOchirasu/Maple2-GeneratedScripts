""" trigger/52000083_qd/main.xml """
from common import *
import state


class 연출출력체크50001536(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001536], questStates=[1]):
            return 연출시작()
        if quest_user_detected(boxIds=[9000], questIds=[50100260], questStates=[1]):
            return 연출시작()
        if not quest_user_detected(boxIds=[9000], questIds=[50001536], questStates=[1]):
            return 조건체크01()
        if not quest_user_detected(boxIds=[9000], questIds=[50100260], questStates=[1]):
            return 조건체크01()


class 조건체크01(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001536], questStates=[2]):
            return 연출이후()
        if quest_user_detected(boxIds=[9000], questIds=[50100260], questStates=[2]):
            return 연출이후()
        if not quest_user_detected(boxIds=[9000], questIds=[50001536], questStates=[2]):
            return 조건체크02()
        if not quest_user_detected(boxIds=[9000], questIds=[50100260], questStates=[2]):
            return 조건체크02()


class 조건체크02(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001536], questStates=[3]):
            return 조건체크03()
        if not quest_user_detected(boxIds=[9000], questIds=[50001536], questStates=[3]):
            return 전투종료후()
        if quest_user_detected(boxIds=[9000], questIds=[50100260], questStates=[3]):
            return 조건체크03()
        if not quest_user_detected(boxIds=[9000], questIds=[50100260], questStates=[3]):
            return 조건체크03()


class 조건체크03(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001537], questStates=[1]):
            return 연출이후()
        if not quest_user_detected(boxIds=[9000], questIds=[50001537], questStates=[1]):
            return 연출이후()
        if quest_user_detected(boxIds=[9000], questIds=[50100270], questStates=[1]):
            return 연출이후()
        if not quest_user_detected(boxIds=[9000], questIds=[50100270], questStates=[1]):
            return 연출이후()


class 연출이후(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1002], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 종료()


class 전투종료후(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 연출종료()


class 연출시작(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1001], arg2=False) # 스턴당한 디나
        create_monster(spawnIds=[1011], arg2=False) # 싸우고 있는 의문의 검사
        create_monster(spawnIds=[1021], arg2=False) # 연출용 어둠의 세력 몬스터 스폰포인트 1
        create_monster(spawnIds=[1022], arg2=False) # 연출용 어둠의 세력 몬스터 스폰포인트 2
        create_monster(spawnIds=[1023], arg2=False) # 연출용 어둠의 세력 몬스터 스폰포인트 3
        create_monster(spawnIds=[1024], arg2=False) # 연출용 어둠의 세력 몬스터 스폰포인트 4
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 몬스터처치()


class 몬스터처치(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1021,1022,1023,1024]):
            return 경로이동01()


class 경로이동01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_user_path(patrolName='MS2PatrolData_PC_01')
        move_npc(spawnId=1011, patrolName='MS2PatrolData_blader_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 경로이동02()


class 경로이동02(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_PC_02')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            destroy_monster(spawnIds=[1011])
            create_monster(spawnIds=[1012], arg2=False)
            return PC말풍선01()


class PC말풍선01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52000083_QD__MAIN__0$', arg4=3, arg5=0)
        # <action name="SetNpcEmotionLoop" arg1="1012" arg2="Idle_A" arg3="30000"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 검사시네마틱대사()


class 검사시네마틱대사(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004022, illustId='11004022', msg='$52000083_QD__MAIN__1$', align='left', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return PC말풍선02()


class PC말풍선02(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52000083_QD__MAIN__2$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return PC말풍선03()


class PC말풍선03(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52000083_QD__MAIN__3$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 디나말풍선01()


class 디나말풍선01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=1001, script='$52000083_QD__MAIN__4$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 디나기상()


class 디나기상(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=1001, sequenceName='Idle_A', duration=69000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 검사대화01()


class 검사대화01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8001,8002], returnView=False)
        set_npc_emotion_loop(spawnId=1012, sequenceName='Talk_A', duration=3000)
        add_cinematic_talk(npcId=11004022, illustId='11004022', msg='$52000083_QD__MAIN__5$', align='left', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 디나대화01()


class 디나대화01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11003065, script='$52000083_QD__MAIN__6$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 검사대화02()


class 검사대화02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004022, illustId='11004022', msg='$52000083_QD__MAIN__7$', align='left', duration=3000)
        set_npc_emotion_loop(spawnId=1012, sequenceName='Talk_A', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 디나대화02()


class 디나대화02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11003065, script='$52000083_QD__MAIN__8$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 검사대화03()


class 검사대화03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004022, illustId='11004022', msg='$52000083_QD__MAIN__9$', align='left', duration=3000)
        set_npc_emotion_loop(spawnId=1012, sequenceName='Talk_A', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 디나대화03()


class 디나대화03(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11003065, script='$52000083_QD__MAIN__10$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 디나대화04()


class 디나대화04(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11003065, script='$52000083_QD__MAIN__11$', arg4=4, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 디나대화05()


class 디나대화05(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11003065, script='$52000083_QD__MAIN__12$', arg4=4, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 디나대화05To1()


class 디나대화05To1(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11003065, script='$52000083_QD__MAIN__13$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 검사대화04()


class 검사대화04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004022, illustId='11004022', msg='$52000083_QD__MAIN__14$', align='left', duration=3000)
        set_npc_emotion_loop(spawnId=1012, sequenceName='Talk_A', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 디나대화06()


class 디나대화06(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11003065, script='$52000083_QD__MAIN__15$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 검사대화06()


class 검사대화06(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004022, illustId='11004022', msg='$52000083_QD__MAIN__16$', align='left', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 시점이동()


class 시점이동(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8003], returnView=False)
        set_npc_emotion_loop(spawnId=1012, sequenceName='Bore_B', duration=2000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 검사퇴장01()


class 검사퇴장01(state.State):
    def on_enter(self):
        move_npc(spawnId=1012, patrolName='MS2PatrolData_blader_02')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return PC따라감()


class PC따라감(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_PC_03')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return PC말풍선04()


class PC말풍선04(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52000083_QD__MAIN__17$', arg4=3, arg5=0)
        set_pc_emotion_loop(sequenceName='Talk_B', duration=2500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return PC말풍선05()


class PC말풍선05(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52000083_QD__MAIN__18$', arg4=3, arg5=0)
        set_pc_emotion_loop(sequenceName='Talk_B', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 검사시네마틱대사02()


class 검사시네마틱대사02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004022, illustId='11004022', msg='$52000083_QD__MAIN__19$', align='left', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 검사말풍선03()


class 검사말풍선03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004022, illustId='11004022', msg='$52000083_QD__MAIN__20$', align='left', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 검사퇴장02()


class 검사퇴장02(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=3)
        move_npc(spawnId=1012, patrolName='MS2PatrolData_blader_03')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        destroy_monster(spawnIds=[1012])
        destroy_monster(spawnIds=[1001])
        create_monster(spawnIds=[1002], arg2=False)
        set_achievement(triggerId=9000, type='trigger', achieve='meetarcaneblader2nd')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 종료()


class 종료(state.State):
    pass


