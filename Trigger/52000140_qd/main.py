""" trigger/52000140_qd/main.xml """
from common import *
import state


class 준비(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_effect(triggerIds=[5001], visible=False)
        set_cinematic_ui(type=0) # 유저 이동 하게
        set_cinematic_ui(type=2) # UI 숨기기 초기화
        create_monster(spawnIds=[101], arg2=False)
        create_monster(spawnIds=[102], arg2=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[701]):
            return 카메라연출_01()


class 카메라연출_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        select_camera_path(pathIds=[8002], returnView=False)
        set_cinematic_ui(type=1) # 유저 이동 못 하게
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 카메라연출_02()


class 카메라연출_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 카메라연출_04()


class 카메라연출_04(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_2001')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 카메라연출_05()


class 카메라연출_05(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 삼자대화_01()

    def on_exit(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_2002')


class 삼자대화_01(state.State):
    def on_enter(self):
        set_scene_skip(state=투르카소멸_01, arg2='nextState')
        add_cinematic_talk(npcId=0, msg='$52000140_QD__MAIN__0$', duration=2500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 삼자대화_02()


class 삼자대화_02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003328, msg='$52000140_QD__MAIN__1$', duration=3000, align='center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 삼자대화_03()


class 삼자대화_03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003329, msg='$52000140_QD__MAIN__2$', duration=2500, align='right')
        move_npc(spawnId=101, patrolName='MS2PatrolData_2003')
        add_cinematic_talk(npcId=11003329, msg='$52000140_QD__MAIN__3$', duration=2500, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5300):
            return 투르카소멸_01()


class 투르카소멸_01(state.State):
    def on_enter(self):
        set_scene_skip()
        set_effect(triggerIds=[5001], visible=True)
        destroy_monster(spawnIds=[102])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 투르카소멸_02()


class 투르카소멸_02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=False)
        reset_camera(interpolationTime=2)
        set_cinematic_ui(type=2) # UI 숨기기 초기화
        set_cinematic_ui(type=0) # 유저 이동 가능하게
        destroy_monster(spawnIds=[101])
        create_monster(spawnIds=[105], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 어둠의졸개_01()


class 어둠의졸개_01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[103,104], arg2=True)
        show_guide_summary(entityId=25201401, textId=25201401)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[103,104]):
            return 졸개퇴치완료_01()


class 졸개퇴치완료_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        hide_guide_summary(entityId=25201401)
        set_cinematic_ui(type=1) # 유저 이동 못하게
        set_cinematic_ui(type=3) # 상하 레터박스

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 졸개퇴치완료_02()


class 졸개퇴치완료_02(state.State):
    def on_enter(self):
        move_user(mapId=52000140, portalId=99)
        destroy_monster(spawnIds=[105])
        create_monster(spawnIds=[101], arg2=False)
        move_npc(spawnId=101, patrolName='MS2PatrolData_2002')
        select_camera_path(pathIds=[8003], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 졸개퇴치완료_03()


class 졸개퇴치완료_03(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 알론과대화_01()


class 알론과대화_01(state.State):
    def on_enter(self):
        set_scene_skip(state=투르카와전투_01, arg2='nextState')
        add_cinematic_talk(npcId=0, msg='$52000140_QD__MAIN__4$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 알론과대화_02()


class 알론과대화_02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003328, msg='$52000140_QD__MAIN__5$', duration=3000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 알론과대화_03()


class 알론과대화_03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000140_QD__MAIN__6$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 알론과대화_04()


class 알론과대화_04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003328, msg='$52000140_QD__MAIN__7$', duration=2500, align='right')
        add_cinematic_talk(npcId=11003328, msg='$52000140_QD__MAIN__8$', duration=2500, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5300):
            return 알론과대화_05()


class 알론과대화_05(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000140_QD__MAIN__9$', duration=2500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 알론과대화_06()

    def on_exit(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_2003')


class 알론과대화_06(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003328, msg='$52000140_QD__MAIN__10$', duration=2000, align='right')
        move_user_path(patrolName='MS2PatrolData_2008')
        create_monster(spawnIds=[102], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2300):
            return 알론과대화_07()


class 알론과대화_07(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8003,8002], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2200):
            return 차삼자대화_01_2()


class 차삼자대화_01_2(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003329, msg='$52000140_QD__MAIN__11$', duration=3000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 차삼자대화_02_2()


class 차삼자대화_02_2(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000140_QD__MAIN__12$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 차삼자대화_03_2()


class 차삼자대화_03_2(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003329, msg='$52000140_QD__MAIN__13$', duration=2500, align='right')
        add_cinematic_talk(npcId=11003329, msg='$52000140_QD__MAIN__14$', duration=2500, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5200):
            return 차삼자대화_04_2()


class 차삼자대화_04_2(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003328, msg='$52000140_QD__MAIN__15$', duration=2500, align='center')
        add_cinematic_talk(npcId=11003328, msg='$52000140_QD__MAIN__16$', duration=2500, align='center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5200):
            return 차삼자대화_05_2()


class 차삼자대화_05_2(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003329, msg='$52000140_QD__MAIN__17$', duration=2500, align='right')
        add_cinematic_talk(npcId=11003329, msg='$52000140_QD__MAIN__18$', duration=2500, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5300):
            return 차삼자대화_06_2()


class 차삼자대화_06_2(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003328, msg='$52000140_QD__MAIN__19$', duration=2500, align='center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 차삼자대화_07_2()


class 차삼자대화_07_2(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003329, msg='$52000140_QD__MAIN__20$', duration=2500, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 차삼자대화_08_2()


class 차삼자대화_08_2(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003328, msg='$52000140_QD__MAIN__21$', duration=2000, align='center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2300):
            return 투르카와전투_01()


class 투르카와전투_01(state.State):
    def on_enter(self):
        set_scene_skip()
        reset_camera(interpolationTime=2)
        set_cinematic_ui(type=0) # 유저 이동 가능하게
        set_cinematic_ui(type=2) # UI 숨기기 초기화
        destroy_monster(spawnIds=[102])
        create_monster(spawnIds=[106], arg2=True)
        destroy_monster(spawnIds=[101])
        create_monster(spawnIds=[105], arg2=True)
        show_guide_summary(entityId=25201402, textId=25201402)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=15000):
            return 투르카와전투_02()


class 투르카와전투_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        hide_guide_summary(entityId=25201402)
        move_user(mapId=52000140, portalId=99)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 투르카와전투_03()


class 투르카와전투_03(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        select_camera_path(pathIds=[8002], returnView=False)
        destroy_monster(spawnIds=[106])
        create_monster(spawnIds=[102], arg2=False)
        destroy_monster(spawnIds=[105])
        create_monster(spawnIds=[101], arg2=False)
        move_user_path(patrolName='MS2PatrolData_2008')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 차삼자대화_01_3()


class 차삼자대화_01_3(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        add_cinematic_talk(npcId=11003329, msg='$52000140_QD__MAIN__22$', duration=2500, align='right')
        add_cinematic_talk(npcId=11003329, msg='$52000140_QD__MAIN__23$', duration=2500, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5300):
            return 차삼자대화_02_3()


class 차삼자대화_02_3(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000140_QD__MAIN__24$', duration=2000)
        move_user_path(patrolName='MS2PatrolData_2005')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2200):
            return 차삼자대화_03_3()


class 차삼자대화_03_3(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8006], returnView=False)
        add_cinematic_talk(npcId=11003328, msg='$52000140_QD__MAIN__25$', duration=2000, align='center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2200):
            return 투르카퇴장_01()


class 투르카퇴장_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8007], returnView=False)
        set_effect(triggerIds=[5001], visible=True)
        destroy_monster(spawnIds=[102])
        # <action name="SetPcEmotionSequence" arg1="Priest_Sanctuary_A" />
        set_pc_emotion_sequence(sequenceNames=['Priest_Skill_Divine_Protection_A'])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=700):
            return 투르카퇴장_02()


class 투르카퇴장_02(state.State):
    def on_enter(self):
        set_pc_emotion_loop(sequenceName='Down_Idle_A', duration=10000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PC의부상_01()


class PC의부상_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_pc_emotion_loop(sequenceName='Down_Idle_A', duration=10000)
        set_effect(triggerIds=[5001], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return PC의부상_02()


class PC의부상_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        select_camera_path(pathIds=[8004,8005], returnView=False)
        move_npc(spawnId=101, patrolName='MS2PatrolData_2007')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return PC의부상_03()


class PC의부상_03(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 강제이동()


class 강제이동(state.State):
    def on_enter(self):
        move_user(mapId=52000141, portalId=1)


