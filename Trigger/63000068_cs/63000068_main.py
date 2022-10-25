""" trigger/63000068_cs/63000068_main.xml """
import common


class 준비(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_effect(triggerIds=[5001], visible=False)
        self.set_effect(triggerIds=[5002], visible=False)
        self.set_effect(triggerIds=[5003], visible=False)
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[30000358], questStates=[3]):
            return 몬스터등장_04(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[30000358], questStates=[2]):
            return 몬스터등장_04(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[30000358], questStates=[1]):
            return 몬스터등장_04(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[30000357], questStates=[3]):
            return 몬스터등장_04(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[30000357], questStates=[2]):
            return 몬스터등장_04(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[30000357], questStates=[1]):
            return 몬스터등장_04(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[30000356], questStates=[3]):
            return 몬스터등장_04(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[30000356], questStates=[2]):
            return 몬스터등장_04(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[30000356], questStates=[1]):
            return 몬스터등장_04(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[30000355], questStates=[3]):
            return 몬스터등장_04(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[30000355], questStates=[2]):
            return 몬스터등장_04(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[30000355], questStates=[1]):
            return 몬스터등장_04(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[30000354], questStates=[3]):
            return 몬스터등장_03(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[30000354], questStates=[2]):
            return 몬스터등장_02(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[30000354], questStates=[1]):
            return 잠시대기_01(self.ctx)
        if self.user_detected(boxIds=[701]):
            return 몬스터등장_04(self.ctx)


class 잠시대기_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 잠시대기_02(self.ctx)


class 잠시대기_02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8001], returnView=False)
        self.create_monster(spawnIds=[201], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return 마리엔등장_01(self.ctx)


class 마리엔등장_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_scene_skip(state=마리엔등장_10, action='nextState')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 마리엔등장_02(self.ctx)


class 마리엔등장_02(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11004294, msg='$63000068_CS__63000068_MAIN__0$', duration=2000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2500):
            return 마리엔등장_03(self.ctx)


class 마리엔등장_03(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11004294, msg='$63000068_CS__63000068_MAIN__1$', duration=2500, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 마리엔등장_04(self.ctx)


class 마리엔등장_04(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11004294, msg='$63000068_CS__63000068_MAIN__2$', duration=3000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 마리엔등장_05(self.ctx)


class 마리엔등장_05(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8002], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5500):
            return 마리엔등장_06(self.ctx)


class 마리엔등장_06(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8001], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return 마리엔등장_07(self.ctx)


class 마리엔등장_07(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11004294, msg='$63000068_CS__63000068_MAIN__3$', duration=2500, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 마리엔등장_08(self.ctx)


class 마리엔등장_08(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11004294, msg='$63000068_CS__63000068_MAIN__4$', duration=3000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 마리엔등장_09(self.ctx)


class 마리엔등장_09(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_2001')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return 마리엔등장_10(self.ctx)


class 마리엔등장_10(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.select_camera_path(pathIds=[8003], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 몬스터등장_01(self.ctx)


class 몬스터등장_01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.create_monster(spawnIds=[102], animationEffect=False)
        self.create_monster(spawnIds=[103], animationEffect=False)
        self.create_monster(spawnIds=[104], animationEffect=False)
        self.create_monster(spawnIds=[105], animationEffect=False)
        self.create_monster(spawnIds=[106], animationEffect=False)
        self.create_monster(spawnIds=[107], animationEffect=False)
        self.create_monster(spawnIds=[108], animationEffect=False)
        self.create_monster(spawnIds=[109], animationEffect=False)
        self.create_monster(spawnIds=[110], animationEffect=False)
        self.create_monster(spawnIds=[111], animationEffect=False)
        self.create_monster(spawnIds=[112], animationEffect=False)
        self.create_monster(spawnIds=[113], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 마리엔퇴장_01(self.ctx)


class 몬스터등장_02(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.create_monster(spawnIds=[102], animationEffect=False)
        self.create_monster(spawnIds=[103], animationEffect=False)
        self.create_monster(spawnIds=[104], animationEffect=False)
        self.create_monster(spawnIds=[105], animationEffect=False)
        self.create_monster(spawnIds=[106], animationEffect=False)
        self.create_monster(spawnIds=[107], animationEffect=False)
        self.create_monster(spawnIds=[108], animationEffect=False)
        self.create_monster(spawnIds=[109], animationEffect=False)
        self.create_monster(spawnIds=[110], animationEffect=False)
        self.create_monster(spawnIds=[111], animationEffect=False)
        self.create_monster(spawnIds=[112], animationEffect=False)
        self.create_monster(spawnIds=[113], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 재입장시(self.ctx)


class 몬스터등장_03(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.create_monster(spawnIds=[102], animationEffect=False)
        self.create_monster(spawnIds=[103], animationEffect=False)
        self.create_monster(spawnIds=[104], animationEffect=False)
        self.create_monster(spawnIds=[105], animationEffect=False)
        self.create_monster(spawnIds=[106], animationEffect=False)
        self.create_monster(spawnIds=[107], animationEffect=False)
        self.create_monster(spawnIds=[108], animationEffect=False)
        self.create_monster(spawnIds=[109], animationEffect=False)
        self.create_monster(spawnIds=[110], animationEffect=False)
        self.create_monster(spawnIds=[111], animationEffect=False)
        self.create_monster(spawnIds=[112], animationEffect=False)
        self.create_monster(spawnIds=[113], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 퀘스트마리엔등장(self.ctx)


class 몬스터등장_04(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.create_monster(spawnIds=[102], animationEffect=False)
        self.create_monster(spawnIds=[103], animationEffect=False)
        self.create_monster(spawnIds=[104], animationEffect=False)
        self.create_monster(spawnIds=[105], animationEffect=False)
        self.create_monster(spawnIds=[106], animationEffect=False)
        self.create_monster(spawnIds=[107], animationEffect=False)
        self.create_monster(spawnIds=[108], animationEffect=False)
        self.create_monster(spawnIds=[109], animationEffect=False)
        self.create_monster(spawnIds=[110], animationEffect=False)
        self.create_monster(spawnIds=[111], animationEffect=False)
        self.create_monster(spawnIds=[112], animationEffect=False)
        self.create_monster(spawnIds=[113], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class 마리엔퇴장_01(common.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 마리엔퇴장_02(self.ctx)


class 마리엔퇴장_02(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11004294, msg='$63000068_CS__63000068_MAIN__5$', duration=2000, align='right')
        self.set_effect(triggerIds=[5003], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2500):
            return 마리엔퇴장_03(self.ctx)


class 마리엔퇴장_03(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[201])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 마리엔퇴장_04(self.ctx)


class 마리엔퇴장_04(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.show_guide_summary(entityId=26300681, textId=26300681)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[705], questIds=[30000354], questStates=[2]):
            return 암전_01(self.ctx)


class 재입장시(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[705], questIds=[30000354], questStates=[2]):
            return 암전_01(self.ctx)


class 암전_01(common.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=26300681)
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 암전_02(self.ctx)


class 암전_02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8004], returnView=False)
        self.move_user_path(patrolName='MS2PatrolData_2002')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 마리엔재등장_01(self.ctx)


class 마리엔재등장_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_scene_skip(state=재등장연출완료, action='exit')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return 마리엔재등장_02(self.ctx)


class 마리엔재등장_02(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5001], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 마리엔재등장_03(self.ctx)


class 마리엔재등장_03(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[202], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2500):
            return 마리엔재등장_04(self.ctx)


class 마리엔재등장_04(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11004294, msg='$63000068_CS__63000068_MAIN__6$', duration=3000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 마리엔재등장_05(self.ctx)


class 마리엔재등장_05(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11004294, msg='$63000068_CS__63000068_MAIN__7$', duration=3000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 마리엔재등장_06(self.ctx)


class 마리엔재등장_06(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11004294, msg='$63000068_CS__63000068_MAIN__8$', duration=3000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 마리엔재등장_07(self.ctx)


class 마리엔재등장_07(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11004294, msg='$63000068_CS__63000068_MAIN__9$', duration=2000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2500):
            return 재등장연출완료(self.ctx)


class 재등장연출완료(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 퀘스트마리엔등장(self.ctx)


class 퀘스트마리엔등장(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[202])
        self.create_monster(spawnIds=[203], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[705], questIds=[30000355], questStates=[1]):
            return 퀘스트마리엔퇴장_01(self.ctx)
        if self.quest_user_detected(boxIds=[705], questIds=[30000355], questStates=[2]):
            return 퀘스트마리엔퇴장_01(self.ctx)


class 퀘스트마리엔퇴장_01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5002], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return 퀘스트마리엔퇴장_02(self.ctx)


class 퀘스트마리엔퇴장_02(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[203])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)


initial_state = 준비
