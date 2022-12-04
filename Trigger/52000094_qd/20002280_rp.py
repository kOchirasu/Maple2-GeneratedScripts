""" trigger/52000094_qd/20002280_rp.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9100], questIds=[50100550], questStates=[3]):
            return 연출시작(self.ctx)
        if self.quest_user_detected(boxIds=[9100], questIds=[20002280], questStates=[3]):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3003,3004], visible=False)
        self.set_local_camera(cameraId=302, enable=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=300, enable=True)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.spawn_npc_range(rangeIds=[1001,1002,1003,1004,1005], isAutoTargeting=False)
        self.spawn_npc_range(rangeIds=[2101,2102,2103,2104,2105,2106,2107], isAutoTargeting=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 타이틀(self.ctx)


class 타이틀(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000094, portalId=99)
        self.add_buff(boxIds=[9100], skillId=99910170, level=1, isPlayer=False, isSkillSet=False)
        self.set_cinematic_ui(type=9, script='$52000094_QD__20002280_RP__0$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 블랙아이대사01(self.ctx)


class 블랙아이대사01(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3003,3004], visible=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_conversation(type=2, spawnId=11000006, script='$52000094_QD__20002280_RP__1$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return RP시작(self.ctx)


class RP시작(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=300, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=25200941, textId=25200941, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2101,2102,2103,2104,2105,2106,2107]):
            return 데블린소환(self.ctx)
        if self.wait_tick(waitTick=40000):
            return 데블린소환(self.ctx)


class 데블린소환(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=301, enable=True)
        self.create_monster(spawnIds=[2199], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return 데블린사망대기(self.ctx)


class 데블린사망대기(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=25200942, textId=25200942, duration=4000)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=300, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2199]):
            return 미션완료(self.ctx)


class 미션완료(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[2101,2102,2103,2104,2105,2106,2107])
        self.set_event_ui(type=7, arg2='$52000094_QD__20002280_RP__2$', arg3='3000', arg4='0')
        self.set_local_camera(cameraId=302, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            self.set_local_camera(cameraId=302, enable=False)
            return 미션완료02(self.ctx)


class 미션완료02(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.create_monster(spawnIds=[2200], animationEffect=True)
        self.create_monster(spawnIds=[2201], animationEffect=True)
        self.remove_buff(boxId=9100, skillId=99910170)
        self.reset_camera(interpolationTime=0)
        self.set_achievement(triggerId=9100, type='trigger', achieve='BlackEyeRpClear')
        self.move_user(mapId=52000094, portalId=99)


initial_state = 대기
