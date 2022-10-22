""" trigger/52010063_qd/main.xml """
from common import *
import state


class start(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=False) # 트리스탄
        create_monster(spawnIds=[102], arg2=False) # 인페르녹
        create_monster(spawnIds=[111,112,113,114,115], arg2=False) # npc 부하 크림슨 발록
        destroy_monster(spawnIds=[211,212,213,214,215]) # 몬스터 부하 크림슨 발록
        set_effect(triggerIds=[6000,6001,6002,6003,6004,6010,6011], visible=False) # 기빨고기빨리는이펙트
        set_mesh(triggerIds=[4001,4002,4003,4004], visible=False)

    def on_tick(self) -> state.State:
        if check_user():
            return 퀘스트조건체크()


class 퀘스트조건체크(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[91000066], questStates=[3]):
            return 맵이동_작전실로()
        if quest_user_detected(boxIds=[9000], questIds=[91000066], questStates=[2]):
            return 처치후_대기()
        if quest_user_detected(boxIds=[9000], questIds=[91000066], questStates=[1]):
            return 처치후_대기()
        if quest_user_detected(boxIds=[9000], questIds=[91000065], questStates=[3]):
            return 처치후_대기()
        if quest_user_detected(boxIds=[9000], questIds=[91000065], questStates=[2]):
            return 처치후_대기()
        if quest_user_detected(boxIds=[9000], questIds=[91000065], questStates=[1]):
            return 처치후_대기()
        if quest_user_detected(boxIds=[9000], questIds=[91000064], questStates=[3]):
            return 처치후_대기()
        if quest_user_detected(boxIds=[9000], questIds=[91000064], questStates=[2]):
            return 처치후_대기()
        if quest_user_detected(boxIds=[9000], questIds=[91000064], questStates=[1]):
            return 연출시작()


class 처치후_대기(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        destroy_monster(spawnIds=[101,102,111,112,113,114,115,211,212,213,214,215,221,222,223,224,225,226]) # 전체 npc
        move_user(mapId=52010063, portalId=20) # 유저 퀘 시작 위치로
        create_monster(spawnIds=[103], arg2=False) # 퀘스트용 트리스탄

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 처치후()


class 처치후(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출종료()


class 맵이동_작전실로(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101,102,111,112,113,114,115,211,212,213,214,215,221,222,223,224,225,226]) # 트리스탄 제외 전체 npc

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 최종맵이동()


class 최종맵이동(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        move_user(mapId=52010052, portalId=1) # 스카이 포트리스 작전실로

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 최종맵이동()


class 연출시작(state.State):
    def on_enter(self):
        set_scene_skip(state=전투전스킵완료, arg2='nextState') # setsceneskip 1 set
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_npc_emotion_loop(spawnId=101, sequenceName='Dead_A', duration=999999)
        # <action name="SetNpcEmotionLoop" arg1="101" arg2="Attack_02_B" arg3="999999" />
        set_npc_emotion_loop(spawnId=102, sequenceName='Attack_02_D', duration=17000) # 인페르녹 기빨기 모션
        set_effect(triggerIds=[6000,6003], visible=True) # 인페르녹 기빨기 이펙트
        set_effect(triggerIds=[6001], visible=True) # 트리스탄 바닥 이펙트
        set_effect(triggerIds=[6002], visible=True) # 트리스탄 기빨림 이펙트
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 인페르녹줌인00()


class 인페르녹줌인00(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 인페르녹줌인01()


class 인페르녹줌인01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8000,8001,8002], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return PC놀람01()


class PC놀람01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8003], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PC놀람02()


class PC놀람02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52010063_QD__main__0$', duration=3000, align='right') # 트리스탄…?

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 인페르녹줌인02()


class 인페르녹줌인02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8004], returnView=False)
        add_cinematic_talk(npcId=11003832, illustId='infernog_nomal', msg='$52010063_QD__main__1$', duration=5000, align='right')
        set_effect(triggerIds=[6000,6003], visible=False) # 인페르녹 기빨기 이펙트
        set_npc_emotion_sequence(spawnId=102, sequenceName='Attack_03_D') # 인페르녹

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 인페르녹줌인03()


class 인페르녹줌인03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003832, illustId='infernog_nomal', msg='$52010063_QD__main__2$', duration=5000, align='right')
        set_npc_emotion_sequence(spawnId=102, sequenceName='Attack_03_F')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 인페르녹줌인04()


class 인페르녹줌인04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8002], returnView=False)
        add_cinematic_talk(npcId=11003832, illustId='infernog_nomal', msg='$52010063_QD__main__3$', duration=5000, align='right') # 크르르… 너희는 대체 뭘 하고 있었던 것이냐!\n침입자가 들어오게 내버려두다니!
        move_npc(spawnId=102, patrolName='MS2PatrolData_Infernog_goforward') # 인페르녹 전진

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 부하대사01()


class 부하대사01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8011], returnView=False)
        add_cinematic_talk(npcId=11003839, msg='$52010063_QD__main__4$', duration=3000, align='right') # 죄…죄송합니다!
        set_npc_emotion_sequence(spawnId=114, sequenceName='Attack_01_A') # 크림슨발록

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 부하대사02()


class 부하대사02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8012], returnView=False)
        add_cinematic_talk(npcId=11003839, msg='$52010063_QD__main__5$', duration=3000, align='right') # 지금 당장 처단을…! />
        set_npc_emotion_sequence(spawnId=115, sequenceName='Attack_01_A') # 크림슨발록

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 인페르녹대사01()


class 인페르녹대사01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8004], returnView=False)
        add_cinematic_talk(npcId=11003832, illustId='infernog_nomal', msg='$52010063_QD__main__6$', duration=4000, align='right') # 멍청한 녀석들.\n침입자가 들어온 순간 이번 의식은 끝난 것이다. />
        set_npc_emotion_sequence(spawnId=102, sequenceName='Attack_02_F') # 인페르녹

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 인페르녹대사02()


class 인페르녹대사02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8003,8005], returnView=False)
        add_cinematic_talk(npcId=11003832, illustId='infernog_nomal', msg='$52010063_QD__main__7$', duration=6000, align='right') # 이 가문의 버러지들은 사사건건 나를 성가시게 만드는구나….\n본래 내 것인데, 돌려받기 위해 이런 번거로운 일을 하게 만들다니

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 인페르녹대사03()


class 인페르녹대사03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003832, illustId='infernog_nomal', msg='$52010063_QD__main__8$', duration=5000, align='right') # 하지만… 다음 기회를 만드는 것은 아주 쉬운 일이지.\n내 혼을 먹은 이상, 이 녀석은 내 손바닥 안에 있는 것이나 마찬가지니까.
        set_npc_emotion_sequence(spawnId=102, sequenceName='Attack_02_E')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 인페르녹대사04()


class 인페르녹대사04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003832, illustId='infernog_nomal', msg='$52010063_QD__main__9$', duration=5000, align='right')
        # <action name="SetNpcEmotionLoop" arg1="102" arg2="Attack_01_C, Attack_01_E" arg3="4000" />
        set_npc_emotion_sequence(spawnId=102, sequenceName='Attack_03_D') # 나의 충실한 종복들이여. 실수를 만회할 기회를 주겠노라.\n침입자를 깨끗하게 정리하라." />

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 인페르녹대사05()


class 인페르녹대사05(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8004,8000], returnView=False)
        add_cinematic_talk(npcId=11003832, illustId='infernog_nomal', msg='$52010063_QD__main__10$', duration=5000, align='right') # 내가 이번 의식을 마무리하러 떠나 있는 동안 임무를 끝내라.\n두 번의 실수는 없어야 할 것이야!
        set_npc_emotion_sequence(spawnId=102, sequenceName='Leave_01_A,Leave_02_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 부하들준비00()


class 부하들준비00(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8000], returnView=False)
        add_cinematic_talk(npcId=11003839, msg='$52010063_QD__main__11$', duration=3000, align='right') # 받들겠습니다…!
        set_effect(triggerIds=[6010], visible=True) # 인페르녹 붉은 안개
        set_npc_emotion_sequence(spawnId=102, sequenceName='Leave_02_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 부하들등장00()


class 부하들등장00(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_scene_skip() # setsceneskip 1 close

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 부하들등장01()


class 전투전스킵완료(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        destroy_monster(spawnIds=[102]) # 인페르녹
        destroy_monster(spawnIds=[111,112,113,114,115]) # npc 크림슨 발록
        create_monster(spawnIds=[211], arg2=True) # 몬스터 크림슨 발록
        move_user(mapId=52010063, portalId=11) # 유저 전투 시작 위치로
        set_effect(triggerIds=[6000,6003], visible=False) # 인페르녹 기빨기 이펙트
        set_effect(triggerIds=[6010], visible=True) # 인페르녹 붉은 안개

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 부하들등장02()


class 부하들등장01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[102]) # 인페르녹
        destroy_monster(spawnIds=[111,112,113,114,115]) # npc 크림슨 발록
        create_monster(spawnIds=[211,221,222,223,224,225,226], arg2=False) # 몬스터 크림슨 발록
        move_user(mapId=52010063, portalId=11) # 유저 전투 시작 위치로

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 부하들등장02()


class 부하들등장02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        reset_camera(interpolationTime=2)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 부하들등장211()


class 부하들등장211(state.State):
    def on_enter(self):
        create_monster(spawnIds=[212], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[211]):
            return 부하들등장212()


class 부하들등장212(state.State):
    def on_enter(self):
        create_monster(spawnIds=[213], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[212]):
            return 부하들등장213()


class 부하들등장213(state.State):
    def on_enter(self):
        create_monster(spawnIds=[214], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[213]):
            return 부하들등장214215()


class 부하들등장214215(state.State):
    def on_enter(self):
        create_monster(spawnIds=[215], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[214,215]):
            return 트리스탄구출00()


class 트리스탄구출00(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        destroy_monster(spawnIds=[111,112,113,114,115,211,212,213,214,215,221,222,223,224,225,226]) # 부하 몬스터 청소
        set_achievement(triggerId=9000, type='trigger', achieve='crimsonbalrogwipeout')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_mesh(triggerIds=[4001,4002,4003,4004], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 트리스탄구출01()


class 트리스탄구출01(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        destroy_monster(spawnIds=[101]) # 트리스탄
        create_monster(spawnIds=[103], arg2=False) # 퀘스트용 트리스탄
        move_user(mapId=52010063, portalId=20) # 유저 전투 시작 위치로
        set_effect(triggerIds=[6001,6002], visible=False) # 트리스탄 바닥 이펙트

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 트리스탄구출02()


class 트리스탄구출02(state.State):
    def on_enter(self):
        set_scene_skip(state=전투후스킵완료, arg2='nextState') # setsceneskip 2 set
        select_camera_path(pathIds=[8003,8013,8014], returnView=False)
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_npc_emotion_loop(spawnId=103, sequenceName='Dead_A', duration=5000) # 트리스탄
        set_effect(triggerIds=[6004], visible=True) # 트리스탄 잡힌 효과 꺼짐
        add_cinematic_talk(npcId=11003825, illustId='Tristan_normal', msg='$52010063_QD__main__12$', duration=5000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 트리스탄구출03()


class 트리스탄구출03(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6010], visible=False) # 인페르녹 붉은 안개
        set_effect(triggerIds=[6011], visible=True) # 인페르녹 붉은 안개 꺼짐
        move_npc(spawnId=103, patrolName='MS2PatrolData_Tristan_walk') # 트리스탄 전진

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 트리스탄구출04()


class 트리스탄구출04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8022,8021], returnView=False)
        add_cinematic_talk(npcId=11003825, illustId='Tristan_normal', msg='$52010063_QD__main__13$', duration=3000, align='right')
        set_npc_emotion_loop(spawnId=103, sequenceName='ChatUp_A', duration=3000) # 트리스탄
        set_effect(triggerIds=[6004], visible=False)
        set_effect(triggerIds=[6011], visible=False) # 인페르녹 붉은 안개 꺼짐
        set_scene_skip() # setsceneskip 2 close

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 연출종료()


class 전투후스킵완료(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6000,6001,6002,6003,6004,6005,6010,6011], visible=False)
        move_user(mapId=52010063, portalId=20) # 유저 전투 시작 위치로
        move_npc(spawnId=103, patrolName='MS2PatrolData_Tristan_walk') # 트리스탄 전진

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=2)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_mesh(triggerIds=[4001,4002,4003,4004], visible=False)
        set_achievement(triggerId=9000, type='trigger', achieve='tristanrescue') # 퀘스트 완료 업적

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[91000065], questStates=[3]):
            return 콘대르_대사()


class 콘대르_대사(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=11003534, illust='Conder_normal', script='$52010063_QD__main__15$', duration=12098, voice='ko/Npc/00002170')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=12098):
            return 퀘스트유저감지_대사()


class 퀘스트유저감지_대사(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[91000066], questStates=[3]):
            return 블리체_대사()


class 블리체_대사(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=11003533, illust='Bliche_nomal', script='$52010063_QD__main__14$', duration=13000, voice='ko/Npc/00002153')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=13000):
            return 마지막체크()


class 마지막체크(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[91000066], questStates=[3]):
            return 맵이동_작전실로()


class 종료(state.State):
    pass


