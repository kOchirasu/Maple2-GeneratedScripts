""" trigger/52000147_qd/52000147_main.xml """
import common


class 준비(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101], animationEffect=True)
        self.create_monster(spawnIds=[102], animationEffect=True)
        self.set_effect(triggerIds=[5001], visible=False)
        self.set_effect(triggerIds=[5003], visible=False)
        self.set_effect(triggerIds=[5004], visible=False)
        self.set_effect(triggerIds=[5005], visible=False)
        self.set_mesh(triggerIds=[4001,4002], visible=True)
        self.set_mesh_animation(triggerIds=[4001,4002], visible=True, arg3=0, arg4=0)
        self.set_mesh(triggerIds=[4003,4004,4005,4006], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[701]):
            return 잠시대기(self.ctx)


class 잠시대기(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 뚜벅뚜벅_01(self.ctx)


class 뚜벅뚜벅_01(common.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_2001')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return 뚜벅뚜벅_02(self.ctx)


class 뚜벅뚜벅_02(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000147_QD__52000147_MAIN__0$', duration=2500, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6500):
            return 목격_01(self.ctx)


class 목격_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 목격_02(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 목격_02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8001], returnView=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 목격_03(self.ctx)


class 목격_03(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 목격_04(self.ctx)


class 목격_04(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8001,8002], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 목격_05(self.ctx)


class 목격_05(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Bore_A')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1200):
            return 목격_06(self.ctx)


class 목격_06(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5001], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 목격_07(self.ctx)


class 목격_07(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[4001,4002], visible=False)
        self.set_mesh_animation(triggerIds=[4001,4002], visible=False, arg3=0, arg4=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2500):
            return 목격_08(self.ctx)


class 목격_08(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=삼자대화_01)
        self.add_cinematic_talk(npcId=11003382, msg='$52000147_QD__52000147_MAIN__1$', duration=4000, illustId='DarkLord_normal', align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 삼자대화_01(self.ctx)


class 삼자대화_01(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.remove_cinematic_talk()
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return 삼자대화_02(self.ctx)


class 삼자대화_02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8001], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 삼자대화_03(self.ctx)


class 삼자대화_03(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return 삼자대화_04(self.ctx)


class 삼자대화_04(common.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_2003')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 삼자대화_05(self.ctx)


class 삼자대화_05(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=하스터와전투_01, action='nextState')
        self.add_cinematic_talk(npcId=0, msg='$52000147_QD__52000147_MAIN__2$', duration=3500, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 삼자대화_06(self.ctx)


class 삼자대화_06(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_2002')
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2004')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 삼자대화_07(self.ctx)


class 삼자대화_07(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8004], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 삼자대화_08(self.ctx)


class 삼자대화_08(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003189, msg='$52000147_QD__52000147_MAIN__3$', duration=3000, align='left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 삼자대화_09(self.ctx)


class 삼자대화_09(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8003], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 삼자대화_10(self.ctx)


class 삼자대화_10(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003382, msg='$52000147_QD__52000147_MAIN__4$', duration=3000, illustId='DarkLord_normal', align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 삼자대화_11(self.ctx)


class 삼자대화_11(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003189, msg='$52000147_QD__52000147_MAIN__5$', duration=2500, illustId='Hastur_normal', align='left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 삼자대화_12(self.ctx)


class 삼자대화_12(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003382, msg='$52000147_QD__52000147_MAIN__6$', duration=4000, illustId='DarkLord_normal', align='right')
        self.add_cinematic_talk(npcId=11003382, msg='$52000147_QD__52000147_MAIN__7$', duration=3000, illustId='DarkLord_normal', align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8000):
            return 삼자대화_13(self.ctx)


class 삼자대화_13(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000147_QD__52000147_MAIN__8$', duration=4000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4500):
            return 삼자대화_14(self.ctx)


class 삼자대화_14(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003189, msg='$52000147_QD__52000147_MAIN__9$', duration=3000, illustId='Hastur_normal', align='left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 삼자대화_15(self.ctx)


class 삼자대화_15(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003382, msg='$52000147_QD__52000147_MAIN__10$', duration=3000, illustId='DarkLord_normal', align='right')
        self.add_cinematic_talk(npcId=11003382, msg='$52000147_QD__52000147_MAIN__11$', duration=3000, illustId='DarkLord_normal', align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return 삼자대화_16(self.ctx)


class 삼자대화_16(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003189, msg='$52000147_QD__52000147_MAIN__12$', duration=3000, illustId='Hastur_normal', align='left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 삼자대화_17(self.ctx)


class 삼자대화_17(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003382, msg='$52000147_QD__52000147_MAIN__13$', duration=3000, illustId='DarkLord_normal', align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 삼자대화_18(self.ctx)


class 삼자대화_18(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000147_QD__52000147_MAIN__14$', duration=3000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 삼자대화_19(self.ctx)


class 삼자대화_19(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8004], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 삼자대화_20(self.ctx)


class 삼자대화_20(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003189, msg='$52000147_QD__52000147_MAIN__15$', duration=2500, align='left')
        self.set_npc_emotion_loop(spawnId=102, sequenceName='Attack_Idle_A', duration=4000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 하스터와전투_01(self.ctx)


class 하스터와전투_01(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.remove_cinematic_talk()
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 하스터와전투_02(self.ctx)


class 하스터와전투_02(common.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=0)
        self.destroy_monster(spawnIds=[102])
        self.create_monster(spawnIds=[103], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 하스터와전투_03(self.ctx)


class 하스터와전투_03(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.show_guide_summary(entityId=25201471, textId=25201471)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=15000):
            return 하스터와전투_04(self.ctx)


class 하스터와전투_04(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.hide_guide_summary(entityId=25201471)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return 하스터와전투_05(self.ctx)


class 하스터와전투_05(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[103])
        self.create_monster(spawnIds=[104], animationEffect=True)
        self.add_cinematic_talk(npcId=11003189, msg='$52000147_QD__52000147_MAIN__16$', duration=2500, align='left')
        self.move_user(mapId=52000147, portalId=99)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return 하스터와전투_06(self.ctx)


class 하스터와전투_06(common.Trigger):
    def on_enter(self):
        self.set_pc_emotion_loop(sequenceName='Down_Idle_B', duration=60000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 하스터와전투_07(self.ctx)


class 하스터와전투_07(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 전투후대화_01(self.ctx)


class 전투후대화_01(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=전투후대화_02)
        self.add_cinematic_talk(npcId=11003382, msg='$52000147_QD__52000147_MAIN__17$', duration=3000, illustId='DarkLord_normal', align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 전투후대화_02(self.ctx)


class 전투후대화_02(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.remove_cinematic_talk()
        self.move_npc(spawnId=104, patrolName='MS2PatrolData_2005')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return 전투후대화_03(self.ctx)


class 전투후대화_03(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=전투후대화_03_01)
        self.add_cinematic_talk(npcId=11003189, msg='$52000147_QD__52000147_MAIN__18$', duration=3000, illustId='Hastur_normal', align='left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 전투후대화_04(self.ctx)


class 전투후대화_03_01(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 전투후대화_04(self.ctx)


class 전투후대화_04(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=전투후대화_05)
        self.add_cinematic_talk(npcId=11003382, msg='$52000147_QD__52000147_MAIN__19$', duration=3000, illustId='DarkLord_normal', align='right')
        self.add_cinematic_talk(npcId=11003382, msg='$52000147_QD__52000147_MAIN__20$', duration=2500, illustId='DarkLord_normal', align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return 전투후대화_05(self.ctx)


class 전투후대화_05(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.remove_cinematic_talk()
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Bore_A')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 전투후대화_06(self.ctx)


class 전투후대화_06(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5003], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 전투후대화_07(self.ctx)


class 전투후대화_07(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2007')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2500):
            return 전투후대화_08(self.ctx)


class 전투후대화_08(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 전투후대화_09(self.ctx)


class 전투후대화_09(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=104, patrolName='MS2PatrolData_2006')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 전투후대화_10(self.ctx)


class 전투후대화_10(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5005], visible=True)
        self.set_effect(triggerIds=[5004], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 전투후대화_11(self.ctx)


class 전투후대화_11(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=전투후대화_12)
        self.add_cinematic_talk(npcId=11003189, msg='$52000147_QD__52000147_MAIN__21$', duration=3000, illustId='Hastur_normal', align='left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 전투후대화_12(self.ctx)


class 전투후대화_12(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.remove_cinematic_talk()
        self.move_npc(spawnId=104, patrolName='MS2PatrolData_2007')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 전투후대화_13(self.ctx)


class 전투후대화_13(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[104])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 전투후대화_14(self.ctx)


class 전투후대화_14(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return 전투후대화_15(self.ctx)


class 전투후대화_15(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000147_QD__52000147_MAIN__22$', duration=3000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 강제이동(self.ctx)


class 강제이동(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000148, portalId=1)


initial_state = 준비
