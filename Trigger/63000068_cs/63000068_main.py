""" trigger/63000068_cs/63000068_main.xml """
from common import *
import state


class 준비(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        set_effect(triggerIds=[5001], visible=False)
        set_effect(triggerIds=[5002], visible=False)
        set_effect(triggerIds=[5003], visible=False)
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[30000358], questStates=[3]):
            return 몬스터등장_04()
        if quest_user_detected(boxIds=[701], questIds=[30000358], questStates=[2]):
            return 몬스터등장_04()
        if quest_user_detected(boxIds=[701], questIds=[30000358], questStates=[1]):
            return 몬스터등장_04()
        if quest_user_detected(boxIds=[701], questIds=[30000357], questStates=[3]):
            return 몬스터등장_04()
        if quest_user_detected(boxIds=[701], questIds=[30000357], questStates=[2]):
            return 몬스터등장_04()
        if quest_user_detected(boxIds=[701], questIds=[30000357], questStates=[1]):
            return 몬스터등장_04()
        if quest_user_detected(boxIds=[701], questIds=[30000356], questStates=[3]):
            return 몬스터등장_04()
        if quest_user_detected(boxIds=[701], questIds=[30000356], questStates=[2]):
            return 몬스터등장_04()
        if quest_user_detected(boxIds=[701], questIds=[30000356], questStates=[1]):
            return 몬스터등장_04()
        if quest_user_detected(boxIds=[701], questIds=[30000355], questStates=[3]):
            return 몬스터등장_04()
        if quest_user_detected(boxIds=[701], questIds=[30000355], questStates=[2]):
            return 몬스터등장_04()
        if quest_user_detected(boxIds=[701], questIds=[30000355], questStates=[1]):
            return 몬스터등장_04()
        if quest_user_detected(boxIds=[701], questIds=[30000354], questStates=[3]):
            return 몬스터등장_03()
        if quest_user_detected(boxIds=[701], questIds=[30000354], questStates=[2]):
            return 몬스터등장_02()
        if quest_user_detected(boxIds=[701], questIds=[30000354], questStates=[1]):
            return 잠시대기_01()
        if user_detected(boxIds=[701]):
            return 몬스터등장_04()


class 잠시대기_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 잠시대기_02()


class 잠시대기_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8001], returnView=False)
        create_monster(spawnIds=[201], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 마리엔등장_01()


class 마리엔등장_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        set_scene_skip(state=마리엔등장_10, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 마리엔등장_02()


class 마리엔등장_02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004294, msg='$63000068_CS__63000068_MAIN__0$', duration=2000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 마리엔등장_03()


class 마리엔등장_03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004294, msg='$63000068_CS__63000068_MAIN__1$', duration=2500, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 마리엔등장_04()


class 마리엔등장_04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004294, msg='$63000068_CS__63000068_MAIN__2$', duration=3000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 마리엔등장_05()


class 마리엔등장_05(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8002], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5500):
            return 마리엔등장_06()


class 마리엔등장_06(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8001], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 마리엔등장_07()


class 마리엔등장_07(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004294, msg='$63000068_CS__63000068_MAIN__3$', duration=2500, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 마리엔등장_08()


class 마리엔등장_08(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004294, msg='$63000068_CS__63000068_MAIN__4$', duration=3000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 마리엔등장_09()


class 마리엔등장_09(state.State):
    def on_enter(self):
        move_npc(spawnId=201, patrolName='MS2PatrolData_2001')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 마리엔등장_10()


class 마리엔등장_10(state.State):
    def on_enter(self):
        set_scene_skip()
        select_camera_path(pathIds=[8003], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 몬스터등장_01()


class 몬스터등장_01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=False)
        create_monster(spawnIds=[102], arg2=False)
        create_monster(spawnIds=[103], arg2=False)
        create_monster(spawnIds=[104], arg2=False)
        create_monster(spawnIds=[105], arg2=False)
        create_monster(spawnIds=[106], arg2=False)
        create_monster(spawnIds=[107], arg2=False)
        create_monster(spawnIds=[108], arg2=False)
        create_monster(spawnIds=[109], arg2=False)
        create_monster(spawnIds=[110], arg2=False)
        create_monster(spawnIds=[111], arg2=False)
        create_monster(spawnIds=[112], arg2=False)
        create_monster(spawnIds=[113], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 마리엔퇴장_01()


class 몬스터등장_02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=False)
        create_monster(spawnIds=[102], arg2=False)
        create_monster(spawnIds=[103], arg2=False)
        create_monster(spawnIds=[104], arg2=False)
        create_monster(spawnIds=[105], arg2=False)
        create_monster(spawnIds=[106], arg2=False)
        create_monster(spawnIds=[107], arg2=False)
        create_monster(spawnIds=[108], arg2=False)
        create_monster(spawnIds=[109], arg2=False)
        create_monster(spawnIds=[110], arg2=False)
        create_monster(spawnIds=[111], arg2=False)
        create_monster(spawnIds=[112], arg2=False)
        create_monster(spawnIds=[113], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 재입장시()


class 몬스터등장_03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=False)
        create_monster(spawnIds=[102], arg2=False)
        create_monster(spawnIds=[103], arg2=False)
        create_monster(spawnIds=[104], arg2=False)
        create_monster(spawnIds=[105], arg2=False)
        create_monster(spawnIds=[106], arg2=False)
        create_monster(spawnIds=[107], arg2=False)
        create_monster(spawnIds=[108], arg2=False)
        create_monster(spawnIds=[109], arg2=False)
        create_monster(spawnIds=[110], arg2=False)
        create_monster(spawnIds=[111], arg2=False)
        create_monster(spawnIds=[112], arg2=False)
        create_monster(spawnIds=[113], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 퀘스트마리엔등장()


class 몬스터등장_04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=False)
        create_monster(spawnIds=[102], arg2=False)
        create_monster(spawnIds=[103], arg2=False)
        create_monster(spawnIds=[104], arg2=False)
        create_monster(spawnIds=[105], arg2=False)
        create_monster(spawnIds=[106], arg2=False)
        create_monster(spawnIds=[107], arg2=False)
        create_monster(spawnIds=[108], arg2=False)
        create_monster(spawnIds=[109], arg2=False)
        create_monster(spawnIds=[110], arg2=False)
        create_monster(spawnIds=[111], arg2=False)
        create_monster(spawnIds=[112], arg2=False)
        create_monster(spawnIds=[113], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 종료()


class 마리엔퇴장_01(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 마리엔퇴장_02()


class 마리엔퇴장_02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004294, msg='$63000068_CS__63000068_MAIN__5$', duration=2000, align='right')
        set_effect(triggerIds=[5003], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 마리엔퇴장_03()


class 마리엔퇴장_03(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[201])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 마리엔퇴장_04()


class 마리엔퇴장_04(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        show_guide_summary(entityId=26300681, textId=26300681)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[705], questIds=[30000354], questStates=[2]):
            return 암전_01()


class 재입장시(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[705], questIds=[30000354], questStates=[2]):
            return 암전_01()


class 암전_01(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=26300681)
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 암전_02()


class 암전_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8004], returnView=False)
        move_user_path(patrolName='MS2PatrolData_2002')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 마리엔재등장_01()


class 마리엔재등장_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        set_scene_skip(state=재등장연출완료, arg2='exit')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 마리엔재등장_02()


class 마리엔재등장_02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 마리엔재등장_03()


class 마리엔재등장_03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[202], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 마리엔재등장_04()


class 마리엔재등장_04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004294, msg='$63000068_CS__63000068_MAIN__6$', duration=3000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 마리엔재등장_05()


class 마리엔재등장_05(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004294, msg='$63000068_CS__63000068_MAIN__7$', duration=3000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 마리엔재등장_06()


class 마리엔재등장_06(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004294, msg='$63000068_CS__63000068_MAIN__8$', duration=3000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 마리엔재등장_07()


class 마리엔재등장_07(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004294, msg='$63000068_CS__63000068_MAIN__9$', duration=2000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 재등장연출완료()


class 재등장연출완료(state.State):
    def on_enter(self):
        set_scene_skip()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 퀘스트마리엔등장()


class 퀘스트마리엔등장(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[202])
        create_monster(spawnIds=[203], arg2=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[705], questIds=[30000355], questStates=[1]):
            return 퀘스트마리엔퇴장_01()
        if quest_user_detected(boxIds=[705], questIds=[30000355], questStates=[2]):
            return 퀘스트마리엔퇴장_01()


class 퀘스트마리엔퇴장_01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5002], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 퀘스트마리엔퇴장_02()


class 퀘스트마리엔퇴장_02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[203])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)


