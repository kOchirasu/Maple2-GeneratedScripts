""" trigger/52100101_qd/52100101.xml """
import trigger_api


class wait_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[2001]):
            return wait_02(self.ctx)


class wait_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5001], visible=False) # 정리
        self.destroy_monster(spawnIds=[101])
        self.destroy_monster(spawnIds=[102])
        self.destroy_monster(spawnIds=[103])
        self.destroy_monster(spawnIds=[104])
        self.destroy_monster(spawnIds=[105])
        self.destroy_monster(spawnIds=[106])
        self.destroy_monster(spawnIds=[107])
        self.destroy_monster(spawnIds=[108])
        self.destroy_monster(spawnIds=[109])
        self.destroy_monster(spawnIds=[110])
        self.destroy_monster(spawnIds=[111])
        self.destroy_monster(spawnIds=[112])
        self.destroy_monster(spawnIds=[113])
        self.destroy_monster(spawnIds=[114]) # 다시생성
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Dead_A')
        self.create_monster(spawnIds=[102], animationEffect=False)
        self.set_npc_emotion_sequence(spawnId=102, sequenceName='Dead_B')
        self.create_monster(spawnIds=[103], animationEffect=False)
        self.set_npc_emotion_sequence(spawnId=103, sequenceName='Dead_A')
        self.create_monster(spawnIds=[104], animationEffect=False)
        self.set_npc_emotion_sequence(spawnId=104, sequenceName='Dead_B')
        self.create_monster(spawnIds=[105], animationEffect=False)
        self.set_npc_emotion_sequence(spawnId=105, sequenceName='Dead_A')
        self.create_monster(spawnIds=[106], animationEffect=False)
        self.set_npc_emotion_sequence(spawnId=106, sequenceName='Dead_B')
        self.create_monster(spawnIds=[107], animationEffect=False)
        self.set_npc_emotion_sequence(spawnId=107, sequenceName='Dead_B')
        self.create_monster(spawnIds=[108], animationEffect=False)
        self.set_npc_emotion_sequence(spawnId=108, sequenceName='Dead_A')
        self.create_monster(spawnIds=[114], animationEffect=False) # 클라디아
        self.set_npc_emotion_loop(spawnId=114, sequenceName='Sit_Down_A', duration=1E+10) # 클라디아

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[50100860], questStates=[2]):
            return wait_01_02(self.ctx)
        if self.quest_user_detected(boxIds=[2002], questIds=[50100870], questStates=[3]):
            return wait_01_03(self.ctx)


class wait_01_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return wait_01_02_003(self.ctx)


class wait_01_02_003(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.move_user(mapId=52100101, portalId=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 구릉도착(self.ctx)


class 구릉도착(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 구릉도착_01_2(self.ctx)


class 구릉도착_01_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4001,4002,4003], returnView=False)
        self.move_user_path(patrolName='MS2PatrolData_3001')
        self.set_scene_skip(state=Skip_1, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 구릉도착_02(self.ctx)


class 구릉도착_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npcId=0, msg='$52100101_QD__52100101__0$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 검은군단들(self.ctx)


class 검은군단들(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4004], returnView=False) # 미사일포트 조금 더 적게
        self.add_cinematic_talk(npcId=0, msg='$52100101_QD__52100101__1$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 검은군단들2(self.ctx)


class 검은군단들2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4005,4007], returnView=False) # 시간 계산 다시
        self.add_cinematic_talk(npcId=0, msg='$52100101_QD__52100101__2$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 검은군단들3(self.ctx)


class 검은군단들3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=0, msg='$52100101_QD__52100101__3$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 정리_01(self.ctx)


class 정리_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 정리_02(self.ctx)


class 정리_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolationTime=0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        # Missing State: State
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 밝아짐(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.reset_camera(interpolationTime=0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 밝아짐(self.ctx)


class 밝아짐(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2002], questIds=[50100870], questStates=[3]):
            return wait_01_03(self.ctx)


class wait_01_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return wait_01_04(self.ctx)


class wait_01_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.move_user(mapId=52100101, portalId=3)
        self.create_monster(spawnIds=[109], animationEffect=False) # 장교
        self.create_monster(spawnIds=[110], animationEffect=False) # 병사
        self.create_monster(spawnIds=[111], animationEffect=False)
        self.create_monster(spawnIds=[112], animationEffect=False)
        self.create_monster(spawnIds=[113], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 클라디아바라봄(self.ctx)


class 클라디아바라봄(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 클라디아바라봄_02(self.ctx)


class 클라디아바라봄_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4009], returnView=False)
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npcId=0, msg='$52100101_QD__52100101__4$', duration=3000)
        self.add_cinematic_talk(npcId=11004422, msg='$52100101_QD__52100101__5$', duration=3000)
        self.set_scene_skip(state=Skip_2, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 게오르크_04(self.ctx)


class 게오르크_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4011,4013], returnView=False) # 바로 오는 것으로
        self.move_npc(spawnId=109, patrolName='MS2PatrolData_3002')
        self.move_npc(spawnId=110, patrolName='MS2PatrolData_3003')
        self.move_npc(spawnId=111, patrolName='MS2PatrolData_3004')
        self.move_npc(spawnId=112, patrolName='MS2PatrolData_3005')
        self.move_npc(spawnId=113, patrolName='MS2PatrolData_3006')
        self.add_cinematic_talk(npcId=0, msg='$52100101_QD__52100101__6$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 게오르크_04_02(self.ctx)


class 게오르크_04_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11004422, msg='$52100101_QD__52100101__7$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4500):
            return 게오르크_05(self.ctx)


class 게오르크_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=0, msg='$52100101_QD__52100101__8$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 게오르크_06(self.ctx)


class 게오르크_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4014], returnView=False)
        self.move_user_path(patrolName='MS2PatrolData_3007')
        self.add_cinematic_talk(npcId=0, msg='$52100101_QD__52100101__9$', duration=4000)
        self.add_cinematic_talk(npcId=11004422, msg='$52100101_QD__52100101__10$', duration=4000)
        self.add_cinematic_talk(npcId=0, msg='$52100101_QD__52100101__11$', duration=4500)
        self.add_cinematic_talk(npcId=0, msg='$52100101_QD__52100101__12$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=16500):
            return 게오르크_07(self.ctx)


class 게오르크_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11004422, msg='$52100101_QD__52100101__13$', duration=4500)
        self.add_cinematic_talk(npcId=11004422, msg='$52100101_QD__52100101__14$', duration=4500)
        self.add_cinematic_talk(npcId=0, msg='$52100101_QD__52100101__15$', duration=4500)
        self.add_cinematic_talk(npcId=11004422, msg='$52100101_QD__52100101__16$', duration=4000)
        self.add_cinematic_talk(npcId=11004422, msg='$52100101_QD__52100101__17$', duration=4500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=22000):
            return 잠시후(self.ctx)


class 잠시후(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 잠시후_2(self.ctx)


class 잠시후_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='$52100101_QD__52100101__18$')
        self.select_camera_path(pathIds=[4015], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 잠시후_3(self.ctx)


class 잠시후_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[109]) # 장교
        self.destroy_monster(spawnIds=[110]) # 병사
        self.destroy_monster(spawnIds=[111])
        self.destroy_monster(spawnIds=[112])
        self.destroy_monster(spawnIds=[113])
        self.destroy_monster(spawnIds=[114])
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.visible_my_pc(isVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 잠시후_4(self.ctx)


class 잠시후_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 잠시후_5(self.ctx)


class 잠시후_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4016], returnView=False)
        self.set_effect(triggerIds=[5001], visible=True)
        self.add_cinematic_talk(npcId=11004421, msg='$52100101_QD__52100101__19$', duration=3000)
        self.add_cinematic_talk(npcId=11004421, msg='$52100101_QD__52100101__20$', duration=3000)
        self.add_cinematic_talk(npcId=11004421, msg='$52100101_QD__52100101__21$', duration=3000)
        self.add_cinematic_talk(npcId=11004421, msg='$52100101_QD__52100101__22$', duration=3000)
        # Missing State: State
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=12000):
            return 이동(self.ctx)


class Skip_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 이동_02(self.ctx)


class 이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 이동_02(self.ctx)


class 이동_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.visible_my_pc(isVisible=True)
        self.move_user(mapId=2020029, portalId=3)


initial_state = wait_01
