""" trigger/52010070_qd/52010070.xml """
from common import *
import state


class wait_01(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[2001], jobCode=0):
            return 엔피씨스폰()


class 엔피씨스폰(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=False) # 유페리아
        create_monster(spawnIds=[102], arg2=False) # 이슈라
        create_monster(spawnIds=[103], arg2=False) # 렌듀비앙
        create_monster(spawnIds=[107], arg2=False) # 라네모네
        create_monster(spawnIds=[109], arg2=False) # 홀슈타트
        set_effect(triggerIds=[5001], visible=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[50100800], questStates=[2]):
            return 룬블즈_일어남()
        if quest_user_detected(boxIds=[2001], questIds=[50100790], questStates=[2]):
            return 룬블즈_일어남()
        if quest_user_detected(boxIds=[2001], questIds=[50100790], questStates=[3]):
            return 룬블즈_일어남()


class 룬블즈_일어남(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_scene_skip(state=Skip_1, arg2='nextState')
        set_cinematic_ui(type=1)
        select_camera_path(pathIds=[4004], returnView=False)
        move_user(mapId=52010070, portalId=6001)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 룬블즈_일어남_02()


class 룬블즈_일어남_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 룬블즈_일어남_03()


class 룬블즈_일어남_03(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=109, sequenceName='Attack_Idle_A', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 룬블즈_일어남_04()


class 룬블즈_일어남_04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4003], returnView=False)
        set_npc_emotion_loop(spawnId=107, sequenceName='Bore_A', duration=4000)
        set_npc_emotion_loop(spawnId=109, sequenceName='Attack_01_A', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 룬블즈_일어남_04_01()


class 룬블즈_일어남_04_01(state.State):
    def on_enter(self):
        set_time_scale(enable=True, startScale=0.1, endScale=0.5, duration=5, interpolator=1)
        set_npc_emotion_loop(spawnId=109, sequenceName='Attack_Idle_A', duration=4000)
        set_effect(triggerIds=[5001], visible=True)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 룬블즈_일어남_05()


class Skip_1(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 룬블즈_일어남_05()


class 룬블즈_일어남_05(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_onetime_effect(id=30, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOut.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 룬블즈_일어남_07()


class 룬블즈_일어남_07(state.State):
    def on_enter(self):
        set_onetime_effect(id=30, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOut.xml')
        set_scene_skip(state=Skip_2, arg2='nextState')
        select_camera_path(pathIds=[4001], returnView=False)
        create_monster(spawnIds=[104], arg2=False) # 유페리아
        create_monster(spawnIds=[105], arg2=False) # 이슈라
        create_monster(spawnIds=[106], arg2=False) # 렌듀비앙
        destroy_monster(spawnIds=[101], arg2=False)
        destroy_monster(spawnIds=[102], arg2=False)
        destroy_monster(spawnIds=[103], arg2=False)
        set_effect(triggerIds=[5001], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 룬블즈_일어남_08()


class 룬블즈_일어남_08(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4002], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 룬블즈_일어남_09()


class 룬블즈_일어남_09(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 룬블즈_일어남_09_01()


class 룬블즈_일어남_09_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 룬블즈_일어남_10()


class Skip_2(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_onetime_effect(id=30, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOut.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 룬블즈_일어남_10()


class 룬블즈_일어남_10(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[50100790], questStates=[3]):
            return 홀슈타트로바꾸기()


class 홀슈타트로바꾸기(state.State):
    def on_enter(self):
        create_monster(spawnIds=[108], arg2=False)
        destroy_monster(spawnIds=[109], arg2=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[50100800], questStates=[2]):
            return 에레브흑화()


class 에레브흑화(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_scene_skip(state=Skip_3, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 에레브흑화_02()


class 에레브흑화_02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[4005], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 에레브흑화_03()


class 에레브흑화_03(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 에레브흑화_04()


class 에레브흑화_04(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        move_user(mapId=52010070, portalId=6001)
        move_npc(spawnId=104, patrolName='MS2PatrolData_3001')
        add_cinematic_talk(npcId=11004128, align='left', illustId='Ishura_normal', msg='$52010070_QD__52010070__0$', duration=4000)
        add_cinematic_talk(npcId=11004191, align='left', illustId='11004022', msg='$52010070_QD__52010070__1$', duration=4000)
        add_cinematic_talk(npcId=11004128, align='left', illustId='Ishura_normal', msg='$52010070_QD__52010070__2$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=11000):
            return 에레브흑화_05()


class 에레브흑화_05(state.State):
    def on_enter(self):
        create_widget(type='SceneMovie')
        widget_action(type='SceneMovie', func='Clear')
        play_scene_movie(fileName='ProphecyofFall.swf', movieId=1)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 에레브흑화_06()
        if wait_tick(waitTick=85000):
            return 에레브흑화_06()


class Skip_3(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 에레브흑화_06()


class 에레브흑화_06(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[50100800], questStates=[3]):
            return 이동시키기()


class 이동시키기(state.State):
    def on_enter(self):
        move_user(mapId=52010072, portalId=1)


