""" trigger/52000143_qd/52000143_main.xml """
import trigger_api


class 준비(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.set_mesh(triggerIds=[4003,4004,4005,4006], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[701]):
            return 잠시대기(self.ctx)


class 잠시대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(pathIds=[8001], returnView=False)
        self.add_buff(boxIds=[701], skillId=70000124, level=1, isPlayer=False, isSkillSet=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 한번더대기(self.ctx)


class 한번더대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 로베와대화_01(self.ctx)


class 로베와대화_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=로베와전투_01, action='nextState')
        self.add_cinematic_talk(npcId=0, msg='$52000143_QD__52000143_MAIN__0$', duration=3000, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 로베와대화_02(self.ctx)


class 로베와대화_02(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003401, msg='$52000143_QD__52000143_MAIN__1$', duration=3500, illustId='Robe_normal', align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 로베와대화_03(self.ctx)


class 로베와대화_03(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000143_QD__52000143_MAIN__2$', duration=3000, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 로베와대화_04(self.ctx)


class 로베와대화_04(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003401, msg='$52000143_QD__52000143_MAIN__3$', duration=2500, illustId='Robe_normal', align='right')
        self.add_cinematic_talk(npcId=11003401, msg='$52000143_QD__52000143_MAIN__4$', duration=3000, illustId='Robe_normal', align='right')
        self.add_cinematic_talk(npcId=11003401, msg='$52000143_QD__52000143_MAIN__5$', duration=2500, illustId='Robe_normal', align='right')
        self.add_cinematic_talk(npcId=11003401, msg='$52000143_QD__52000143_MAIN__6$', duration=3000, illustId='Robe_normal', align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=12000):
            return 로베와대화_05(self.ctx)


class 로베와대화_05(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000143_QD__52000143_MAIN__7$', duration=3500, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 로베와대화_06(self.ctx)


class 로베와대화_06(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003401, msg='$52000143_QD__52000143_MAIN__8$', duration=1000, illustId='Robe_normal', align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 로베와대화_07(self.ctx)


class 로베와대화_07(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Bore_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 로베와전투_01(self.ctx)


class 로베와전투_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 로베와전투_02(self.ctx)


class 로베와전투_02(trigger_api.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=0)
        self.destroy_monster(spawnIds=[101])
        self.create_monster(spawnIds=[102], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 로베와전투_03(self.ctx)


class 로베와전투_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.show_guide_summary(entityId=25201431, textId=25201431)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=20000):
            return 로베와전투_04(self.ctx)


class 로베와전투_04(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.hide_guide_summary(entityId=25201431)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 로베와전투_05(self.ctx)


class 로베와전투_05(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[102])
        self.create_monster(spawnIds=[103], animationEffect=False)
        self.create_monster(spawnIds=[104], animationEffect=False)
        self.create_monster(spawnIds=[105], animationEffect=False)
        self.create_monster(spawnIds=[106], animationEffect=False)
        self.create_monster(spawnIds=[107], animationEffect=False)
        self.add_cinematic_talk(npcId=11003404, msg='$52000143_QD__52000143_MAIN__9$', duration=2500, align='center')
        self.move_user(mapId=52000143, portalId=99)
        self.select_camera_path(pathIds=[8002], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 알론등장_01(self.ctx)


class 알론등장_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 알론등장_02(self.ctx)


class 알론등장_02(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=104, patrolName='MS2PatrolData_2001')
        self.move_npc(spawnId=105, patrolName='MS2PatrolData_2002')
        self.move_npc(spawnId=106, patrolName='MS2PatrolData_2003')
        self.move_npc(spawnId=107, patrolName='MS2PatrolData_2004')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 자대화_03_3(self.ctx)


class 자대화_03_3(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8002,8003], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 자대화_04_3(self.ctx)


class 자대화_04_3(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=마무리_01, action='nextState')
        self.add_cinematic_talk(npcId=11003401, msg='$52000143_QD__52000143_MAIN__10$', duration=2500, illustId='Robe_normal', align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 자대화_05_3(self.ctx)


class 자대화_05_3(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003404, msg='$52000143_QD__52000143_MAIN__11$', duration=3000, illustId='Alon_normal', align='center')
        self.add_cinematic_talk(npcId=11003404, msg='$52000143_QD__52000143_MAIN__12$', duration=2500, illustId='Alon_normal', align='center')
        self.add_cinematic_talk(npcId=11003404, msg='$52000143_QD__52000143_MAIN__13$', duration=3000, illustId='Alon_normal', align='center')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=9000):
            return 자대화_06_3(self.ctx)


class 자대화_06_3(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003401, msg='$52000143_QD__52000143_MAIN__14$', duration=3500, illustId='Robe_normal', align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 자대화_07_3(self.ctx)


class 자대화_07_3(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003404, msg='$52000143_QD__52000143_MAIN__15$', duration=3000, illustId='Alon_normal', align='center')
        self.add_cinematic_talk(npcId=11003404, msg='$52000143_QD__52000143_MAIN__16$', duration=3000, illustId='Alon_normal', align='center')
        self.add_cinematic_talk(npcId=11003404, msg='$52000143_QD__52000143_MAIN__17$', duration=3000, illustId='Alon_normal', align='center')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return 자대화_08_3(self.ctx)


class 자대화_08_3(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003401, msg='$52000143_QD__52000143_MAIN__18$', duration=2500, illustId='Robe_normal', align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 자대화_09_3(self.ctx)


class 자대화_09_3(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000143_QD__52000143_MAIN__19$', duration=2500, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 자대화_10_3(self.ctx)


class 자대화_10_3(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003404, msg='$52000143_QD__52000143_MAIN__20$', duration=3000, illustId='Alon_normal', align='center')
        self.add_cinematic_talk(npcId=11003404, msg='$52000143_QD__52000143_MAIN__21$', duration=2500, illustId='Alon_normal', align='center')
        self.add_cinematic_talk(npcId=11003404, msg='$52000143_QD__52000143_MAIN__22$', duration=3000, illustId='Alon_normal', align='center')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=9000):
            return 자대화_10_1_3(self.ctx)


class 자대화_10_1_3(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8005], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 자대화_10_2_3(self.ctx)


class 자대화_10_2_3(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000143_QD__52000143_MAIN__23$', duration=2500, align='left')
        self.move_npc(spawnId=104, patrolName='MS2PatrolData_2006')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return 자대화_11_3(self.ctx)


class 자대화_11_3(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8004], returnView=False)
        self.move_user_path(patrolName='MS2PatrolData_2005')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 자대화_11_1_3(self.ctx)


class 자대화_11_1_3(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000143_QD__52000143_MAIN__28$', duration=3000, align='left')
        self.set_pc_emotion_sequence(sequenceNames=['Knight_Bore_A'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 자대화_12_3(self.ctx)


class 자대화_12_3(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003404, msg='$52000143_QD__52000143_MAIN__24$', duration=5500, illustId='Alon_normal', align='right')
        self.add_cinematic_talk(npcId=11003404, msg='$52000143_QD__52000143_MAIN__25$', duration=5500, illustId='Alon_normal', align='right')
        self.add_cinematic_talk(npcId=11003404, msg='$52000143_QD__52000143_MAIN__26$', duration=5000, illustId='Alon_normal', align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=17000):
            return 마무리_01(self.ctx)


class 마무리_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 마무리_02(self.ctx)


class 마무리_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$52000143_QD__52000143_MAIN__27$')
        self.remove_buff(boxId=701, skillId=70000124)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 강제이동(self.ctx)


class 강제이동(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000144, portalId=1)


initial_state = 준비
