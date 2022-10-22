""" trigger/52000081_qd/main.xml """
from common import *
import state


class start(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=False)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001532], questStates=[1]):
            return 연출01시작()
        if quest_user_detected(boxIds=[9000], questIds=[50100230], questStates=[1]):
            return 연출01시작()


class 연출01시작(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            move_user_path(patrolName='MS2PatrolData_PC_01')
            return PC말풍선01()


class PC말풍선01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52000081_QD__MAIN__0$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return PC말풍선02()


class PC말풍선02(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52000081_QD__MAIN__1$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return PC말풍선03()


class PC말풍선03(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52000081_QD__MAIN__2$', arg4=1, arg5=0)
        set_pc_emotion_loop(sequenceName='Push_A', duration=10000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 감옥이펙트()


class 감옥이펙트(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 몹소환()


class 몹소환(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52000081_QD__MAIN__3$', arg4=2, arg5=0)
        set_pc_emotion_loop(sequenceName='Push_A', duration=15000)
        create_monster(spawnIds=[1001,1003,1004], arg2=False) # 연출용 어둠의 세력 몬스터

    def on_tick(self) -> state.State:
        if not monster_dead(boxIds=[1001,1003,1004]):
            return 검사등장()
        if monster_dead(boxIds=[1001,1003,1004]):
            return PC구출01()


class 검사등장(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8001], returnView=False)
        create_monster(spawnIds=[1002], arg2=False) # 연출용 의문의 검사
        move_npc(spawnId=1002, patrolName='MS2PatrolData_NPC_01')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1001]):
            return PC구출01()
        if wait_tick(waitTick=15000):
            return 예비용00()


class 예비용00(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1001,1003,1004])
        move_npc(spawnId=1002, patrolName='MS2PatrolData_NPC_02')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return PC구출01()


class PC구출01(state.State):
    def on_enter(self):
        move_npc(spawnId=1002, patrolName='MS2PatrolData_NPC_02')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return PC구출02()


class PC구출02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8002], returnView=False)
        move_npc(spawnId=1002, patrolName='MS2PatrolData_NPC_02_1')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return PC구출03()


class PC구출03(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=1002, sequenceName='Attack_01_D', duration=2000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return PC구출04()


class PC구출04(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=False)
        set_pc_emotion_loop(sequenceName='Idle_A', duration=10000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 검사대화01()


class 검사대화01(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=1002, sequenceName='Bore_A', duration=1500)
        add_cinematic_talk(npcId=11004022, illustId='11004022', msg='$52000081_QD__MAIN__4$', align='left', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 검사대화02()


class 검사대화02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004022, illustId='11004022', msg='$52000081_QD__MAIN__5$', align='left', duration=3000)
        move_npc(spawnId=1002, patrolName='MS2PatrolData_NPC_03')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return PC말풍선04()


class PC말풍선04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8004,8005], returnView=False)
        set_conversation(type=1, spawnId=0, script='$52000081_QD__MAIN__6$', arg4=3, arg5=0)
        move_user_path(patrolName='MS2PatrolData_PC_02')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return PC말풍선05()


class PC말풍선05(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52000081_QD__MAIN__7$', arg4=3, arg5=0)
        move_npc(spawnId=1002, patrolName='MS2PatrolData_NPC_04')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 검사대화03()


class 검사대화03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004022, illustId='11004022', msg='$52000081_QD__MAIN__17$', align='left', duration=2000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return PC말풍선06()


class PC말풍선06(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52000081_QD__MAIN__8$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return PC말풍선07()


class PC말풍선07(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52000081_QD__MAIN__9$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return PC말풍선08()


class PC말풍선08(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52000081_QD__MAIN__10$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 검사대화04()


class 검사대화04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004022, illustId='11004022', msg='$52000081_QD__MAIN__11$', align='left', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 검사대화05()


class 검사대화05(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004022, illustId='11004022', msg='$52000081_QD__MAIN__12$', align='left', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 검사대화06()


class 검사대화06(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004022, illustId='11004022', msg='$52000081_QD__MAIN__13$', align='left', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 검사퇴장01()


class 검사퇴장01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8003], returnView=False)
        move_npc(spawnId=1002, patrolName='MS2PatrolData_NPC_05')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 검사대화07()


class 검사대화07(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004022, illustId='11004022', msg='$52000081_QD__MAIN__14$', align='left', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 검사대화08()


class 검사대화08(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004022, illustId='11004022', msg='$52000081_QD__MAIN__15$', align='left', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 검사대화09()


class 검사대화09(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004022, illustId='11004022', msg='$52000081_QD__MAIN__16$', align='left', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 검사퇴장02()


class 검사퇴장02(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=3)
        move_npc(spawnId=1002, patrolName='MS2PatrolData_NPC_06')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1002])
        set_achievement(triggerId=9000, type='trigger', achieve='meetarcaneblader1st')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 종료()


class 종료(state.State):
    pass


