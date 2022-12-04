""" trigger/63000071_cs/63000071_main.xml """
import trigger_api


class standby(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9000]):
            return openingscene_start(self.ctx)


class openingscene_start(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.visible_my_pc(isVisible=False)
        self.select_camera_path(pathIds=[8000,8001], returnView=False)
        self.create_monster(spawnIds=[101], animationEffect=False) # 연출용 NPC 준비 : 몽슈슈만 생성
        self.set_effect(triggerIds=[5000], visible=True)
        self.set_scene_skip(state=openingskip_1, action='exit') # openingscene 전체스킵

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return openingscene_1_1(self.ctx)

    def on_exit(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml') # 불끄기


class openingscene_1_1(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml') # 불켜기
        self.set_effect(triggerIds=[5000], visible=False)
        self.add_balloon_talk(spawnId=101, msg='$63000071_CS__63000071_MAIN__0$', duration=2500, delayTick=1000) # 내 유언장 내놔!
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Attack_01_A,Attack_01_B')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return openingscene_1_2(self.ctx)


class openingscene_1_2(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Attack_Idle_A', duration=3500)
        self.add_balloon_talk(spawnId=101, msg='$63000071_CS__63000071_MAIN__1$', duration=2500, delayTick=500) # 내 딸을! 내 딸을 찾아줘!

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return openingscene_1_3(self.ctx)


class openingscene_1_3(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Stun_A', duration=8000)
        self.add_balloon_talk(spawnId=101, msg='$63000071_CS__63000071_MAIN__2$', duration=2500, delayTick=500) # 마리엔! 어디있니
        self.add_balloon_talk(spawnId=101, msg='$63000071_CS__63000071_MAIN__3$', duration=3500, delayTick=4000) # 모든게 잘못됐어! 가만두지 않겠어!!

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8500):
            return openingscene_2(self.ctx)

    def on_exit(self):
        self.create_monster(spawnIds=[102], animationEffect=False) # 연출용 NPC : 마리엔 등장
        self.set_effect(triggerIds=[5001], visible=True)
        self.select_camera_path(pathIds=[8002], returnView=False)
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml') # 불끄기


class openingscene_2(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml') # 불켜기
        self.set_effect(triggerIds=[5001], visible=False)
        self.add_balloon_talk(spawnId=102, msg='$63000071_CS__63000071_MAIN__4$', duration=2500, delayTick=500) # 아빠…
        self.add_balloon_talk(spawnId=102, msg='$63000071_CS__63000071_MAIN__5$', duration=2500, delayTick=4000) # 아빠 나 여기있어…

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=7000):
            return openingscene_3(self.ctx)

    def on_exit(self):
        self.select_camera_path(pathIds=[8003], returnView=False)
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_marien3')


class openingscene_3(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11004310, msg='$63000071_CS__63000071_MAIN__6$', duration=2500) # 우리 아빠... 날 보지 못해
        self.add_cinematic_talk(npcId=11004310, msg='$63000071_CS__63000071_MAIN__7$', duration=3000) # 화가 나서 그래
        self.add_cinematic_talk(npcId=11004310, msg='$63000071_CS__63000071_MAIN__8$', duration=3500) # 우리 아빠가 편하게 눈감을 수 있도록 도와줘

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=9500):
            return openingscene_end(self.ctx)


class openingscene_end(trigger_api.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=2)
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return Bossbattle_ready(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[101,102])
        self.set_effect(triggerIds=[5002], visible=True)
        self.set_effect(triggerIds=[5003], visible=True)


class openingskip_1(trigger_api.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=2)
        self.destroy_monster(spawnIds=[101,102])
        self.set_effect(triggerIds=[5002], visible=True)
        self.set_effect(triggerIds=[5003], visible=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml') # 불켜기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Bossbattle_ready(self.ctx)


class Bossbattle_ready(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5002], visible=False)
        self.set_effect(triggerIds=[5003], visible=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.visible_my_pc(isVisible=True)
        self.create_monster(spawnIds=[201], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Bossbattle_start(self.ctx)


class Bossbattle_start(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[201]):
            return endingscene_start(self.ctx)

    def on_exit(self):
        self.create_monster(spawnIds=[103,104], animationEffect=False)
        self.set_effect(triggerIds=[5004], visible=True)
        self.set_effect(triggerIds=[5005], visible=True)
        self.destroy_monster(spawnIds=[201])


class endingscene_start(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.visible_my_pc(isVisible=False)
        self.select_camera_path(pathIds=[8000,8001], returnView=False)
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml') # 불끄기
        self.set_scene_skip(state=endingskip_1, action='exit') # endingscene 전체스킵
        self.set_effect(triggerIds=[5004], visible=False)
        self.set_effect(triggerIds=[5005], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return endingscene_1(self.ctx)


class endingscene_1(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml') # 불켜기
        self.add_balloon_talk(spawnId=104, msg='$63000071_CS__63000071_MAIN__9$', duration=2500, delayTick=500) # 아빠. 이제 다 끝났어
        self.add_balloon_talk(spawnId=103, msg='$63000071_CS__63000071_MAIN__10$', duration=2500, delayTick=4000) # 오, 마리엔! 우리 아가!
        self.add_balloon_talk(spawnId=104, msg='$63000071_CS__63000071_MAIN__11$', duration=2500, delayTick=8000) # 보고 싶었어. 아빠…
        self.add_balloon_talk(spawnId=103, msg='$63000071_CS__63000071_MAIN__12$', duration=2500, delayTick=11500) # 아빠가 죽고 얼마나 고생이 많았니
        self.add_balloon_talk(spawnId=103, msg='$63000071_CS__63000071_MAIN__13$', duration=2500, delayTick=15000) # 아빤 너무 마음이 아팠단다
        self.add_balloon_talk(spawnId=104, msg='$63000071_CS__63000071_MAIN__14$', duration=2500, delayTick=19000) # 괜찮아... 이제 다 끝났잖아

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=22000):
            return endingscene_2(self.ctx)

    def on_exit(self):
        self.move_npc(spawnId=104, patrolName='MS2PatrolData_marien')


class endingscene_2(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8004], returnView=False)
        self.add_cinematic_talk(npcId=11004310, msg='$63000071_CS__63000071_MAIN__15$', duration=6000) # 도와줘서 고마웠어.\n덕분에 나쁜 사람이 누군지 알게 됐어.\n그리고 호텔의 진짜 주인이 지배인 아저씨란 것도 알게 됐어.

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5500):
            return endingscene_3(self.ctx)

    def on_exit(self):
        self.move_npc(spawnId=104, patrolName='MS2PatrolData_marien1')


class endingscene_3(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8001], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return endingscene_4(self.ctx)


class endingscene_4(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=104, msg='$63000071_CS__63000071_MAIN__16$', duration=3000, delayTick=500) # 아빠. 여긴 이제 우리가 있을 곳이 아니야
        self.add_balloon_talk(spawnId=104, msg='$63000071_CS__63000071_MAIN__17$', duration=3000, delayTick=4000) # 우리가 가야할 곳으로 돌아가자

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=7500):
            return endingscene_5(self.ctx)


class endingscene_5(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_papa')
        self.move_npc(spawnId=104, patrolName='MS2PatrolData_marien2')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9001, spawnIds=[0]):
            return endingscene_end(self.ctx)


class endingscene_end(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[103])
        self.destroy_monster(spawnIds=[104])
        self.set_effect(triggerIds=[5006], visible=True)
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return final(self.ctx)


class endingskip_1(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[103])
        self.destroy_monster(spawnIds=[104])
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml') # 불켜기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return final(self.ctx)


class final(trigger_api.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=2)
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.visible_my_pc(isVisible=True)
        self.set_effect(triggerIds=[5006], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return scene_fin(self.ctx)


class scene_fin(trigger_api.Trigger):
    pass


initial_state = standby
