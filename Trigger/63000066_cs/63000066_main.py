""" trigger/63000066_cs/63000066_main.xml """
import trigger_api


class 준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101], auto_target=True)
        self.spawn_monster(spawn_ids=[102], auto_target=True)
        self.spawn_monster(spawn_ids=[103], auto_target=True)
        self.spawn_monster(spawn_ids=[104], auto_target=True)
        self.spawn_monster(spawn_ids=[105], auto_target=True)
        self.spawn_monster(spawn_ids=[111], auto_target=True)
        self.spawn_monster(spawn_ids=[112], auto_target=True)
        self.spawn_monster(spawn_ids=[113], auto_target=True)
        self.spawn_monster(spawn_ids=[114], auto_target=True)
        self.spawn_monster(spawn_ids=[115], auto_target=True)
        self.spawn_monster(spawn_ids=[116], auto_target=True)
        self.set_effect(trigger_ids=[5001,5002], visible=False)
        self.set_effect(trigger_ids=[5003], visible=False)
        self.set_portal(portal_id=2, visible=False, enable=False, minimap_visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[30000351], quest_states=[1]):
            return 서랍장안내(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[30000351], quest_states=[2]):
            return 사다리안내(self.ctx)
        if self.user_detected(box_ids=[701]):
            return 종료(self.ctx)


class 서랍장안내(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=26300661, text_id=26300661)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[702], quest_ids=[30000351], quest_states=[2]):
            return 사다리안내(self.ctx)


class 사다리안내(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=26300661)
        self.show_guide_summary(entity_id=26300662, text_id=26300662)
        self.set_effect(trigger_ids=[5001,5002], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[703], quest_ids=[30000351], quest_states=[2]):
            return 암전_01(self.ctx)


class 암전_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=26300662)
        self.set_effect(trigger_ids=[5001,5002], visible=False)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 암전_02(self.ctx)


class 암전_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8001], return_view=False)
        self.move_user_path(patrol_name='MS2PatrolData_2001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 마리엔등장_01(self.ctx)


class 마리엔등장_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[201], auto_target=True)
        self.add_cinematic_talk(npc_id=11004293, msg='$63000066_CS__63000066_MAIN__0$', duration=2500, align='right')
        self.set_scene_skip(state=스킵종료, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 마리엔등장_02(self.ctx)


class 마리엔등장_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=800):
            return 마리엔등장_03(self.ctx)


class 마리엔등장_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_sequence(sequence_names=['Emotion_Suprise_A'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 마리엔등장_04(self.ctx)


class 마리엔등장_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8002], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 마리엔등장_05(self.ctx)


class 마리엔등장_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004293, msg='$63000066_CS__63000066_MAIN__1$', duration=2500, align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 마리엔등장_06(self.ctx)


class 마리엔등장_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8003], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 마리엔등장_07(self.ctx)


class 마리엔등장_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004293, msg='$63000066_CS__63000066_MAIN__2$', duration=3000, align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 마리엔등장_08(self.ctx)


class 마리엔등장_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8001], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 마리엔등장_09(self.ctx)


class 마리엔등장_09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.face_emotion(spawn_id=0, emotion_name='Think_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 마리엔등장_10(self.ctx)


class 마리엔등장_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8003], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 마리엔등장_11(self.ctx)


class 마리엔등장_11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004293, msg='$63000066_CS__63000066_MAIN__3$', duration=2500, align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 마리엔퇴장_01(self.ctx)


class 마리엔퇴장_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.destroy_monster(spawn_ids=[201])
        self.set_effect(trigger_ids=[5003], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 마리엔퇴장_02(self.ctx)


class 마리엔퇴장_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.face_emotion(spawn_id=0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolation_time=0)

    def on_tick(self) -> trigger_api.Trigger:
        return 종료(self.ctx)


class 스킵종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.face_emotion(spawn_id=0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolation_time=0)
        self.destroy_monster(spawn_ids=[201])

    def on_tick(self) -> trigger_api.Trigger:
        return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.set_effect(trigger_ids=[5003], visible=False)
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)


initial_state = 준비
