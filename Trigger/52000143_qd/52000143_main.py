""" trigger/52000143_qd/52000143_main.xml """
from common import *
import state


class 준비(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        create_monster(spawnIds=[101], arg2=False)
        set_mesh(triggerIds=[4003,4004,4005,4006], visible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[701]):
            return 잠시대기()


class 잠시대기(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[8001], returnView=False)
        add_buff(boxIds=[701], skillId=70000124, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 한번더대기()


class 한번더대기(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 로베와대화_01()


class 로베와대화_01(state.State):
    def on_enter(self):
        set_scene_skip(state=로베와전투_01, arg2='nextState')
        add_cinematic_talk(npcId=0, msg='$52000143_QD__52000143_MAIN__0$', duration=3000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 로베와대화_02()


class 로베와대화_02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003401, msg='$52000143_QD__52000143_MAIN__1$', duration=3500, illustId='Robe_normal', align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 로베와대화_03()


class 로베와대화_03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000143_QD__52000143_MAIN__2$', duration=3000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 로베와대화_04()


class 로베와대화_04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003401, msg='$52000143_QD__52000143_MAIN__3$', duration=2500, illustId='Robe_normal', align='right')
        add_cinematic_talk(npcId=11003401, msg='$52000143_QD__52000143_MAIN__4$', duration=3000, illustId='Robe_normal', align='right')
        add_cinematic_talk(npcId=11003401, msg='$52000143_QD__52000143_MAIN__5$', duration=2500, illustId='Robe_normal', align='right')
        add_cinematic_talk(npcId=11003401, msg='$52000143_QD__52000143_MAIN__6$', duration=3000, illustId='Robe_normal', align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=12000):
            return 로베와대화_05()


class 로베와대화_05(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000143_QD__52000143_MAIN__7$', duration=3500, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 로베와대화_06()


class 로베와대화_06(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003401, msg='$52000143_QD__52000143_MAIN__8$', duration=1000, illustId='Robe_normal', align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 로베와대화_07()


class 로베와대화_07(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=101, sequenceName='Bore_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 로베와전투_01()


class 로베와전투_01(state.State):
    def on_enter(self):
        set_scene_skip()
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 로베와전투_02()


class 로베와전투_02(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)
        destroy_monster(spawnIds=[101])
        create_monster(spawnIds=[102], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 로베와전투_03()


class 로베와전투_03(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        show_guide_summary(entityId=25201431, textId=25201431)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=20000):
            return 로베와전투_04()


class 로베와전투_04(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        hide_guide_summary(entityId=25201431)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 로베와전투_05()


class 로베와전투_05(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[102])
        create_monster(spawnIds=[103], arg2=False)
        create_monster(spawnIds=[104], arg2=False)
        create_monster(spawnIds=[105], arg2=False)
        create_monster(spawnIds=[106], arg2=False)
        create_monster(spawnIds=[107], arg2=False)
        add_cinematic_talk(npcId=11003404, msg='$52000143_QD__52000143_MAIN__9$', duration=2500, align='center')
        move_user(mapId=52000143, portalId=99)
        select_camera_path(pathIds=[8002], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 알론등장_01()


class 알론등장_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 알론등장_02()


class 알론등장_02(state.State):
    def on_enter(self):
        move_npc(spawnId=104, patrolName='MS2PatrolData_2001')
        move_npc(spawnId=105, patrolName='MS2PatrolData_2002')
        move_npc(spawnId=106, patrolName='MS2PatrolData_2003')
        move_npc(spawnId=107, patrolName='MS2PatrolData_2004')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 자대화_03_3()


class 자대화_03_3(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8002,8003], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 자대화_04_3()


class 자대화_04_3(state.State):
    def on_enter(self):
        set_scene_skip(state=마무리_01, arg2='nextState')
        add_cinematic_talk(npcId=11003401, msg='$52000143_QD__52000143_MAIN__10$', duration=2500, illustId='Robe_normal', align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 자대화_05_3()


class 자대화_05_3(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003404, msg='$52000143_QD__52000143_MAIN__11$', duration=3000, illustId='Alon_normal', align='center')
        add_cinematic_talk(npcId=11003404, msg='$52000143_QD__52000143_MAIN__12$', duration=2500, illustId='Alon_normal', align='center')
        add_cinematic_talk(npcId=11003404, msg='$52000143_QD__52000143_MAIN__13$', duration=3000, illustId='Alon_normal', align='center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return 자대화_06_3()


class 자대화_06_3(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003401, msg='$52000143_QD__52000143_MAIN__14$', duration=3500, illustId='Robe_normal', align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 자대화_07_3()


class 자대화_07_3(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003404, msg='$52000143_QD__52000143_MAIN__15$', duration=3000, illustId='Alon_normal', align='center')
        add_cinematic_talk(npcId=11003404, msg='$52000143_QD__52000143_MAIN__16$', duration=3000, illustId='Alon_normal', align='center')
        add_cinematic_talk(npcId=11003404, msg='$52000143_QD__52000143_MAIN__17$', duration=3000, illustId='Alon_normal', align='center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return 자대화_08_3()


class 자대화_08_3(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003401, msg='$52000143_QD__52000143_MAIN__18$', duration=2500, illustId='Robe_normal', align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 자대화_09_3()


class 자대화_09_3(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000143_QD__52000143_MAIN__19$', duration=2500, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 자대화_10_3()


class 자대화_10_3(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003404, msg='$52000143_QD__52000143_MAIN__20$', duration=3000, illustId='Alon_normal', align='center')
        add_cinematic_talk(npcId=11003404, msg='$52000143_QD__52000143_MAIN__21$', duration=2500, illustId='Alon_normal', align='center')
        add_cinematic_talk(npcId=11003404, msg='$52000143_QD__52000143_MAIN__22$', duration=3000, illustId='Alon_normal', align='center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return 자대화_10_1_3()


class 자대화_10_1_3(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8005], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 자대화_10_2_3()


class 자대화_10_2_3(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000143_QD__52000143_MAIN__23$', duration=2500, align='left')
        move_npc(spawnId=104, patrolName='MS2PatrolData_2006')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 자대화_11_3()


class 자대화_11_3(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8004], returnView=False)
        move_user_path(patrolName='MS2PatrolData_2005')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 자대화_11_1_3()


class 자대화_11_1_3(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000143_QD__52000143_MAIN__28$', duration=3000, align='left')
        set_pc_emotion_sequence(sequenceNames=['Knight_Bore_A'])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 자대화_12_3()


class 자대화_12_3(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003404, msg='$52000143_QD__52000143_MAIN__24$', duration=5500, illustId='Alon_normal', align='right')
        add_cinematic_talk(npcId=11003404, msg='$52000143_QD__52000143_MAIN__25$', duration=5500, illustId='Alon_normal', align='right')
        add_cinematic_talk(npcId=11003404, msg='$52000143_QD__52000143_MAIN__26$', duration=5000, illustId='Alon_normal', align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=17000):
            return 마무리_01()


class 마무리_01(state.State):
    def on_enter(self):
        set_scene_skip()
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 마무리_02()


class 마무리_02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$52000143_QD__52000143_MAIN__27$')
        remove_buff(boxId=701, skillId=70000124)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 강제이동()


class 강제이동(state.State):
    def on_enter(self):
        move_user(mapId=52000144, portalId=1)


