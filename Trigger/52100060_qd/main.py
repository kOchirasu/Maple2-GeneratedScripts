""" trigger/52100060_qd/main.xml """
import trigger_api


class QuestDungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_local_camera(cameraId=8100, enable=True) # LocalTargetCamera

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[1000], questIds=[50100320], questStates=[3]): # >
            return teleport02000487(self.ctx)
        if self.quest_user_detected(boxIds=[1000], questIds=[50100320], questStates=[2]):
            return Ready(self.ctx)
        if self.quest_user_detected(boxIds=[1000], questIds=[50100320], questStates=[1]):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=1, enable=True)
        self.visible_my_pc(isVisible=False) # 유저 투명 처리
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_effect(triggerIds=[600], visible=False)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[1000]):
            return narration01(self.ctx)


class narration01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='$52100060_QD__MAIN__12$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Camera_Move_01(self.ctx)


class Camera_Move_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_effect(triggerIds=[600], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return NPC_Show(self.ctx)


class NPC_Show(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip(state=teleport02000487)
        self.create_monster(spawnIds=[1,2], animationEffect=False)
        self.set_npc_rotation(spawnId=1, rotation=180)
        self.set_npc_rotation(spawnId=2, rotation=180)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return NPC_Change_1(self.ctx)


class NPC_Change_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[1,2], arg2=False)
        self.create_monster(spawnIds=[101,102], animationEffect=False)
        self.select_camera_path(pathIds=[2,3], returnView=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Talk_1(self.ctx)


class Talk_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[600], visible=False)
        self.select_camera(triggerId=4, enable=True)
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Attack_01_A')
        self.add_cinematic_talk(npcId=11004022, illustId='11004022', msg='$52100060_QD__MAIN__0$', duration=2000, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Talk_2(self.ctx)


class Talk_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=5, enable=True)
        self.set_npc_emotion_sequence(spawnId=102, sequenceName='Bore_B')
        self.add_cinematic_talk(npcId=11001813, illustId='11001813', msg='$52100060_QD__MAIN__1$', duration=3000, align='Right')
        self.add_cinematic_talk(npcId=11001813, illustId='11001813', msg='$52100060_QD__MAIN__2$', duration=3000, align='Right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return Talk_3(self.ctx)


class Talk_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[10,11,12], returnView=False)
        self.set_npc_emotion_sequence(spawnId=102, sequenceName='Bore_A')
        self.add_cinematic_talk(npcId=11001813, illustId='11001813', msg='$52100060_QD__MAIN__3$', duration=3000, align='Right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return Talk_4(self.ctx)


class Talk_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=4, enable=True)
        self.add_cinematic_talk(npcId=11004022, illustId='11004022', msg='$52100060_QD__MAIN__4$', duration=3000, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Talk_5(self.ctx)


class Talk_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[6,7], returnView=False)
        self.add_cinematic_talk(npcId=11001813, illustId='11001813', msg='$52100060_QD__MAIN__5$', duration=3000, align='Right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Talk_6(self.ctx)


class Talk_6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[77,78], returnView=False)
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Bore_B')
        self.add_cinematic_talk(npcId=11004022, illustId='11004022', msg='$52100060_QD__MAIN__6$', duration=2000, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Talk_7(self.ctx)


class Talk_7(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11004022, illustId='11004022', msg='$52100060_QD__MAIN__7$', duration=3000, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Talk_8(self.ctx)


class Talk_8(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=44, enable=True)
        self.destroy_monster(spawnIds=[101])
        self.create_monster(spawnIds=[200])
        self.add_cinematic_talk(npcId=11001813, illustId='11001813', msg='$52100060_QD__MAIN__8$', duration=4000, align='Right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return Talk_9(self.ctx)


class Talk_9(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[13,14,15], returnView=False)
        self.set_effect(triggerIds=[600], visible=False)
        self.add_cinematic_talk(npcId=11001813, illustId='11001813', msg='$52100060_QD__MAIN__9$', duration=3000, align='Right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return Talk_10(self.ctx)


class Talk_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawnId=200, sequenceName='Bore_A')
        self.add_cinematic_talk(npcId=11001593, illustId='11001593', msg='$52100060_QD__MAIN__10$', duration=4000, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return Talk_11(self.ctx)


class Talk_11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=16, enable=True)
        self.set_npc_emotion_sequence(spawnId=102, sequenceName='Bore_B')
        self.add_cinematic_talk(npcId=11001813, illustId='11001813', msg='$52100060_QD__MAIN__11$', duration=2000, align='Right')
        self.select_camera(triggerId=8, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return NPC_Attack_Move(self.ctx)


class NPC_Attack_Move(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_time_scale(enable=True, startScale=0.5, endScale=0.3, duration=3, interpolator=1)
        self.select_camera_path(pathIds=[8,9], returnView=False)
        self.move_npc(spawnId=200, patrolName='MS2PatrolData2')
        self.move_npc(spawnId=102, patrolName='MS2PatrolData3')
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return teleport02000487(self.ctx)


class teleport02000487(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Missing State: State
        self.set_skip()
        self.destroy_monster(spawnIds=[-1])
        self.visible_my_pc(isVisible=True)
        # 프론티어 재단 저택 맵 3번 회의실 앞 포탈
        self.move_user(mapId=2000487, portalId=3)


initial_state = QuestDungeonStart
