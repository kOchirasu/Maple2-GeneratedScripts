""" trigger/63000067_cs/63000067_main.xml """
from common import *
import state


class 준비(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=True)
        create_monster(spawnIds=[102], arg2=True)
        create_monster(spawnIds=[103], arg2=True)
        create_monster(spawnIds=[104], arg2=True)
        create_monster(spawnIds=[105], arg2=True)
        create_monster(spawnIds=[106], arg2=True)
        create_monster(spawnIds=[107], arg2=True)
        create_monster(spawnIds=[108], arg2=True)
        create_monster(spawnIds=[109], arg2=True)
        create_monster(spawnIds=[110], arg2=True)
        create_monster(spawnIds=[111], arg2=True)
        create_monster(spawnIds=[112], arg2=True)
        create_monster(spawnIds=[113], arg2=True)
        set_effect(triggerIds=[5001], visible=False)
        set_effect(triggerIds=[5002], visible=False)
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[30000352], questStates=[1]):
            return 인형찾기()
        if quest_user_detected(boxIds=[701], questIds=[30000352], questStates=[2]):
            return 마리엔의방()
        if user_detected(boxIds=[701]):
            return 종료_일반()


class 인형찾기(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26300671, textId=26300671)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[702], questIds=[30000352], questStates=[2]):
            return 암전_01()


class 마리엔의방(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[702], questIds=[30000352], questStates=[2]):
            return 암전_01()


class 암전_01(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=26300671)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 암전_02()


class 암전_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8001], returnView=False)
        move_user_path(patrolName='MS2PatrolData_2001')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 마리엔등장_01()


class 마리엔등장_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        set_scene_skip(state=스킵종료, arg2='exit')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 마리엔등장_02()


class 마리엔등장_02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 마리엔등장_03()

    def on_exit(self):
        select_camera_path(pathIds=[8002], returnView=False)


class 마리엔등장_03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[201], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 마리엔등장_04()


class 마리엔등장_04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004294, msg='$63000067_CS__63000067_MAIN__0$', duration=3000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 마리엔등장_05()


class 마리엔등장_05(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004294, msg='$63000067_CS__63000067_MAIN__1$', duration=3500, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 마리엔등장_06()


class 마리엔등장_06(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8003], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 마리엔등장_07()


class 마리엔등장_07(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004294, msg='$63000067_CS__63000067_MAIN__2$', duration=3500, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 마리엔등장_08()


class 마리엔등장_08(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8002], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 마리엔등장_09()


class 마리엔등장_09(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004294, msg='$63000067_CS__63000067_MAIN__3$', duration=2000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 마리엔등장_10()


class 마리엔등장_10(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004294, msg='$63000067_CS__63000067_MAIN__4$', duration=2500, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 마리엔퇴장_01()


class 마리엔퇴장_01(state.State):
    def on_enter(self):
        set_scene_skip()
        destroy_monster(spawnIds=[201])
        set_effect(triggerIds=[5002], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 마리엔퇴장_02()


class 마리엔퇴장_02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0)

    def on_tick(self) -> state.State:
        if true():
            return 종료_퀘스트()


class 스킵종료(state.State):
    def on_enter(self):
        set_scene_skip()
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0)
        destroy_monster(spawnIds=[201])

    def on_tick(self) -> state.State:
        if true():
            return 종료_퀘스트()


class 종료_퀘스트(state.State):
    def on_enter(self):
        set_scene_skip()
        set_effect(triggerIds=[5002], visible=False)
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)


class 종료_일반(state.State):
    pass


