""" trigger/52100103_qd/main.xml """
from common import *
import state


class Ready(state.State):
    def on_enter(self):
        set_effect(triggerIds=[600], visible=False)
        set_effect(triggerIds=[700], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출시작체크()


class 연출시작체크(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[10000], questIds=[50100960], questStates=[2]):
            return 연출시작준비()


class 연출시작준비(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[-1], arg2=False)
        set_effect(triggerIds=[600], visible=False)
        set_effect(triggerIds=[700], visible=False)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출NPC소환()


class 연출NPC소환(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        move_user(mapId=52100103, portalId=3)
        create_monster(spawnIds=[1000], arg2=False)
        create_monster(spawnIds=[2000], arg2=False)
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 시작암전1()


class 시작암전1(state.State):
    def on_enter(self):
        move_user(mapId=52100103, portalId=3)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_scene_skip(state=엔딩암전, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 클라디아대사1()


class 클라디아대사1(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_3sec.xml')
        select_camera_path(pathIds=[1000,1001], returnView=False)
        set_npc_emotion_loop(spawnId=2000, sequenceName='Bore_A', duration=1333)
        add_cinematic_talk(npcId=11004419, msg='$52100103_QD__MAIN__0$', duration=3000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 마를레네대사1()


class 마를레네대사1(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_3sec.xml')
        set_npc_emotion_loop(spawnId=1000, sequenceName='Talk_A', duration=1333)
        add_cinematic_talk(npcId=11004395, msg='$52100103_QD__MAIN__1$', duration=3000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 카메라흔들기()


class 카메라흔들기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[700], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 마를레네대사2()


class 마를레네대사2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[3], arg2=False)
        create_monster(spawnIds=[200], arg2=False)
        create_monster(spawnIds=[201], arg2=False)
        create_monster(spawnIds=[202], arg2=False)
        create_monster(spawnIds=[203], arg2=False)
        set_npc_rotation(spawnId=1000, rotation=-45)
        set_npc_rotation(spawnId=2000, rotation=45)
        add_cinematic_talk(npcId=11004395, msg='$52100103_QD__MAIN__2$', duration=2000, align='left')
        add_cinematic_talk(npcId=11004419, msg='$52100103_QD__MAIN__3$', duration=2000, align='left')
        set_npc_emotion_loop(spawnId=3, sequenceName='Bore_A', duration=1333)
        select_camera(triggerId=100, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 투르카대사1()


class 투르카대사1(state.State):
    def on_enter(self):
        move_user_path(patrolName='PatrolData_PC_01')
        add_cinematic_talk(npcId=11004430, msg='$52100103_QD__MAIN__4$', duration=3000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PC돌아보기()


class PC돌아보기(state.State):
    def on_enter(self):
        select_camera(triggerId=200, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 포탈오픈()


class 포탈오픈(state.State):
    def on_enter(self):
        set_effect(triggerIds=[600], visible=True)
        select_camera(triggerId=1002, enable=True)
        create_monster(spawnIds=[300], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PC대사()


class PC대사(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004395, msg='$52100103_QD__MAIN__5$', duration=3000, align='left')
        move_user(mapId=52100103, portalId=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 투르카이동1()


class 투르카이동1(state.State):
    def on_enter(self):
        move_npc(spawnId=300, patrolName='PatrolData_Turka_1')
        move_npc(spawnId=200, patrolName='PatrolData_200_1')
        move_npc(spawnId=201, patrolName='PatrolData_201_1')
        move_npc(spawnId=202, patrolName='PatrolData_202_1')
        move_npc(spawnId=203, patrolName='PatrolData_203_1')
        select_camera(triggerId=1003, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PC이동()


class PC이동(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1000], arg2=False)
        create_monster(spawnIds=[1001], arg2=False)
        add_cinematic_talk(npcId=11004430, msg='$52100103_QD__MAIN__6$', duration=3000, align='left')
        move_npc(spawnId=1001, patrolName='PatrolData_1001_1')
        move_npc(spawnId=300, patrolName='PatrolData_Turka_2')
        move_npc(spawnId=200, patrolName='PatrolData_200_2')
        move_npc(spawnId=201, patrolName='PatrolData_201_2')
        move_npc(spawnId=202, patrolName='PatrolData_202_2')
        move_npc(spawnId=203, patrolName='PatrolData_203_2')
        move_user_path(patrolName='PatrolData_PC_02')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PC말풍선대사()


class PC말풍선대사(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52100103_QD__MAIN__7$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PC공격자세()


class PC공격자세(state.State):
    def on_enter(self):
        set_pc_emotion_loop(sequenceName='Attack_Idle_A', duration=30000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 투르카대사협박1()


class 투르카대사협박1(state.State):
    def on_enter(self):
        set_npc_rotation(spawnId=202, rotation=45)
        set_npc_rotation(spawnId=201, rotation=-45)
        set_npc_rotation(spawnId=200, rotation=15)
        set_npc_rotation(spawnId=203, rotation=-15)
        add_cinematic_talk(npcId=11004430, msg='$52100103_QD__MAIN__8$', duration=3000, align='left')
        set_npc_emotion_loop(spawnId=300, sequenceName='Bore_A', duration=1333)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 마를레네협박()


class 마를레네협박(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004395, msg='$52100103_QD__MAIN__9$', duration=3000, align='left')
        set_npc_emotion_loop(spawnId=1001, sequenceName='Talk_A', duration=1333)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 투르카대사협박2()


class 투르카대사협박2(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004430, msg='$52100103_QD__MAIN__10$', duration=6000, align='left')
        add_cinematic_talk(npcId=11004395, msg='$52100103_QD__MAIN__11$', duration=2000, align='left')
        add_cinematic_talk(npcId=11004430, msg='$52100103_QD__MAIN__12$', duration=3000, align='left')
        set_npc_emotion_loop(spawnId=300, sequenceName='Bore_A', duration=1333)
        destroy_monster(spawnIds=[2000], arg2=False)
        create_monster(spawnIds=[2001], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 클라디아대사()


class 클라디아대사(state.State):
    def on_enter(self):
        move_npc(spawnId=2001, patrolName='PatrolData_2001_1')
        add_cinematic_talk(npcId=11004385, msg='$52100103_QD__MAIN__13$', duration=2000, align='left')
        add_cinematic_talk(npcId=11004385, msg='$52100103_QD__MAIN__14$', duration=3500, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 마를레네대사()


class 마를레네대사(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004395, msg='$52100103_QD__MAIN__15$', duration=2000, align='left')
        set_npc_rotation(spawnId=1001, rotation=45)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 클라디아마를레네바라보기()


class 클라디아마를레네바라보기(state.State):
    def on_enter(self):
        set_npc_rotation(spawnId=2001, rotation=-90)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 클라디아대사2()


class 클라디아대사2(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=2001, sequenceName='Talk_A', duration=1333)
        add_cinematic_talk(npcId=11004385, msg='$52100103_QD__MAIN__16$', duration=4000, align='left')
        add_cinematic_talk(npcId=11004395, msg='$52100103_QD__MAIN__17$', duration=3000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 투르카대사3()


class 투르카대사3(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004430, msg='$52100103_QD__MAIN__18$', duration=3000, align='left')
        set_npc_emotion_loop(spawnId=300, sequenceName='Bore_A', duration=1333)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 클라디아퇴장()


class 클라디아퇴장(state.State):
    def on_enter(self):
        set_effect(triggerIds=[600], visible=True)
        select_camera(triggerId=1004, enable=True)
        move_npc(spawnId=2001, patrolName='PatrolData_2001_2')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 부하퇴장()


class 부하퇴장(state.State):
    def on_enter(self):
        move_npc(spawnId=200, patrolName='PatrolData_200_3')
        move_npc(spawnId=201, patrolName='PatrolData_201_3')
        move_npc(spawnId=202, patrolName='PatrolData_202_3')
        move_npc(spawnId=203, patrolName='PatrolData_203_3')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 투르카퇴장()


class 투르카퇴장(state.State):
    def on_enter(self):
        move_npc(spawnId=300, patrolName='PatrolData_Turka_3')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 마를레네엔딩대사()


class 마를레네엔딩대사(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[1005,1006], returnView=False)
        add_cinematic_talk(npcId=11004395, msg='$52100103_QD__MAIN__19$', duration=2000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 엔딩암전()


class 엔딩암전(state.State):
    def on_enter(self):
        set_onetime_effect(id=101, enable=True, path='BG/Common/ScreenMask/Eff_fadein_3sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 몬스터정리()


class 몬스터정리(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[-1], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 상황정리()


class 상황정리(state.State):
    def on_enter(self):
        move_user(mapId=52100109, portalId=2)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0)
        set_onetime_effect(id=101, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 마를레네생성준비()


class 마를레네생성준비(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[-1], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 마를레네생성()


class 마를레네생성(state.State):
    def on_enter(self):
        set_effect(triggerIds=[600], visible=False)
        set_effect(triggerIds=[700], visible=False)
        create_monster(spawnIds=[1], arg2=False)
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return None # Missing State: 


