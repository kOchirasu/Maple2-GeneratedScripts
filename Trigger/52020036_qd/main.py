""" trigger/52020036_qd/main.xml """
import common


class 딜레이(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9000]):
            return 준비(self.ctx)


class 준비(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000043], state=2)
        self.set_mesh(triggerIds=[9999], visible=True) # 발록 함선 보이기
        self.create_monster(spawnIds=[7000])
        self.create_monster(spawnIds=[7001])
        self.create_monster(spawnIds=[7002])
        self.create_monster(spawnIds=[7003])
        self.create_monster(spawnIds=[7004])
        # <action name="메쉬를설정한다" arg1="4000" arg2="0" /> 공습용 공중 발판 끄기1
        self.set_mesh(triggerIds=[4002], visible=False) # 공습용 공중 발판 끄기1
        self.create_monster(spawnIds=[201], animationEffect=False) # 구르는 천둥
        self.create_monster(spawnIds=[901], animationEffect=False) # 시끄러운 주먹
        self.create_monster(spawnIds=[400], animationEffect=False) # 티나
        self.create_monster(spawnIds=[10000], animationEffect=False)
        self.create_monster(spawnIds=[10001], animationEffect=False)
        self.create_monster(spawnIds=[10002], animationEffect=False)
        self.create_monster(spawnIds=[10003], animationEffect=False)
        self.create_monster(spawnIds=[10004], animationEffect=False)
        self.create_monster(spawnIds=[10006], animationEffect=False)
        self.create_monster(spawnIds=[10007], animationEffect=False)
        self.create_monster(spawnIds=[10008], animationEffect=False)
        self.create_monster(spawnIds=[10009], animationEffect=False)
        self.create_monster(spawnIds=[10010], animationEffect=False)
        self.create_monster(spawnIds=[10011], animationEffect=False)
        self.create_monster(spawnIds=[10014], animationEffect=False)
        self.create_monster(spawnIds=[10015], animationEffect=False)
        self.create_monster(spawnIds=[10016], animationEffect=False)
        self.create_monster(spawnIds=[10017], animationEffect=False)
        self.create_monster(spawnIds=[10018], animationEffect=False)
        self.create_monster(spawnIds=[10019], animationEffect=False)
        self.create_monster(spawnIds=[10020], animationEffect=False)
        self.create_monster(spawnIds=[10021], animationEffect=False)
        self.create_monster(spawnIds=[10022], animationEffect=False)
        self.create_monster(spawnIds=[10023], animationEffect=False)
        self.create_monster(spawnIds=[10024], animationEffect=False)
        self.create_monster(spawnIds=[10025], animationEffect=False)
        self.create_monster(spawnIds=[10026], animationEffect=False)
        self.create_monster(spawnIds=[10027], animationEffect=False)
        self.create_monster(spawnIds=[10028], animationEffect=False)
        self.create_monster(spawnIds=[10029], animationEffect=False)
        self.create_monster(spawnIds=[10030], animationEffect=False)
        self.create_monster(spawnIds=[10031], animationEffect=False)
        self.create_monster(spawnIds=[10032], animationEffect=False)
        self.create_monster(spawnIds=[10033], animationEffect=False)
        self.create_monster(spawnIds=[10034], animationEffect=False)
        self.create_monster(spawnIds=[10035], animationEffect=False)
        self.create_monster(spawnIds=[10036], animationEffect=False)
        self.create_monster(spawnIds=[10037], animationEffect=False)
        self.create_monster(spawnIds=[10038], animationEffect=False)
        self.create_monster(spawnIds=[10039], animationEffect=False)
        self.create_monster(spawnIds=[10040], animationEffect=False)
        self.create_monster(spawnIds=[10041], animationEffect=False)
        self.create_monster(spawnIds=[10042], animationEffect=False)
        self.create_monster(spawnIds=[10043], animationEffect=False)
        self.create_monster(spawnIds=[10044], animationEffect=False)
        self.create_monster(spawnIds=[10045], animationEffect=False)
        self.create_monster(spawnIds=[10046], animationEffect=False)
        self.create_monster(spawnIds=[10047], animationEffect=False)
        self.create_monster(spawnIds=[10048], animationEffect=False)
        self.create_monster(spawnIds=[10049], animationEffect=False)
        self.create_monster(spawnIds=[10050], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[91000049], questStates=[3]):
            return 공중지원퀘스트완료(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[91000049], questStates=[2]):
            return 공중지원퀘스트완료(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[91000049], questStates=[1]):
            return 네이린팝업1(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[91000048], questStates=[3]):
            return 부상자옮기기대사(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[91000048], questStates=[2]):
            return 부상자옮기기대사(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[91000048], questStates=[1]):
            return 티나비추기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[91000047], questStates=[3]):
            return 침략자소탕퀘스트완료(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[91000047], questStates=[2]):
            return 침략자소탕퀘스트완료(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[91000047], questStates=[1]):
            return 오프닝연출끝(self.ctx)
        if self.wait_tick(waitTick=1000):
            return 피그밍그부족의제단원경신1(self.ctx)


# 피그밍그 부족의 제단 원경신1
class 피그밍그부족의제단원경신1(common.Trigger):
    def on_enter(self):
        self.set_quest_accept(questId=91000047)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.show_caption(type='VerticalCaption', title='$52020036_QD__MAIN__0$', desc='$52020036_QD__MAIN__1$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=7000, scale=2.5)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(pathIds=[3000,3001], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 피그밍그부족의제단원경신2(self.ctx)


# 피그밍그 부족의 제단 원경신2
class 피그밍그부족의제단원경신2(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[3013,3014], returnView=False)
        self.set_scene_skip(state=콘대르소환, action='nextState')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 전투상황비추기(self.ctx)


class 전투상황비추기(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.select_camera(triggerId=3003, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 유저발록보이게위치옮김(self.ctx)


class 유저발록보이게위치옮김(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52020036, portalId=4)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 오프닝크림슨발록비추기(self.ctx)


class 오프닝크림슨발록비추기(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=3015, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 크림슨발록오프닝대사(self.ctx)


class 크림슨발록오프닝대사(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003781, msg='$52020036_QD__MAIN__2$', duration=3000, align='left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 콘대르등장카메라(self.ctx)


# 콘대르 등장
class 콘대르등장카메라(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=3002, enable=True)
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=0):
            return 콘대르소환(self.ctx)


class 콘대르소환(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52020036, portalId=1)
        self.create_monster(spawnIds=[100], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=0):
            return 유저를경로이동시킨다(self.ctx)


class 유저를경로이동시킨다(common.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='User_PatrolData_0')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 콘대르등장대사(self.ctx)


class 콘대르등장대사(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003776, illustId='Conder_normal', msg='$52020036_QD__MAIN__3$', duration=3000, align='left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 콘대르이동(self.ctx)


class 콘대르이동(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=100, patrolName='Conder_Spawn_Opening_PatrolData_1')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 오프닝연출끝(self.ctx)


class 오프닝연출끝(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.destroy_monster(spawnIds=[100])
        self.create_monster(spawnIds=[101], animationEffect=False) # 콘대르
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 구르는천둥대사(self.ctx)


# 구르는천둥대사1
class 구르는천둥대사(common.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=11000009, illust='RollingThunder_normal', duration=7000, script='$52020036_QD__main__12$', voice='ko/Npc/00002150')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return 콘대르전투참여대사(self.ctx)


# 콘대르전투참여대사
class 콘대르전투참여대사(common.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=11003776, illust='Conder_normal', duration=8300, script='$52020036_QD__main__13$', voice='ko/Npc/00002147')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8300):
            return 침략자소탕퀘스트완료체크(self.ctx)


class 침략자소탕퀘스트완료체크(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[91000047], questStates=[2]):
            return 침략자소탕퀘스트완료(self.ctx)


class 침략자소탕퀘스트완료(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_quest_complete(questId=91000047)
        self.set_quest_accept(questId=91000048)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(pathIds=[3005,3006], returnView=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 티나비추기(self.ctx)


# 티나비추기
class 티나비추기(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera(triggerId=3004, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=0):
            return 티나대사1(self.ctx)


class 티나대사1(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.add_cinematic_talk(npcId=11000136, illustId='Tina_normal', msg='$52020036_QD__MAIN__4$', duration=5000, align='Right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 몬스터한번더스폰(self.ctx)


class 몬스터한번더스폰(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[20001], animationEffect=False)
        self.create_monster(spawnIds=[10000], animationEffect=False)
        self.create_monster(spawnIds=[10001], animationEffect=False)
        self.create_monster(spawnIds=[10002], animationEffect=False)
        self.create_monster(spawnIds=[10003], animationEffect=False)
        self.create_monster(spawnIds=[10004], animationEffect=False)
        self.create_monster(spawnIds=[10005], animationEffect=False)
        self.create_monster(spawnIds=[10006], animationEffect=False)
        self.create_monster(spawnIds=[10007], animationEffect=False)
        self.create_monster(spawnIds=[10008], animationEffect=False)
        self.create_monster(spawnIds=[10010], animationEffect=False)
        self.create_monster(spawnIds=[10012], animationEffect=False)
        self.create_monster(spawnIds=[10014], animationEffect=False)
        self.create_monster(spawnIds=[10016], animationEffect=False)
        self.create_monster(spawnIds=[10016], animationEffect=False)
        self.create_monster(spawnIds=[10017], animationEffect=False)
        self.create_monster(spawnIds=[10018], animationEffect=False)
        self.create_monster(spawnIds=[10019], animationEffect=False)
        self.create_monster(spawnIds=[10020], animationEffect=False)
        self.create_monster(spawnIds=[10021], animationEffect=False)
        self.create_monster(spawnIds=[10022], animationEffect=False)
        self.create_monster(spawnIds=[10023], animationEffect=False)
        self.create_monster(spawnIds=[10024], animationEffect=False)
        self.create_monster(spawnIds=[10025], animationEffect=False)
        self.create_monster(spawnIds=[10026], animationEffect=False)
        self.create_monster(spawnIds=[10027], animationEffect=False)
        self.create_monster(spawnIds=[10028], animationEffect=False)
        self.create_monster(spawnIds=[10029], animationEffect=False)
        self.create_monster(spawnIds=[10030], animationEffect=False)
        self.create_monster(spawnIds=[10031], animationEffect=False)
        self.create_monster(spawnIds=[10032], animationEffect=False)
        self.create_monster(spawnIds=[10033], animationEffect=False)
        self.create_monster(spawnIds=[10034], animationEffect=False)
        self.create_monster(spawnIds=[10035], animationEffect=False)
        self.create_monster(spawnIds=[10036], animationEffect=False)
        self.create_monster(spawnIds=[10037], animationEffect=False)
        self.create_monster(spawnIds=[10038], animationEffect=False)
        self.create_monster(spawnIds=[10039], animationEffect=False)
        self.create_monster(spawnIds=[10040], animationEffect=False)
        self.create_monster(spawnIds=[10041], animationEffect=False)
        self.create_monster(spawnIds=[10042], animationEffect=False)
        self.create_monster(spawnIds=[10043], animationEffect=False)
        self.create_monster(spawnIds=[10044], animationEffect=False)
        self.create_monster(spawnIds=[10045], animationEffect=False)
        self.create_monster(spawnIds=[10046], animationEffect=False)
        self.create_monster(spawnIds=[10047], animationEffect=False)
        self.create_monster(spawnIds=[10048], animationEffect=False)
        self.create_monster(spawnIds=[10049], animationEffect=False)
        self.create_monster(spawnIds=[10050], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=0):
            return 부상자구하기시작(self.ctx)


class 부상자구하기시작(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 부상자구출퀘스트완료체크(self.ctx)


class 부상자구출퀘스트완료체크(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[91000048], questStates=[2]):
            return 부상자옮기기대사(self.ctx)


# 티나 팝업 대사 UI_1
class 부상자옮기기대사(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_quest_complete(questId=91000048)
        self.set_quest_accept(questId=91000049)
        self.side_npc_talk(npcId=11003780, illust='WhitewolfGirl_normal', duration=5648, script='$52020036_QD__main__14$', voice='ko/Npc/00002151')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5648):
            return 네이린팝업1(self.ctx)


# 네이린팝업1
class 네이린팝업1(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.side_npc_talk(npcId=11003536, illust='Neirin_normal', duration=7000, script='$52020036_QD__main__15$', voice='ko/Npc/00002126')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return 네이린팝업2(self.ctx)


class 네이린팝업2(common.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=11003536, illust='Neirin_smile', duration=7000, script='$52020036_QD__main__16$', voice='ko/Npc/00002127')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return 네이린팝업3(self.ctx)


class 네이린팝업3(common.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=11003536, illust='Neirin_normal', duration=7000, script='$52020036_QD__main__17$', voice='ko/Npc/00002128')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return 공중지원퀘스트자동수락(self.ctx)


class 공중지원퀘스트자동수락(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000043], state=1)
        self.destroy_monster(spawnIds=[901])
        self.destroy_monster(spawnIds=[101])
        self.destroy_monster(spawnIds=[201])
        self.destroy_monster(spawnIds=[-1])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=0):
            return 콘대르구르는천둥P3스폰(self.ctx)


class 콘대르구르는천둥P3스폰(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[902], animationEffect=False)
        self.create_monster(spawnIds=[8000], animationEffect=False)
        self.create_monster(spawnIds=[8001], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 석궁비추기(self.ctx)


# 석궁비추기
class 석궁비추기(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=3007, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 석궁비추기끝(self.ctx)


class 석궁비추기끝(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=0):
            return 콘대르팝업1(self.ctx)


class 콘대르팝업1(common.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=11003776, illust='Conder_normal', duration=7000, script='$52020036_QD__main__18$', voice='ko/Npc/00002148')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return 네이린팝업4(self.ctx)


class 네이린팝업4(common.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=11003536, illust='Neirin_shy', duration=7000, script='$52020036_QD__main__19$', voice='ko/Npc/00002129')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return 콘대르팝업2(self.ctx)


class 콘대르팝업2(common.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=11003776, illust='Conder_normal', duration=6000, script='$52020036_QD__main__20$', voice='ko/Npc/00002149')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return 네이린웨이브경고팝업(self.ctx)


class 네이린웨이브경고팝업(common.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=11003536, illust='Neirin_surprise', duration=1000, script='$52020036_QD__main__21$', voice='ko/Npc/00002130')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1340):
            return 네이린웨이브경고팝업1(self.ctx)


class 네이린웨이브경고팝업1(common.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=11003536, illust='Neirin_surprise', duration=7000, script='$52020036_QD__main__22$', voice='ko/Npc/00002131')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7012):
            return 네이린웨이브경고팝업2(self.ctx)


class 네이린웨이브경고팝업2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 웨이브스폰1(self.ctx)


class 웨이브스폰1(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[10051], animationEffect=False)
        self.create_monster(spawnIds=[10059], animationEffect=False)
        self.create_monster(spawnIds=[10067], animationEffect=False)
        self.create_monster(spawnIds=[10075], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 웨이브스폰1패트롤(self.ctx)


class 웨이브스폰1패트롤(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=10051, patrolName='WavePatrolDataEast')
        self.move_npc(spawnId=10059, patrolName='WavePatrolDataEast')
        self.move_npc(spawnId=10067, patrolName='WavePatrolDataWest')
        self.move_npc(spawnId=10075, patrolName='WavePatrolDataSouth')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 웨이브스폰2(self.ctx)


class 웨이브스폰2(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[10055], animationEffect=False)
        self.create_monster(spawnIds=[10063], animationEffect=False)
        self.create_monster(spawnIds=[10071], animationEffect=False)
        self.create_monster(spawnIds=[10079], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 웨이브스폰3(self.ctx)


class 웨이브스폰3(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[10052], animationEffect=False)
        self.create_monster(spawnIds=[10060], animationEffect=False)
        self.create_monster(spawnIds=[10068], animationEffect=False)
        self.create_monster(spawnIds=[10076], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 웨이브스폰4(self.ctx)


class 웨이브스폰4(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[10056], animationEffect=False)
        self.create_monster(spawnIds=[10064], animationEffect=False)
        self.create_monster(spawnIds=[10072], animationEffect=False)
        self.create_monster(spawnIds=[10080], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 웨이브스폰5(self.ctx)


class 웨이브스폰5(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[10053], animationEffect=False)
        self.create_monster(spawnIds=[10061], animationEffect=False)
        self.create_monster(spawnIds=[10069], animationEffect=False)
        self.create_monster(spawnIds=[10078], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 웨이브스폰6(self.ctx)


class 웨이브스폰6(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[10054], animationEffect=False)
        self.create_monster(spawnIds=[10057], animationEffect=False)
        self.create_monster(spawnIds=[10065], animationEffect=False)
        self.create_monster(spawnIds=[10073], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 웨이브스폰7(self.ctx)


class 웨이브스폰7(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[10058], animationEffect=False)
        self.create_monster(spawnIds=[10062], animationEffect=False)
        self.create_monster(spawnIds=[10066], animationEffect=False)
        self.create_monster(spawnIds=[10070], animationEffect=False)
        self.create_monster(spawnIds=[10074], animationEffect=False)
        self.create_monster(spawnIds=[10077], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 차웨이브스폰1_2(self.ctx)


class 차웨이브스폰1_2(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[10051], animationEffect=False)
        self.create_monster(spawnIds=[10059], animationEffect=False)
        self.create_monster(spawnIds=[10067], animationEffect=False)
        self.create_monster(spawnIds=[10075], animationEffect=False)
        self.create_monster(spawnIds=[10079], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 차웨이브스폰2_2(self.ctx)


class 차웨이브스폰2_2(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[10052], animationEffect=False)
        self.create_monster(spawnIds=[10055], animationEffect=False)
        self.create_monster(spawnIds=[10060], animationEffect=False)
        self.create_monster(spawnIds=[10063], animationEffect=False)
        self.create_monster(spawnIds=[10071], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 차웨이브스폰3_2(self.ctx)


class 차웨이브스폰3_2(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[10056], animationEffect=False)
        self.create_monster(spawnIds=[10064], animationEffect=False)
        self.create_monster(spawnIds=[10068], animationEffect=False)
        self.create_monster(spawnIds=[10072], animationEffect=False)
        self.create_monster(spawnIds=[10076], animationEffect=False)
        self.create_monster(spawnIds=[10080], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 차웨이브스폰4_2(self.ctx)


class 차웨이브스폰4_2(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[10053], animationEffect=False)
        self.create_monster(spawnIds=[10057], animationEffect=False)
        self.create_monster(spawnIds=[10061], animationEffect=False)
        self.create_monster(spawnIds=[10065], animationEffect=False)
        self.create_monster(spawnIds=[10069], animationEffect=False)
        self.create_monster(spawnIds=[10073], animationEffect=False)
        self.create_monster(spawnIds=[10078], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 차웨이브스폰5_2(self.ctx)


class 차웨이브스폰5_2(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[10054], animationEffect=False)
        self.create_monster(spawnIds=[10058], animationEffect=False)
        self.create_monster(spawnIds=[10062], animationEffect=False)
        self.create_monster(spawnIds=[10066], animationEffect=False)
        self.create_monster(spawnIds=[10070], animationEffect=False)
        self.create_monster(spawnIds=[10074], animationEffect=False)
        self.create_monster(spawnIds=[10077], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=0):
            return 공중지원퀘스트완료체크(self.ctx)


class 공중지원퀘스트완료체크(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[91000049], questStates=[2]):
            return 공중지원퀘스트완료(self.ctx)


class 공중지원퀘스트완료(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000043], state=0)
        self.visible_my_pc(isVisible=False) # 캐릭터 숨김
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.destroy_monster(spawnIds=[-1])
        self.set_quest_complete(questId=91000049)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 엔딩크림슨발록보이는위치로유저이동(self.ctx)


class 엔딩크림슨발록보이는위치로유저이동(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52020036, portalId=4)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 엔딩크림슨발록비추기(self.ctx)


class 엔딩크림슨발록비추기(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=3015, enable=True)
        self.create_monster(spawnIds=[7000], animationEffect=False)
        self.create_monster(spawnIds=[7001], animationEffect=False)
        self.create_monster(spawnIds=[7002], animationEffect=False)
        self.create_monster(spawnIds=[7003], animationEffect=False)
        self.create_monster(spawnIds=[7004], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 크림슨발록엔딩닝대사(self.ctx)


class 크림슨발록엔딩닝대사(common.Trigger):
    def on_enter(self):
        self.remove_buff(boxId=9000, skillId=99910150)
        self.add_cinematic_talk(npcId=11003781, msg='$52020036_QD__MAIN__5$', duration=5000, align='left')
        self.set_npc_emotion_sequence(spawnId=7000, sequenceName='Attack_01_A', durationTick=1900)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 엔딩연출준비(self.ctx)


class 엔딩연출준비(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[7000])
        self.destroy_monster(spawnIds=[7001])
        self.destroy_monster(spawnIds=[7002])
        self.destroy_monster(spawnIds=[7003])
        self.destroy_monster(spawnIds=[7004])
        self.set_mesh(triggerIds=[9999], visible=False, scale=0) # 발록 함선 지우기

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=0):
            return 엔딩연출1(self.ctx)


class 엔딩연출1(common.Trigger):
    def on_enter(self):
        self.visible_my_pc(isVisible=True) # 캐릭터 보임
        self.create_monster(spawnIds=[3500], animationEffect=False)
        self.create_monster(spawnIds=[4500], animationEffect=False)
        self.create_monster(spawnIds=[5500], animationEffect=False)
        self.set_scene_skip(state=전부지우기, action='nextState')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=0):
            return 엔딩카메라1(self.ctx)


class 엔딩카메라1(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=3008, enable=True)
        self.move_user(mapId=52020036, portalId=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=0):
            return 콘대르엔딩대사1(self.ctx)


class 콘대르엔딩대사1(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003776, illustId='Conder_normal', msg='$52020036_QD__MAIN__6$', duration=4000, align='left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 구르는천둥엔딩대사1(self.ctx)


class 구르는천둥엔딩대사1(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003779, illustId='LoudFist_normal', msg='$52020036_QD__MAIN__7$', duration=4000, align='left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 트리스탄생성1(self.ctx)


class 트리스탄생성1(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[6500], animationEffect=False)
        self.move_user(mapId=52020036, portalId=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=0):
            return 트리스탄등장카메라1(self.ctx)


class 트리스탄등장카메라1(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=3009, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 트리스탄대사1(self.ctx)


class 트리스탄대사1(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11001975, illustId='Tristan_normal', msg='$52020036_QD__MAIN__8$', duration=3000, align='left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 콘대르엔딩카메라1(self.ctx)


class 콘대르엔딩카메라1(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=3010, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 콘대르엔딩카메라2(self.ctx)


class 콘대르엔딩카메라2(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=3010, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=0):
            return 콘대르엔딩대사2(self.ctx)


class 콘대르엔딩대사2(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003776, illustId='Conder_normal', msg='$52020036_QD__MAIN__9$', duration=1000, align='left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 콘대르엔딩카메라3(self.ctx)


class 콘대르엔딩카메라3(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=3012, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=0):
            return 콘대르엔딩대사3(self.ctx)


class 콘대르엔딩대사3(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003776, illustId='Conder_normal', msg='$52020036_QD__MAIN__10$', duration=2000, align='left')
        self.set_npc_emotion_sequence(spawnId=3500, sequenceName='Bore_A', durationTick=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 트리스탄엔딩카메라2(self.ctx)


class 트리스탄엔딩카메라2(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=3009, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 트리스탄엔딩대사2(self.ctx)


class 트리스탄엔딩대사2(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003777, illustId='Tristan_normal', msg='$52020036_QD__MAIN__11$', duration=4000, align='left')
        self.set_npc_emotion_sequence(spawnId=6500, sequenceName='Talk_A', durationTick=7000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 엔딩카메라2(self.ctx)


class 엔딩카메라2(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[3007,3016], returnView=False)
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 전부지우기(self.ctx)


class 전부지우기(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[-1])
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)
        self.move_user(mapId=52010052, portalId=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=0):
            return None # Missing State: 


initial_state = 딜레이
