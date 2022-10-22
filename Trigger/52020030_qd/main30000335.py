""" trigger/52020030_qd/main30000335.xml """
from common import *
import state


#  투르카와 전투 
class 입장1(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=False)
        set_effect(triggerIds=[5002], visible=False)
        set_effect(triggerIds=[5003], visible=False)
        set_effect(triggerIds=[5004], visible=False)
        set_effect(triggerIds=[5007], visible=False)
        set_effect(triggerIds=[5006], visible=False)
        set_onetime_effect(id=300, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_onetime_effect(id=301, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2003], questIds=[30000335], questStates=[1]):
            return 투르카이오네연출시작()


class 투르카이오네연출시작(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        create_monster(spawnIds=[109], arg2=False)
        destroy_monster(spawnIds=[111]) # 퀘스트용 크란츠 삭제
        select_camera_path(pathIds=[4011], returnView=False)
        move_user(mapId=52020030, portalId=6004)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 투르카이오네연출시작_02()


class 투르카이오네연출시작_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        create_monster(spawnIds=[102], arg2=False)
        create_monster(spawnIds=[103], arg2=False)
        set_effect(triggerIds=[5001], visible=True)
        set_effect(triggerIds=[5002], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 투르카의등장()


class 투르카의등장(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4031], returnView=False)
        add_cinematic_talk(npcId=11003762, msg='천공의 심장을 손에 넣었군.', duration=3000)
        # Missing State: 공명준비
        set_scene_skip(arg2='exit')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 투르카의등장_01()


class 투르카의등장_01(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=103, sequenceName='Bore_B')
        add_cinematic_talk(npcId=11003762, msg='이리 가져와라. 크란츠.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 투르카의등장02()


class 투르카의등장02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4019], returnView=False)
        add_cinematic_talk(npcId=11003761, msg='어디서 감히 명령이지?', duration=3000)
        add_cinematic_talk(npcId=11003761, msg='나에게 명령을 내릴 수 있는 자는 오직 이오네 왕녀님 뿐이다.', duration=3000)
        set_npc_emotion_loop(spawnId=102, sequenceName='Quest_Frustration_A', duration=9500)
        set_npc_emotion_loop(spawnId=102, sequenceName='Talk_A', duration=12000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 투르카의등장03()


class 투르카의등장03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4018], returnView=False)
        add_cinematic_talk(npcId=11003760, msg='크란츠... 지금은 이 자의 말을 듣도록 해.', duration=3000)
        add_cinematic_talk(npcId=11003760, msg='천공의 심장을 이리로.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 투르카의등장04()


class 투르카의등장04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4019], returnView=False)
        add_cinematic_talk(npcId=11003761, msg='... 넵. 왕녀님', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 반대하는플레이어()


class 반대하는플레이어(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4025], returnView=False)
        face_emotion(spawnId=0, emotionName='defaultBattle')
        set_pc_emotion_loop(sequenceName='Talk_A', duration=4000)
        add_cinematic_talk(npcId=0, msg='천공의 심장을 넘기면 안돼!\n투르카가 티마이온을!!!', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 반대하는플레이어02()


class 반대하는플레이어02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4019,4035], returnView=False)
        add_cinematic_talk(npcId=11003761, msg='어쩔 수 없어.\n모든 것은 왕녀님을 위해...', duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 반대하는플레이어03()


class 반대하는플레이어03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4036], returnView=False)
        move_npc(spawnId=109, patrolName='MS2PatrolData_3002')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 반대하는플레이어04()


class 반대하는플레이어04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4025], returnView=False)
        face_emotion(spawnId=0, emotionName='defaultBattle')
        set_pc_emotion_loop(sequenceName='Talk_A', duration=4000)
        add_cinematic_talk(npcId=0, msg='안돼!!!', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 크란츠이동()


class 크란츠이동(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        destroy_monster(spawnIds=[109])
        create_monster(spawnIds=[105], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 크란츠이동_02()


class 크란츠이동_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        select_camera_path(pathIds=[4037], returnView=False)
        move_npc(spawnId=105, patrolName='MS2PatrolData_3005')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 크란츠이동_03()


class 크란츠이동_03(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=102, sequenceName='Talk_A', duration=3000)
        add_cinematic_talk(npcId=11003760, msg='수고했어요, 크란츠.', duration=3000)
        add_cinematic_talk(npcId=11003761, msg='왕녀님의 말씀이라면...', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 공명준비이오네()


class 공명준비이오네(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[105])
        create_monster(spawnIds=[110], arg2=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[4031], returnView=False)
        add_cinematic_talk(npcId=11003762, msg='자, 그럼 이오네.\n파멸의 날개에 천공의 심장을 공명시켜라.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 공명준비이오네_02()


class 공명준비이오네_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4018], returnView=False)
        add_cinematic_talk(npcId=11003760, msg='알았어.\n바로 시작하도록 하지.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 공명준비이오네03()


class 공명준비이오네03(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=102, sequenceName='Quest_Spell_A')
        add_cinematic_talk(npcId=11003760, msg='파멸의 날개여, 마법의 힘을 받아들여라.', duration=3000)
        set_effect(triggerIds=[5001], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 공명준비이오네04()


class 공명준비이오네04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4034], returnView=False)
        set_npc_emotion_loop(spawnId=102, sequenceName='Quest_Resonance_A', duration=1.2E+09)
        set_effect(triggerIds=[5004], visible=True)
        set_effect(triggerIds=[5007], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 투르카공격준비()


class 투르카공격준비(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4031], returnView=False)
        add_cinematic_talk(npcId=11003762, msg='크하하.', duration=3000)
        add_cinematic_talk(npcId=11003762, msg='계획대로 되어가는군.', duration=3000)
        add_cinematic_talk(npcId=11003762, msg='자 그럼... 이제 방해꾼을 처리해 보도록 할까.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return 투르카공격준비_1()


class 투르카공격준비_1(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        create_monster(spawnIds=[104], arg2=False)
        destroy_monster(spawnIds=[103])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 투르카공격준비01()


class 투르카공격준비01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4021], returnView=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_npc_emotion_sequence(spawnId=104, sequenceName='Attack_02_C')
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_onetime_effect(id=300, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        add_cinematic_talk(npcId=11003762, msg='너 따위는 내가 직접 나설 것도 없지.\n이 곳에서 영원히 잠들어라.', duration=3000)
        add_cinematic_talk(npcId=11003762, msg='나와라. 어둠의 그림자들이여...', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 투르카공격준비03()


class 투르카공격준비03(state.State):
    def on_enter(self):
        set_onetime_effect(id=400, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        select_camera_path(pathIds=[4032,4033], returnView=False)
        set_effect(triggerIds=[5003], visible=True)
        set_npc_emotion_loop(spawnId=104, sequenceName='Bore_A', duration=100000)
        create_monster(spawnIds=[501], arg2=True)
        create_monster(spawnIds=[502], arg2=True)
        create_monster(spawnIds=[503], arg2=True)
        create_monster(spawnIds=[504], arg2=True)
        create_monster(spawnIds=[505], arg2=True)
        create_monster(spawnIds=[506], arg2=True)
        create_monster(spawnIds=[507], arg2=True)
        create_monster(spawnIds=[508], arg2=True)
        create_monster(spawnIds=[509], arg2=True)
        create_monster(spawnIds=[510], arg2=True)
        create_monster(spawnIds=[511], arg2=True)
        create_monster(spawnIds=[512], arg2=True)
        create_monster(spawnIds=[513], arg2=True)
        create_monster(spawnIds=[514], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 투르카공격준비04()


class 투르카공격준비04(state.State):
    def on_enter(self):
        set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 투르카공격준비05()


class 투르카공격준비05(state.State):
    def on_enter(self):
        move_user(mapId=52020030, portalId=6005)
        set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_onetime_effect(id=300, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_event_ui(type=1, arg2='투르카의 부하들을 처치하세요.', arg3='2000', arg4='0')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        create_monster(spawnIds=[103], arg2=False)
        destroy_monster(spawnIds=[104])
        reset_camera(interpolationTime=0)
        set_effect(triggerIds=[5003], visible=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[501,502,503,504,505,506,507,508,509,510,511,512,513,514]):
            return 공명완료()


class 공명완료(state.State):
    def on_enter(self):
        set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_effect(triggerIds=[5001], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 공명완료02()


class 공명완료02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4011], returnView=False)
        set_onetime_effect(id=5, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_onetime_effect(id=301, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_npc_emotion_loop(spawnId=102, sequenceName='Bore_A', duration=100000)
        add_cinematic_talk(npcId=11003760, msg='공명이 완료 되었어.\n다음 재료를 찾으러 이동 해야해.', duration=3000)
        add_cinematic_talk(npcId=11003762, msg='후후. 빠르군.', duration=3000)
        set_effect(triggerIds=[5004], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 공명완료02_01()


class 공명완료02_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4039], returnView=False)
        add_cinematic_talk(npcId=11003761, msg='왕녀님, 몸음 괜찮으신 겁니까. \n혹시 무리라도 하신건...', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 공명완료02_02()


class 공명완료02_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4018], returnView=False)
        set_npc_emotion_loop(spawnId=102, sequenceName='Talk_A', duration=3000)
        add_cinematic_talk(npcId=11003760, msg='난 괜찮아 크란츠. ', duration=3000)
        add_cinematic_talk(npcId=11003760, msg='투르카, 어서 다음 재료의 장소로 이동을.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 공명완료02_03()


class 공명완료02_03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4011], returnView=False)
        set_npc_emotion_loop(spawnId=103, sequenceName='Bore_A', duration=100000)
        add_cinematic_talk(npcId=11003762, msg='자, 그럼 이동해볼까.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 공명완료03()


class 공명완료03(state.State):
    def on_enter(self):
        set_onetime_effect(id=6, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        create_monster(spawnIds=[107], arg2=False)
        destroy_monster(spawnIds=[102])
        destroy_monster(spawnIds=[103])
        destroy_monster(spawnIds=[110])
        set_effect(triggerIds=[5001], visible=True)
        set_effect(triggerIds=[5002], visible=True)
        set_effect(triggerIds=[5005], visible=True)
        move_user(mapId=52020030, portalId=6005)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 공명완료03_01()


class 공명완료03_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4038], returnView=False)
        set_onetime_effect(id=6, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        face_emotion(spawnId=0, emotionName='defaultBattle')
        set_pc_emotion_loop(sequenceName='Idle_A', duration=8000)
        add_cinematic_talk(npcId=0, msg='이럴수가...', duration=3000)
        add_cinematic_talk(npcId=0, msg='이오네 왕녀가 투르카와 손을 잡다니...', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 공명완료04()


class 공명완료04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4017], returnView=False)
        move_npc(spawnId=107, patrolName='MS2PatrolData_3002')
        add_cinematic_talk(npcId=11003753, msg='자네... 무사했군....', duration=3000)
        set_effect(triggerIds=[5001], visible=False)
        set_effect(triggerIds=[5002], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 공명완료05()


class 공명완료05(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0.5)
        set_achievement(triggerId=2003, type='trigger', achieve='SkyTower')
        destroy_monster(spawnIds=[107])
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


