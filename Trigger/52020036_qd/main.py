""" trigger/52020036_qd/main.xml """
from common import *
import state


class 딜레이(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return 준비()


class 준비(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000043], state=2)
        set_mesh(triggerIds=[9999], visible=True) # 발록 함선 보이기
        create_monster(spawnIds=[7000])
        create_monster(spawnIds=[7001])
        create_monster(spawnIds=[7002])
        create_monster(spawnIds=[7003])
        create_monster(spawnIds=[7004])
        # <action name="메쉬를설정한다" arg1="4000" arg2="0" /> 공습용 공중 발판 끄기1
        set_mesh(triggerIds=[4002], visible=False) # 공습용 공중 발판 끄기1
        create_monster(spawnIds=[201], arg2=False) # 구르는 천둥
        create_monster(spawnIds=[901], arg2=False) # 시끄러운 주먹
        create_monster(spawnIds=[400], arg2=False) # 티나
        create_monster(spawnIds=[10000], arg2=False)
        create_monster(spawnIds=[10001], arg2=False)
        create_monster(spawnIds=[10002], arg2=False)
        create_monster(spawnIds=[10003], arg2=False)
        create_monster(spawnIds=[10004], arg2=False)
        create_monster(spawnIds=[10006], arg2=False)
        create_monster(spawnIds=[10007], arg2=False)
        create_monster(spawnIds=[10008], arg2=False)
        create_monster(spawnIds=[10009], arg2=False)
        create_monster(spawnIds=[10010], arg2=False)
        create_monster(spawnIds=[10011], arg2=False)
        create_monster(spawnIds=[10014], arg2=False)
        create_monster(spawnIds=[10015], arg2=False)
        create_monster(spawnIds=[10016], arg2=False)
        create_monster(spawnIds=[10017], arg2=False)
        create_monster(spawnIds=[10018], arg2=False)
        create_monster(spawnIds=[10019], arg2=False)
        create_monster(spawnIds=[10020], arg2=False)
        create_monster(spawnIds=[10021], arg2=False)
        create_monster(spawnIds=[10022], arg2=False)
        create_monster(spawnIds=[10023], arg2=False)
        create_monster(spawnIds=[10024], arg2=False)
        create_monster(spawnIds=[10025], arg2=False)
        create_monster(spawnIds=[10026], arg2=False)
        create_monster(spawnIds=[10027], arg2=False)
        create_monster(spawnIds=[10028], arg2=False)
        create_monster(spawnIds=[10029], arg2=False)
        create_monster(spawnIds=[10030], arg2=False)
        create_monster(spawnIds=[10031], arg2=False)
        create_monster(spawnIds=[10032], arg2=False)
        create_monster(spawnIds=[10033], arg2=False)
        create_monster(spawnIds=[10034], arg2=False)
        create_monster(spawnIds=[10035], arg2=False)
        create_monster(spawnIds=[10036], arg2=False)
        create_monster(spawnIds=[10037], arg2=False)
        create_monster(spawnIds=[10038], arg2=False)
        create_monster(spawnIds=[10039], arg2=False)
        create_monster(spawnIds=[10040], arg2=False)
        create_monster(spawnIds=[10041], arg2=False)
        create_monster(spawnIds=[10042], arg2=False)
        create_monster(spawnIds=[10043], arg2=False)
        create_monster(spawnIds=[10044], arg2=False)
        create_monster(spawnIds=[10045], arg2=False)
        create_monster(spawnIds=[10046], arg2=False)
        create_monster(spawnIds=[10047], arg2=False)
        create_monster(spawnIds=[10048], arg2=False)
        create_monster(spawnIds=[10049], arg2=False)
        create_monster(spawnIds=[10050], arg2=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[91000049], questStates=[3]):
            return 공중지원퀘스트완료()
        if quest_user_detected(boxIds=[9000], questIds=[91000049], questStates=[2]):
            return 공중지원퀘스트완료()
        if quest_user_detected(boxIds=[9000], questIds=[91000049], questStates=[1]):
            return 네이린팝업1()
        if quest_user_detected(boxIds=[9000], questIds=[91000048], questStates=[3]):
            return 부상자옮기기대사()
        if quest_user_detected(boxIds=[9000], questIds=[91000048], questStates=[2]):
            return 부상자옮기기대사()
        if quest_user_detected(boxIds=[9000], questIds=[91000048], questStates=[1]):
            return 티나비추기()
        if quest_user_detected(boxIds=[9000], questIds=[91000047], questStates=[3]):
            return 침략자소탕퀘스트완료()
        if quest_user_detected(boxIds=[9000], questIds=[91000047], questStates=[2]):
            return 침략자소탕퀘스트완료()
        if quest_user_detected(boxIds=[9000], questIds=[91000047], questStates=[1]):
            return 오프닝연출끝()
        if wait_tick(waitTick=1000):
            return 피그밍그부족의제단원경신1()


#  피그밍그 부족의 제단 원경신1 
class 피그밍그부족의제단원경신1(state.State):
    def on_enter(self):
        set_quest_accept(questId=91000047)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        show_caption(type='VerticalCaption', title='$52020036_QD__MAIN__0$', desc='$52020036_QD__MAIN__1$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=7000, scale=2.5)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[3000,3001], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 피그밍그부족의제단원경신2()


#  피그밍그 부족의 제단 원경신2 
class 피그밍그부족의제단원경신2(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[3013,3014], returnView=False)
        set_scene_skip(state=콘대르소환, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 전투상황비추기()


class 전투상황비추기(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)
        select_camera(triggerId=3003, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 유저발록보이게위치옮김()


class 유저발록보이게위치옮김(state.State):
    def on_enter(self):
        move_user(mapId=52020036, portalId=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 오프닝크림슨발록비추기()


class 오프닝크림슨발록비추기(state.State):
    def on_enter(self):
        select_camera(triggerId=3015, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 크림슨발록오프닝대사()


class 크림슨발록오프닝대사(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003781, msg='$52020036_QD__MAIN__2$', duration=3000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 콘대르등장카메라()


#  콘대르 등장 
class 콘대르등장카메라(state.State):
    def on_enter(self):
        select_camera(triggerId=3002, enable=True)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=0):
            return 콘대르소환()


class 콘대르소환(state.State):
    def on_enter(self):
        move_user(mapId=52020036, portalId=1)
        create_monster(spawnIds=[100], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=0):
            return 유저를경로이동시킨다()


class 유저를경로이동시킨다(state.State):
    def on_enter(self):
        move_user_path(patrolName='User_PatrolData_0')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 콘대르등장대사()


class 콘대르등장대사(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003776, illustId='Conder_normal', msg='$52020036_QD__MAIN__3$', duration=3000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 콘대르이동()


class 콘대르이동(state.State):
    def on_enter(self):
        move_npc(spawnId=100, patrolName='Conder_Spawn_Opening_PatrolData_1')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 오프닝연출끝()


class 오프닝연출끝(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        destroy_monster(spawnIds=[100])
        create_monster(spawnIds=[101], arg2=False) # 콘대르
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 구르는천둥대사()


#  구르는천둥대사1 
class 구르는천둥대사(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11000009, illust='RollingThunder_normal', duration=7000, script='$52020036_QD__main__12$', voice='ko/Npc/00002150')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 콘대르전투참여대사()


#  콘대르전투참여대사 
class 콘대르전투참여대사(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11003776, illust='Conder_normal', duration=8300, script='$52020036_QD__main__13$', voice='ko/Npc/00002147')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8300):
            return 침략자소탕퀘스트완료체크()


class 침략자소탕퀘스트완료체크(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[91000047], questStates=[2]):
            return 침략자소탕퀘스트완료()


class 침략자소탕퀘스트완료(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_quest_complete(questId=91000047)
        set_quest_accept(questId=91000048)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[3005,3006], returnView=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 티나비추기()


#  티나비추기
class 티나비추기(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        select_camera(triggerId=3004, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=0):
            return 티나대사1()


class 티나대사1(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        add_cinematic_talk(npcId=11000136, illustId='Tina_normal', msg='$52020036_QD__MAIN__4$', duration=5000, align='Right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 몬스터한번더스폰()


class 몬스터한번더스폰(state.State):
    def on_enter(self):
        create_monster(spawnIds=[20001], arg2=False)
        create_monster(spawnIds=[10000], arg2=False)
        create_monster(spawnIds=[10001], arg2=False)
        create_monster(spawnIds=[10002], arg2=False)
        create_monster(spawnIds=[10003], arg2=False)
        create_monster(spawnIds=[10004], arg2=False)
        create_monster(spawnIds=[10005], arg2=False)
        create_monster(spawnIds=[10006], arg2=False)
        create_monster(spawnIds=[10007], arg2=False)
        create_monster(spawnIds=[10008], arg2=False)
        create_monster(spawnIds=[10010], arg2=False)
        create_monster(spawnIds=[10012], arg2=False)
        create_monster(spawnIds=[10014], arg2=False)
        create_monster(spawnIds=[10016], arg2=False)
        create_monster(spawnIds=[10016], arg2=False)
        create_monster(spawnIds=[10017], arg2=False)
        create_monster(spawnIds=[10018], arg2=False)
        create_monster(spawnIds=[10019], arg2=False)
        create_monster(spawnIds=[10020], arg2=False)
        create_monster(spawnIds=[10021], arg2=False)
        create_monster(spawnIds=[10022], arg2=False)
        create_monster(spawnIds=[10023], arg2=False)
        create_monster(spawnIds=[10024], arg2=False)
        create_monster(spawnIds=[10025], arg2=False)
        create_monster(spawnIds=[10026], arg2=False)
        create_monster(spawnIds=[10027], arg2=False)
        create_monster(spawnIds=[10028], arg2=False)
        create_monster(spawnIds=[10029], arg2=False)
        create_monster(spawnIds=[10030], arg2=False)
        create_monster(spawnIds=[10031], arg2=False)
        create_monster(spawnIds=[10032], arg2=False)
        create_monster(spawnIds=[10033], arg2=False)
        create_monster(spawnIds=[10034], arg2=False)
        create_monster(spawnIds=[10035], arg2=False)
        create_monster(spawnIds=[10036], arg2=False)
        create_monster(spawnIds=[10037], arg2=False)
        create_monster(spawnIds=[10038], arg2=False)
        create_monster(spawnIds=[10039], arg2=False)
        create_monster(spawnIds=[10040], arg2=False)
        create_monster(spawnIds=[10041], arg2=False)
        create_monster(spawnIds=[10042], arg2=False)
        create_monster(spawnIds=[10043], arg2=False)
        create_monster(spawnIds=[10044], arg2=False)
        create_monster(spawnIds=[10045], arg2=False)
        create_monster(spawnIds=[10046], arg2=False)
        create_monster(spawnIds=[10047], arg2=False)
        create_monster(spawnIds=[10048], arg2=False)
        create_monster(spawnIds=[10049], arg2=False)
        create_monster(spawnIds=[10050], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=0):
            return 부상자구하기시작()


class 부상자구하기시작(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 부상자구출퀘스트완료체크()


class 부상자구출퀘스트완료체크(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[91000048], questStates=[2]):
            return 부상자옮기기대사()


#  티나 팝업 대사 UI_1 
class 부상자옮기기대사(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_quest_complete(questId=91000048)
        set_quest_accept(questId=91000049)
        side_npc_talk(npcId=11003780, illust='WhitewolfGirl_normal', duration=5648, script='$52020036_QD__main__14$', voice='ko/Npc/00002151')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5648):
            return 네이린팝업1()


#  네이린팝업1 
class 네이린팝업1(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        side_npc_talk(npcId=11003536, illust='Neirin_normal', duration=7000, script='$52020036_QD__main__15$', voice='ko/Npc/00002126')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 네이린팝업2()


class 네이린팝업2(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11003536, illust='Neirin_smile', duration=7000, script='$52020036_QD__main__16$', voice='ko/Npc/00002127')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 네이린팝업3()


class 네이린팝업3(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11003536, illust='Neirin_normal', duration=7000, script='$52020036_QD__main__17$', voice='ko/Npc/00002128')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 공중지원퀘스트자동수락()


class 공중지원퀘스트자동수락(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000043], state=1)
        destroy_monster(spawnIds=[901])
        destroy_monster(spawnIds=[101])
        destroy_monster(spawnIds=[201])
        destroy_monster(spawnIds=[-1])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=0):
            return 콘대르구르는천둥P3스폰()


class 콘대르구르는천둥P3스폰(state.State):
    def on_enter(self):
        create_monster(spawnIds=[902], arg2=False)
        create_monster(spawnIds=[8000], arg2=False)
        create_monster(spawnIds=[8001], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 석궁비추기()


#  석궁비추기 
class 석궁비추기(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=3007, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 석궁비추기끝()


class 석궁비추기끝(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=0):
            return 콘대르팝업1()


class 콘대르팝업1(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11003776, illust='Conder_normal', duration=7000, script='$52020036_QD__main__18$', voice='ko/Npc/00002148')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 네이린팝업4()


class 네이린팝업4(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11003536, illust='Neirin_shy', duration=7000, script='$52020036_QD__main__19$', voice='ko/Npc/00002129')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 콘대르팝업2()


class 콘대르팝업2(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11003776, illust='Conder_normal', duration=6000, script='$52020036_QD__main__20$', voice='ko/Npc/00002149')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 네이린웨이브경고팝업()


class 네이린웨이브경고팝업(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11003536, illust='Neirin_surprise', duration=1000, script='$52020036_QD__main__21$', voice='ko/Npc/00002130')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1340):
            return 네이린웨이브경고팝업1()


class 네이린웨이브경고팝업1(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11003536, illust='Neirin_surprise', duration=7000, script='$52020036_QD__main__22$', voice='ko/Npc/00002131')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7012):
            return 네이린웨이브경고팝업2()


class 네이린웨이브경고팝업2(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 웨이브스폰1()


class 웨이브스폰1(state.State):
    def on_enter(self):
        create_monster(spawnIds=[10051], arg2=False)
        create_monster(spawnIds=[10059], arg2=False)
        create_monster(spawnIds=[10067], arg2=False)
        create_monster(spawnIds=[10075], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 웨이브스폰1패트롤()


class 웨이브스폰1패트롤(state.State):
    def on_enter(self):
        move_npc(spawnId=10051, patrolName='WavePatrolDataEast')
        move_npc(spawnId=10059, patrolName='WavePatrolDataEast')
        move_npc(spawnId=10067, patrolName='WavePatrolDataWest')
        move_npc(spawnId=10075, patrolName='WavePatrolDataSouth')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 웨이브스폰2()


class 웨이브스폰2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[10055], arg2=False)
        create_monster(spawnIds=[10063], arg2=False)
        create_monster(spawnIds=[10071], arg2=False)
        create_monster(spawnIds=[10079], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 웨이브스폰3()


class 웨이브스폰3(state.State):
    def on_enter(self):
        create_monster(spawnIds=[10052], arg2=False)
        create_monster(spawnIds=[10060], arg2=False)
        create_monster(spawnIds=[10068], arg2=False)
        create_monster(spawnIds=[10076], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 웨이브스폰4()


class 웨이브스폰4(state.State):
    def on_enter(self):
        create_monster(spawnIds=[10056], arg2=False)
        create_monster(spawnIds=[10064], arg2=False)
        create_monster(spawnIds=[10072], arg2=False)
        create_monster(spawnIds=[10080], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 웨이브스폰5()


class 웨이브스폰5(state.State):
    def on_enter(self):
        create_monster(spawnIds=[10053], arg2=False)
        create_monster(spawnIds=[10061], arg2=False)
        create_monster(spawnIds=[10069], arg2=False)
        create_monster(spawnIds=[10078], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 웨이브스폰6()


class 웨이브스폰6(state.State):
    def on_enter(self):
        create_monster(spawnIds=[10054], arg2=False)
        create_monster(spawnIds=[10057], arg2=False)
        create_monster(spawnIds=[10065], arg2=False)
        create_monster(spawnIds=[10073], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 웨이브스폰7()


class 웨이브스폰7(state.State):
    def on_enter(self):
        create_monster(spawnIds=[10058], arg2=False)
        create_monster(spawnIds=[10062], arg2=False)
        create_monster(spawnIds=[10066], arg2=False)
        create_monster(spawnIds=[10070], arg2=False)
        create_monster(spawnIds=[10074], arg2=False)
        create_monster(spawnIds=[10077], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 차웨이브스폰1_2()


class 차웨이브스폰1_2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[10051], arg2=False)
        create_monster(spawnIds=[10059], arg2=False)
        create_monster(spawnIds=[10067], arg2=False)
        create_monster(spawnIds=[10075], arg2=False)
        create_monster(spawnIds=[10079], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 차웨이브스폰2_2()


class 차웨이브스폰2_2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[10052], arg2=False)
        create_monster(spawnIds=[10055], arg2=False)
        create_monster(spawnIds=[10060], arg2=False)
        create_monster(spawnIds=[10063], arg2=False)
        create_monster(spawnIds=[10071], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 차웨이브스폰3_2()


class 차웨이브스폰3_2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[10056], arg2=False)
        create_monster(spawnIds=[10064], arg2=False)
        create_monster(spawnIds=[10068], arg2=False)
        create_monster(spawnIds=[10072], arg2=False)
        create_monster(spawnIds=[10076], arg2=False)
        create_monster(spawnIds=[10080], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 차웨이브스폰4_2()


class 차웨이브스폰4_2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[10053], arg2=False)
        create_monster(spawnIds=[10057], arg2=False)
        create_monster(spawnIds=[10061], arg2=False)
        create_monster(spawnIds=[10065], arg2=False)
        create_monster(spawnIds=[10069], arg2=False)
        create_monster(spawnIds=[10073], arg2=False)
        create_monster(spawnIds=[10078], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 차웨이브스폰5_2()


class 차웨이브스폰5_2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[10054], arg2=False)
        create_monster(spawnIds=[10058], arg2=False)
        create_monster(spawnIds=[10062], arg2=False)
        create_monster(spawnIds=[10066], arg2=False)
        create_monster(spawnIds=[10070], arg2=False)
        create_monster(spawnIds=[10074], arg2=False)
        create_monster(spawnIds=[10077], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=0):
            return 공중지원퀘스트완료체크()


class 공중지원퀘스트완료체크(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[91000049], questStates=[2]):
            return 공중지원퀘스트완료()


class 공중지원퀘스트완료(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000043], state=0)
        visible_my_pc(isVisible=False) # 캐릭터 숨김
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        destroy_monster(spawnIds=[-1])
        set_quest_complete(questId=91000049)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 엔딩크림슨발록보이는위치로유저이동()


class 엔딩크림슨발록보이는위치로유저이동(state.State):
    def on_enter(self):
        move_user(mapId=52020036, portalId=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 엔딩크림슨발록비추기()


class 엔딩크림슨발록비추기(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=3015, enable=True)
        create_monster(spawnIds=[7000], arg2=False)
        create_monster(spawnIds=[7001], arg2=False)
        create_monster(spawnIds=[7002], arg2=False)
        create_monster(spawnIds=[7003], arg2=False)
        create_monster(spawnIds=[7004], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 크림슨발록엔딩닝대사()


class 크림슨발록엔딩닝대사(state.State):
    def on_enter(self):
        remove_buff(boxId=9000, skillId=99910150)
        add_cinematic_talk(npcId=11003781, msg='$52020036_QD__MAIN__5$', duration=5000, align='left')
        set_npc_emotion_sequence(spawnId=7000, sequenceName='Attack_01_A', durationTick=1900)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 엔딩연출준비()


class 엔딩연출준비(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[7000])
        destroy_monster(spawnIds=[7001])
        destroy_monster(spawnIds=[7002])
        destroy_monster(spawnIds=[7003])
        destroy_monster(spawnIds=[7004])
        set_mesh(triggerIds=[9999], visible=False, arg5=0) # 발록 함선 지우기

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=0):
            return 엔딩연출1()


class 엔딩연출1(state.State):
    def on_enter(self):
        visible_my_pc(isVisible=True) # 캐릭터 보임
        create_monster(spawnIds=[3500], arg2=False)
        create_monster(spawnIds=[4500], arg2=False)
        create_monster(spawnIds=[5500], arg2=False)
        set_scene_skip(state=전부지우기, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=0):
            return 엔딩카메라1()


class 엔딩카메라1(state.State):
    def on_enter(self):
        select_camera(triggerId=3008, enable=True)
        move_user(mapId=52020036, portalId=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=0):
            return 콘대르엔딩대사1()


class 콘대르엔딩대사1(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003776, illustId='Conder_normal', msg='$52020036_QD__MAIN__6$', duration=4000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 구르는천둥엔딩대사1()


class 구르는천둥엔딩대사1(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003779, illustId='LoudFist_normal', msg='$52020036_QD__MAIN__7$', duration=4000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 트리스탄생성1()


class 트리스탄생성1(state.State):
    def on_enter(self):
        create_monster(spawnIds=[6500], arg2=False)
        move_user(mapId=52020036, portalId=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=0):
            return 트리스탄등장카메라1()


class 트리스탄등장카메라1(state.State):
    def on_enter(self):
        select_camera(triggerId=3009, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 트리스탄대사1()


class 트리스탄대사1(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11001975, illustId='Tristan_normal', msg='$52020036_QD__MAIN__8$', duration=3000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 콘대르엔딩카메라1()


class 콘대르엔딩카메라1(state.State):
    def on_enter(self):
        select_camera(triggerId=3010, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 콘대르엔딩카메라2()


class 콘대르엔딩카메라2(state.State):
    def on_enter(self):
        select_camera(triggerId=3010, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=0):
            return 콘대르엔딩대사2()


class 콘대르엔딩대사2(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003776, illustId='Conder_normal', msg='$52020036_QD__MAIN__9$', duration=1000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 콘대르엔딩카메라3()


class 콘대르엔딩카메라3(state.State):
    def on_enter(self):
        select_camera(triggerId=3012, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=0):
            return 콘대르엔딩대사3()


class 콘대르엔딩대사3(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003776, illustId='Conder_normal', msg='$52020036_QD__MAIN__10$', duration=2000, align='left')
        set_npc_emotion_sequence(spawnId=3500, sequenceName='Bore_A', durationTick=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 트리스탄엔딩카메라2()


class 트리스탄엔딩카메라2(state.State):
    def on_enter(self):
        select_camera(triggerId=3009, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 트리스탄엔딩대사2()


class 트리스탄엔딩대사2(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003777, illustId='Tristan_normal', msg='$52020036_QD__MAIN__11$', duration=4000, align='left')
        set_npc_emotion_sequence(spawnId=6500, sequenceName='Talk_A', durationTick=7000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 엔딩카메라2()


class 엔딩카메라2(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[3007,3016], returnView=False)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 전부지우기()


class 전부지우기(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[-1])
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=4)
        move_user(mapId=52010052, portalId=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=0):
            return None # Missing State: 


