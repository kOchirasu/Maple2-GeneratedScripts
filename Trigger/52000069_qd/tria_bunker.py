""" trigger/52000069_qd/tria_bunker.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=False)
        set_effect(triggerIds=[602], visible=False)
        set_effect(triggerIds=[603], visible=False)
        set_effect(triggerIds=[604], visible=False)
        set_effect(triggerIds=[605], visible=False)
        set_effect(triggerIds=[606], visible=False)
        set_effect(triggerIds=[607], visible=False)
        set_effect(triggerIds=[608], visible=False)
        set_effect(triggerIds=[609], visible=False)
        set_effect(triggerIds=[610], visible=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_agent(triggerIds=[8000], visible=True)
        set_agent(triggerIds=[8001], visible=True)
        set_agent(triggerIds=[8002], visible=True)
        set_agent(triggerIds=[8003], visible=True)
        set_agent(triggerIds=[8004], visible=True)
        set_agent(triggerIds=[8005], visible=True)
        set_agent(triggerIds=[8006], visible=True)
        set_agent(triggerIds=[8007], visible=True)
        set_agent(triggerIds=[8008], visible=True)
        set_agent(triggerIds=[8009], visible=True)
        set_agent(triggerIds=[8010], visible=True)
        set_agent(triggerIds=[8011], visible=True)
        set_agent(triggerIds=[8012], visible=True)
        set_agent(triggerIds=[8013], visible=True)
        set_agent(triggerIds=[8014], visible=True)
        set_agent(triggerIds=[8015], visible=True)
        set_agent(triggerIds=[8016], visible=True)
        set_agent(triggerIds=[8017], visible=True)
        set_agent(triggerIds=[8018], visible=True)
        set_agent(triggerIds=[8019], visible=True)
        set_agent(triggerIds=[8020], visible=True)
        set_agent(triggerIds=[8021], visible=True)
        create_monster(spawnIds=[1000,1001,1002,1003], arg2=False)
        create_monster(spawnIds=[1100,1101,1102,1103,1104,1105,1106,1107,1108,1109,1110], arg2=False)
        create_monster(spawnIds=[1201,1202,1203], arg2=False)
        create_monster(spawnIds=[2001,2101,2102,2103,2104,2105,2106,2107,2108], arg2=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[199]):
            return 연출시작()


class 연출시작(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            set_scene_skip(state=연출종료)
            set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
            return 카메라이동()


class 카메라이동(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=301, enable=True)
        add_cinematic_talk(npcId=11000064, illustId='Lennon_normal', msg='$52000069_QD__TRIA_BUNKER__0$', duration=9195, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        set_scene_skip()
        add_buff(boxIds=[199], skillId=70000109, level=1, arg4=False, arg5=False) # 초생회
        select_camera(triggerId=301, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        move_npc(spawnId=1003, patrolName='MS2PatrolData_1003A')
        set_conversation(type=1, spawnId=1003, script='$52000069_QD__TRIA_BUNKER__1$', arg4=4, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 차연출2()


class 차연출2(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=11100101, enable=True, path='BG/Common/Sound/Eff_Object_Devlin_Appear_01.xml ')
        set_npc_emotion_sequence(spawnId=2001, sequenceName='AttackReady_A')
        select_camera(triggerId=302, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 프레이대사01()


class 프레이대사01(state.State):
    def on_enter(self):
        select_camera(triggerId=303, enable=True)
        set_npc_emotion_sequence(spawnId=2003, sequenceName='Bore_A')
        add_cinematic_talk(npcId=11000119, illustId='Fray_serious', msg='$52000069_QD__TRIA_BUNKER__2$', duration=4000, align='center')
        set_scene_skip(state=대사스킵용01)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 돌격()


class 대사스킵용01(state.State):
    def on_enter(self):
        set_scene_skip()
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return 돌격()


class 돌격(state.State):
    def on_enter(self):
        set_scene_skip()
        select_camera(triggerId=304, enable=True)
        set_agent(triggerIds=[8004], visible=False)
        set_agent(triggerIds=[8005], visible=False)
        set_agent(triggerIds=[8006], visible=False)
        set_agent(triggerIds=[8007], visible=False)
        set_agent(triggerIds=[8008], visible=False)
        set_agent(triggerIds=[8009], visible=False)
        set_agent(triggerIds=[8010], visible=False)
        set_agent(triggerIds=[8011], visible=False)
        set_agent(triggerIds=[8012], visible=False)
        set_agent(triggerIds=[8013], visible=False)
        set_agent(triggerIds=[8014], visible=False)
        set_agent(triggerIds=[8015], visible=False)
        set_agent(triggerIds=[8016], visible=False)
        set_agent(triggerIds=[8017], visible=False)
        set_agent(triggerIds=[8018], visible=False)
        set_agent(triggerIds=[8019], visible=False)
        set_agent(triggerIds=[8020], visible=False)
        set_agent(triggerIds=[8021], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 지원군대기()


class 지원군대기(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=304, enable=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=20000):
            return 지원군등장()


class 지원군등장(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1201,1202,1203])
        destroy_monster(spawnIds=[2101,2102,2103])
        create_monster(spawnIds=[1004,1005,1301,1302,1303,1304], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 지원군연출()


class 지원군연출(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        add_buff(boxIds=[199], skillId=70000107, level=1, arg4=False, arg5=False)
        select_camera(triggerId=305, enable=True)
        set_conversation(type=1, spawnId=1004, script='$52000069_QD__TRIA_BUNKER__3$', arg4=4, arg5=0)
        set_conversation(type=1, spawnId=1005, script='$52000069_QD__TRIA_BUNKER__4$', arg4=4, arg5=0)
        move_npc(spawnId=1004, patrolName='MS2PatrolData_1004A')
        move_npc(spawnId=1005, patrolName='MS2PatrolData_1005A')
        move_npc(spawnId=1301, patrolName='MS2PatrolData_1301A')
        move_npc(spawnId=1302, patrolName='MS2PatrolData_1302A')
        move_npc(spawnId=1303, patrolName='MS2PatrolData_1303A')
        move_npc(spawnId=1304, patrolName='MS2PatrolData_1304A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4500):
            return 임무종료대기()


class 임무종료대기(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        remove_buff(boxId=199, skillId=70000107)
        select_camera(triggerId=305, enable=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 데블린사망딜레이()


class 데블린사망딜레이(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 암전()


class 암전(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return NPC교체()


class NPC교체(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        move_user(mapId=52000069, portalId=2)
        create_monster(spawnIds=[1006,1007,1009], arg2=False)
        destroy_monster(spawnIds=[1100,1101,1102,1103,1104,1105,1106,1107,1108,1109,1110])
        destroy_monster(spawnIds=[1003,1004,1005,1301,1302,1303,1304,2001,2101,2102,2103,2104,2105,2106,2107,2108])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 에레브연출시작()


class 에레브연출시작(state.State):
    def on_enter(self):
        set_scene_skip(state=NPC교체2, arg2='nextState')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=306, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 에레브대사01()


class 에레브대사01(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_npc_emotion_sequence(spawnId=1000, sequenceName='Talk_A')
        set_sound(triggerId=90000, arg2=True) # TriaAttack
        set_conversation(type=2, spawnId=11000075, script='$52000069_QD__TRIA_BUNKER__5$', arg4=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 에레브대사02()


class 에레브대사02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000064, script='$52000069_QD__TRIA_BUNKER__6$', arg4=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 에레브대사03()


class 에레브대사03(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001975, script='$52000069_QD__TRIA_BUNKER__7$', arg4=4)
        set_onetime_effect(id=1991, enable=True, path='BG/Common/Sound/Eff_Madria_TriaSeige_02_00001991.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 에레브대사04()


class 에레브대사04(state.State):
    def on_enter(self):
        set_sound(triggerId=90000, arg2=False) # TriaAttack
        add_cinematic_talk(npcId=11000075, illustId='Ereb_surprise', msg='$52000069_QD__TRIA_BUNKER__8$', duration=4000, align='center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 마드리아등장()


class 마드리아등장(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=True)
        select_camera(triggerId=307, enable=True)
        create_monster(spawnIds=[2000], arg2=False, arg3=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 방향전환()


class 방향전환(state.State):
    def on_enter(self):
        set_effect(triggerIds=[609], visible=True)
        move_npc(spawnId=1006, patrolName='MS2PatrolData_1006A')
        move_npc(spawnId=1007, patrolName='MS2PatrolData_1007A') # action name="NPC를이동시킨다" arg1="1008" arg2="MS2PatrolData_1008A" /
        move_npc(spawnId=1009, patrolName='MS2PatrolData_1009A')
        move_user_path(patrolName='MS2PatrolData_PCA')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 광역마법()


class 광역마법(state.State):
    def on_enter(self):
        set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')
        move_npc(spawnId=2000, patrolName='MS2PatrolData_2000A')
        set_effect(triggerIds=[609], visible=True)
        set_effect(triggerIds=[602], visible=True)
        set_effect(triggerIds=[603], visible=True)
        set_effect(triggerIds=[604], visible=True)
        set_effect(triggerIds=[605], visible=True)
        set_effect(triggerIds=[606], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 처맞음()


class 처맞음(state.State):
    def on_enter(self):
        set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')
        set_npc_emotion_sequence(spawnId=1006, sequenceName='Damg_A')
        set_npc_emotion_sequence(spawnId=1007, sequenceName='Damg_A')
        set_npc_emotion_sequence(spawnId=1009, sequenceName='Damg_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=250):
            return 쓰러짐()


class 쓰러짐(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=1006, sequenceName='Down_Idle_A', duration=1E+09)
        set_npc_emotion_loop(spawnId=1007, sequenceName='Down_Idle_A', duration=1E+09) # action name="SetNpcEmotionLoop" arg1="1008" arg2="Down_Idle" arg3="999999999" /
        set_npc_emotion_loop(spawnId=1009, sequenceName='Dead_Idle_A', duration=1E+09)
        set_pc_emotion_loop(sequenceName='Down_Idle_A', duration=12000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 쓰러짐2()


class 쓰러짐2(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1001,1002])
        select_camera(triggerId=309, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 마드리아워킹()


class 마드리아워킹(state.State):
    def on_enter(self):
        select_camera(triggerId=308, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 마드리아오버숄더()


class 마드리아오버숄더(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001820, script='$52000069_QD__TRIA_BUNKER__9$', arg4=7) # 대사
        set_onetime_effect(id=1992, enable=True, path='BG/Common/Sound/Eff_Madria_TriaSeige_03_00001992.xml')
        select_camera(triggerId=310, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return 마드리아공격()


class 마드리아공격(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11000075, illustId='Ereb_serious', msg='$52000069_QD__TRIA_BUNKER__10$', duration=3000, align='center')
        select_camera(triggerId=311, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 마드리아공격2()


class 마드리아공격2(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001820, script='$52000069_QD__TRIA_BUNKER__11$', arg4=12) # 대사
        set_onetime_effect(id=1993, enable=True, path='BG/Common/Sound/Eff_Madria_TriaSeige_04_00001993.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=12500):
            return 마드리아공격3()


class 마드리아공격3(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001820, script='$52000069_QD__TRIA_BUNKER__12$', arg4=11) # 대사
        set_onetime_effect(id=1994, enable=True, path='BG/Common/Sound/Eff_Madria_TriaSeige_05_00001994.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=11200):
            return 마드리아공격4()


class 마드리아공격4(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001820, script='$52000069_QD__TRIA_BUNKER__13$', arg4=8) # 대사
        set_onetime_effect(id=1995, enable=True, path='BG/Common/Sound/Eff_Madria_TriaSeige_06_00001995.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8100):
            return 마드리아공격5()


class 마드리아공격5(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=1000, sequenceName='Damg_A')
        select_camera(triggerId=315, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 에레브각성()


class 에레브각성(state.State):
    def on_enter(self):
        set_effect(triggerIds=[607], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 에레브각성2()


class 에레브각성2(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=1000, sequenceName='Damg_Idle_B', duration=1E+09)
        select_camera(triggerId=312, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 마드리아놀람()


class 마드리아놀람(state.State):
    def on_enter(self):
        select_camera(triggerId=314, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 카메라눈속임()


class 카메라눈속임(state.State):
    def on_enter(self):
        select_camera(triggerId=312, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 에레브버프2()


class 에레브버프2(state.State):
    def on_enter(self):
        select_camera(triggerId=313, enable=True)
        set_npc_emotion_sequence(spawnId=1000, sequenceName='Spell_A')
        set_onetime_effect(id=2100287, enable=True, path='BG/Common/Sound/Eff_System_Chapter8_Destruction_of_Ereb_01.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 화이트아웃()


class 화이트아웃(state.State):
    def on_enter(self):
        set_effect(triggerIds=[608], visible=True)
        set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOut.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 마드리아대사01()


class 마드리아대사01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001820, script='$52000069_QD__TRIA_BUNKER__14$', arg4=7) # 대사
        set_onetime_effect(id=1996, enable=True, path='BG/Common/Sound/Eff_Madria_TriaSeige_07_00001996.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return 마드리아대사02()


class 마드리아대사02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001820, script='$52000069_QD__TRIA_BUNKER__15$', arg4=3) # 대사
        set_onetime_effect(id=1997, enable=True, path='BG/Common/Sound/Eff_Madria_TriaSeige_08_00001997.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return NPC교체2()


class NPC교체2(state.State):
    def on_enter(self):
        set_scene_skip()
        remove_buff(boxId=199, skillId=70000109)
        set_effect(triggerIds=[601], visible=False)
        set_effect(triggerIds=[607], visible=False)
        set_pc_emotion_sequence(sequenceNames=['Idle_A'])
        destroy_monster(spawnIds=[1000,1006,1007,1009,2000,1001,1002])
        move_user(mapId=52000069, portalId=2)
        create_monster(spawnIds=[1000,1006,1007,1010,1011,1001,1002,9999], arg2=False)
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOut.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_achievement(triggerId=91000, type='trigger', achieve='TriaSeigeClear')
        set_sound(triggerId=90000, arg2=True) # TriaAttack
        select_camera(triggerId=313, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


