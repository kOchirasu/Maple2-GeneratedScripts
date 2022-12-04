""" trigger/52000016_qd/tutorial04.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[10000], visible=True) # 입구 길막기
        self.set_agent(triggerIds=[10001], visible=True) # 입구 길막기
        self.set_agent(triggerIds=[10002], visible=True) # 입구 길막기
        self.set_agent(triggerIds=[10003], visible=True) # 입구 길막기
        self.set_agent(triggerIds=[10004], visible=True) # 입구 길막기
        self.set_agent(triggerIds=[10005], visible=True) # 입구 길막기
        self.set_agent(triggerIds=[10010], visible=True) # 입구 길막기
        self.set_agent(triggerIds=[10006], visible=True) # 다리 길막기
        self.set_agent(triggerIds=[10007], visible=True) # 다리 길막기
        self.set_agent(triggerIds=[10008], visible=True) # 다리 길막기
        self.set_agent(triggerIds=[10009], visible=True) # 다리 길막기
        self.set_effect(triggerIds=[6000], visible=False) # 가이드 서머리 알림 사운드
        self.set_effect(triggerIds=[7000], visible=False) # 먼지
        self.set_effect(triggerIds=[7001], visible=False) # 먼지
        self.set_effect(triggerIds=[7002], visible=False) # 먼지
        self.set_effect(triggerIds=[7003], visible=False) # 먼지
        self.set_effect(triggerIds=[7004], visible=False) # 먼지
        self.set_effect(triggerIds=[7005], visible=False) # 먼지
        self.set_effect(triggerIds=[7006], visible=False) # 먼지
        self.set_effect(triggerIds=[7007], visible=False) # 먼지
        self.set_effect(triggerIds=[7010], visible=False) # 동굴 입구 흔들림
        self.set_effect(triggerIds=[7020], visible=False) # 동굴 입구 무너지는 소리
        self.set_effect(triggerIds=[7011], visible=False) # 다리 생길 때 흔들림
        self.set_effect(triggerIds=[7021], visible=False) # 다리 나타날 때 효과음
        self.set_effect(triggerIds=[7030], visible=False) # 레버 장치에서 들리는 소리
        self.set_effect(triggerIds=[7040], visible=False) # 전투 연출에서 룬 쉴드 이펙트 소리
        self.set_effect(triggerIds=[7050], visible=False) # 전투 연출에서 공격 스킬 이펙트 소리 NEW
        self.set_skill(triggerIds=[910], enable=False) # 입구 큐브 부수기 스킬
        self.set_skill(triggerIds=[911], enable=False) # 입구 큐브 부수기 스킬
        self.set_skill(triggerIds=[912], enable=False) # 입구 큐브 부수기 스킬
        self.set_skill(triggerIds=[913], enable=False) # 입구 큐브 부수기 스킬
        self.set_skill(triggerIds=[914], enable=False) # 입구 큐브 부수기 스킬
        self.set_mesh(triggerIds=[2000], visible=True, arg3=0, delay=0, scale=0) # PCProtect barrier ON
        self.set_mesh(triggerIds=[3000], visible=True, arg3=0, delay=0, scale=0) # invisible barrier ON
        self.set_mesh(triggerIds=[3001], visible=True, arg3=0, delay=0, scale=0) # bridge barrier ON
        self.set_mesh(triggerIds=[4000,4001,4002,4003,4004,4005,4006,4007,4008,4009,4010,4011,4012,4013,4014,4015], visible=False, arg3=0, delay=0, scale=0) # Rock  Visible OFF
        self.set_mesh(triggerIds=[4020,4021,4022,4023,4024,4025,4026,4027], visible=False, arg3=0, delay=0, scale=0) # Bridge  Visible OFF
        self.set_interact_object(triggerIds=[10000825], state=0) # 기관 작동 레버
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_effect(triggerIds=[8200], visible=False) # 이슈라 플레임 쉴드 이펙트
        self.set_effect(triggerIds=[8300], visible=False) # 홀슈타트 아이스 쉴드 이펙트
        self.set_effect(triggerIds=[8201], visible=False) # 이슈라 플레임 임팩트 이펙트
        self.set_effect(triggerIds=[8301], visible=False) # 홀슈타트 아이스 임팩트 이펙트
        self.set_effect(triggerIds=[8202], visible=False) # 이슈라 플레임 그라운드 이펙트
        self.set_effect(triggerIds=[8302], visible=False) # 홀슈타트 아이스 그라운드 이펙트
        self.set_effect(triggerIds=[8203], visible=False) # 이슈라 플레임 인피니티 이펙트
        self.set_effect(triggerIds=[8303], visible=False) # 홀슈타트 아이스 인피니티 이펙트
        self.set_effect(triggerIds=[8000], visible=False) # 싸울 때 흔들림
        self.set_effect(triggerIds=[6100], visible=False) # 척후병 시네마틱 음성 01 사운드
        self.set_effect(triggerIds=[6101], visible=False) # 척후병 시네마틱 음성 02 사운드
        self.set_effect(triggerIds=[6102], visible=False) # 척후병 시네마틱 음성 03 사운드
        self.set_effect(triggerIds=[6103], visible=False) # 척후병 시네마틱 음성 04 사운드
        self.set_effect(triggerIds=[6104], visible=False) # 척후병 시네마틱 음성 05 사운드
        self.set_effect(triggerIds=[6105], visible=False) # 척후병 시네마틱 음성 06 사운드
        self.set_effect(triggerIds=[6106], visible=False) # 척후병 시네마틱 음성 06 사운드
        self.set_effect(triggerIds=[6200], visible=False) # 이슈라 시네마틱 음성 01 사운드
        self.set_effect(triggerIds=[6201], visible=False) # 이슈라 시네마틱 음성 02 사운드
        self.set_effect(triggerIds=[6202], visible=False) # 이슈라 시네마틱 음성 03 사운드
        self.set_effect(triggerIds=[6203], visible=False) # 이슈라 시네마틱 음성 04 사운드
        self.set_effect(triggerIds=[6210], visible=False) # 홀슈타트 시네마틱 음성 01 사운드
        self.set_effect(triggerIds=[6211], visible=False) # 홀슈타트 시네마틱 음성 02 사운드
        self.set_effect(triggerIds=[6212], visible=False) # 홀슈타트 시네마틱 음성 03 사운드
        self.set_effect(triggerIds=[6300], visible=False) # 렌듀비앙 시네마틱 음성 01 사운드
        self.set_effect(triggerIds=[6301], visible=False) # 렌듀비앙 시네마틱 음성 02 사운드
        self.set_effect(triggerIds=[6302], visible=False) # 렌듀비앙 시네마틱 음성 03 사운드
        self.set_effect(triggerIds=[6400], visible=False) # 이슈라 시네마틱 음성 05 사운드
        self.set_effect(triggerIds=[6401], visible=False) # 이슈라 시네마틱 음성 06 사운드
        self.set_effect(triggerIds=[6402], visible=False) # 이슈라 시네마틱 음성 07 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[90000417], questStates=[1]):
            return 딜레이01(self.ctx)


class 딜레이01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_random_mesh(triggerIds=[4000,4001,4002,4003,4004,4005,4006,4007,4008,4009,4010,4011,4012,4013,4014,4015], visible=True, meshCount=16, arg4=50, delay=80) # Rock Visible  ON

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 막힌길발견01(self.ctx)


class 막힌길발견01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=601, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 딜레이02(self.ctx)


class 딜레이02(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[910], enable=True) # 입구 큐브 부수기 스킬
        self.set_skill(triggerIds=[911], enable=True) # 입구 큐브 부수기 스킬
        self.set_skill(triggerIds=[912], enable=True) # 입구 큐브 부수기 스킬
        self.set_skill(triggerIds=[913], enable=True) # 입구 큐브 부수기 스킬
        self.set_skill(triggerIds=[914], enable=True) # 입구 큐브 부수기 스킬
        self.set_effect(triggerIds=[7010], visible=True) # 동굴 입구 흔들림
        self.set_effect(triggerIds=[7020], visible=True) # 동굴 입구 무너지는 소리

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 막힌길발견02(self.ctx)


class 막힌길발견02(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=4)
        self.set_effect(triggerIds=[7000], visible=True) # 먼지
        self.set_effect(triggerIds=[7001], visible=True) # 먼지
        self.set_effect(triggerIds=[7002], visible=True) # 먼지
        self.set_effect(triggerIds=[7003], visible=True) # 먼지
        self.set_effect(triggerIds=[7004], visible=True) # 먼지
        self.set_effect(triggerIds=[7005], visible=True) # 먼지
        self.set_effect(triggerIds=[7006], visible=True) # 먼지
        self.set_effect(triggerIds=[7007], visible=True) # 먼지

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return 척후병입장(self.ctx)

    def on_exit(self):
        self.set_mesh(triggerIds=[2000], visible=False, arg3=0, delay=0, scale=0) # PCProtect barrier ON


class 척후병입장(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3)
        self.create_monster(spawnIds=[101], animationEffect=True)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_1000')
        self.set_effect(triggerIds=[6100], visible=True) # 척후병 시네마틱 음성 01 사운드
        self.set_conversation(type=2, spawnId=11001249, script='$52000016_QD__TUTORIAL04__0$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 돌치우기안내01(self.ctx)


class 돌치우기안내01(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=3)
        self.set_effect(triggerIds=[6101], visible=True) # 척후병 시네마틱 음성 02 사운드
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_1001')
        self.set_conversation(type=2, spawnId=11001249, script='$52000016_QD__TUTORIAL04__1$', arg4=3)
        self.set_skip(state=돌치우기안내03)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 돌치우기안내03(self.ctx)

    def on_exit(self):
        self.remove_cinematic_talk()
        self.set_effect(triggerIds=[7010], visible=False) # 동굴 입구 흔들림
        self.set_effect(triggerIds=[7020], visible=False) # 동굴 입구 무너지는 소리
        self.set_skill(triggerIds=[910], enable=False) # 입구 큐브 부수기 스킬
        self.set_skill(triggerIds=[911], enable=False) # 입구 큐브 부수기 스킬
        self.set_skill(triggerIds=[912], enable=False) # 입구 큐브 부수기 스킬
        self.set_skill(triggerIds=[913], enable=False) # 입구 큐브 부수기 스킬
        self.set_skill(triggerIds=[914], enable=False) # 입구 큐브 부수기 스킬


class 돌치우기안내03(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=601, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 첫번째돌들기가이드01(self.ctx)


class 첫번째돌들기가이드01(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6000], visible=True) # 가이드 서머리 알림 사운드
        self.show_guide_summary(entityId=10014010, textId=10014010) # 가이드 : 스페이스 키를 눌러 바위덩이 들기

    def on_tick(self) -> trigger_api.Trigger:
        if not self.detect_liftable_object(boxIds=[9001], itemId=30000440):
            return 첫번째돌놓기01(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=10014010)


class 첫번째돌놓기01(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6000], visible=True) # 가이드 서머리 알림 사운드
        self.show_guide_summary(entityId=10014020, textId=10014020) # 가이드 : 스페이스 키를 눌러 눌러 바위덩이  내려놓기

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9011,9012], itemId=30000440):
            return 척후병이동01(self.ctx)


class 척후병이동01(trigger_api.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=10014020)
        self.create_monster(spawnIds=[901,902,903,904,905,906,907], animationEffect=False)
        self.set_random_mesh(triggerIds=[4000,4001,4002,4003,4004,4005,4006,4007,4008,4009,4010,4011,4012,4013,4014,4015], visible=False, meshCount=16, arg4=100, delay=80) # Rock Visible  OFF
        self.set_mesh(triggerIds=[3000], visible=False, arg3=0, delay=0, scale=0) # invisible barrier OFF
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_1002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9004, spawnIds=[101]):
            return 척후병이동02(self.ctx)


class 척후병이동02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=101, script='$52000016_QD__TUTORIAL04__2$', arg4=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9005, spawnIds=[101]):
            return 척후병전투시작01(self.ctx)


class 척후병전투시작01(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='9', seconds=1)
        self.set_agent(triggerIds=[10000], visible=False) # 입구 길막기
        self.set_agent(triggerIds=[10001], visible=False) # 입구 길막기
        self.set_agent(triggerIds=[10002], visible=False) # 입구 길막기
        self.set_agent(triggerIds=[10003], visible=False) # 입구 길막기
        self.set_agent(triggerIds=[10004], visible=False) # 입구 길막기
        self.set_agent(triggerIds=[10005], visible=False) # 입구 길막기
        self.set_agent(triggerIds=[10010], visible=False) # 입구 길막기

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='9'):
            return 전투중01(self.ctx)


class 전투중01(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='10', seconds=2)
        self.set_conversation(type=1, spawnId=101, script='$52000016_QD__TUTORIAL04__3$', arg4=2)
        self.set_effect(triggerIds=[6102], visible=True) # 척후병 시네마틱 음성 03 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='10'):
            return 전투중02(self.ctx)


class 전투중02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=101, script='$52000016_QD__TUTORIAL04__4$', arg4=2)
        self.set_effect(triggerIds=[6000], visible=True) # 가이드 서머리 알림 사운드
        self.show_guide_summary(entityId=10014030, textId=10014030) # 가이드 : 주변 몬스터 모두 처치하기

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[901,902,903,904,905,906,907]):
            return 전투종료01(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=10014030)


class 전투종료01(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='11', seconds=2)
        self.set_effect(triggerIds=[6103], visible=True) # 척후병 시네마틱 음성 04 사운드
        self.set_conversation(type=1, spawnId=101, script='$52000016_QD__TUTORIAL04__5$', arg4=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='11'):
            return 전투종료02(self.ctx)


class 전투종료02(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='12', seconds=2)
        self.set_conversation(type=1, spawnId=101, script='$52000016_QD__TUTORIAL04__6$', arg4=2)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_1003')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='12'):
            return 다리로이동01(self.ctx)


class 다리로이동01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9006, spawnIds=[101]):
            return 연출준비01(self.ctx)


class 연출준비01(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='13', seconds=3)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=602, enable=True)
        self.set_conversation(type=2, spawnId=11001249, script='$52000016_QD__TUTORIAL04__7$', arg4=3)
        self.set_effect(triggerIds=[6104], visible=True) # 척후병 시네마틱 음성 05 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='13'):
            return 연출준비02(self.ctx)


class 연출준비02(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='14', seconds=2)
        self.set_conversation(type=2, spawnId=11001249, script='$52000016_QD__TUTORIAL04__8$', arg4=2)
        self.set_effect(triggerIds=[6105], visible=True) # 척후병 시네마틱 음성 06 사운드
        self.create_monster(spawnIds=[201], animationEffect=True) # 연출용 이슈라
        self.create_monster(spawnIds=[301], animationEffect=True) # 연출용 홀슈타트
        self.create_monster(spawnIds=[210,211,212,213,214,215,216,217], animationEffect=True) # 연출용 아군8
        self.create_monster(spawnIds=[310,311,312,313], animationEffect=True) # 연출용 아군4

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='14'):
            return 연출시작01대기(self.ctx)


class 연출시작01대기(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 연출시작01(self.ctx)


class 연출시작01(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=연출종료01_skip, action='nextState')
        self.set_timer(timerId='16', seconds=1)
        self.select_camera_path(pathIds=[602,603], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='16'):
            return 대결연출01(self.ctx)


class 대결연출01(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='18', seconds=3)
        self.set_conversation(type=2, spawnId=11001244, script='$52000016_QD__TUTORIAL04__9$', arg4=3)
        self.set_effect(triggerIds=[6200], visible=True) # 이슈라 시네마틱 음성 01 사운드
        self.destroy_monster(spawnIds=[101]) # 전투용 척후병 삭제
        self.create_monster(spawnIds=[102], animationEffect=True) # 연출용 척후병 생성
        self.set_skip(state=대결연출02대기)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='18'):
            return 대결연출02대기(self.ctx)


class 대결연출02대기(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 대결연출02(self.ctx)


class 대결연출02(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='19', seconds=7)
        self.set_conversation(type=2, spawnId=11001231, script='$52000016_QD__TUTORIAL04__10$', arg4=6)
        self.set_effect(triggerIds=[6200], visible=False) # 이슈라 시네마틱 음성 01 사운드
        self.set_effect(triggerIds=[6210], visible=True) # 홀슈타트 시네마틱 음성 01 사운드
        self.set_skip(state=대결연출03대기)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='19'):
            return 대결연출03대기(self.ctx)


class 대결연출03대기(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 대결연출03(self.ctx)


class 대결연출03(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='20', seconds=5)
        self.set_conversation(type=2, spawnId=11001244, script='$52000016_QD__TUTORIAL04__11$', arg4=4)
        self.set_effect(triggerIds=[6210], visible=False) # 홀슈타트 시네마틱 음성 01 사운드
        self.set_effect(triggerIds=[6201], visible=True) # 이슈라 시네마틱 음성 02 사운드
        self.set_skip(state=대결연출04대기)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='20'):
            return 대결연출04대기(self.ctx)


class 대결연출04대기(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 대결연출04(self.ctx)


class 대결연출04(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='21', seconds=5)
        self.set_conversation(type=2, spawnId=11001231, script='$52000016_QD__TUTORIAL04__12$', arg4=5)
        self.set_effect(triggerIds=[6201], visible=False) # 이슈라 시네마틱 음성 02 사운드
        self.set_effect(triggerIds=[6211], visible=True) # 홀슈타트 시네마틱 음성 02 사운드
        self.set_skip(state=대결연출05대기)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='21'):
            return 대결연출05대기(self.ctx)


class 대결연출05대기(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 대결연출05(self.ctx)


class 대결연출05(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='22', seconds=4)
        self.set_conversation(type=2, spawnId=11001244, script='$52000016_QD__TUTORIAL04__13$', arg4=3)
        self.set_effect(triggerIds=[6211], visible=False) # 홀슈타트 시네마틱 음성 02 사운드
        self.set_effect(triggerIds=[6202], visible=True) # 이슈라 시네마틱 음성 03 사운드
        self.set_skip(state=대결연출06대기)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='22'):
            return 대결연출06대기(self.ctx)


class 대결연출06대기(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 대결연출06(self.ctx)


class 대결연출06(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='23', seconds=4)
        self.set_conversation(type=2, spawnId=11001231, script='$52000016_QD__TUTORIAL04__14$', arg4=3)
        self.set_effect(triggerIds=[6202], visible=False) # 이슈라 시네마틱 음성 03 사운드
        self.set_effect(triggerIds=[6212], visible=True) # 홀슈타트 시네마틱 음성 03 사운드
        self.set_skip(state=대결연출07대기)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='23'):
            return 대결연출07대기(self.ctx)


class 대결연출07대기(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 대결연출07(self.ctx)


class 대결연출07(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='24', seconds=1)
        self.select_camera(triggerId=606, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='24'):
            return 대결연출08(self.ctx)


class 대결연출08(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='25', seconds=1)
        self.set_effect(triggerIds=[7050], visible=True) # 전투 연출에서 공격 스킬 이펙트 소리 NEW
        self.set_conversation(type=2, spawnId=11001244, script='$52000016_QD__TUTORIAL04__15$', arg4=2)
        self.set_effect(triggerIds=[6212], visible=False) # 홀슈타트 시네마틱 음성 03 사운드
        self.set_effect(triggerIds=[6203], visible=True) # 이슈라 시네마틱 음성 04 사운드
        self.set_effect(triggerIds=[8200], visible=True) # 이슈라 플레임 쉴드 이펙트
        self.set_effect(triggerIds=[8300], visible=True) # 홀슈타트 아이스 쉴드 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='25'):
            return 이펙트연출01(self.ctx)


class 이펙트연출01(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='26', seconds=2)
        self.set_effect(triggerIds=[8201], visible=True) # 이슈라 플레임 임팩트 이펙트
        self.set_effect(triggerIds=[8301], visible=True) # 홀슈타트 아이스 임팩트 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='26'):
            return 이펙트연출02(self.ctx)

    def on_exit(self):
        self.set_effect(triggerIds=[8200], visible=False) # 이슈라 플레임 쉴드 이펙트
        self.set_effect(triggerIds=[8300], visible=False) # 홀슈타트 아이스 쉴드 이펙트


class 이펙트연출02(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='27', seconds=1)
        self.set_effect(triggerIds=[8201], visible=False) # 이슈라 플레임 임팩트 이펙트
        self.set_effect(triggerIds=[8301], visible=False) # 홀슈타트 아이스 임팩트 이펙트
        self.set_effect(triggerIds=[8000], visible=True) # 싸울 때 흔들림
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_2100')
        self.move_npc(spawnId=301, patrolName='MS2PatrolData_3100')
        self.set_effect(triggerIds=[8203], visible=True) # 이슈라 플레임 인피니티 이펙트
        self.set_effect(triggerIds=[8303], visible=True) # 홀슈타트 아이스 인피니티 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='27'):
            return 이펙트연출03(self.ctx)


class 이펙트연출03(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='28', seconds=1)
        self.set_effect(triggerIds=[8202], visible=True) # 이슈라 플레임 그라운드 이펙트
        self.set_effect(triggerIds=[8302], visible=True) # 홀슈타트 아이스 그라운드 이펙트
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='28'):
            return 연출종료01(self.ctx)


class 연출종료01(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='30', seconds=1)
        self.set_cinematic_ui(type=4)
        self.select_camera(triggerId=606, enable=False)
        self.select_camera(triggerId=602, enable=False)
        self.select_camera(triggerId=603, enable=False)
        self.set_effect(triggerIds=[8203], visible=False) # 이슈라 플레임 인피니티 이펙트
        self.set_effect(triggerIds=[8303], visible=False) # 홀슈타트 아이스 인피니티 이펙트
        self.set_effect(triggerIds=[8202], visible=False) # 이슈라 플레임 그라운드 이펙트
        self.set_effect(triggerIds=[8302], visible=False) # 홀슈타트 아이스 그라운드 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='30'):
            return 레버당기기01(self.ctx)

    def on_exit(self):
        self.set_effect(triggerIds=[7040], visible=False) # 전투 연출에서 룬 쉴드 이펙트 소리
        self.set_effect(triggerIds=[7050], visible=False) # 전투 연출에서 공격 스킬 이펙트 소리 NEW
        self.set_effect(triggerIds=[8000], visible=False) # 싸울 때 흔들림


class 연출종료01_skip(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101]) # 전투용 척후병 삭제
        self.destroy_monster(spawnIds=[102]) # 연출용 척후병 삭제
        self.remove_cinematic_talk()
        self.set_timer(timerId='30', seconds=1)
        self.create_monster(spawnIds=[102], animationEffect=True) # 연출용 척후병 생성
        self.set_cinematic_ui(type=4)
        self.select_camera(triggerId=606, enable=False)
        self.select_camera(triggerId=602, enable=False)
        self.select_camera(triggerId=603, enable=False)
        self.set_effect(triggerIds=[8203], visible=False) # 이슈라 플레임 인피니티 이펙트
        self.set_effect(triggerIds=[8303], visible=False) # 홀슈타트 아이스 인피니티 이펙트
        self.set_effect(triggerIds=[8202], visible=False) # 이슈라 플레임 그라운드 이펙트
        self.set_effect(triggerIds=[8302], visible=False) # 홀슈타트 아이스 그라운드 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='30'):
            return 레버당기기01(self.ctx)

    def on_exit(self):
        self.set_effect(triggerIds=[7040], visible=False) # 전투 연출에서 룬 쉴드 이펙트 소리
        self.set_effect(triggerIds=[7050], visible=False) # 전투 연출에서 공격 스킬 이펙트 소리 NEW
        self.set_effect(triggerIds=[8000], visible=False) # 싸울 때 흔들림


class 레버당기기01(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='31', seconds=1)
        self.set_cinematic_ui(type=4)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=605, enable=True)
        self.set_interact_object(triggerIds=[10000825], state=1) # 기관 작동 레버
        self.set_effect(triggerIds=[7030], visible=True) # 레버 장치에서 들리는 소리

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='31'):
            return 레버당기기02(self.ctx)


class 레버당기기02(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='35', seconds=3)
        self.set_conversation(type=2, spawnId=11001249, script='$52000016_QD__TUTORIAL04__16$', arg4=3)
        self.set_effect(triggerIds=[6106], visible=True) # 척후병 시네마틱 음성 06 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='35'):
            return 다리만들기01(self.ctx)

    def on_exit(self):
        self.set_effect(triggerIds=[6000], visible=True) # 가이드 서머리 알림 사운드
        self.show_guide_summary(entityId=10014031, textId=10014031) # 가이드 : 레버 작동시키기


class 다리만들기01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=605, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.destroy_monster(spawnIds=[301]) # 연출용 홀슈타트
        self.destroy_monster(spawnIds=[210,211,212,213,214,215,216,217]) # 연출용 아군8
        self.destroy_monster(spawnIds=[310,311,312,313]) # 연출용 아군4
        self.create_monster(spawnIds=[220,221,222,223,224,225,226,227], animationEffect=True) # 쓰러진 연출용 아군4
        self.set_effect(triggerIds=[7030], visible=False) # 레버 장치에서 들리는 소리

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000825], stateValue=0):
            return 다리만들기02(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=10014031)


class 다리만들기02(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='40', seconds=1)
        self.set_random_mesh(triggerIds=[4020,4021,4022,4023,4024,4025,4026,4027], visible=True, meshCount=8, arg4=120, delay=120) # Bridge Visible  ON
        self.set_effect(triggerIds=[7011], visible=True) # 다리 생길 때 흔들림
        self.set_effect(triggerIds=[7021], visible=True) # 다리 나타날 때 효과음
        self.set_agent(triggerIds=[10006], visible=False) # 다리 길막기
        self.set_agent(triggerIds=[10007], visible=False) # 다리 길막기
        self.set_agent(triggerIds=[10008], visible=False) # 다리 길막기
        self.set_agent(triggerIds=[10009], visible=False) # 다리 길막기
        self.set_effect(triggerIds=[6000], visible=True) # 가이드 서머리 알림 사운드
        self.show_guide_summary(entityId=10014032, textId=10014032) # 가이드 : 다리 건너가기
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_2000')
        self.set_mesh(triggerIds=[3001], visible=False, arg3=0, delay=0, scale=0) # bridge barrier OFF

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='40'):
            return 다리건너기01(self.ctx)


class 다리건너기01(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_1004')
        self.change_monster(removeSpawnId=201, addSpawnId=202)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9020, spawnIds=[102]):
            return 다리건너기02(self.ctx)


class 다리건너기02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9021]):
            return 마무리준비01(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=10014032)


class 마무리준비01(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='41', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='41'):
            return 마무리연출01(self.ctx)


class 마무리연출01(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='42', seconds=1)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=604, enable=True)
        self.set_scene_skip(state=마무리연출08, action='nextState')
        self.create_monster(spawnIds=[401], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='42'):
            return 마무리연출02(self.ctx)


class 마무리연출02(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='43', seconds=3)
        self.move_npc(spawnId=401, patrolName='MS2PatrolData_4000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='43'):
            return 마무리연출03(self.ctx)


class 마무리연출03(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='44', seconds=3)
        self.set_conversation(type=2, spawnId=11001230, script='$52000016_QD__TUTORIAL04__17$', arg4=3)
        self.set_effect(triggerIds=[6300], visible=True) # 렌듀비앙 시네마틱 음성 01 사운드
        self.set_skip(state=마무리연출04대기)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='44'):
            return 마무리연출04대기(self.ctx)


class 마무리연출04대기(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 마무리연출04(self.ctx)


class 마무리연출04(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='45', seconds=5)
        self.set_effect(triggerIds=[6300], visible=False) # 렌듀비앙 시네마틱 음성 01 사운드
        self.set_conversation(type=2, spawnId=11001244, script='$52000016_QD__TUTORIAL04__18$', arg4=4)
        self.set_effect(triggerIds=[6400], visible=True) # 이슈라 시네마틱 음성 05 사운드
        self.set_skip(state=마무리연출05대기)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='45'):
            return 마무리연출05대기(self.ctx)


class 마무리연출05대기(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 마무리연출05(self.ctx)


class 마무리연출05(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='46', seconds=5)
        self.set_effect(triggerIds=[6400], visible=False) # 이슈라 시네마틱 음성 05 사운드
        self.set_conversation(type=2, spawnId=11001230, script='$52000016_QD__TUTORIAL04__19$', arg4=4)
        self.set_effect(triggerIds=[6301], visible=True) # 렌듀비앙 시네마틱 음성 02 사운드
        self.set_skip(state=마무리연출06대기)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='46'):
            return 마무리연출06대기(self.ctx)


class 마무리연출06대기(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 마무리연출06(self.ctx)


class 마무리연출06(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='47', seconds=5)
        self.set_effect(triggerIds=[6301], visible=False) # 렌듀비앙 시네마틱 음성 02 사운드
        self.set_conversation(type=2, spawnId=11001244, script='$52000016_QD__TUTORIAL04__20$', arg4=4)
        self.set_effect(triggerIds=[6401], visible=True) # 이슈라 시네마틱 음성 06 사운드
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='47'):
            return 마무리연출07대기(self.ctx)


class 마무리연출07대기(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 마무리연출07(self.ctx)


class 마무리연출07(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='48', seconds=5)
        self.set_effect(triggerIds=[6401], visible=False) # 이슈라 시네마틱 음성 06 사운드
        self.set_conversation(type=2, spawnId=11001230, script='$52000016_QD__TUTORIAL04__21$', arg4=4)
        self.set_effect(triggerIds=[6302], visible=True) # 렌듀비앙 시네마틱 음성 03 사운드
        self.set_skip(state=마무리연출08대기)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='48'):
            return 마무리연출08대기(self.ctx)


class 마무리연출08대기(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 마무리연출08(self.ctx)


class 마무리연출08(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
        self.move_npc(spawnId=401, patrolName='MS2PatrolData_4001')
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_1005')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9030, spawnIds=[401]):
            return 마무리연출09(self.ctx)


class 마무리연출09(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='49', seconds=5)
        self.destroy_monster(spawnIds=[102,401])
        self.set_effect(triggerIds=[6302], visible=False) # 렌듀비앙 시네마틱 음성 03 사운드
        self.set_conversation(type=2, spawnId=11001244, script='$52000016_QD__TUTORIAL04__22$', arg4=3)
        self.set_effect(triggerIds=[6402], visible=True) # 이슈라 시네마틱 음성 07 사운드
        self.set_skip(state=퇴장준비01대기)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='49'):
            return 퇴장준비01대기(self.ctx)


class 퇴장준비01대기(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 퇴장준비01(self.ctx)


class 퇴장준비01(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='50', seconds=1)
        self.select_camera(triggerId=604, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='50'):
            return 퇴장준비02(self.ctx)

    def on_exit(self):
        self.set_effect(triggerIds=[6402], visible=False) # 이슈라 시네마틱 음성 07 사운드
        self.set_achievement(triggerId=9040, type='trigger', achieve='complete_tombmission')


class 퇴장준비02(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=202, patrolName='MS2PatrolData_2001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9030, spawnIds=[202]):
            return 퇴장완료01(self.ctx)


class 퇴장완료01(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=10014040, textId=10014040) # 가이드 : 칼리브 요새로 이동하기
        self.destroy_monster(spawnIds=[202])

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(boxIds=[9040]):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=10014040)


initial_state = 대기
