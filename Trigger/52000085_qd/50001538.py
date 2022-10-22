""" trigger/52000085_qd/50001538.xml """
from common import *
import state


class 퀘스트체크(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[199], questIds=[50100280], questStates=[1]):
            return 대기()
        if quest_user_detected(boxIds=[199], questIds=[50100280], questStates=[2]):
            return 던전종료()
        if quest_user_detected(boxIds=[199], questIds=[50100280], questStates=[3]):
            return 던전종료()


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=False)
        set_effect(triggerIds=[602], visible=False)
        set_effect(triggerIds=[603], visible=False)
        set_mesh(triggerIds=[3000,3001], visible=True, arg3=0, arg4=0, arg5=0)
        create_monster(spawnIds=[1001,1002,1003], arg2=False)
        set_portal(portalId=91, visible=False, enabled=False, minimapVisible=False)
        remove_buff(boxId=199, skillId=70000115)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[199]):
            return 연출시작()


class 연출시작(state.State):
    def on_enter(self):
        set_local_camera(cameraId=2000, enable=False)
        set_npc_emotion_loop(spawnId=1001, sequenceName='Attack_Idle_A', duration=1E+12)
        set_pc_emotion_loop(sequenceName='Attack_Idle_A', duration=1E+12)
        set_skip(state=연출종료)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=300, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 트루카대사01()


class 트루카대사01(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=1003, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003071, illustId='11003762', msg='$52000085_QD__50001538__0$', align='left', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 트루카대사02()


class 트루카대사02(state.State):
    def on_enter(self):
        select_camera(triggerId=301, enable=True)
        add_cinematic_talk(npcId=11003071, illustId='11003762', msg='$52000085_QD__50001538__1$', align='left', duration=6000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 에르다대사01()


class 에르다대사01(state.State):
    def on_enter(self):
        select_camera(triggerId=302, enable=True)
        move_npc(spawnId=1002, patrolName='MS2PatrolData_1002A')
        add_cinematic_talk(npcId=11003069, illustId='SnowQueen_normal', msg='$52000085_QD__50001538__2$', align='right', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 에르다대사02()


class 에르다대사02(state.State):
    def on_enter(self):
        move_npc(spawnId=1003, patrolName='MS2PatrolData_1003A')
        add_cinematic_talk(npcId=11003069, illustId='SnowQueen_normal', msg='$52000085_QD__50001538__3$', align='right', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 트루카대사03()


class 트루카대사03(state.State):
    def on_enter(self):
        select_camera(triggerId=303, enable=True)
        set_npc_emotion_sequence(spawnId=1003, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003071, illustId='11003762', msg='$52000085_QD__50001538__4$', align='left', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 트루카대사04()


class 트루카대사04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003071, illustId='11003762', msg='$52000085_QD__50001538__5$', align='left', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 에르다대사03()


class 에르다대사03(state.State):
    def on_enter(self):
        select_camera(triggerId=302, enable=True)
        add_cinematic_talk(npcId=11003069, illustId='SnowQueen_normal', msg='$52000085_QD__50001538__6$', align='right', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 트루카대사05()


class 트루카대사05(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003071, illustId='11003762', msg='$52000085_QD__50001538__7$', align='left', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 트루카대사06()


class 트루카대사06(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003071, illustId='11003762', msg='$52000085_QD__50001538__8$', align='left', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 트루카대사07()


class 트루카대사07(state.State):
    def on_enter(self):
        select_camera(triggerId=303, enable=True)
        add_cinematic_talk(npcId=11003071, illustId='11003762', msg='$52000085_QD__50001538__9$', align='left', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 에르다대사04()


class 에르다대사04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003069, illustId='SnowQueen_normal', msg='$52000085_QD__50001538__10$', align='right', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 설눈이이동01()


class 설눈이이동01(state.State):
    def on_enter(self):
        select_camera(triggerId=304, enable=True)
        move_npc(spawnId=1001, patrolName='MS2PatrolData_1001A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 설눈이대사01()


class 설눈이대사01(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=1001, sequenceName='Attack_Idle_A', duration=1E+12)
        add_cinematic_talk(npcId=11003068, illustId='Seolnunyi_normal', msg='$52000085_QD__50001538__11$', align='right', duration=6000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 트루카대사08()


class 트루카대사08(state.State):
    def on_enter(self):
        select_camera(triggerId=305, enable=True)
        move_npc(spawnId=1003, patrolName='MS2PatrolData_1003B')
        add_cinematic_talk(npcId=11003071, illustId='11003762', msg='$52000085_QD__50001538__12$', align='left', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 트루카대사09()


class 트루카대사09(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1004], arg2=False)
        add_cinematic_talk(npcId=11003071, illustId='11003762', msg='$52000085_QD__50001538__13$', align='left', duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 홀슈타트등장()


class 홀슈타트등장(state.State):
    def on_enter(self):
        select_camera(triggerId=306, enable=True)
        move_npc(spawnId=1004, patrolName='MS2PatrolData_1004A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 홀슈타트대사01()


class 홀슈타트대사01(state.State):
    def on_enter(self):
        select_camera(triggerId=307, enable=True)
        add_cinematic_talk(npcId=11004022, illustId='11004022', msg='$52000085_QD__50001538__14$', align='left', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 트루카대사10()


class 트루카대사10(state.State):
    def on_enter(self):
        select_camera(triggerId=308, enable=True)
        add_cinematic_talk(npcId=11003071, illustId='11003762', msg='$52000085_QD__50001538__15$', align='right', duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 홀슈타트대사02()


class 홀슈타트대사02(state.State):
    def on_enter(self):
        select_camera(triggerId=310, enable=True)
        add_cinematic_talk(npcId=11004022, illustId='11004022', msg='$52000085_QD__50001538__16$', align='left', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 트루카대사11()


class 트루카대사11(state.State):
    def on_enter(self):
        select_camera(triggerId=308, enable=True)
        add_cinematic_talk(npcId=11003071, illustId='11003762', msg='$52000085_QD__50001538__17$', align='right', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 트루카대사12()


class 트루카대사12(state.State):
    def on_enter(self):
        select_camera(triggerId=309, enable=True)
        add_cinematic_talk(npcId=11003071, illustId='11003762', msg='$52000085_QD__50001538__18$', align='right', duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 포털이펙트()


class 포털이펙트(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=1003, sequenceName='Bore_A')
        set_effect(triggerIds=[601], visible=True)
        add_cinematic_talk(npcId=11004022, illustId='11004022', msg='$52000085_QD__50001538__19$', align='left', duration=2000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return NPC합체()


class NPC합체(state.State):
    def on_enter(self):
        move_npc(spawnId=1003, patrolName='MS2PatrolData_1099')
        move_npc(spawnId=1004, patrolName='MS2PatrolData_1099')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=600):
            return NPC소멸()


class NPC소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1003,1004])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 포털삭제()


class 포털삭제(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 설눈이이동02()


class 설눈이이동02(state.State):
    def on_enter(self):
        select_camera(triggerId=311, enable=True)
        move_user_path(patrolName='MS2PatrolData_PC')
        move_npc(spawnId=1001, patrolName='MS2PatrolData_1001B')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 설눈이대사02()


class 설눈이대사02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003068, illustId='Seolnunyi_normal', msg='$52000085_QD__50001538__20$', align='right', duration=6000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 에르다방향전환()


class 에르다방향전환(state.State):
    def on_enter(self):
        move_npc(spawnId=1002, patrolName='MS2PatrolData_1002B')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 에르다대사05()


class 에르다대사05(state.State):
    def on_enter(self):
        select_camera(triggerId=312, enable=True)
        add_cinematic_talk(npcId=11003069, illustId='SnowQueen_normal', msg='$52000085_QD__50001538__21$', align='left', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 설눈이대사03()


class 설눈이대사03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003068, illustId='Seolnunyi_normal', msg='$52000085_QD__50001538__22$', align='right', duration=2000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 에르다대사06()


class 에르다대사06(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=1002, sequenceName='Attack_Idle_A', duration=1E+12)
        select_camera(triggerId=313, enable=True)
        add_cinematic_talk(npcId=11003069, illustId='SnowQueen_normal', msg='$52000085_QD__50001538__23$', align='left', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        set_skip()
        destroy_monster(spawnIds=[1001,1002,1003,1004])
        create_monster(spawnIds=[2001,2002], arg2=True)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0)
        move_user(mapId=52000085, portalId=99)
        add_buff(boxIds=[199], skillId=70000115, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7500):
            create_monster(spawnIds=[2003,2004,2005], arg2=False)
            return 에르다사망대기()


class 에르다사망대기(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2002]):
            return 에르다사망딜레이()


class 에르다사망딜레이(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[2003,2004,2005])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 암전()


class 암전(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_user(mapId=52000085, portalId=98)
        destroy_monster(spawnIds=[2001,2002])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 종료연출시작()


class 종료연출시작(state.State):
    def on_enter(self):
        set_skip(state=종료연출종료)
        create_monster(spawnIds=[1005,1006], arg2=False)
        select_camera(triggerId=314, enable=True)
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 에르다대사07()


class 에르다대사07(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003069, illustId='SnowQueen_normal', msg='$52000085_QD__50001538__24$', align='left', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 설눈이대사04()


class 설눈이대사04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003068, illustId='Seolnunyi_normal', msg='$52000085_QD__50001538__25$', align='right', duration=6000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 에르다공중부양준비()


class 에르다공중부양준비(state.State):
    def on_enter(self):
        select_camera(triggerId=315, enable=True)
        set_npc_emotion_loop(spawnId=1006, sequenceName='Attack_Idle_A', duration=1E+12)
        add_cinematic_talk(npcId=11003069, illustId='SnowQueen_normal', msg='$52000085_QD__50001538__26$', align='left', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 에르다공중부양()


class 에르다공중부양(state.State):
    def on_enter(self):
        set_skip()
        move_npc(spawnId=1006, patrolName='MS2PatrolData_1006')
        add_cinematic_talk(npcId=11003068, illustId='Seolnunyi_normal', msg='$52000085_QD__50001538__27$', align='right', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 얼림()


class 얼림(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=1005, sequenceName='Stun_A', duration=1E+12)
        set_pc_emotion_loop(sequenceName='StunFrozen_A', duration=25000)
        set_effect(triggerIds=[602], visible=True)
        set_effect(triggerIds=[603], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 에르다공중부양중()


class 에르다공중부양중(state.State):
    def on_enter(self):
        select_camera(triggerId=316, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return PC말풍선대사01()


class PC말풍선대사01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1006])
        select_camera(triggerId=317, enable=True)
        set_conversation(type=1, spawnId=0, script='$52000085_QD__50001538__28$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 설눈이말풍선대사01()


class 설눈이말풍선대사01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1007], arg2=False)
        set_conversation(type=1, spawnId=1005, script='$52000085_QD__50001538__29$', arg4=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return PC말풍선대사02()


class PC말풍선대사02(state.State):
    def on_enter(self):
        select_camera(triggerId=318, enable=True)
        set_conversation(type=1, spawnId=0, script='$52000085_QD__50001538__30$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 설만이이동01()


class 설만이이동01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=1007, script='$52000085_QD__50001538__31$', arg4=5)
        move_npc(spawnId=1007, patrolName='MS2PatrolData_1007A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 설눈이인사()


class 설눈이인사(state.State):
    def on_enter(self):
        set_effect(triggerIds=[603], visible=False)
        set_npc_emotion_loop(spawnId=1005, sequenceName='Idle_A', duration=1E+12)
        set_conversation(type=1, spawnId=1005, script='$52000085_QD__50001538__32$', arg4=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 설만이이동02()


class 설만이이동02(state.State):
    def on_enter(self):
        move_npc(spawnId=1005, patrolName='MS2PatrolData_1005A')
        move_npc(spawnId=1007, patrolName='MS2PatrolData_1007B')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return PC말풍선대사03()


class PC말풍선대사03(state.State):
    def on_enter(self):
        set_effect(triggerIds=[602], visible=False)
        set_pc_emotion_loop(sequenceName='Idle_A', duration=1000)
        move_user_path(patrolName='MS2PatrolData_PC2')
        move_npc(spawnId=1007, patrolName='MS2PatrolData_1007C')
        set_conversation(type=1, spawnId=0, script='$52000085_QD__50001538__33$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 설만이대사01()


class 설만이대사01(state.State):
    def on_enter(self):
        set_skip(state=종료연출종료)
        select_camera(triggerId=319, enable=True)
        add_cinematic_talk(npcId=11003073, illustId='11000404', msg='$52000085_QD__50001538__34$', align='right', duration=6000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 설눈이대사05()


class 설눈이대사05(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003068, illustId='Seolnunyi_normal', msg='$52000085_QD__50001538__35$', align='left', duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 설만이대사02()


class 설만이대사02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003073, illustId='11000404', msg='$52000085_QD__50001538__36$', align='right', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 설눈이대사06()


class 설눈이대사06(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003068, illustId='Seolnunyi_normal', msg='$52000085_QD__50001538__37$', align='left', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 설눈이대사07()


class 설눈이대사07(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003068, illustId='Seolnunyi_normal', msg='$52000085_QD__50001538__38$', align='left', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 종료연출종료()


class 종료연출종료(state.State):
    def on_enter(self):
        set_skip()
        set_npc_emotion_loop(spawnId=1005, sequenceName='Idle_A', duration=1E+12)
        set_pc_emotion_loop(sequenceName='Idle_A', duration=1000)
        destroy_monster(spawnIds=[1005,1006,1007])
        set_achievement(triggerId=199, type='trigger', achieve='snowqueenerda')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 던전종료()


class 던전종료(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1008,1009], arg2=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_effect(triggerIds=[601], visible=False)
        set_effect(triggerIds=[602], visible=False)
        set_effect(triggerIds=[603], visible=False)
        set_portal(portalId=91, visible=True, enabled=True, minimapVisible=True)
        reset_camera(interpolationTime=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 종료()


class 종료(state.State):
    pass


