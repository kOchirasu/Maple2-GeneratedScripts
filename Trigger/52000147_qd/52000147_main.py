""" trigger/52000147_qd/52000147_main.xml """
from common import *
import state


class 준비(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=True)
        create_monster(spawnIds=[102], arg2=True)
        set_effect(triggerIds=[5001], visible=False)
        set_effect(triggerIds=[5003], visible=False)
        set_effect(triggerIds=[5004], visible=False)
        set_effect(triggerIds=[5005], visible=False)
        set_mesh(triggerIds=[4001,4002], visible=True)
        set_mesh_animation(triggerIds=[4001,4002], visible=True, arg3=0, arg4=0)
        set_mesh(triggerIds=[4003,4004,4005,4006], visible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[701]):
            return 잠시대기()


class 잠시대기(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 뚜벅뚜벅_01()


class 뚜벅뚜벅_01(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_2001')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 뚜벅뚜벅_02()


class 뚜벅뚜벅_02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000147_QD__52000147_MAIN__0$', duration=2500, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6500):
            return 목격_01()


class 목격_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 목격_02()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class 목격_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8001], returnView=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 목격_03()


class 목격_03(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 목격_04()


class 목격_04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8001,8002], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 목격_05()


class 목격_05(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=101, sequenceName='Bore_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1200):
            return 목격_06()


class 목격_06(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 목격_07()


class 목격_07(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4001,4002], visible=False)
        set_mesh_animation(triggerIds=[4001,4002], visible=False, arg3=0, arg4=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 목격_08()


class 목격_08(state.State):
    def on_enter(self):
        set_scene_skip(state=삼자대화_01)
        add_cinematic_talk(npcId=11003382, msg='$52000147_QD__52000147_MAIN__1$', duration=4000, illustId='DarkLord_normal', align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 삼자대화_01()


class 삼자대화_01(state.State):
    def on_enter(self):
        set_scene_skip()
        remove_cinematic_talk()
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 삼자대화_02()


class 삼자대화_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8001], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 삼자대화_03()


class 삼자대화_03(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 삼자대화_04()


class 삼자대화_04(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_2003')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 삼자대화_05()


class 삼자대화_05(state.State):
    def on_enter(self):
        set_scene_skip(state=하스터와전투_01, arg2='nextState')
        add_cinematic_talk(npcId=0, msg='$52000147_QD__52000147_MAIN__2$', duration=3500, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 삼자대화_06()


class 삼자대화_06(state.State):
    def on_enter(self):
        move_npc(spawnId=102, patrolName='MS2PatrolData_2002')
        move_npc(spawnId=101, patrolName='MS2PatrolData_2004')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 삼자대화_07()


class 삼자대화_07(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8004], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 삼자대화_08()


class 삼자대화_08(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003189, msg='$52000147_QD__52000147_MAIN__3$', duration=3000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 삼자대화_09()


class 삼자대화_09(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8003], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 삼자대화_10()


class 삼자대화_10(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003382, msg='$52000147_QD__52000147_MAIN__4$', duration=3000, illustId='DarkLord_normal', align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 삼자대화_11()


class 삼자대화_11(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003189, msg='$52000147_QD__52000147_MAIN__5$', duration=2500, illustId='Hastur_normal', align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 삼자대화_12()


class 삼자대화_12(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003382, msg='$52000147_QD__52000147_MAIN__6$', duration=4000, illustId='DarkLord_normal', align='right')
        add_cinematic_talk(npcId=11003382, msg='$52000147_QD__52000147_MAIN__7$', duration=3000, illustId='DarkLord_normal', align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 삼자대화_13()


class 삼자대화_13(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000147_QD__52000147_MAIN__8$', duration=4000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4500):
            return 삼자대화_14()


class 삼자대화_14(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003189, msg='$52000147_QD__52000147_MAIN__9$', duration=3000, illustId='Hastur_normal', align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 삼자대화_15()


class 삼자대화_15(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003382, msg='$52000147_QD__52000147_MAIN__10$', duration=3000, illustId='DarkLord_normal', align='right')
        add_cinematic_talk(npcId=11003382, msg='$52000147_QD__52000147_MAIN__11$', duration=3000, illustId='DarkLord_normal', align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 삼자대화_16()


class 삼자대화_16(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003189, msg='$52000147_QD__52000147_MAIN__12$', duration=3000, illustId='Hastur_normal', align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 삼자대화_17()


class 삼자대화_17(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003382, msg='$52000147_QD__52000147_MAIN__13$', duration=3000, illustId='DarkLord_normal', align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 삼자대화_18()


class 삼자대화_18(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000147_QD__52000147_MAIN__14$', duration=3000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 삼자대화_19()


class 삼자대화_19(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8004], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 삼자대화_20()


class 삼자대화_20(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003189, msg='$52000147_QD__52000147_MAIN__15$', duration=2500, align='left')
        set_npc_emotion_loop(spawnId=102, sequenceName='Attack_Idle_A', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 하스터와전투_01()


class 하스터와전투_01(state.State):
    def on_enter(self):
        set_scene_skip()
        remove_cinematic_talk()
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 하스터와전투_02()


class 하스터와전투_02(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)
        destroy_monster(spawnIds=[102])
        create_monster(spawnIds=[103], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 하스터와전투_03()


class 하스터와전투_03(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        show_guide_summary(entityId=25201471, textId=25201471)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=15000):
            return 하스터와전투_04()


class 하스터와전투_04(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        hide_guide_summary(entityId=25201471)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 하스터와전투_05()


class 하스터와전투_05(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[103])
        create_monster(spawnIds=[104], arg2=True)
        add_cinematic_talk(npcId=11003189, msg='$52000147_QD__52000147_MAIN__16$', duration=2500, align='left')
        move_user(mapId=52000147, portalId=99)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 하스터와전투_06()


class 하스터와전투_06(state.State):
    def on_enter(self):
        set_pc_emotion_loop(sequenceName='Down_Idle_B', duration=60000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 하스터와전투_07()


class 하스터와전투_07(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 전투후대화_01()


class 전투후대화_01(state.State):
    def on_enter(self):
        set_scene_skip(state=전투후대화_02)
        add_cinematic_talk(npcId=11003382, msg='$52000147_QD__52000147_MAIN__17$', duration=3000, illustId='DarkLord_normal', align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 전투후대화_02()


class 전투후대화_02(state.State):
    def on_enter(self):
        set_scene_skip()
        remove_cinematic_talk()
        move_npc(spawnId=104, patrolName='MS2PatrolData_2005')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 전투후대화_03()


class 전투후대화_03(state.State):
    def on_enter(self):
        set_scene_skip(state=전투후대화_03_01)
        add_cinematic_talk(npcId=11003189, msg='$52000147_QD__52000147_MAIN__18$', duration=3000, illustId='Hastur_normal', align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 전투후대화_04()


class 전투후대화_03_01(state.State):
    def on_enter(self):
        set_scene_skip()
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 전투후대화_04()


class 전투후대화_04(state.State):
    def on_enter(self):
        set_scene_skip(state=전투후대화_05)
        add_cinematic_talk(npcId=11003382, msg='$52000147_QD__52000147_MAIN__19$', duration=3000, illustId='DarkLord_normal', align='right')
        add_cinematic_talk(npcId=11003382, msg='$52000147_QD__52000147_MAIN__20$', duration=2500, illustId='DarkLord_normal', align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 전투후대화_05()


class 전투후대화_05(state.State):
    def on_enter(self):
        set_scene_skip()
        remove_cinematic_talk()
        set_npc_emotion_sequence(spawnId=101, sequenceName='Bore_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 전투후대화_06()


class 전투후대화_06(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5003], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 전투후대화_07()


class 전투후대화_07(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_2007')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 전투후대화_08()


class 전투후대화_08(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 전투후대화_09()


class 전투후대화_09(state.State):
    def on_enter(self):
        move_npc(spawnId=104, patrolName='MS2PatrolData_2006')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 전투후대화_10()


class 전투후대화_10(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5005], visible=True)
        set_effect(triggerIds=[5004], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 전투후대화_11()


class 전투후대화_11(state.State):
    def on_enter(self):
        set_scene_skip(state=전투후대화_12)
        add_cinematic_talk(npcId=11003189, msg='$52000147_QD__52000147_MAIN__21$', duration=3000, illustId='Hastur_normal', align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 전투후대화_12()


class 전투후대화_12(state.State):
    def on_enter(self):
        set_scene_skip()
        remove_cinematic_talk()
        move_npc(spawnId=104, patrolName='MS2PatrolData_2007')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 전투후대화_13()


class 전투후대화_13(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[104])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 전투후대화_14()


class 전투후대화_14(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 전투후대화_15()


class 전투후대화_15(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000147_QD__52000147_MAIN__22$', duration=3000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 강제이동()


class 강제이동(state.State):
    def on_enter(self):
        move_user(mapId=52000148, portalId=1)


