""" trigger/63000070_cs/63000070_main.xml """
from common import *
import state


class standby(state.State):
    def on_enter(self):
        set_portal(portalId=20, visible=False, enabled=False, minimapVisible=False)
        set_mesh(triggerIds=[529], visible=True, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[601], visible=False)
        set_effect(triggerIds=[602], visible=False)
        set_effect(triggerIds=[603], visible=False)
        set_effect(triggerIds=[604], visible=False)
        set_effect(triggerIds=[605], visible=False)
        set_interact_object(triggerIds=[32000015], state=2)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return questcheck()


class questcheck(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[30000357], questStates=[2]):
            return gotolobby_ready()
        if quest_user_detected(boxIds=[9000], questIds=[30000357], questStates=[1]):
            return scene1_ready()
        if quest_user_detected(boxIds=[9000], questIds=[30000357], questStates=[3]):
            return emptyroom()
        if wait_tick(waitTick=1000):
            return emptyroom()


class emptyroom(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101,105,111,112,113,114,115,116,117,118,119,120,201,211,221]) # 연출용 NPC 준비 : 지우기

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[30000357], questStates=[2]):
            return gotolobby_ready()
        if quest_user_detected(boxIds=[9000], questIds=[30000357], questStates=[1]):
            return scene1_ready()
        if wait_tick(waitTick=1000):
            return scene_fin()


class gotolobby_ready(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101,105,111,112,113,114,115,116,117,118,119,120,201,211,221]) # 연출용 NPC 준비 : 지우기
        create_monster(spawnIds=[105], arg2=False) # 연출용 NPC 준비 : 꼬마유령 마리엔만 생성
        set_portal(portalId=20, visible=True, enabled=True, minimapVisible=True) # 로비로 이동하는 포탈

    def on_tick(self) -> state.State:
        if not quest_user_detected(boxIds=[9000], questIds=[30000357], questStates=[2]):
            return questcheck()
        if wait_tick(waitTick=1000):
            return scene_fin()


class scene1_ready(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101,105,111,112,113,114,115,116,117,118,119,120,201,211,221]) # 연출용 NPC 준비 : 지우기
        create_monster(spawnIds=[101,111,112,113,114,115,116,117,118,119,120], arg2=False) # 연출용 NPC 준비 : 생성
        set_interact_object(triggerIds=[32000015], state=2) # 연출용 오브젝트 서류가방 : 반응완료 상태로 만들어 안 보이게 처리
        visible_my_pc(isVisible=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 불끄기

    def on_tick(self) -> state.State:
        if not quest_user_detected(boxIds=[9000], questIds=[30000357], questStates=[1]):
            return questcheck()
        if wait_tick(waitTick=1000):
            return scene1_set()


class scene1_set(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 불끄기

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return scene1_start()


class scene1_start(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8000,8001], returnView=False)
        set_scene_skip(state=sceneskip_1, arg2='exit') # setsceneskip 1 set
        add_cinematic_talk(npcId=11004289, illustId='Rue_Halloween', msg='$63000070_CS__63000070_MAIN__0$', duration=3000) # 세상에는 바보들이 참 많아.\n자신들이 할 수 없는 일에 쓸데없이 힘을 쏟는, 그런 바보들 말이야.

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene1_ladymonologue1()


class scene1_ladymonologue1(state.State):
    def on_enter(self):
        move_user(mapId=63000070, portalId=10) # PC, 복도 앞으로 자동 이동
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 불켜기
        add_cinematic_talk(npcId=11004289, illustId='Rue_Halloween', msg='$63000070_CS__63000070_MAIN__1$', duration=4000) # 고아가 된 어린애나,\n유언장을 찾겠다고 나서는 것들이나….

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return scene1_ladymonologue2()


class scene1_ladymonologue2(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8003], returnView=False)
        add_cinematic_talk(npcId=11004289, illustId='Rue_Halloween', msg='$63000070_CS__63000070_MAIN__2$', duration=3000) # 뭔가 바꿀 수 있을 거라고 생각해?
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene1_ladyzoomin()


class scene1_ladyzoomin(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8005,8006], returnView=False)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 불켜기
        add_cinematic_talk(npcId=11004289, msg='$63000070_CS__63000070_MAIN__3$', duration=4000) # 어리석은 자들!\n아무 것도 바꿀 수 없어!
        set_npc_emotion_loop(spawnId=101, sequenceName='Idle_A', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return scene1_ladygoback1()


class scene1_ladygoback1(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8006,8007], returnView=False)
        move_npc(spawnId=101, patrolName='Patrol_lady_backward_01')
        add_cinematic_talk(npcId=11004289, illustId='Rue_Halloween', align='right', msg='$63000070_CS__63000070_MAIN__4$', duration=5000) # 하지만 여기까지 온 것이 가상하니까,\n제안을 하나 하지.

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return scene1_ladygoback2()


class scene1_ladygoback2(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8008], returnView=False)
        add_cinematic_talk(npcId=11004289, illustId='Rue_Halloween', align='right', msg='$63000070_CS__63000070_MAIN__5$', duration=3000) # 자, 네가 원하던 것!\n가질 수 있다면 가져봐.

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene1_ladygoback3()


class scene1_ladygoback3(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8010], returnView=False)
        move_npc(spawnId=101, patrolName='Patrol_lady_backward_02')
        add_cinematic_talk(npcId=11004289, illustId='Rue_Halloween', align='right', msg='$63000070_CS__63000070_MAIN__6$', duration=4000) # 그래… 네가 찾으려던 것, 이 안에 있어.\n하지만 넌 얻을 수 없을 거야.

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return scene1_ladygoback4()


class scene1_ladygoback4(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004289, illustId='Rue_Halloween', align='right', msg='$63000070_CS__63000070_MAIN__7$', duration=4000) # 왠줄 알아?
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return scene1_robottroops()


class scene1_robottroops(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8011], returnView=False)
        move_npc(spawnId=111, patrolName='Patrol_bot_01')
        move_npc(spawnId=112, patrolName='Patrol_bot_02')
        move_npc(spawnId=113, patrolName='Patrol_bot_03')
        move_npc(spawnId=114, patrolName='Patrol_bot_04')
        move_npc(spawnId=115, patrolName='Patrol_bot_05')
        move_npc(spawnId=116, patrolName='Patrol_bot_06')
        move_npc(spawnId=117, patrolName='Patrol_bot_07')
        move_npc(spawnId=118, patrolName='Patrol_bot_08')
        move_npc(spawnId=119, patrolName='Patrol_bot_09')
        move_npc(spawnId=120, patrolName='Patrol_bot_10')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return scene1_ladygoback5()


class scene1_ladygoback5(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='Patrol_lady_backward_03')
        add_cinematic_talk(npcId=11004289, illustId='Rue_Halloween', align='center', msg='$63000070_CS__63000070_MAIN__8$', duration=3000) # 그 전에 목숨을 잃게 될 테니까!

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene1_readytofight()


class scene1_readytofight(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=2)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 불끄기
        set_scene_skip() # setsceneskip 1 close

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return scene1_setbattle()


class sceneskip_1(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=1)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 불끄기
        move_user(mapId=63000070, portalId=10) # PC, 복도 앞으로 자동 이동
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return scene1_setbattle()


class scene1_setbattle(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101,105,111,112,113,114,115,116,117,118,119,120]) # 연출용 NPC 준비 : 지우기
        visible_my_pc(isVisible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return scene1_setbattle1()


class scene1_setbattle1(state.State):
    def on_enter(self):
        move_user_path(patrolName='Patrol_PC_fightposition') # 전투하는 곳으로 달려감
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return wave_1st_ready()


class wave_1st_ready(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 불켜기
        create_monster(spawnIds=[201], arg2=True) # 몬스터 준비 : 생성
        set_effect(triggerIds=[601], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return wave_1st_go()


class wave_1st_go(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 불켜기

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[201]):
            return wave_2nd_ready()


class wave_2nd_ready(state.State):
    def on_enter(self):
        set_effect(triggerIds=[602], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return wave_2nd_go()


class wave_2nd_go(state.State):
    def on_enter(self):
        create_monster(spawnIds=[211], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[211]):
            return wave_3rd_ready()


class wave_3rd_ready(state.State):
    def on_enter(self):
        set_effect(triggerIds=[603], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return wave_3rd_go()


class wave_3rd_go(state.State):
    def on_enter(self):
        create_monster(spawnIds=[221], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[221]):
            return scene2_marienneappears_ready()


class scene2_marienneappears_ready(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 불끄기
        destroy_monster(spawnIds=[101,105,111,112,113,114,115,116,117,118,119,120,1001,1011,1021]) # NPC,몬스터 남아있을 수 있는 애들 다 지우기
        create_monster(spawnIds=[105], arg2=True) # NPC 생성 : 꼬마유령 마리엔
        move_user(mapId=63000070, portalId=11) # 연출포인트로 PC 이동
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return scene2_marienneappears_set()


class scene2_marienneappears_set(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8020], returnView=False)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 불끄기
        set_interact_object(triggerIds=[32000015], state=1) # 연출용 오브젝트 서류가방 : 반응가능 상태로 만들어 보이게 처리
        set_mesh(triggerIds=[529], visible=False, arg3=0, arg4=0, arg5=0) # 연출용 오브젝트 서류가방 더미 :  끔
        set_scene_skip(state=sceneskip_2, arg2='exit') # setsceneskip 2 set

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return scene2_start()


class scene2_start(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8021], returnView=False)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 불켜기
        set_effect(triggerIds=[604], visible=True)
        move_npc(spawnId=105, patrolName='Patrol_girl')
        add_cinematic_talk(npcId=11004308, msg='$63000070_CS__63000070_MAIN__9$', duration=3000) # 여기까지 와줬구나.\n정말 고마워

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene2_girltalk()


class scene2_girltalk(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8022], returnView=False)
        add_cinematic_talk(npcId=11004308, msg='$63000070_CS__63000070_MAIN__10$', duration=2000) # 이제
        set_npc_emotion_loop(spawnId=105, sequenceName='Talk_A', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return scene2_casezoomin()


class scene2_casezoomin(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004308, align='right', msg='$63000070_CS__63000070_MAIN__11$', duration=3000) # 진실을 확인할 시간
        set_scene_skip() # setsceneskip 2 close

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene2_readytosearch()


class sceneskip_2(state.State):
    def on_enter(self):
        move_npc(spawnId=105, patrolName='Patrol_girl')
        set_effect(triggerIds=[604], visible=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return scene2_readytosearch()


class scene2_readytosearch(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=1)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 불끄기

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return scene2_search_ready()


class scene2_search_ready(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 불켜기
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return scene2_search()


class scene2_search(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 불켜기

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[32000015], arg2=0):
            return scene3_ready()


class scene3_ready(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_scene_skip(state=sceneskip_3, arg2='exit') # setsceneskip 3 set

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return scene3_start()


class scene3_start(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004308, msg='$63000070_CS__63000070_MAIN__12$', duration=3500) # 유언장이네…\n이제 모든 걸 알 것 같아.

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return scene3_girltalk0()


class scene3_girltalk0(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8021], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return scene3_girltalk1()


class scene3_girltalk1(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004308, msg='$63000070_CS__63000070_MAIN__13$', duration=5000) # 아빠는 날 지키려고 날 지배인 아저씨의 양녀로 만들고\n모든 걸 지배인 아저씨에게 남겼어
        set_npc_emotion_loop(spawnId=105, sequenceName='Talk_A', duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5500):
            return scene3_girltalk2()


class scene3_girltalk2(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004308, msg='$63000070_CS__63000070_MAIN__14$', duration=4500) # 나, 마지막 부탁이 있는데 들어줄 수 있어?\n로비에서 만나자.
        set_npc_emotion_loop(spawnId=105, sequenceName='Talk_A', duration=4500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4800):
            return scene3_girlgoout()


class scene3_girlgoout(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8022], returnView=False)
        move_npc(spawnId=105, patrolName='Patrol_girl_out')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return scene3_girldisappears()


class scene3_girldisappears(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[105]) # NPC 마리엔 소멸
        set_effect(triggerIds=[605], visible=True)
        set_scene_skip() # setsceneskip 3 close

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return scene3_readytoend()


class sceneskip_3(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[105]) # NPC 마리엔 소멸
        set_effect(triggerIds=[605], visible=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return scene3_readytoend()


class scene3_readytoend(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=2)
        set_portal(portalId=20, visible=True, enabled=True, minimapVisible=True)
        set_effect(triggerIds=[605], visible=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return scene_fin()


class scene_fin(state.State):
    pass


