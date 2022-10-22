""" trigger/52000146_qd/52000146_main.xml """
from common import *
import state


class 준비(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        create_monster(spawnIds=[101], arg2=True)
        create_monster(spawnIds=[102], arg2=True)
        create_monster(spawnIds=[103], arg2=True)
        create_monster(spawnIds=[104], arg2=True)
        create_monster(spawnIds=[105], arg2=True)
        create_monster(spawnIds=[106], arg2=True)
        set_effect(triggerIds=[5001,5002,5003,5004,5005,5006], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[701]):
            return 잠시대기()


class 잠시대기(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 한번더대기()


class 한번더대기(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 카메라이동_01()


class 카메라이동_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8001], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 카메라이동_02()


class 카메라이동_02(state.State):
    def on_enter(self):
        show_caption(type='VerticalCaption', title='$52000146_QD__52000146_MAIN__0$', desc='$52000146_QD__52000146_MAIN__1$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=4000, scale=2.5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 카메라리셋_01()


class 카메라리셋_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 카메라리셋_02()


class 카메라리셋_02(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 카메라리셋_03()


class 카메라리셋_03(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 걸으며대화_01()


class 걸으며대화_01(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_2001')
        move_npc(spawnId=101, patrolName='MS2PatrolData_2002')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 걸으며대화_02()


class 걸으며대화_02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003189, msg='$52000146_QD__52000146_MAIN__2$', duration=3000, illustId='Hastur_normal', align='left')
        add_cinematic_talk(npcId=11003189, msg='$52000146_QD__52000146_MAIN__3$', duration=4000, illustId='Hastur_normal', align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 걸으며대화_03()


class 걸으며대화_03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000146_QD__52000146_MAIN__4$', duration=3000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 걸으며대화_04()


class 걸으며대화_04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003189, msg='$52000146_QD__52000146_MAIN__5$', duration=3000, illustId='Hastur_normal', align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 걸으며대화_05()


class 걸으며대화_05(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000146_QD__52000146_MAIN__6$', duration=3500, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 걸으며대화_06()


class 걸으며대화_06(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003189, msg='$52000146_QD__52000146_MAIN__7$', duration=3000, illustId='Hastur_normal', align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 멈춰서대화_01()


class 멈춰서대화_01(state.State):
    def on_enter(self):
        set_scene_skip(state=전투_01, arg2='nextState')
        add_cinematic_talk(npcId=0, msg='$52000146_QD__52000146_MAIN__8$', duration=3000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 멈춰서대화_02()


class 멈춰서대화_02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003189, msg='$52000146_QD__52000146_MAIN__9$', duration=4000, illustId='Hastur_normal', align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 전투_01()


class 전투_01(state.State):
    def on_enter(self):
        set_scene_skip()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        destroy_monster(spawnIds=[102,103,104,105,106])
        create_monster(spawnIds=[107,108,109,110,111], arg2=True)
        destroy_monster(spawnIds=[101])
        create_monster(spawnIds=[112], arg2=False)
        show_guide_summary(entityId=25201461, textId=25201461)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[107,108,109,110,111]):
            return 전투_02()


class 전투_02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[107,108,109,110,111], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[107,108,109,110,111]):
            return 전투종료_01()


class 전투종료_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        hide_guide_summary(entityId=25201461)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 전투종료_02()


class 전투종료_02(state.State):
    def on_enter(self):
        move_user(mapId=52000146, portalId=99)
        destroy_monster(spawnIds=[112])
        create_monster(spawnIds=[113], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 전투종료_03()


class 전투종료_03(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 전투후대화_01()


class 전투후대화_01(state.State):
    def on_enter(self):
        set_scene_skip(state=스킵도착_01, arg2='nextState')
        add_cinematic_talk(npcId=0, msg='$52000146_QD__52000146_MAIN__10$', duration=4000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 전투후대화_02()


class 전투후대화_02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003189, msg='$52000146_QD__52000146_MAIN__11$', duration=3000, illustId='Hastur_normal', align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 전투후대화_03()


class 전투후대화_03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000146_QD__52000146_MAIN__12$', duration=3500, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 전투후대화_04()


class 전투후대화_04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003189, msg='$52000146_QD__52000146_MAIN__13$', duration=3500, illustId='Hastur_normal', align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 전투후대화_05()


class 전투후대화_05(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000146_QD__52000146_MAIN__14$', duration=3500, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 전투후대화_06()


class 전투후대화_06(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003189, msg='$52000146_QD__52000146_MAIN__15$', duration=4000, illustId='Hastur_normal', align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 전투후대화_07()


class 전투후대화_07(state.State):
    def on_enter(self):
        move_npc(spawnId=113, patrolName='MS2PatrolData_2003')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 전투후대화_08()

    def on_exit(self):
        destroy_monster(spawnIds=[113])


class 전투후대화_08(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000146_QD__52000146_MAIN__16$', duration=5000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 전투후대화_09()


class 스킵도착_01(state.State):
    def on_enter(self):
        set_scene_skip()
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        destroy_monster(spawnIds=[113])
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 스킵도착_02()


class 스킵도착_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 전투후대화_09()


class 전투후대화_09(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$52000146_QD__52000146_MAIN__17$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 전투후대화_10()

    def on_exit(self):
        set_cinematic_ui(type=2)


class 전투후대화_10(state.State):
    def on_enter(self):
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 전투후대화_11()


class 전투후대화_11(state.State):
    def on_enter(self):
        set_scene_skip(state=하스터찾기_01, arg2='nextState')
        add_cinematic_talk(npcId=0, msg='$52000146_QD__52000146_MAIN__18$', duration=4000, align='right')
        add_cinematic_talk(npcId=0, msg='$52000146_QD__52000146_MAIN__19$', duration=3000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7500):
            return 하스터찾기_01()


class 하스터찾기_01(state.State):
    def on_enter(self):
        set_scene_skip()
        remove_cinematic_talk()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        show_guide_summary(entityId=25201462, textId=25201462)
        set_effect(triggerIds=[5001,5002,5003,5004,5005,5006], visible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[702]):
            return 강제이동()


class 강제이동(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=25201462)
        move_user(mapId=52000147, portalId=1)


