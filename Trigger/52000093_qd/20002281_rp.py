""" trigger/52000093_qd/20002281_rp.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9100], questIds=[50100560], questStates=[3]):
            return 연출시작(self.ctx)
        if self.quest_user_detected(boxIds=[9100], questIds=[20002281], questStates=[3]):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3003,3004], visible=False)
        self.reset_camera(interpolationTime=0)
        self.set_local_camera(cameraId=302, enable=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=300, enable=True)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.spawn_npc_range(rangeIds=[1101,1102,1103,1104,1105,1106], isAutoTargeting=False)
        self.spawn_npc_range(rangeIds=[2101,2102,2103,2104,2105,2106,2107,2108,2109], isAutoTargeting=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 타이틀(self.ctx)


class 타이틀(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000093, portalId=99)
        self.add_buff(boxIds=[9100], skillId=99910190, level=1, isPlayer=False, isSkillSet=False)
        self.set_cinematic_ui(type=9, script='$52000093_QD__20002281_RP__0$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 오스칼대사01(self.ctx)


class 오스칼대사01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_conversation(type=2, spawnId=11000015, script='$52000093_QD__20002281_RP__1$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return RP시작(self.ctx)


class RP시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3003,3004], visible=True) # 뒤로 못나가게 한다
        self.select_camera(triggerId=300, enable=False)
        self.set_local_camera(cameraId=302, enable=True)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=25200931, textId=25200931, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2101,2102,2103,2104,2105,2106,2107,2108,2109]):
            return 데보라크소환(self.ctx)
        if self.wait_tick(waitTick=40000):
            return 데보라크소환(self.ctx)


class 데보라크소환(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=301, enable=True)
        self.create_monster(spawnIds=[2199], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return 데보라크사망대기(self.ctx)


class 데보라크사망대기(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=25200932, textId=25200932, duration=4000)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_local_camera(cameraId=302, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2199]):
            return 미션완료(self.ctx)


class 미션완료(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[2101,2102,2103,2104,2105,2106,2107,2108,2109])
        self.set_event_ui(type=7, arg2='$52000093_QD__20002281_RP__2$', arg3='3000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            self.set_local_camera(cameraId=302, enable=False)
            self.reset_camera(interpolationTime=0)
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
        self.create_monster(spawnIds=[1100], animationEffect=True)
        self.remove_buff(boxId=9100, skillId=99910190)
        self.reset_camera(interpolationTime=0)
        self.set_achievement(triggerId=9100, type='trigger', achieve='OscalRpClear')
        self.move_user(mapId=52000093, portalId=99)


initial_state = 대기
