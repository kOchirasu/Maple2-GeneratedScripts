""" trigger/52000192_qd/52000192.xml """
import common


class wait_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=101, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_effect(triggerIds=[6001], visible=False)
        self.set_effect(triggerIds=[6002], visible=False)
        self.set_effect(triggerIds=[6003], visible=False)
        self.set_effect(triggerIds=[6004], visible=False)
        self.set_interact_object(triggerIds=[10001453], state=2)
        self.set_interact_object(triggerIds=[10001454], state=2)
        self.set_interact_object(triggerIds=[10001455], state=2)
        self.set_interact_object(triggerIds=[10001456], state=2)
        self.set_portal(portalId=5003, visible=False, enable=False)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[10003423], questStates=[1]):
            return wait_01_02(self.ctx)
        if not self.quest_user_detected(boxIds=[2001], questIds=[10003423], questStates=[1]):
            return 이동(self.ctx)


class wait_01_02(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return wait_01_03(self.ctx)


class wait_01_03(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.move_user(mapId=52000192, portalId=5001)
        self.select_camera_path(pathIds=[4001], returnView=False)
        self.create_monster(spawnIds=[101]) # 바론
        self.create_monster(spawnIds=[102]) # 여제

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 불난통로_01(self.ctx)


class 불난통로_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_scene_skip(state=Skip_1, action='nextState')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 불난통로_02(self.ctx)


class 불난통로_02(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npcId=11004785, msg='$52000192_QD__52000192__0$', align='left', illustId='Ereb_surprise', duration=4000)
        self.select_camera_path(pathIds=[4002,4003], returnView=False)
        self.set_pc_emotion_loop(sequenceName='Attack_Idle_A', duration=5000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 불난통로_03(self.ctx)


class 불난통로_03(common.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=0)
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npcId=0, msg='$52000192_QD__52000192__1$', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 불난통로_04(self.ctx)


class 불난통로_04(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000192_QD__52000192__2$', duration=5000)
        self.add_cinematic_talk(npcId=11004787, msg='$52000192_QD__52000192__3$', align='left', illustId='Baron_normal', duration=4000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=9000):
            return 불끄기준비(self.ctx)


class 불끄기준비(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 불끄기준비_02(self.ctx)


class Skip_1(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.reset_camera(interpolationTime=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 불끄기준비_02(self.ctx)


class 불끄기준비_02(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101])
        self.destroy_monster(spawnIds=[102])
        self.create_monster(spawnIds=[103]) # 바론
        self.create_monster(spawnIds=[104]) # 여제
        self.set_effect(triggerIds=[6001], visible=True) # 여제 지킴
        self.set_interact_object(triggerIds=[10001453], state=1)
        self.move_user(mapId=52000192, portalId=5002)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 불꺼라불꺼(self.ctx)


class 불꺼라불꺼(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.side_npc_talk(type='talk', npcId=11004787, illust='Baron_normal', script='$52000192_QD__52000192__4$', duration=3000)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001453], stateValue=0):
            return 불꺼라불꺼_02(self.ctx)


class 불꺼라불꺼_02(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.add_balloon_talk(spawnId=104, msg='$52000192_QD__52000192__5$', duration=4000)
        self.set_effect(triggerIds=[6021], visible=False) # 불끄기
        self.set_effect(triggerIds=[6005], visible=True)
        self.set_effect(triggerIds=[6006], visible=True)
        self.set_effect(triggerIds=[6007], visible=True)
        self.set_effect(triggerIds=[6008], visible=True)
        self.create_monster(spawnIds=[201])
        self.create_monster(spawnIds=[202])
        self.create_monster(spawnIds=[203])
        self.create_monster(spawnIds=[204])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 불꺼라불꺼_02_02(self.ctx)


class 불꺼라불꺼_02_02(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npcId=11004787, msg='$52000192_QD__52000192__6$', illust='Baron_normal', align='left', duration=4000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 불꺼라불꺼_02_01(self.ctx)


class 불꺼라불꺼_02_01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[201,202,203,204]):
            return 불꺼라불꺼_03(self.ctx)


class 불꺼라불꺼_03(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=104, msg='$52000192_QD__52000192__7$', duration=4000)
        self.set_effect(triggerIds=[6001], visible=False)
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_3001')
        self.move_npc(spawnId=104, patrolName='MS2PatrolData_3002')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 불꺼라불꺼_04(self.ctx)


class 불꺼라불꺼_04(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6002], visible=True) # 여제 지킴
        self.set_interact_object(triggerIds=[10001454], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001454], stateValue=0):
            return 불꺼라불꺼_05(self.ctx)


class 불꺼라불꺼_05(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=104, msg='$52000192_QD__52000192__8$', duration=4000)
        self.set_effect(triggerIds=[6022], visible=False) # 불끄기
        self.set_effect(triggerIds=[6009], visible=True)
        self.set_effect(triggerIds=[6010], visible=True)
        self.set_effect(triggerIds=[6011], visible=True)
        self.set_effect(triggerIds=[6012], visible=True)
        self.create_monster(spawnIds=[205])
        self.create_monster(spawnIds=[206])
        self.create_monster(spawnIds=[207])
        self.create_monster(spawnIds=[208])

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[205,206,207,208]):
            return 불꺼라불꺼_06(self.ctx)


class 불꺼라불꺼_06(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=104, msg='$52000192_QD__52000192__9$', duration=4000)
        self.set_effect(triggerIds=[6002], visible=False)
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_3003')
        self.move_npc(spawnId=104, patrolName='MS2PatrolData_3004')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return 불꺼라불꺼_07(self.ctx)


class 불꺼라불꺼_07(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6003], visible=True) # 여제 지킴
        self.set_interact_object(triggerIds=[10001455], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001455], stateValue=0):
            return 불꺼라불꺼_08(self.ctx)


class 불꺼라불꺼_08(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=104, msg='$52000192_QD__52000192__10$', duration=4000)
        self.set_effect(triggerIds=[6023], visible=False) # 불끄기
        self.set_effect(triggerIds=[6013], visible=True)
        self.set_effect(triggerIds=[6014], visible=True)
        self.set_effect(triggerIds=[6015], visible=True)
        self.set_effect(triggerIds=[6016], visible=True)
        self.create_monster(spawnIds=[209])
        self.create_monster(spawnIds=[210])
        self.create_monster(spawnIds=[211])
        self.create_monster(spawnIds=[212])

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[209,210,211,212]):
            return 불꺼라불꺼_09(self.ctx)


class 불꺼라불꺼_09(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6003], visible=False)
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_3005')
        self.move_npc(spawnId=104, patrolName='MS2PatrolData_3006')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return 불꺼라불꺼_10(self.ctx)


class 불꺼라불꺼_10(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6004], visible=True) # 여제 지킴
        self.set_interact_object(triggerIds=[10001456], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001456], stateValue=0):
            return 불꺼라불꺼_11(self.ctx)


class 불꺼라불꺼_11(common.Trigger):
    def on_enter(self):
        self.side_npc_talk(type='talk', npcId=11004787, illust='Baron_normal', script='$52000192_QD__52000192__11$', duration=3000)
        self.set_effect(triggerIds=[6024], visible=False) # 불끄기
        self.set_effect(triggerIds=[6017], visible=True)
        self.set_effect(triggerIds=[6018], visible=True)
        self.set_effect(triggerIds=[6019], visible=True)
        self.set_effect(triggerIds=[6020], visible=True)
        self.create_monster(spawnIds=[213])
        self.create_monster(spawnIds=[214])
        self.create_monster(spawnIds=[215])
        self.create_monster(spawnIds=[216])

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[213,214,215,216]):
            return 불꺼라불꺼_12(self.ctx)


class 불꺼라불꺼_12(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=104, msg='$52000192_QD__52000192__12$', duration=3000)
        self.set_effect(triggerIds=[6004], visible=False)
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_3007')
        self.move_npc(spawnId=104, patrolName='MS2PatrolData_3008')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return 다왔다(self.ctx)


class 다왔다(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=101, enable=True, path='BG/Common/Eff_Com_Vibrate.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_pc_emotion_loop(sequenceName='Attack_Idle_A', duration=6000)
        self.add_cinematic_talk(npcId=0, msg='$52000192_QD__52000192__13$', duration=3000)
        self.add_cinematic_talk(npcId=11004785, msg='$52000192_QD__52000192__14$', illustId='Ereb_surprise', duration=4000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return 밖으로(self.ctx)


class 밖으로(common.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=2001, achieve='EscapePrisonTower')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_portal(portalId=5003, visible=True, enable=True)


class 이동(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=2000119, portalId=20)


initial_state = wait_01
