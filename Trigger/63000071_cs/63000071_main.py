""" trigger/63000071_cs/63000071_main.xml """
from common import *
import state


class standby(state.State):
    def on_enter(self):
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return openingscene_start()


class openingscene_start(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        visible_my_pc(isVisible=False)
        select_camera_path(pathIds=[8000,8001], returnView=False)
        create_monster(spawnIds=[101], arg2=False) # 연출용 NPC 준비 : 몽슈슈만 생성
        set_effect(triggerIds=[5000], visible=True)
        set_scene_skip(state=openingskip_1, arg2='exit') # openingscene 전체스킵

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return openingscene_1_1()

    def on_exit(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml') # 불끄기


class openingscene_1_1(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml') # 불켜기
        set_effect(triggerIds=[5000], visible=False)
        add_balloon_talk(spawnId=101, msg='$63000071_CS__63000071_MAIN__0$', duration=2500, delayTick=1000) # 내 유언장 내놔!
        set_npc_emotion_sequence(spawnId=101, sequenceName='Attack_01_A,Attack_01_B')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return openingscene_1_2()


class openingscene_1_2(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=101, sequenceName='Attack_Idle_A', duration=3500)
        add_balloon_talk(spawnId=101, msg='$63000071_CS__63000071_MAIN__1$', duration=2500, delayTick=500) # 내 딸을! 내 딸을 찾아줘!

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return openingscene_1_3()


class openingscene_1_3(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=101, sequenceName='Stun_A', duration=8000)
        add_balloon_talk(spawnId=101, msg='$63000071_CS__63000071_MAIN__2$', duration=2500, delayTick=500) # 마리엔! 어디있니
        add_balloon_talk(spawnId=101, msg='$63000071_CS__63000071_MAIN__3$', duration=3500, delayTick=4000) # 모든게 잘못됐어! 가만두지 않겠어!!

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8500):
            return openingscene_2()

    def on_exit(self):
        create_monster(spawnIds=[102], arg2=False) # 연출용 NPC : 마리엔 등장
        set_effect(triggerIds=[5001], visible=True)
        select_camera_path(pathIds=[8002], returnView=False)
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml') # 불끄기


class openingscene_2(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml') # 불켜기
        set_effect(triggerIds=[5001], visible=False)
        add_balloon_talk(spawnId=102, msg='$63000071_CS__63000071_MAIN__4$', duration=2500, delayTick=500) # 아빠…
        add_balloon_talk(spawnId=102, msg='$63000071_CS__63000071_MAIN__5$', duration=2500, delayTick=4000) # 아빠 나 여기있어…

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return openingscene_3()

    def on_exit(self):
        select_camera_path(pathIds=[8003], returnView=False)
        move_npc(spawnId=102, patrolName='MS2PatrolData_marien3')


class openingscene_3(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004310, msg='$63000071_CS__63000071_MAIN__6$', duration=2500) # 우리 아빠... 날 보지 못해
        add_cinematic_talk(npcId=11004310, msg='$63000071_CS__63000071_MAIN__7$', duration=3000) # 화가 나서 그래
        add_cinematic_talk(npcId=11004310, msg='$63000071_CS__63000071_MAIN__8$', duration=3500) # 우리 아빠가 편하게 눈감을 수 있도록 도와줘

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9500):
            return openingscene_end()


class openingscene_end(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=2)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return Bossbattle_ready()

    def on_exit(self):
        destroy_monster(spawnIds=[101,102])
        set_effect(triggerIds=[5002], visible=True)
        set_effect(triggerIds=[5003], visible=True)


class openingskip_1(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=2)
        destroy_monster(spawnIds=[101,102])
        set_effect(triggerIds=[5002], visible=True)
        set_effect(triggerIds=[5003], visible=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=4)
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml') # 불켜기

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Bossbattle_ready()


class Bossbattle_ready(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5002], visible=False)
        set_effect(triggerIds=[5003], visible=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        visible_my_pc(isVisible=True)
        create_monster(spawnIds=[201], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Bossbattle_start()


class Bossbattle_start(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[201]):
            return endingscene_start()

    def on_exit(self):
        create_monster(spawnIds=[103,104], arg2=False)
        set_effect(triggerIds=[5004], visible=True)
        set_effect(triggerIds=[5005], visible=True)
        destroy_monster(spawnIds=[201])


class endingscene_start(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        visible_my_pc(isVisible=False)
        select_camera_path(pathIds=[8000,8001], returnView=False)
        set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml') # 불끄기
        set_scene_skip(state=endingskip_1, arg2='exit') # endingscene 전체스킵
        set_effect(triggerIds=[5004], visible=False)
        set_effect(triggerIds=[5005], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return endingscene_1()


class endingscene_1(state.State):
    def on_enter(self):
        set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml') # 불켜기
        add_balloon_talk(spawnId=104, msg='$63000071_CS__63000071_MAIN__9$', duration=2500, delayTick=500) # 아빠. 이제 다 끝났어
        add_balloon_talk(spawnId=103, msg='$63000071_CS__63000071_MAIN__10$', duration=2500, delayTick=4000) # 오, 마리엔! 우리 아가!
        add_balloon_talk(spawnId=104, msg='$63000071_CS__63000071_MAIN__11$', duration=2500, delayTick=8000) # 보고 싶었어. 아빠…
        add_balloon_talk(spawnId=103, msg='$63000071_CS__63000071_MAIN__12$', duration=2500, delayTick=11500) # 아빠가 죽고 얼마나 고생이 많았니
        add_balloon_talk(spawnId=103, msg='$63000071_CS__63000071_MAIN__13$', duration=2500, delayTick=15000) # 아빤 너무 마음이 아팠단다
        add_balloon_talk(spawnId=104, msg='$63000071_CS__63000071_MAIN__14$', duration=2500, delayTick=19000) # 괜찮아... 이제 다 끝났잖아

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=22000):
            return endingscene_2()

    def on_exit(self):
        move_npc(spawnId=104, patrolName='MS2PatrolData_marien')


class endingscene_2(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8004], returnView=False)
        add_cinematic_talk(npcId=11004310, msg='$63000071_CS__63000071_MAIN__15$', duration=6000) # 도와줘서 고마웠어.\n덕분에 나쁜 사람이 누군지 알게 됐어.\n그리고 호텔의 진짜 주인이 지배인 아저씨란 것도 알게 됐어.

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5500):
            return endingscene_3()

    def on_exit(self):
        move_npc(spawnId=104, patrolName='MS2PatrolData_marien1')


class endingscene_3(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8001], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return endingscene_4()


class endingscene_4(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=104, msg='$63000071_CS__63000071_MAIN__16$', duration=3000, delayTick=500) # 아빠. 여긴 이제 우리가 있을 곳이 아니야
        add_balloon_talk(spawnId=104, msg='$63000071_CS__63000071_MAIN__17$', duration=3000, delayTick=4000) # 우리가 가야할 곳으로 돌아가자

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7500):
            return endingscene_5()


class endingscene_5(state.State):
    def on_enter(self):
        move_npc(spawnId=103, patrolName='MS2PatrolData_papa')
        move_npc(spawnId=104, patrolName='MS2PatrolData_marien2')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=9001, spawnIds=[0]):
            return endingscene_end()


class endingscene_end(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[103])
        destroy_monster(spawnIds=[104])
        set_effect(triggerIds=[5006], visible=True)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return final()


class endingskip_1(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[103])
        destroy_monster(spawnIds=[104])
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=4)
        set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml') # 불켜기

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return final()


class final(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=2)
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        visible_my_pc(isVisible=True)
        set_effect(triggerIds=[5006], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return scene_fin()


class scene_fin(state.State):
    pass


