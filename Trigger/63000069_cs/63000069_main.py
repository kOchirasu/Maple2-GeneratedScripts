""" trigger/63000069_cs/63000069_main.xml """
import trigger_api


class standby(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 불끄기
        self.create_monster(spawnIds=[101,102,103,104,105,106,107,108,109], animationEffect=False) # 연출용 NPC 준비 : 꼬마유령 마리엔 빼고 모두 생성
        self.set_effect(triggerIds=[601], visible=False)
        self.set_effect(triggerIds=[602], visible=False)
        self.set_mesh(triggerIds=[4001], visible=False)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_01_girl') # 연출용 NPC 이동 : 움직임 없는 09번 어린 여자아이 유령 제외 전체 어슬렁어슬렁
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_02_man')
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_03_girlmaid')
        self.move_npc(spawnId=104, patrolName='MS2PatrolData_04_boymaid')
        self.move_npc(spawnId=105, patrolName='MS2PatrolData_05_blackstaragent')
        self.move_npc(spawnId=106, patrolName='MS2PatrolData_06_oldman')
        self.move_npc(spawnId=107, patrolName='MS2PatrolData_07_cat')
        self.move_npc(spawnId=108, patrolName='MS2PatrolData_08_youngboy')
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9000]):
            return questcheck(self.ctx)


class questcheck(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[150]) # 연출용 NPC : 꼬마유령 마리엔 지우기
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 불켜기

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[30000356], questStates=[3]):
            return fin(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[30000356], questStates=[2]):
            return scene1_ready(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[30000356], questStates=[1]):
            return searching_check(self.ctx)


class searching_check(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=26300691, textId=26300691) # 단서 찾으라는 가이드 스트링 출력

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[30000356], questStates=[2]):
            return scene1_ready(self.ctx)


class scene1_ready(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 불끄기
        self.hide_guide_summary(entityId=26300691, textId=26300691) # 단서 찾으라는 가이드 스트링 감춤
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_03_girlmaid_out') # 연출용 NPC 여자 메이드 이동 : 카메라에 걸리지 않는 위치로 멀리 보내기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return scene1_set(self.ctx)


class scene1_set(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=63000069, portalId=11) # 안전포인트로 PC 이동
        self.set_mesh(triggerIds=[4001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.quest_user_detected(boxIds=[9000], questIds=[30000356], questStates=[2]):
            return questcheck(self.ctx)
        if self.wait_tick(waitTick=1000):
            return scene1_start(self.ctx)


class scene1_start(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 불켜기
        self.set_scene_skip(state=sceneskip, action='exit') # setsceneskip set
        self.select_camera_path(pathIds=[8000,8001], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return scene1_girlmonologue0(self.ctx)


class scene1_girlmonologue0(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[150], animationEffect=False) # 연출용 NPC 준비 : 마리엔 생성
        self.set_effect(triggerIds=[601], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return scene1_girlmonologue1(self.ctx)


class scene1_girlmonologue1(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=150, patrolName='MS2PatrolData_50_marienne')
        self.set_effect(triggerIds=[601], visible=False)
        self.add_cinematic_talk(npcId=11004308, msg='$63000069_CS__63000069_MAIN__0$', duration=3000) # 맞지? 내 말.\n아빠 친구, 여기 왔었어.

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene1_girlmonologue2(self.ctx)


class scene1_girlmonologue2(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11004308, msg='$63000069_CS__63000069_MAIN__1$', duration=4500) # 아빠 친구, 나랑 지배인 아저씨한테 할 말이 있다고 했는데…\n사라져 버렸어.
        self.set_npc_emotion_loop(spawnId=150, sequenceName='Talk_A', duration=4500)
        self.set_effect(triggerIds=[601], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return scene1_girlmonologue3(self.ctx)


class scene1_girlmonologue3(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11004308, msg='$63000069_CS__63000069_MAIN__2$', duration=5500) # 나한텐 아무도 없었어…\n아빠도… 아빠 친구도…
        self.set_npc_emotion_loop(spawnId=150, sequenceName='Bore_B', duration=5500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5500):
            return scene1_girlrealize0(self.ctx)


class scene1_girlrealize0(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8002], returnView=False)
        self.add_cinematic_talk(npcId=11004308, msg='$63000069_CS__63000069_MAIN__3$', duration=3000) # ……아
        self.set_npc_emotion_loop(spawnId=150, sequenceName='Damg_A', duration=100)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene1_girlrealize1(self.ctx)


class scene1_girlrealize1(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8003], returnView=False)
        self.add_cinematic_talk(npcId=11004308, msg='$63000069_CS__63000069_MAIN__4$', duration=4000) # 그런데… 나…
        self.move_user(mapId=63000069, portalId=10) # 연출포인트로 PC 이동
        self.move_npc(spawnId=150, patrolName='MS2PatrolData_51_marienne1')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return scene1_girlrealize2(self.ctx)


class scene1_girlrealize2(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11004308, msg='$63000069_CS__63000069_MAIN__5$', duration=5000) # 나… 아저씨 방에서 누가 나오는 걸 봤어.\n유언장…이라고 적힌 걸 갖고 444호 객실로 가는 걸 말야.
        self.set_npc_emotion_loop(spawnId=150, sequenceName='Talk_A', duration=4500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return scene1_girlmonologue5(self.ctx)


class scene1_girlmonologue5(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8004], returnView=False)
        self.add_cinematic_talk(npcId=11004308, msg='$63000069_CS__63000069_MAIN__6$', duration=3500) # 이 사실을 알려줘.\n지배인 아저씨께…
        self.set_effect(triggerIds=[602], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return scene_readytoend(self.ctx)


class scene_readytoend(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 불끄기
        self.set_mesh(triggerIds=[4001], visible=False)
        self.set_scene_skip() # setsceneskip close

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return scene_fin_ready(self.ctx)


class sceneskip(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[150]) # NPC 마리엔 소멸
        self.set_mesh(triggerIds=[4001], visible=False)
        self.move_user(mapId=63000069, portalId=10) # 연출포인트로 PC 이동
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return scene_fin_ready(self.ctx)


class scene_fin_ready(trigger_api.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=1)
        self.destroy_monster(spawnIds=[150]) # NPC 마리엔 소멸
        self.set_effect(triggerIds=[602], visible=False)
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_03_girlmaid')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return scene_fin(self.ctx)


class scene_fin(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 불켜기
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class fin(trigger_api.Trigger):
    pass


initial_state = standby
