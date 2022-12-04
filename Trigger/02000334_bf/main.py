""" trigger/02000334_bf/main.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


# 플레이어 감지
class main(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=12, visible=False, enable=False, minimapVisible=False)
        self.set_interact_object(triggerIds=[13000012], state=2) # 보상 상태 (없음)
        self.set_effect(triggerIds=[98001], visible=False)
        self.set_effect(triggerIds=[98002], visible=False)
        self.set_effect(triggerIds=[98003], visible=False)
        self.set_effect(triggerIds=[98004], visible=False)
        self.set_effect(triggerIds=[98005], visible=False)
        self.set_effect(triggerIds=[98006], visible=False)
        self.set_effect(triggerIds=[90021], visible=False)
        self.set_effect(triggerIds=[90022], visible=False)
        self.set_effect(triggerIds=[98031], visible=True)
        self.select_camera(triggerId=8000, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=90001, boxId=1):
            return CheckUserCount(self.ctx)


# 플레이어 감지하면 1초 대기
class DungeonStart(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=10, visible=False, enable=False, minimapVisible=False) # 보상으로 연결되는 포탈 제어 (끔)
        self.create_monster(spawnIds=[199], animationEffect=True) # 퀘스트 주는 NPC가 앞으로 걸어나옴
        self.select_camera(triggerId=8001, enable=True) # 연출 카메라
        self.set_timer(timerId='1', seconds=1)
        self.create_monster(spawnIds=[401,402,403,404,405,406], animationEffect=True) # 성벽 지키는 NPC 소환
        self.create_monster(spawnIds=[801,802,803,804,805,806,807,808,809], animationEffect=True) # 성벽 지키는 NPC 소환
        self.set_mesh(triggerIds=[6000,6001,6002,6003,6004,6005,6006,6007,6008,6009,6010,6011,6012,6013,6014,6015,6016], visible=True) # 가림막

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 시작_02(self.ctx)


class 시작_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_timer(timerId='5', seconds=5, interval=0)
        self.set_skip(state=시작_03)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 시작_03(self.ctx)


class 시작_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3, interval=0)
        self.set_conversation(type=2, spawnId=11000015, script='$02000334_BF__MAIN__1$', arg4=3) # 오스칼 대사
        self.create_monster(spawnIds=[190], animationEffect=False) # 보스 등장
        self.set_skip(state=단계_시작1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 단계_시작1(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)
        self.set_cinematic_ui(type=4)


# 해당 단계에서 플레이어의 위치를 조명해줌
# 1 단계 시작 카운트
class 단계_시작1(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8013,8015], returnView=False)
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 단계_시작02_1(self.ctx)


class 단계_시작02_1(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_conversation(type=2, spawnId=24001205, script='$02000334_BF__MAIN__6$', arg4=3) # 보스 대사 : 성벽따위 금방 부숴주지
        self.set_timer(timerId='3', seconds=3)
        self.set_skip(state=단계_시작03_1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 단계_시작03_1(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)


class 단계_시작03_1(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=0, arg2='1,4')
        self.show_count_ui(text='$02000334_BF__MAIN__2$', stage=1, count=5)
        self.set_timer(timerId='4', seconds=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='4'):
            return 단계_시작04_1(self.ctx)


class 단계_시작04_1(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=199, script='$02000334_BF__MAIN__3$', arg4=3) # 오스칼 말풍선 대사
        self.create_monster(spawnIds=[201,203], animationEffect=True) # 성벽 지키는 NPC 리필
        self.set_conversation(type=1, spawnId=203, script='$02000334_BF__MAIN__4$', arg4=3) # 병사 말풍선 대사
        self.set_conversation(type=1, spawnId=201, script='$02000334_BF__MAIN__5$', arg4=3) # 병사 말풍선 대사
        self.set_timer(timerId='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return 단계_타이머1(self.ctx)
        if self.monster_dead(boxIds=[999]):
            return 게임오버(self.ctx)


# 1 단계 시작
class 단계_타이머1(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[90022], visible=True) # 점프 뛰는 소리 ON
        self.create_monster(spawnIds=[160], animationEffect=False) # 웨이브 가이드
        self.create_monster(spawnIds=[150], animationEffect=False)
        self.set_timer(timerId='60', seconds=60, interval=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='60'):
            return 단계_준비2(self.ctx)
        if self.monster_dead(boxIds=[999]):
            return 게임오버(self.ctx)
        if self.user_detected(boxIds=[99999]):
            return 클리어(self.ctx)

    def on_exit(self):
        self.set_effect(triggerIds=[90022], visible=False) # 점프 뛰는 소리 OFF


class 단계_준비2(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.destroy_monster(spawnIds=[101,102,103,104,105,106,107,108,111,112,113,114,115,131,132,133,134,135,150,151,152,991,992,993,994,995,996,997,998])
        self.set_timer(timerId='3', seconds=3, interval=0)
        self.set_conversation(type=2, spawnId=11000015, script='$02000334_BF__MAIN__7$', arg4=3) # 오스칼 대사
        self.set_skip(state=단계_시작2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 단계_시작2(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)


# 2 단계 시작 카운트
class 단계_시작2(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[204,205], animationEffect=True) # 성벽 지키는 NPC 리필
        self.set_conversation(type=1, spawnId=199, script='$02000334_BF__MAIN__8$', arg4=3) # 오스칼 대사
        self.set_mesh(triggerIds=[6000,6001,6002,6003,6004,6005,6006,6007,6008,6009,6010,6011,6012,6013,6014,6015,6016], visible=False, delay=250, scale=1) # 가림막 해제
        self.set_event_ui(type=0, arg2='2,4')
        self.show_count_ui(text='$02000334_BF__MAIN__2$', stage=2, count=5)
        self.set_timer(timerId='6', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='6'):
            return 단계_타이머2(self.ctx)
        if self.monster_dead(boxIds=[999]):
            return 게임오버(self.ctx)


# 2 단계 시작
class 단계_타이머2(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[90022], visible=True) # 점프 뛰는 소리 ON
        self.select_camera(triggerId=8000, enable=True) # 사이드뷰 카메라
        self.create_monster(spawnIds=[150,151], animationEffect=False) # 1,2 차 웨이브 몬스터 작동 장치
        self.set_timer(timerId='60', seconds=60, interval=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='60'):
            return 단계_준비3(self.ctx)
        if self.monster_dead(boxIds=[999]):
            return 게임오버(self.ctx)

    def on_exit(self):
        self.set_effect(triggerIds=[90022], visible=False) # 점프 뛰는 소리 OFF


class 단계_준비3(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.destroy_monster(spawnIds=[101,102,103,104,105,106,107,108,111,112,113,114,115,131,132,133,134,135,150,151,991,992,993,994,995,996,997,998])
        self.set_timer(timerId='3', seconds=3, interval=0)
        self.set_conversation(type=2, spawnId=11000015, script='$02000334_BF__MAIN__9$', arg4=3) # 오스칼 대사
        self.set_skip(state=단계_시작3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 단계_시작3(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)


# 3 단계 시작 카운트
class 단계_시작3(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[206,207], animationEffect=True) # 성벽 지키는 NPC 리필
        self.set_event_ui(type=0, arg2='3,4')
        self.show_count_ui(text='$02000334_BF__MAIN__2$', stage=3, count=5)
        self.set_timer(timerId='6', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='6'):
            return 단계_타이머3(self.ctx)
        if self.monster_dead(boxIds=[999]):
            return 게임오버(self.ctx)


# 3 단계 시작
class 단계_타이머3(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[90022], visible=True) # 점프 뛰는 소리 ON
        self.create_monster(spawnIds=[150,151,152], animationEffect=False) # 1,2,3차 웨이브 몬스터 작동 장치
        self.set_timer(timerId='60', seconds=60, interval=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='60'):
            return 단계_준비_01_4(self.ctx)
        if self.monster_dead(boxIds=[999]):
            return 게임오버(self.ctx)

    def on_exit(self):
        self.set_effect(triggerIds=[90022], visible=False) # 점프 뛰는 소리 OFF


class 단계_준비_01_4(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.destroy_monster(spawnIds=[101,102,103,104,105,106,107,108,111,112,113,114,115,131,132,133,134,135,150,151,152,991,992,993,994,995,996,997,998])
        self.set_timer(timerId='3', seconds=3, interval=0)
        self.set_conversation(type=2, spawnId=11000015, script='$02000334_BF__MAIN__10$', arg4=3) # 오스칼 대사

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 단계_준비_02_4(self.ctx)


class 단계_준비_02_4(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3, interval=0)
        self.set_conversation(type=2, spawnId=24001205, script='$02000334_BF__MAIN__11$', arg4=3) # 보스 대사

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 단계_시작4(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)


# 4 단계 시작 카운트
class 단계_시작4(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101,102,103,104,105,106,107,108,111,112,113,114,115,131,132,133,134,135,150,151,152,991,992,993,994,995,996,997,998])
        self.move_npc(spawnId=190, patrolName='MS2PatrolData_2999') # 보스 등장
        self.set_event_ui(type=0, arg2='4,4')
        self.show_count_ui(text='$02000334_BF__MAIN__2$', stage=4, count=5)
        self.set_timer(timerId='6', seconds=6)
        self.set_conversation(type=1, spawnId=190, script='$02000334_BF__WAVE__2$', arg4=3) # 보스 대사

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='6'):
            return 단계_타이머4(self.ctx)
        if self.monster_dead(boxIds=[999]):
            return 게임오버(self.ctx)

    def on_exit(self):
        self.create_monster(spawnIds=[150,151], animationEffect=False) # 1,2차 웨이브 몬스터 작동 장치


# 4 단계 시작
class 단계_타이머4(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[90022], visible=True) # 점프 뛰는 소리 ON
        self.set_timer(timerId='150', seconds=150, interval=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[999]):
            return 게임오버(self.ctx)
        if self.time_expired(timerId='150'):
            return 게임오버(self.ctx)
        if self.monster_dead(boxIds=[190]):
            return 클리어(self.ctx)

    def on_exit(self):
        self.set_effect(triggerIds=[90022], visible=False) # 점프 뛰는 소리 OFF


# 게임 오버 스테이트
class 게임오버(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101,102,103,104,105,106,107,108,111,112,113,114,115,131,132,133,134,135,150,151,152,190,991,992,993,994,995,996,997,998])
        self.set_event_ui(type=5, arg3='3000')
        self.set_event_ui(type=0, arg2='0,0')
        self.set_timer(timerId='3', seconds=3, interval=0)
        self.set_effect(triggerIds=[98031], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 게임오버_이벤트(self.ctx)


class 게임오버_이벤트(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.destroy_monster(spawnIds=[101,102,103,104,105,106,107,108,111,112,113,114,115,131,132,133,134,135,150,151,152,190,991,992,993,994,995,996,997,998])
        self.set_timer(timerId='3', seconds=3, interval=0)
        self.set_conversation(type=2, spawnId=24001205, script='$02000334_BF__MAIN__13$', arg4=3) # 보스 대사
        self.set_skip(state=게임오버_강퇴)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 게임오버_강퇴(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)


class 게임오버_강퇴(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=5, interval=1)
        self.set_event_ui(type=1, arg2='$02000334_BF__MAIN__14$', arg3='5000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 강퇴(self.ctx)


class 강퇴(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=0, portalId=0, boxId=90001)


# 클리어
class 클리어(trigger_api.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=90001, type='trigger', achieve='TaboKill') # 돼지왕 타보 죽임 처리
        self.destroy_monster(spawnIds=[101,102,103,104,105,106,107,108,111,112,113,114,115,131,132,133,134,135,150,151,152,991,992,993,994,995,996,997,998]) # 폭죽 터뜨림
        self.set_effect(triggerIds=[98002], visible=True)
        self.set_effect(triggerIds=[98003], visible=True)
        self.set_effect(triggerIds=[98004], visible=True)
        self.set_effect(triggerIds=[98005], visible=True)
        self.set_timer(timerId='3', seconds=3)
        self.set_effect(triggerIds=[98031], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 클리어_이벤트(self.ctx)

    def on_exit(self):
        self.set_effect(triggerIds=[98002], visible=False)
        self.set_effect(triggerIds=[98003], visible=False)
        self.set_effect(triggerIds=[98004], visible=False)
        self.set_effect(triggerIds=[98005], visible=False)


class 클리어_이벤트(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101,102,103,104,105,106,107,108,111,112,113,114,115,131,132,133,134,135,150,151,152,991,992,993,994,995,996,997,998]) # 몬스터 정리
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_conversation(type=2, spawnId=11000015, script='$02000334_BF__MAIN__16$', arg4=3) # 오스칼 대사
        self.set_mesh(triggerIds=[6000,6001,6002,6003,6004,6005,6006,6007,6008,6009,6010,6011,6012,6013,6014,6015,6016], visible=False, delay=250, scale=1) # 가림막 해제
        self.set_skip(state=클리어_보상)
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 클리어_보상(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)


class 클리어_보상(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=10, visible=True, enable=True, minimapVisible=False)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=103, textId=40009) # 포탈로 이동하세요
        self.move_npc(spawnId=199, patrolName='MS2PatrolData_2015') # 오스칼 장소 이동
        self.set_timer(timerId='10', seconds=10, interval=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[90099]):
            return 클리어_보상_02(self.ctx)
        if self.time_expired(timerId='10'):
            return 클리어_보상_02(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=103)


class 클리어_보상_02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=8003, enable=True) # 연출 카메라
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_conversation(type=2, spawnId=11000015, script='$02000334_BF__MAIN__18$', arg4=3) # 오스칼 대사
        self.set_timer(timerId='3', seconds=3)
        # <action name="오브젝트반응설정한다" arg1="13000012" arg2="1" />

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 클리어_보상_03(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)


class 클리어_보상_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=199, script='$02000334_BF__MAIN__19$', arg4=5) # 오스칼 대사

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            self.dungeon_clear()
            self.set_portal(portalId=12, visible=True, enable=True, minimapVisible=True)
            return 종료(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=103)


class 종료(trigger_api.Trigger):
    pass


initial_state = main
