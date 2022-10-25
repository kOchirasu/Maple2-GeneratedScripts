""" trigger/52020019_qd/main.xml """
import common


class Idle(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_white.xml')
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_effect(triggerIds=[5001], visible=False)
        self.set_effect(triggerIds=[5002], visible=False)
        self.set_sound(triggerId=7001, enable=False)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[60200010], questStates=[1]):
            return Ready(self.ctx)


class Ready(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.create_monster(spawnIds=[101], animationEffect=True) # 이오네
        self.create_monster(spawnIds=[102], animationEffect=True) # 미카엘
        self.move_user(mapId=52020019, portalId=6001)
        self.select_camera_path(pathIds=[4001], returnView=False)
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Camera_Work_01(self.ctx)


class Camera_Work_01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(pathIds=[4002,4003], returnView=False)
        self.set_scene_skip(action='nextState')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ShowCaption(self.ctx)


class ShowCaption(common.Trigger):
    def on_enter(self):
        self.show_caption(type='VerticalCaption', title='$map:52020019$', desc='$npcName:11003614$의 두 번째 시험장.', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=2000, scale=1.5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return Camera_Work_02(self.ctx)


class Camera_Work_02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4004], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return EventScene_01(self.ctx)


class EventScene_01(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003614, msg='자, 시작하세요.', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return EventScene_02(self.ctx)


class EventScene_02(common.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_3001')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return EventScene_03(self.ctx)


class EventScene_03(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_3002')
        self.add_cinematic_talk(npcId=11003598, msg='오호.... 제법 기합을 넣을 줄 아시는군요.', duration=2500, illustId='Michael_normal', align='Right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return EventScene_04(self.ctx)


class EventScene_04(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=102, sequenceName='Talk_A')
        self.add_cinematic_talk(npcId=11003598, msg='그럼 시작하기전에....', duration=2500, illustId='Michael_normal', align='Right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return EventScene_05(self.ctx)


class EventScene_05(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=102, sequenceName='Talk_A')
        self.add_cinematic_talk(npcId=11003598, msg='정식으로 제 소개를 하죠.', duration=2500, illustId='Michael_normal', align='Right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return EventScene_06(self.ctx)


class EventScene_06(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_cinematic_talk(npcId=11003598, msg='제 이름은 $npcName:11003598$.', duration=2500, illustId='Michael_normal', align='Center')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return EventScene_07(self.ctx)


class EventScene_07(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003598, msg='크리티아스 제 3기사. 몽환의 $npcName:11003598$입니다.', duration=3000, illustId='Michael_normal', align='Center')
        self.show_caption(type='NameCaption', title='$npcName:11003598$', desc='몽환의 기사', align='centerLeft', offsetRateX=0.05, offsetRateY=0.15, duration=3000, scale=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return EventScene_08(self.ctx)


class EventScene_08(common.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=0)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_white.xml')
        self.set_effect(triggerIds=[5001], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return EventScene_09(self.ctx)


class EventScene_09(common.Trigger):
    def on_enter(self):
        self.set_pc_emotion_sequence(sequenceNames=['Bore_A'])
        self.add_balloon_talk(spawnId=0, msg='!!!', duration=2000, delayTick=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return EventScene_10(self.ctx)


class EventScene_10(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_npc_emotion_sequence(spawnId=102, sequenceName='Emotion_B')
        self.add_cinematic_talk(npcId=11003598, msg='자, 그럼 당신의 실력을 확인해보도록 하죠.', duration=3000, illustId='Michael_normal', align='Center')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return White(self.ctx)


class White(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_white.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return Battle_Ready(self.ctx)


class Battle_Ready(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5002], visible=True)
        self.destroy_monster(spawnIds=[102]) # 미카엘
        self.create_monster(spawnIds=[201], animationEffect=True) # 미카엘 몬스터

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return Battle(self.ctx)


class Battle(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_white.xml')
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.reset_camera(interpolationTime=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=30000):
            return Battle_Stop(self.ctx)


class Battle_Stop(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=101, msg='그만!', duration=3000, delayTick=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Battle_End(self.ctx)


class Battle_End(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.destroy_monster(spawnIds=[201]) # 미카엘

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return EventScene_11(self.ctx)


class EventScene_11(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003614, msg='그만 하세요.', duration=2500)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return EventScene_12(self.ctx)


class EventScene_12(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003598, msg='이런, 이제 막 재미있어지려는 참이었는데 아쉽군요.', duration=2500, illustId='Michael_normal', align='Right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return EventScene_13(self.ctx)


class EventScene_13(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003598, msg='뭐, 다음 기회라는 것도 있으니 이번엔 여기까지만 하겠습니다.', duration=2500, illustId='Michael_normal', align='Right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return EventScene_14(self.ctx)


class EventScene_14(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003614, msg='.......', duration=2500)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return EventScene_15(self.ctx)


class EventScene_15(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003614, msg='돌아가죠. $npcName:11003598$.', duration=2500)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return EventScene_16(self.ctx)


class EventScene_16(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003598, msg='네. 분부대로.', duration=2500, illustId='Michael_normal', align='Right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return QuestComplete(self.ctx)


class QuestComplete(common.Trigger):
    def on_enter(self):
        self.set_achievement(type='trigger', achieve='ForgottenrRoad')
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Warp(self.ctx)


class Warp(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=2020006, portalId=6002)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[60200010], questStates=[1]):
            return QuestComplete(self.ctx)


initial_state = Idle
