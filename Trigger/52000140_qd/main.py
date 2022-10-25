""" trigger/52000140_qd/main.xml """
import common


class 준비(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_effect(triggerIds=[5001], visible=False)
        self.set_cinematic_ui(type=0) # 유저 이동 하게
        self.set_cinematic_ui(type=2) # UI 숨기기 초기화
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.create_monster(spawnIds=[102], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[701]):
            return 카메라연출_01(self.ctx)


class 카메라연출_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(pathIds=[8002], returnView=False)
        self.set_cinematic_ui(type=1) # 유저 이동 못 하게
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 카메라연출_02(self.ctx)


class 카메라연출_02(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 카메라연출_04(self.ctx)


class 카메라연출_04(common.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_2001')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return 카메라연출_05(self.ctx)


class 카메라연출_05(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 삼자대화_01(self.ctx)

    def on_exit(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2002')


class 삼자대화_01(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=투르카소멸_01, action='nextState')
        self.add_cinematic_talk(npcId=0, msg='$52000140_QD__MAIN__0$', duration=2500)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 삼자대화_02(self.ctx)


class 삼자대화_02(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003328, msg='$52000140_QD__MAIN__1$', duration=3000, align='center')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 삼자대화_03(self.ctx)


class 삼자대화_03(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003329, msg='$52000140_QD__MAIN__2$', duration=2500, align='right')
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2003')
        self.add_cinematic_talk(npcId=11003329, msg='$52000140_QD__MAIN__3$', duration=2500, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5300):
            return 투르카소멸_01(self.ctx)


class 투르카소멸_01(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.set_effect(triggerIds=[5001], visible=True)
        self.destroy_monster(spawnIds=[102])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 투르카소멸_02(self.ctx)


class 투르카소멸_02(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5001], visible=False)
        self.reset_camera(interpolationTime=2)
        self.set_cinematic_ui(type=2) # UI 숨기기 초기화
        self.set_cinematic_ui(type=0) # 유저 이동 가능하게
        self.destroy_monster(spawnIds=[101])
        self.create_monster(spawnIds=[105], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 어둠의졸개_01(self.ctx)


class 어둠의졸개_01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[103,104], animationEffect=True)
        self.show_guide_summary(entityId=25201401, textId=25201401)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[103,104]):
            return 졸개퇴치완료_01(self.ctx)


class 졸개퇴치완료_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.hide_guide_summary(entityId=25201401)
        self.set_cinematic_ui(type=1) # 유저 이동 못하게
        self.set_cinematic_ui(type=3) # 상하 레터박스

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 졸개퇴치완료_02(self.ctx)


class 졸개퇴치완료_02(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000140, portalId=99)
        self.destroy_monster(spawnIds=[105])
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2002')
        self.select_camera_path(pathIds=[8003], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 졸개퇴치완료_03(self.ctx)


class 졸개퇴치완료_03(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 알론과대화_01(self.ctx)


class 알론과대화_01(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=투르카와전투_01, action='nextState')
        self.add_cinematic_talk(npcId=0, msg='$52000140_QD__MAIN__4$', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 알론과대화_02(self.ctx)


class 알론과대화_02(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003328, msg='$52000140_QD__MAIN__5$', duration=3000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 알론과대화_03(self.ctx)


class 알론과대화_03(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000140_QD__MAIN__6$', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 알론과대화_04(self.ctx)


class 알론과대화_04(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003328, msg='$52000140_QD__MAIN__7$', duration=2500, align='right')
        self.add_cinematic_talk(npcId=11003328, msg='$52000140_QD__MAIN__8$', duration=2500, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5300):
            return 알론과대화_05(self.ctx)


class 알론과대화_05(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000140_QD__MAIN__9$', duration=2500)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 알론과대화_06(self.ctx)

    def on_exit(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2003')


class 알론과대화_06(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003328, msg='$52000140_QD__MAIN__10$', duration=2000, align='right')
        self.move_user_path(patrolName='MS2PatrolData_2008')
        self.create_monster(spawnIds=[102], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2300):
            return 알론과대화_07(self.ctx)


class 알론과대화_07(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8003,8002], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2200):
            return 차삼자대화_01_2(self.ctx)


class 차삼자대화_01_2(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003329, msg='$52000140_QD__MAIN__11$', duration=3000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 차삼자대화_02_2(self.ctx)


class 차삼자대화_02_2(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000140_QD__MAIN__12$', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 차삼자대화_03_2(self.ctx)


class 차삼자대화_03_2(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003329, msg='$52000140_QD__MAIN__13$', duration=2500, align='right')
        self.add_cinematic_talk(npcId=11003329, msg='$52000140_QD__MAIN__14$', duration=2500, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5200):
            return 차삼자대화_04_2(self.ctx)


class 차삼자대화_04_2(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003328, msg='$52000140_QD__MAIN__15$', duration=2500, align='center')
        self.add_cinematic_talk(npcId=11003328, msg='$52000140_QD__MAIN__16$', duration=2500, align='center')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5200):
            return 차삼자대화_05_2(self.ctx)


class 차삼자대화_05_2(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003329, msg='$52000140_QD__MAIN__17$', duration=2500, align='right')
        self.add_cinematic_talk(npcId=11003329, msg='$52000140_QD__MAIN__18$', duration=2500, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5300):
            return 차삼자대화_06_2(self.ctx)


class 차삼자대화_06_2(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003328, msg='$52000140_QD__MAIN__19$', duration=2500, align='center')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 차삼자대화_07_2(self.ctx)


class 차삼자대화_07_2(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003329, msg='$52000140_QD__MAIN__20$', duration=2500, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 차삼자대화_08_2(self.ctx)


class 차삼자대화_08_2(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003328, msg='$52000140_QD__MAIN__21$', duration=2000, align='center')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2300):
            return 투르카와전투_01(self.ctx)


class 투르카와전투_01(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.reset_camera(interpolationTime=2)
        self.set_cinematic_ui(type=0) # 유저 이동 가능하게
        self.set_cinematic_ui(type=2) # UI 숨기기 초기화
        self.destroy_monster(spawnIds=[102])
        self.create_monster(spawnIds=[106], animationEffect=True)
        self.destroy_monster(spawnIds=[101])
        self.create_monster(spawnIds=[105], animationEffect=True)
        self.show_guide_summary(entityId=25201402, textId=25201402)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=15000):
            return 투르카와전투_02(self.ctx)


class 투르카와전투_02(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.hide_guide_summary(entityId=25201402)
        self.move_user(mapId=52000140, portalId=99)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 투르카와전투_03(self.ctx)


class 투르카와전투_03(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(pathIds=[8002], returnView=False)
        self.destroy_monster(spawnIds=[106])
        self.create_monster(spawnIds=[102], animationEffect=False)
        self.destroy_monster(spawnIds=[105])
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.move_user_path(patrolName='MS2PatrolData_2008')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 차삼자대화_01_3(self.ctx)


class 차삼자대화_01_3(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_cinematic_talk(npcId=11003329, msg='$52000140_QD__MAIN__22$', duration=2500, align='right')
        self.add_cinematic_talk(npcId=11003329, msg='$52000140_QD__MAIN__23$', duration=2500, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5300):
            return 차삼자대화_02_3(self.ctx)


class 차삼자대화_02_3(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000140_QD__MAIN__24$', duration=2000)
        self.move_user_path(patrolName='MS2PatrolData_2005')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2200):
            return 차삼자대화_03_3(self.ctx)


class 차삼자대화_03_3(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8006], returnView=False)
        self.add_cinematic_talk(npcId=11003328, msg='$52000140_QD__MAIN__25$', duration=2000, align='center')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2200):
            return 투르카퇴장_01(self.ctx)


class 투르카퇴장_01(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8007], returnView=False)
        self.set_effect(triggerIds=[5001], visible=True)
        self.destroy_monster(spawnIds=[102])
        # <action name="SetPcEmotionSequence" arg1="Priest_Sanctuary_A" />
        self.set_pc_emotion_sequence(sequenceNames=['Priest_Skill_Divine_Protection_A'])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=700):
            return 투르카퇴장_02(self.ctx)


class 투르카퇴장_02(common.Trigger):
    def on_enter(self):
        self.set_pc_emotion_loop(sequenceName='Down_Idle_A', duration=10000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return PC의부상_01(self.ctx)


class PC의부상_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_pc_emotion_loop(sequenceName='Down_Idle_A', duration=10000)
        self.set_effect(triggerIds=[5001], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return PC의부상_02(self.ctx)


class PC의부상_02(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(pathIds=[8004,8005], returnView=False)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2007')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return PC의부상_03(self.ctx)


class PC의부상_03(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 강제이동(self.ctx)


class 강제이동(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000141, portalId=1)


initial_state = 준비
