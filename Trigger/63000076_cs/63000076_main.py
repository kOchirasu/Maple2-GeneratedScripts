""" trigger/63000076_cs/63000076_main.xml """
from common import *
import state


class 준비(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        create_monster(spawnIds=[105], arg2=False)
        create_monster(spawnIds=[106], arg2=False)
        create_monster(spawnIds=[107], arg2=False)
        create_monster(spawnIds=[118], arg2=False)
        create_monster(spawnIds=[119], arg2=False)
        set_mesh(triggerIds=[4001], visible=True)
        set_mesh(triggerIds=[4002], visible=True)
        set_mesh(triggerIds=[4003], visible=True)
        set_mesh(triggerIds=[4004], visible=True)
        set_mesh(triggerIds=[4005], visible=False)
        set_mesh(triggerIds=[4006], visible=False)
        set_mesh(triggerIds=[4007], visible=False)
        set_mesh(triggerIds=[4008], visible=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[30000375], questStates=[2]):
            return 보보스발소리_01()
        if quest_user_detected(boxIds=[701], questIds=[30000375], questStates=[1]):
            return 잠시대기_01()
        if user_detected(boxIds=[701]):
            return 종료()


class 잠시대기_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 잠시대기_02()


class 잠시대기_02(state.State):
    def on_enter(self):
        select_camera(triggerId=8001, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 요정잡담_01()


class 요정잡담_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        set_scene_skip(state=요정잡담종료_01, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 요정잡담_02()


class 요정잡담_02(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=103, msg='$63000076_CS__63000076_MAIN__0$', duration=2500) # $npcName:11004372$가 맛있는 디저트를 준대!

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 요정잡담_03()


class 요정잡담_03(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=101, msg='$63000076_CS__63000076_MAIN__1$', duration=2500) # 착한 $npcName:11004372$!\n달콤한 걸 먹는 게 내 소원이었어!

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 요정잡담_04()


class 요정잡담_04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8002], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 요정잡담_05()


class 요정잡담_05(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=105, msg='$63000076_CS__63000076_MAIN__2$', duration=2500) # $npcName:11004372$가 얼른 왔으면 좋겠어

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 요정잡담_06()


class 요정잡담_06(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=107, msg='$63000076_CS__63000076_MAIN__3$', duration=2500) # 입에 침이 고였어. 추릅

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 요정잡담_07()


class 요정잡담_07(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8002,8003], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 요정잡담_08()


class 요정잡담_08(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=112, msg='$63000076_CS__63000076_MAIN__4$', duration=2500) # 틀림없이 맛있을 거야

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 요정잡담_09()


class 요정잡담_09(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=113, msg='$63000076_CS__63000076_MAIN__5$', duration=2500) # 착한 $npcName:11004372$가 내 소원을 들어주겠대

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 요정잡담_10()


class 요정잡담_10(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=114, msg='$63000076_CS__63000076_MAIN__6$', duration=2500) # 얼른 케이크 먹고 싶어

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 요정잡담종료_01()


class 요정잡담종료_01(state.State):
    def on_enter(self):
        set_scene_skip()
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 요정잡담종료_02()

    def on_exit(self):
        reset_camera(interpolationTime=0)


class 요정잡담종료_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        # <action name="ShowGuideSummary" entityID="26300731" textID="26300731"/>

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701,702,703,704,705,706,707,708], questIds=[30000375], questStates=[2]):
            return 보보스발소리_01()


class 보보스발소리_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 보보스발소리_02()


class 보보스발소리_02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[201,202,203,204,208,209,210,211,212,213,214,215,216,217])
        move_user(mapId=63000076, portalId=1)
        set_scene_skip(state=연출종료_01, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 보보스발소리_03()


class 보보스발소리_03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004375, msg='$63000076_CS__63000076_MAIN__7$', duration=2000, align='right') # 오잉? 소리가 들린다!

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 보보스발소리_04()


class 보보스발소리_04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004375, msg='$63000076_CS__63000076_MAIN__8$', duration=3000, align='right') # $npcName:11004372$다!\n$npcName:11004372$$pp:가,이$ 오는 소리야!

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 보보스등장_01()


class 보보스등장_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8004], returnView=False)
        create_monster(spawnIds=[141], arg2=False)
        create_monster(spawnIds=[142], arg2=False)
        set_mesh(triggerIds=[4001], visible=False)
        set_mesh(triggerIds=[4002], visible=False)
        set_mesh(triggerIds=[4003], visible=False)
        set_mesh(triggerIds=[4004], visible=False)
        set_mesh(triggerIds=[4005], visible=True)
        set_mesh(triggerIds=[4006], visible=True)
        set_mesh(triggerIds=[4007], visible=True)
        set_mesh(triggerIds=[4008], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 보보스등장_02()


class 보보스등장_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 보보스등장_03()


class 보보스등장_03(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=106, msg='$63000076_CS__63000076_MAIN__9$', duration=2500) # $npcName:11004372$$pp:가,이$ 달콤한 걸 갖고 왔다!

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 보보스등장_04()


class 보보스등장_04(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=111, msg='$63000076_CS__63000076_MAIN__10$', duration=2500) # 와! 달콤한 거다!

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 보보스등장_05()


class 보보스등장_05(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004372, msg='$63000076_CS__63000076_MAIN__11$', duration=3000, align='right') # 맛있게 먹어! 크리스마스 케이크야!

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 보보스등장_06()


class 보보스등장_06(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8004,8006], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 보보스등장_07()


class 보보스등장_07(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=142, msg='$63000076_CS__63000076_MAIN__12$', duration=4000) # 읍, 읍…

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 보보스등장_08()


class 보보스등장_08(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$63000076_CS__63000076_MAIN__13$', duration=2500, align='right') # 뭐지? 사람 소리 같은데?

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 보보스등장_09()


class 보보스등장_09(state.State):
    def on_enter(self):
        set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 보보스등장_10()


class 보보스등장_10(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$63000076_CS__63000076_MAIN__14$') # 잠시 후

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 사라진케이크_01()

    def on_exit(self):
        set_cinematic_ui(type=2)


class 사라진케이크_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 사라진케이크_02()


class 사라진케이크_02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004375, msg='$63000076_CS__63000076_MAIN__15$', duration=2500, align='right') # 착한 $npcName:11004372$! 잘 먹었어!
        set_mesh(triggerIds=[4005], visible=False)
        set_mesh(triggerIds=[4006], visible=False)
        set_mesh(triggerIds=[4007], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 사라진케이크_03()


class 사라진케이크_03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004375, msg='$63000076_CS__63000076_MAIN__16$', duration=3000, align='right') # $npcName:11004372$$pp:는,은$ 산타클로스의 좋은 친구가 될 수 있을 거야!

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 사라진케이크_04()

    def on_exit(self):
        destroy_monster(spawnIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119])


class 사라진케이크_04(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$63000076_CS__63000076_MAIN__17$') # 요정들은 순식간에 케이크를 먹어치워 버렸고,\n그 녀석을 남긴 채 모두 사라졌다."

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 사라진케이크_05()

    def on_exit(self):
        set_cinematic_ui(type=2)


class 사라진케이크_05(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8004], returnView=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 미아등장_01()


class 미아등장_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 미아등장_02()


class 미아등장_02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004372, msg='$63000076_CS__63000076_MAIN__18$', duration=3000, align='right') # 다 먹어 버렸네… 미안…

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 미아등장_03()


class 미아등장_03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004372, msg='$63000076_CS__63000076_MAIN__19$', duration=3000, align='right') # 그치만… 케이크 속에 파묻혀 지냈으니 난 소원 들어 준 거야.

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 미아등장_04()


class 미아등장_04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004372, msg='$63000076_CS__63000076_MAIN__20$', duration=3000, align='right') # 난 또 소원 들어주러 가야 해서 이만

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 미아등장_05()


class 미아등장_05(state.State):
    def on_enter(self):
        move_npc(spawnId=141, patrolName='MS2PatrolData_2001')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 미아등장_06()


class 미아등장_06(state.State):
    def on_enter(self):
        set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 미아등장_07()


class 미아등장_07(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[141])
        select_camera_path(pathIds=[8008], returnView=False)
        move_user(mapId=63000076, portalId=2)
        move_npc(spawnId=142, patrolName='MS2PatrolData_2002')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 미아등장_08()


class 미아등장_08(state.State):
    def on_enter(self):
        set_onetime_effect(id=5, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 미아등장_09()


class 미아등장_09(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004364, msg='$63000076_CS__63000076_MAIN__21$', duration=3000, illustId='Mia_annoyed', align='right') # …으, 하얀 털북숭이 녀석. 이게 대체 무슨 일이람

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 미아등장_10()


class 미아등장_10(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$63000076_CS__63000076_MAIN__22$', duration=2500, align='right') # 괜찮으세요?

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 미아등장_11()


class 미아등장_11(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004364, msg='$63000076_CS__63000076_MAIN__23$', duration=2500, illustId='Mia_annoyed', align='right') # 누구시죠?

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 미아등장_12()


class 미아등장_12(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$63000076_CS__63000076_MAIN__24$', duration=3500, align='right') # $npcName:11004354$$pp:와,과$ $npcName:11004359$의 부탁으로 당신을 찾아왔어요.

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 미아등장_13()


class 미아등장_13(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004364, msg='$63000076_CS__63000076_MAIN__25$', duration=3000, illustId='Mia_normal', align='right') # 아! 우리 아이들은 어디에 있나요? 무사한가요?

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 미아등장_14()


class 미아등장_14(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$63000076_CS__63000076_MAIN__26$', duration=2500, align='right') # 거실에 있어요. (그것도 아주 잘…)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 미아등장_15()


class 미아등장_15(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004364, msg='$63000076_CS__63000076_MAIN__27$', duration=3000, illustId='Mia_annoyed', align='right') # 다행이네요. 어서 만나봐야겠어요.\n거실에서 만나요.

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 미아등장_16()


class 미아등장_16(state.State):
    def on_enter(self):
        set_onetime_effect(id=6, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 미아등장_17()


class 미아등장_17(state.State):
    def on_enter(self):
        set_scene_skip()
        destroy_monster(spawnIds=[142])
        reset_camera(interpolationTime=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 미아등장_18()


class 미아등장_18(state.State):
    def on_enter(self):
        set_onetime_effect(id=6, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if true():
            return 종료()


class 연출종료_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=7, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_scene_skip()
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출종료_02()


class 연출종료_02(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4001], visible=False)
        set_mesh(triggerIds=[4002], visible=False)
        set_mesh(triggerIds=[4003], visible=False)
        set_mesh(triggerIds=[4004], visible=False)
        set_mesh(triggerIds=[4005], visible=False)
        set_mesh(triggerIds=[4006], visible=False)
        set_mesh(triggerIds=[4007], visible=False)
        set_mesh(triggerIds=[4008], visible=True)
        destroy_monster(spawnIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,141,142])
        reset_camera(interpolationTime=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출종료_03()


class 연출종료_03(state.State):
    def on_enter(self):
        set_onetime_effect(id=7, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


