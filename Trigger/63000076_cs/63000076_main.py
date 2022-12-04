""" trigger/63000076_cs/63000076_main.xml """
import trigger_api


class 준비(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.create_monster(spawnIds=[105], animationEffect=False)
        self.create_monster(spawnIds=[106], animationEffect=False)
        self.create_monster(spawnIds=[107], animationEffect=False)
        self.create_monster(spawnIds=[118], animationEffect=False)
        self.create_monster(spawnIds=[119], animationEffect=False)
        self.set_mesh(triggerIds=[4001], visible=True)
        self.set_mesh(triggerIds=[4002], visible=True)
        self.set_mesh(triggerIds=[4003], visible=True)
        self.set_mesh(triggerIds=[4004], visible=True)
        self.set_mesh(triggerIds=[4005], visible=False)
        self.set_mesh(triggerIds=[4006], visible=False)
        self.set_mesh(triggerIds=[4007], visible=False)
        self.set_mesh(triggerIds=[4008], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[30000375], questStates=[2]):
            return 보보스발소리_01(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[30000375], questStates=[1]):
            return 잠시대기_01(self.ctx)
        if self.user_detected(boxIds=[701]):
            return 종료(self.ctx)


class 잠시대기_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 잠시대기_02(self.ctx)


class 잠시대기_02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=8001, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 요정잡담_01(self.ctx)


class 요정잡담_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_scene_skip(state=요정잡담종료_01, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 요정잡담_02(self.ctx)


class 요정잡담_02(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=103, msg='$63000076_CS__63000076_MAIN__0$', duration=2500) # $npcName:11004372$가 맛있는 디저트를 준대!

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return 요정잡담_03(self.ctx)


class 요정잡담_03(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=101, msg='$63000076_CS__63000076_MAIN__1$', duration=2500) # 착한 $npcName:11004372$!\n달콤한 걸 먹는 게 내 소원이었어!

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return 요정잡담_04(self.ctx)


class 요정잡담_04(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8002], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 요정잡담_05(self.ctx)


class 요정잡담_05(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=105, msg='$63000076_CS__63000076_MAIN__2$', duration=2500) # $npcName:11004372$가 얼른 왔으면 좋겠어

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return 요정잡담_06(self.ctx)


class 요정잡담_06(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=107, msg='$63000076_CS__63000076_MAIN__3$', duration=2500) # 입에 침이 고였어. 추릅

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return 요정잡담_07(self.ctx)


class 요정잡담_07(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8002,8003], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 요정잡담_08(self.ctx)


class 요정잡담_08(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=112, msg='$63000076_CS__63000076_MAIN__4$', duration=2500) # 틀림없이 맛있을 거야

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return 요정잡담_09(self.ctx)


class 요정잡담_09(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=113, msg='$63000076_CS__63000076_MAIN__5$', duration=2500) # 착한 $npcName:11004372$가 내 소원을 들어주겠대

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return 요정잡담_10(self.ctx)


class 요정잡담_10(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=114, msg='$63000076_CS__63000076_MAIN__6$', duration=2500) # 얼른 케이크 먹고 싶어

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 요정잡담종료_01(self.ctx)


class 요정잡담종료_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 요정잡담종료_02(self.ctx)

    def on_exit(self):
        self.reset_camera(interpolationTime=0)


class 요정잡담종료_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        # <action name="ShowGuideSummary" entityID="26300731" textID="26300731"/>

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[701,702,703,704,705,706,707,708], questIds=[30000375], questStates=[2]):
            return 보보스발소리_01(self.ctx)


class 보보스발소리_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 보보스발소리_02(self.ctx)


class 보보스발소리_02(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[201,202,203,204,208,209,210,211,212,213,214,215,216,217])
        self.move_user(mapId=63000076, portalId=1)
        self.set_scene_skip(state=연출종료_01, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 보보스발소리_03(self.ctx)


class 보보스발소리_03(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11004375, msg='$63000076_CS__63000076_MAIN__7$', duration=2000, align='right') # 오잉? 소리가 들린다!

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return 보보스발소리_04(self.ctx)


class 보보스발소리_04(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11004375, msg='$63000076_CS__63000076_MAIN__8$', duration=3000, align='right') # $npcName:11004372$다!\n$npcName:11004372$$pp:가,이$ 오는 소리야!

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 보보스등장_01(self.ctx)


class 보보스등장_01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8004], returnView=False)
        self.create_monster(spawnIds=[141], animationEffect=False)
        self.create_monster(spawnIds=[142], animationEffect=False)
        self.set_mesh(triggerIds=[4001], visible=False)
        self.set_mesh(triggerIds=[4002], visible=False)
        self.set_mesh(triggerIds=[4003], visible=False)
        self.set_mesh(triggerIds=[4004], visible=False)
        self.set_mesh(triggerIds=[4005], visible=True)
        self.set_mesh(triggerIds=[4006], visible=True)
        self.set_mesh(triggerIds=[4007], visible=True)
        self.set_mesh(triggerIds=[4008], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 보보스등장_02(self.ctx)


class 보보스등장_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 보보스등장_03(self.ctx)


class 보보스등장_03(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=106, msg='$63000076_CS__63000076_MAIN__9$', duration=2500) # $npcName:11004372$$pp:가,이$ 달콤한 걸 갖고 왔다!

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 보보스등장_04(self.ctx)


class 보보스등장_04(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=111, msg='$63000076_CS__63000076_MAIN__10$', duration=2500) # 와! 달콤한 거다!

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 보보스등장_05(self.ctx)


class 보보스등장_05(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11004372, msg='$63000076_CS__63000076_MAIN__11$', duration=3000, align='right') # 맛있게 먹어! 크리스마스 케이크야!

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 보보스등장_06(self.ctx)


class 보보스등장_06(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8004,8006], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return 보보스등장_07(self.ctx)


class 보보스등장_07(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=142, msg='$63000076_CS__63000076_MAIN__12$', duration=4000) # 읍, 읍…

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return 보보스등장_08(self.ctx)


class 보보스등장_08(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$63000076_CS__63000076_MAIN__13$', duration=2500, align='right') # 뭐지? 사람 소리 같은데?

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 보보스등장_09(self.ctx)


class 보보스등장_09(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 보보스등장_10(self.ctx)


class 보보스등장_10(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$63000076_CS__63000076_MAIN__14$') # 잠시 후

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return 사라진케이크_01(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=2)


class 사라진케이크_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 사라진케이크_02(self.ctx)


class 사라진케이크_02(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11004375, msg='$63000076_CS__63000076_MAIN__15$', duration=2500, align='right') # 착한 $npcName:11004372$! 잘 먹었어!
        self.set_mesh(triggerIds=[4005], visible=False)
        self.set_mesh(triggerIds=[4006], visible=False)
        self.set_mesh(triggerIds=[4007], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 사라진케이크_03(self.ctx)


class 사라진케이크_03(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11004375, msg='$63000076_CS__63000076_MAIN__16$', duration=3000, align='right') # $npcName:11004372$$pp:는,은$ 산타클로스의 좋은 친구가 될 수 있을 거야!

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 사라진케이크_04(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119])


class 사라진케이크_04(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$63000076_CS__63000076_MAIN__17$') # 요정들은 순식간에 케이크를 먹어치워 버렸고,\n그 녀석을 남긴 채 모두 사라졌다."

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 사라진케이크_05(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=2)


class 사라진케이크_05(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8004], returnView=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 미아등장_01(self.ctx)


class 미아등장_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 미아등장_02(self.ctx)


class 미아등장_02(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11004372, msg='$63000076_CS__63000076_MAIN__18$', duration=3000, align='right') # 다 먹어 버렸네… 미안…

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 미아등장_03(self.ctx)


class 미아등장_03(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11004372, msg='$63000076_CS__63000076_MAIN__19$', duration=3000, align='right') # 그치만… 케이크 속에 파묻혀 지냈으니 난 소원 들어 준 거야.

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 미아등장_04(self.ctx)


class 미아등장_04(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11004372, msg='$63000076_CS__63000076_MAIN__20$', duration=3000, align='right') # 난 또 소원 들어주러 가야 해서 이만

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 미아등장_05(self.ctx)


class 미아등장_05(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=141, patrolName='MS2PatrolData_2001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 미아등장_06(self.ctx)


class 미아등장_06(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 미아등장_07(self.ctx)


class 미아등장_07(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[141])
        self.select_camera_path(pathIds=[8008], returnView=False)
        self.move_user(mapId=63000076, portalId=2)
        self.move_npc(spawnId=142, patrolName='MS2PatrolData_2002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 미아등장_08(self.ctx)


class 미아등장_08(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=5, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 미아등장_09(self.ctx)


class 미아등장_09(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11004364, msg='$63000076_CS__63000076_MAIN__21$', duration=3000, illustId='Mia_annoyed', align='right') # …으, 하얀 털북숭이 녀석. 이게 대체 무슨 일이람

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 미아등장_10(self.ctx)


class 미아등장_10(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$63000076_CS__63000076_MAIN__22$', duration=2500, align='right') # 괜찮으세요?

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 미아등장_11(self.ctx)


class 미아등장_11(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11004364, msg='$63000076_CS__63000076_MAIN__23$', duration=2500, illustId='Mia_annoyed', align='right') # 누구시죠?

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 미아등장_12(self.ctx)


class 미아등장_12(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$63000076_CS__63000076_MAIN__24$', duration=3500, align='right') # $npcName:11004354$$pp:와,과$ $npcName:11004359$의 부탁으로 당신을 찾아왔어요.

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 미아등장_13(self.ctx)


class 미아등장_13(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11004364, msg='$63000076_CS__63000076_MAIN__25$', duration=3000, illustId='Mia_normal', align='right') # 아! 우리 아이들은 어디에 있나요? 무사한가요?

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 미아등장_14(self.ctx)


class 미아등장_14(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$63000076_CS__63000076_MAIN__26$', duration=2500, align='right') # 거실에 있어요. (그것도 아주 잘…)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 미아등장_15(self.ctx)


class 미아등장_15(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11004364, msg='$63000076_CS__63000076_MAIN__27$', duration=3000, illustId='Mia_annoyed', align='right') # 다행이네요. 어서 만나봐야겠어요.\n거실에서 만나요.

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 미아등장_16(self.ctx)


class 미아등장_16(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=6, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 미아등장_17(self.ctx)


class 미아등장_17(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.destroy_monster(spawnIds=[142])
        self.reset_camera(interpolationTime=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 미아등장_18(self.ctx)


class 미아등장_18(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=6, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 종료(self.ctx)


class 연출종료_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=7, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_scene_skip()
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출종료_02(self.ctx)


class 연출종료_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[4001], visible=False)
        self.set_mesh(triggerIds=[4002], visible=False)
        self.set_mesh(triggerIds=[4003], visible=False)
        self.set_mesh(triggerIds=[4004], visible=False)
        self.set_mesh(triggerIds=[4005], visible=False)
        self.set_mesh(triggerIds=[4006], visible=False)
        self.set_mesh(triggerIds=[4007], visible=False)
        self.set_mesh(triggerIds=[4008], visible=True)
        self.destroy_monster(spawnIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,141,142])
        self.reset_camera(interpolationTime=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출종료_03(self.ctx)


class 연출종료_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=7, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = 준비
