""" trigger/52000016_qd/tutorial04.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_agent(triggerIds=[10000], visible=True) # 입구 길막기
        set_agent(triggerIds=[10001], visible=True) # 입구 길막기
        set_agent(triggerIds=[10002], visible=True) # 입구 길막기
        set_agent(triggerIds=[10003], visible=True) # 입구 길막기
        set_agent(triggerIds=[10004], visible=True) # 입구 길막기
        set_agent(triggerIds=[10005], visible=True) # 입구 길막기
        set_agent(triggerIds=[10010], visible=True) # 입구 길막기
        set_agent(triggerIds=[10006], visible=True) # 다리 길막기
        set_agent(triggerIds=[10007], visible=True) # 다리 길막기
        set_agent(triggerIds=[10008], visible=True) # 다리 길막기
        set_agent(triggerIds=[10009], visible=True) # 다리 길막기
        set_effect(triggerIds=[6000], visible=False) # 가이드 서머리 알림 사운드
        set_effect(triggerIds=[7000], visible=False) # 먼지
        set_effect(triggerIds=[7001], visible=False) # 먼지
        set_effect(triggerIds=[7002], visible=False) # 먼지
        set_effect(triggerIds=[7003], visible=False) # 먼지
        set_effect(triggerIds=[7004], visible=False) # 먼지
        set_effect(triggerIds=[7005], visible=False) # 먼지
        set_effect(triggerIds=[7006], visible=False) # 먼지
        set_effect(triggerIds=[7007], visible=False) # 먼지
        set_effect(triggerIds=[7010], visible=False) # 동굴 입구 흔들림
        set_effect(triggerIds=[7020], visible=False) # 동굴 입구 무너지는 소리
        set_effect(triggerIds=[7011], visible=False) # 다리 생길 때 흔들림
        set_effect(triggerIds=[7021], visible=False) # 다리 나타날 때 효과음
        set_effect(triggerIds=[7030], visible=False) # 레버 장치에서 들리는 소리
        set_effect(triggerIds=[7040], visible=False) # 전투 연출에서 룬 쉴드 이펙트 소리
        set_effect(triggerIds=[7050], visible=False) # 전투 연출에서 공격 스킬 이펙트 소리 NEW
        set_skill(triggerIds=[910], isEnable=False) # 입구 큐브 부수기 스킬
        set_skill(triggerIds=[911], isEnable=False) # 입구 큐브 부수기 스킬
        set_skill(triggerIds=[912], isEnable=False) # 입구 큐브 부수기 스킬
        set_skill(triggerIds=[913], isEnable=False) # 입구 큐브 부수기 스킬
        set_skill(triggerIds=[914], isEnable=False) # 입구 큐브 부수기 스킬
        set_mesh(triggerIds=[2000], visible=True, arg3=0, arg4=0, arg5=0) # PCProtect barrier ON
        set_mesh(triggerIds=[3000], visible=True, arg3=0, arg4=0, arg5=0) # invisible barrier ON
        set_mesh(triggerIds=[3001], visible=True, arg3=0, arg4=0, arg5=0) # bridge barrier ON
        set_mesh(triggerIds=[4000,4001,4002,4003,4004,4005,4006,4007,4008,4009,4010,4011,4012,4013,4014,4015], visible=False, arg3=0, arg4=0, arg5=0) # Rock  Visible OFF
        set_mesh(triggerIds=[4020,4021,4022,4023,4024,4025,4026,4027], visible=False, arg3=0, arg4=0, arg5=0) # Bridge  Visible OFF
        set_interact_object(triggerIds=[10000825], state=0) # 기관 작동 레버
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_effect(triggerIds=[8200], visible=False) # 이슈라 플레임 쉴드 이펙트
        set_effect(triggerIds=[8300], visible=False) # 홀슈타트 아이스 쉴드 이펙트
        set_effect(triggerIds=[8201], visible=False) # 이슈라 플레임 임팩트 이펙트
        set_effect(triggerIds=[8301], visible=False) # 홀슈타트 아이스 임팩트 이펙트
        set_effect(triggerIds=[8202], visible=False) # 이슈라 플레임 그라운드 이펙트
        set_effect(triggerIds=[8302], visible=False) # 홀슈타트 아이스 그라운드 이펙트
        set_effect(triggerIds=[8203], visible=False) # 이슈라 플레임 인피니티 이펙트
        set_effect(triggerIds=[8303], visible=False) # 홀슈타트 아이스 인피니티 이펙트
        set_effect(triggerIds=[8000], visible=False) # 싸울 때 흔들림
        set_effect(triggerIds=[6100], visible=False) # 척후병 시네마틱 음성 01 사운드
        set_effect(triggerIds=[6101], visible=False) # 척후병 시네마틱 음성 02 사운드
        set_effect(triggerIds=[6102], visible=False) # 척후병 시네마틱 음성 03 사운드
        set_effect(triggerIds=[6103], visible=False) # 척후병 시네마틱 음성 04 사운드
        set_effect(triggerIds=[6104], visible=False) # 척후병 시네마틱 음성 05 사운드
        set_effect(triggerIds=[6105], visible=False) # 척후병 시네마틱 음성 06 사운드
        set_effect(triggerIds=[6106], visible=False) # 척후병 시네마틱 음성 06 사운드
        set_effect(triggerIds=[6200], visible=False) # 이슈라 시네마틱 음성 01 사운드
        set_effect(triggerIds=[6201], visible=False) # 이슈라 시네마틱 음성 02 사운드
        set_effect(triggerIds=[6202], visible=False) # 이슈라 시네마틱 음성 03 사운드
        set_effect(triggerIds=[6203], visible=False) # 이슈라 시네마틱 음성 04 사운드
        set_effect(triggerIds=[6210], visible=False) # 홀슈타트 시네마틱 음성 01 사운드
        set_effect(triggerIds=[6211], visible=False) # 홀슈타트 시네마틱 음성 02 사운드
        set_effect(triggerIds=[6212], visible=False) # 홀슈타트 시네마틱 음성 03 사운드
        set_effect(triggerIds=[6300], visible=False) # 렌듀비앙 시네마틱 음성 01 사운드
        set_effect(triggerIds=[6301], visible=False) # 렌듀비앙 시네마틱 음성 02 사운드
        set_effect(triggerIds=[6302], visible=False) # 렌듀비앙 시네마틱 음성 03 사운드
        set_effect(triggerIds=[6400], visible=False) # 이슈라 시네마틱 음성 05 사운드
        set_effect(triggerIds=[6401], visible=False) # 이슈라 시네마틱 음성 06 사운드
        set_effect(triggerIds=[6402], visible=False) # 이슈라 시네마틱 음성 07 사운드

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[90000417], questStates=[1]):
            return 딜레이01()


class 딜레이01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_random_mesh(triggerIds=[4000,4001,4002,4003,4004,4005,4006,4007,4008,4009,4010,4011,4012,4013,4014,4015], visible=True, meshCount=16, arg4=50, delay=80) # Rock Visible  ON

    def on_tick(self) -> state.State:
        if true():
            return 막힌길발견01()


class 막힌길발견01(state.State):
    def on_enter(self):
        select_camera(triggerId=601, enable=True)

    def on_tick(self) -> state.State:
        if true():
            return 딜레이02()


class 딜레이02(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[910], isEnable=True) # 입구 큐브 부수기 스킬
        set_skill(triggerIds=[911], isEnable=True) # 입구 큐브 부수기 스킬
        set_skill(triggerIds=[912], isEnable=True) # 입구 큐브 부수기 스킬
        set_skill(triggerIds=[913], isEnable=True) # 입구 큐브 부수기 스킬
        set_skill(triggerIds=[914], isEnable=True) # 입구 큐브 부수기 스킬
        set_effect(triggerIds=[7010], visible=True) # 동굴 입구 흔들림
        set_effect(triggerIds=[7020], visible=True) # 동굴 입구 무너지는 소리

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 막힌길발견02()


class 막힌길발견02(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=4)
        set_effect(triggerIds=[7000], visible=True) # 먼지
        set_effect(triggerIds=[7001], visible=True) # 먼지
        set_effect(triggerIds=[7002], visible=True) # 먼지
        set_effect(triggerIds=[7003], visible=True) # 먼지
        set_effect(triggerIds=[7004], visible=True) # 먼지
        set_effect(triggerIds=[7005], visible=True) # 먼지
        set_effect(triggerIds=[7006], visible=True) # 먼지
        set_effect(triggerIds=[7007], visible=True) # 먼지

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 척후병입장()

    def on_exit(self):
        set_mesh(triggerIds=[2000], visible=False, arg3=0, arg4=0, arg5=0) # PCProtect barrier ON


class 척후병입장(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)
        create_monster(spawnIds=[101], arg2=True)
        move_npc(spawnId=101, patrolName='MS2PatrolData_1000')
        set_effect(triggerIds=[6100], visible=True) # 척후병 시네마틱 음성 01 사운드
        set_conversation(type=2, spawnId=11001249, script='$52000016_QD__TUTORIAL04__0$', arg4=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 돌치우기안내01()


class 돌치우기안내01(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=3)
        set_effect(triggerIds=[6101], visible=True) # 척후병 시네마틱 음성 02 사운드
        move_npc(spawnId=101, patrolName='MS2PatrolData_1001')
        set_conversation(type=2, spawnId=11001249, script='$52000016_QD__TUTORIAL04__1$', arg4=3)
        set_skip(state=돌치우기안내03)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 돌치우기안내03()

    def on_exit(self):
        remove_cinematic_talk()
        set_effect(triggerIds=[7010], visible=False) # 동굴 입구 흔들림
        set_effect(triggerIds=[7020], visible=False) # 동굴 입구 무너지는 소리
        set_skill(triggerIds=[910], isEnable=False) # 입구 큐브 부수기 스킬
        set_skill(triggerIds=[911], isEnable=False) # 입구 큐브 부수기 스킬
        set_skill(triggerIds=[912], isEnable=False) # 입구 큐브 부수기 스킬
        set_skill(triggerIds=[913], isEnable=False) # 입구 큐브 부수기 스킬
        set_skill(triggerIds=[914], isEnable=False) # 입구 큐브 부수기 스킬


class 돌치우기안내03(state.State):
    def on_enter(self):
        select_camera(triggerId=601, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if true():
            return 첫번째돌들기가이드01()


class 첫번째돌들기가이드01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6000], visible=True) # 가이드 서머리 알림 사운드
        show_guide_summary(entityId=10014010, textId=10014010) # 가이드 : 스페이스 키를 눌러 바위덩이 들기

    def on_tick(self) -> state.State:
        if not detect_liftable_object(boxIds=[9001], itemId=30000440):
            return 첫번째돌놓기01()

    def on_exit(self):
        hide_guide_summary(entityId=10014010)


class 첫번째돌놓기01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6000], visible=True) # 가이드 서머리 알림 사운드
        show_guide_summary(entityId=10014020, textId=10014020) # 가이드 : 스페이스 키를 눌러 눌러 바위덩이  내려놓기

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9011,9012], itemId=30000440):
            return 척후병이동01()


class 척후병이동01(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=10014020)
        create_monster(spawnIds=[901,902,903,904,905,906,907], arg2=False)
        set_random_mesh(triggerIds=[4000,4001,4002,4003,4004,4005,4006,4007,4008,4009,4010,4011,4012,4013,4014,4015], visible=False, meshCount=16, arg4=100, delay=80) # Rock Visible  OFF
        set_mesh(triggerIds=[3000], visible=False, arg3=0, arg4=0, arg5=0) # invisible barrier OFF
        move_npc(spawnId=101, patrolName='MS2PatrolData_1002')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=9004, spawnIds=[101]):
            return 척후병이동02()


class 척후병이동02(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=101, script='$52000016_QD__TUTORIAL04__2$', arg4=2)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=9005, spawnIds=[101]):
            return 척후병전투시작01()


class 척후병전투시작01(state.State):
    def on_enter(self):
        set_timer(timerId='9', seconds=1)
        set_agent(triggerIds=[10000], visible=False) # 입구 길막기
        set_agent(triggerIds=[10001], visible=False) # 입구 길막기
        set_agent(triggerIds=[10002], visible=False) # 입구 길막기
        set_agent(triggerIds=[10003], visible=False) # 입구 길막기
        set_agent(triggerIds=[10004], visible=False) # 입구 길막기
        set_agent(triggerIds=[10005], visible=False) # 입구 길막기
        set_agent(triggerIds=[10010], visible=False) # 입구 길막기

    def on_tick(self) -> state.State:
        if time_expired(timerId='9'):
            return 전투중01()


class 전투중01(state.State):
    def on_enter(self):
        set_timer(timerId='10', seconds=2)
        set_conversation(type=1, spawnId=101, script='$52000016_QD__TUTORIAL04__3$', arg4=2)
        set_effect(triggerIds=[6102], visible=True) # 척후병 시네마틱 음성 03 사운드

    def on_tick(self) -> state.State:
        if time_expired(timerId='10'):
            return 전투중02()


class 전투중02(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=101, script='$52000016_QD__TUTORIAL04__4$', arg4=2)
        set_effect(triggerIds=[6000], visible=True) # 가이드 서머리 알림 사운드
        show_guide_summary(entityId=10014030, textId=10014030) # 가이드 : 주변 몬스터 모두 처치하기

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[901,902,903,904,905,906,907]):
            return 전투종료01()

    def on_exit(self):
        hide_guide_summary(entityId=10014030)


class 전투종료01(state.State):
    def on_enter(self):
        set_timer(timerId='11', seconds=2)
        set_effect(triggerIds=[6103], visible=True) # 척후병 시네마틱 음성 04 사운드
        set_conversation(type=1, spawnId=101, script='$52000016_QD__TUTORIAL04__5$', arg4=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11'):
            return 전투종료02()


class 전투종료02(state.State):
    def on_enter(self):
        set_timer(timerId='12', seconds=2)
        set_conversation(type=1, spawnId=101, script='$52000016_QD__TUTORIAL04__6$', arg4=2)
        move_npc(spawnId=101, patrolName='MS2PatrolData_1003')

    def on_tick(self) -> state.State:
        if time_expired(timerId='12'):
            return 다리로이동01()


class 다리로이동01(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=9006, spawnIds=[101]):
            return 연출준비01()


class 연출준비01(state.State):
    def on_enter(self):
        set_timer(timerId='13', seconds=3)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=602, enable=True)
        set_conversation(type=2, spawnId=11001249, script='$52000016_QD__TUTORIAL04__7$', arg4=3)
        set_effect(triggerIds=[6104], visible=True) # 척후병 시네마틱 음성 05 사운드

    def on_tick(self) -> state.State:
        if time_expired(timerId='13'):
            return 연출준비02()


class 연출준비02(state.State):
    def on_enter(self):
        set_timer(timerId='14', seconds=2)
        set_conversation(type=2, spawnId=11001249, script='$52000016_QD__TUTORIAL04__8$', arg4=2)
        set_effect(triggerIds=[6105], visible=True) # 척후병 시네마틱 음성 06 사운드
        create_monster(spawnIds=[201], arg2=True) # 연출용 이슈라
        create_monster(spawnIds=[301], arg2=True) # 연출용 홀슈타트
        create_monster(spawnIds=[210,211,212,213,214,215,216,217], arg2=True) # 연출용 아군8
        create_monster(spawnIds=[310,311,312,313], arg2=True) # 연출용 아군4

    def on_tick(self) -> state.State:
        if time_expired(timerId='14'):
            return 연출시작01대기()


class 연출시작01대기(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return 연출시작01()


class 연출시작01(state.State):
    def on_enter(self):
        set_scene_skip(state=연출종료01_skip, arg2='nextState')
        set_timer(timerId='16', seconds=1)
        select_camera_path(pathIds=[602,603], returnView=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='16'):
            return 대결연출01()


class 대결연출01(state.State):
    def on_enter(self):
        set_timer(timerId='18', seconds=3)
        set_conversation(type=2, spawnId=11001244, script='$52000016_QD__TUTORIAL04__9$', arg4=3)
        set_effect(triggerIds=[6200], visible=True) # 이슈라 시네마틱 음성 01 사운드
        destroy_monster(spawnIds=[101]) # 전투용 척후병 삭제
        create_monster(spawnIds=[102], arg2=True) # 연출용 척후병 생성
        set_skip(state=대결연출02대기)

    def on_tick(self) -> state.State:
        if time_expired(timerId='18'):
            return 대결연출02대기()


class 대결연출02대기(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return 대결연출02()


class 대결연출02(state.State):
    def on_enter(self):
        set_timer(timerId='19', seconds=7)
        set_conversation(type=2, spawnId=11001231, script='$52000016_QD__TUTORIAL04__10$', arg4=6)
        set_effect(triggerIds=[6200], visible=False) # 이슈라 시네마틱 음성 01 사운드
        set_effect(triggerIds=[6210], visible=True) # 홀슈타트 시네마틱 음성 01 사운드
        set_skip(state=대결연출03대기)

    def on_tick(self) -> state.State:
        if time_expired(timerId='19'):
            return 대결연출03대기()


class 대결연출03대기(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return 대결연출03()


class 대결연출03(state.State):
    def on_enter(self):
        set_timer(timerId='20', seconds=5)
        set_conversation(type=2, spawnId=11001244, script='$52000016_QD__TUTORIAL04__11$', arg4=4)
        set_effect(triggerIds=[6210], visible=False) # 홀슈타트 시네마틱 음성 01 사운드
        set_effect(triggerIds=[6201], visible=True) # 이슈라 시네마틱 음성 02 사운드
        set_skip(state=대결연출04대기)

    def on_tick(self) -> state.State:
        if time_expired(timerId='20'):
            return 대결연출04대기()


class 대결연출04대기(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return 대결연출04()


class 대결연출04(state.State):
    def on_enter(self):
        set_timer(timerId='21', seconds=5)
        set_conversation(type=2, spawnId=11001231, script='$52000016_QD__TUTORIAL04__12$', arg4=5)
        set_effect(triggerIds=[6201], visible=False) # 이슈라 시네마틱 음성 02 사운드
        set_effect(triggerIds=[6211], visible=True) # 홀슈타트 시네마틱 음성 02 사운드
        set_skip(state=대결연출05대기)

    def on_tick(self) -> state.State:
        if time_expired(timerId='21'):
            return 대결연출05대기()


class 대결연출05대기(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return 대결연출05()


class 대결연출05(state.State):
    def on_enter(self):
        set_timer(timerId='22', seconds=4)
        set_conversation(type=2, spawnId=11001244, script='$52000016_QD__TUTORIAL04__13$', arg4=3)
        set_effect(triggerIds=[6211], visible=False) # 홀슈타트 시네마틱 음성 02 사운드
        set_effect(triggerIds=[6202], visible=True) # 이슈라 시네마틱 음성 03 사운드
        set_skip(state=대결연출06대기)

    def on_tick(self) -> state.State:
        if time_expired(timerId='22'):
            return 대결연출06대기()


class 대결연출06대기(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return 대결연출06()


class 대결연출06(state.State):
    def on_enter(self):
        set_timer(timerId='23', seconds=4)
        set_conversation(type=2, spawnId=11001231, script='$52000016_QD__TUTORIAL04__14$', arg4=3)
        set_effect(triggerIds=[6202], visible=False) # 이슈라 시네마틱 음성 03 사운드
        set_effect(triggerIds=[6212], visible=True) # 홀슈타트 시네마틱 음성 03 사운드
        set_skip(state=대결연출07대기)

    def on_tick(self) -> state.State:
        if time_expired(timerId='23'):
            return 대결연출07대기()


class 대결연출07대기(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 대결연출07()


class 대결연출07(state.State):
    def on_enter(self):
        set_timer(timerId='24', seconds=1)
        select_camera(triggerId=606, enable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='24'):
            return 대결연출08()


class 대결연출08(state.State):
    def on_enter(self):
        set_timer(timerId='25', seconds=1)
        set_effect(triggerIds=[7050], visible=True) # 전투 연출에서 공격 스킬 이펙트 소리 NEW
        set_conversation(type=2, spawnId=11001244, script='$52000016_QD__TUTORIAL04__15$', arg4=2)
        set_effect(triggerIds=[6212], visible=False) # 홀슈타트 시네마틱 음성 03 사운드
        set_effect(triggerIds=[6203], visible=True) # 이슈라 시네마틱 음성 04 사운드
        set_effect(triggerIds=[8200], visible=True) # 이슈라 플레임 쉴드 이펙트
        set_effect(triggerIds=[8300], visible=True) # 홀슈타트 아이스 쉴드 이펙트

    def on_tick(self) -> state.State:
        if time_expired(timerId='25'):
            return 이펙트연출01()


class 이펙트연출01(state.State):
    def on_enter(self):
        set_timer(timerId='26', seconds=2)
        set_effect(triggerIds=[8201], visible=True) # 이슈라 플레임 임팩트 이펙트
        set_effect(triggerIds=[8301], visible=True) # 홀슈타트 아이스 임팩트 이펙트

    def on_tick(self) -> state.State:
        if time_expired(timerId='26'):
            return 이펙트연출02()

    def on_exit(self):
        set_effect(triggerIds=[8200], visible=False) # 이슈라 플레임 쉴드 이펙트
        set_effect(triggerIds=[8300], visible=False) # 홀슈타트 아이스 쉴드 이펙트


class 이펙트연출02(state.State):
    def on_enter(self):
        set_timer(timerId='27', seconds=1)
        set_effect(triggerIds=[8201], visible=False) # 이슈라 플레임 임팩트 이펙트
        set_effect(triggerIds=[8301], visible=False) # 홀슈타트 아이스 임팩트 이펙트
        set_effect(triggerIds=[8000], visible=True) # 싸울 때 흔들림
        move_npc(spawnId=201, patrolName='MS2PatrolData_2100')
        move_npc(spawnId=301, patrolName='MS2PatrolData_3100')
        set_effect(triggerIds=[8203], visible=True) # 이슈라 플레임 인피니티 이펙트
        set_effect(triggerIds=[8303], visible=True) # 홀슈타트 아이스 인피니티 이펙트

    def on_tick(self) -> state.State:
        if time_expired(timerId='27'):
            return 이펙트연출03()


class 이펙트연출03(state.State):
    def on_enter(self):
        set_timer(timerId='28', seconds=1)
        set_effect(triggerIds=[8202], visible=True) # 이슈라 플레임 그라운드 이펙트
        set_effect(triggerIds=[8302], visible=True) # 홀슈타트 아이스 그라운드 이펙트
        set_scene_skip()

    def on_tick(self) -> state.State:
        if time_expired(timerId='28'):
            return 연출종료01()


class 연출종료01(state.State):
    def on_enter(self):
        set_timer(timerId='30', seconds=1)
        set_cinematic_ui(type=4)
        select_camera(triggerId=606, enable=False)
        select_camera(triggerId=602, enable=False)
        select_camera(triggerId=603, enable=False)
        set_effect(triggerIds=[8203], visible=False) # 이슈라 플레임 인피니티 이펙트
        set_effect(triggerIds=[8303], visible=False) # 홀슈타트 아이스 인피니티 이펙트
        set_effect(triggerIds=[8202], visible=False) # 이슈라 플레임 그라운드 이펙트
        set_effect(triggerIds=[8302], visible=False) # 홀슈타트 아이스 그라운드 이펙트

    def on_tick(self) -> state.State:
        if time_expired(timerId='30'):
            return 레버당기기01()

    def on_exit(self):
        set_effect(triggerIds=[7040], visible=False) # 전투 연출에서 룬 쉴드 이펙트 소리
        set_effect(triggerIds=[7050], visible=False) # 전투 연출에서 공격 스킬 이펙트 소리 NEW
        set_effect(triggerIds=[8000], visible=False) # 싸울 때 흔들림


class 연출종료01_skip(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101]) # 전투용 척후병 삭제
        destroy_monster(spawnIds=[102]) # 연출용 척후병 삭제
        remove_cinematic_talk()
        set_timer(timerId='30', seconds=1)
        create_monster(spawnIds=[102], arg2=True) # 연출용 척후병 생성
        set_cinematic_ui(type=4)
        select_camera(triggerId=606, enable=False)
        select_camera(triggerId=602, enable=False)
        select_camera(triggerId=603, enable=False)
        set_effect(triggerIds=[8203], visible=False) # 이슈라 플레임 인피니티 이펙트
        set_effect(triggerIds=[8303], visible=False) # 홀슈타트 아이스 인피니티 이펙트
        set_effect(triggerIds=[8202], visible=False) # 이슈라 플레임 그라운드 이펙트
        set_effect(triggerIds=[8302], visible=False) # 홀슈타트 아이스 그라운드 이펙트

    def on_tick(self) -> state.State:
        if time_expired(timerId='30'):
            return 레버당기기01()

    def on_exit(self):
        set_effect(triggerIds=[7040], visible=False) # 전투 연출에서 룬 쉴드 이펙트 소리
        set_effect(triggerIds=[7050], visible=False) # 전투 연출에서 공격 스킬 이펙트 소리 NEW
        set_effect(triggerIds=[8000], visible=False) # 싸울 때 흔들림


class 레버당기기01(state.State):
    def on_enter(self):
        set_timer(timerId='31', seconds=1)
        set_cinematic_ui(type=4)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=605, enable=True)
        set_interact_object(triggerIds=[10000825], state=1) # 기관 작동 레버
        set_effect(triggerIds=[7030], visible=True) # 레버 장치에서 들리는 소리

    def on_tick(self) -> state.State:
        if time_expired(timerId='31'):
            return 레버당기기02()


class 레버당기기02(state.State):
    def on_enter(self):
        set_timer(timerId='35', seconds=3)
        set_conversation(type=2, spawnId=11001249, script='$52000016_QD__TUTORIAL04__16$', arg4=3)
        set_effect(triggerIds=[6106], visible=True) # 척후병 시네마틱 음성 06 사운드

    def on_tick(self) -> state.State:
        if time_expired(timerId='35'):
            return 다리만들기01()

    def on_exit(self):
        set_effect(triggerIds=[6000], visible=True) # 가이드 서머리 알림 사운드
        show_guide_summary(entityId=10014031, textId=10014031) # 가이드 : 레버 작동시키기


class 다리만들기01(state.State):
    def on_enter(self):
        select_camera(triggerId=605, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        destroy_monster(spawnIds=[301]) # 연출용 홀슈타트
        destroy_monster(spawnIds=[210,211,212,213,214,215,216,217]) # 연출용 아군8
        destroy_monster(spawnIds=[310,311,312,313]) # 연출용 아군4
        create_monster(spawnIds=[220,221,222,223,224,225,226,227], arg2=True) # 쓰러진 연출용 아군4
        set_effect(triggerIds=[7030], visible=False) # 레버 장치에서 들리는 소리

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000825], arg2=0):
            return 다리만들기02()

    def on_exit(self):
        hide_guide_summary(entityId=10014031)


class 다리만들기02(state.State):
    def on_enter(self):
        set_timer(timerId='40', seconds=1)
        set_random_mesh(triggerIds=[4020,4021,4022,4023,4024,4025,4026,4027], visible=True, meshCount=8, arg4=120, delay=120) # Bridge Visible  ON
        set_effect(triggerIds=[7011], visible=True) # 다리 생길 때 흔들림
        set_effect(triggerIds=[7021], visible=True) # 다리 나타날 때 효과음
        set_agent(triggerIds=[10006], visible=False) # 다리 길막기
        set_agent(triggerIds=[10007], visible=False) # 다리 길막기
        set_agent(triggerIds=[10008], visible=False) # 다리 길막기
        set_agent(triggerIds=[10009], visible=False) # 다리 길막기
        set_effect(triggerIds=[6000], visible=True) # 가이드 서머리 알림 사운드
        show_guide_summary(entityId=10014032, textId=10014032) # 가이드 : 다리 건너가기
        move_npc(spawnId=201, patrolName='MS2PatrolData_2000')
        set_mesh(triggerIds=[3001], visible=False, arg3=0, arg4=0, arg5=0) # bridge barrier OFF

    def on_tick(self) -> state.State:
        if time_expired(timerId='40'):
            return 다리건너기01()


class 다리건너기01(state.State):
    def on_enter(self):
        move_npc(spawnId=102, patrolName='MS2PatrolData_1004')
        change_monster(removeSpawnId=201, addSpawnId=202)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=9020, spawnIds=[102]):
            return 다리건너기02()


class 다리건너기02(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9021]):
            return 마무리준비01()

    def on_exit(self):
        hide_guide_summary(entityId=10014032)


class 마무리준비01(state.State):
    def on_enter(self):
        set_timer(timerId='41', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='41'):
            return 마무리연출01()


class 마무리연출01(state.State):
    def on_enter(self):
        set_timer(timerId='42', seconds=1)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=604, enable=True)
        set_scene_skip(state=마무리연출08, arg2='nextState')
        create_monster(spawnIds=[401], arg2=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='42'):
            return 마무리연출02()


class 마무리연출02(state.State):
    def on_enter(self):
        set_timer(timerId='43', seconds=3)
        move_npc(spawnId=401, patrolName='MS2PatrolData_4000')

    def on_tick(self) -> state.State:
        if time_expired(timerId='43'):
            return 마무리연출03()


class 마무리연출03(state.State):
    def on_enter(self):
        set_timer(timerId='44', seconds=3)
        set_conversation(type=2, spawnId=11001230, script='$52000016_QD__TUTORIAL04__17$', arg4=3)
        set_effect(triggerIds=[6300], visible=True) # 렌듀비앙 시네마틱 음성 01 사운드
        set_skip(state=마무리연출04대기)

    def on_tick(self) -> state.State:
        if time_expired(timerId='44'):
            return 마무리연출04대기()


class 마무리연출04대기(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return 마무리연출04()


class 마무리연출04(state.State):
    def on_enter(self):
        set_timer(timerId='45', seconds=5)
        set_effect(triggerIds=[6300], visible=False) # 렌듀비앙 시네마틱 음성 01 사운드
        set_conversation(type=2, spawnId=11001244, script='$52000016_QD__TUTORIAL04__18$', arg4=4)
        set_effect(triggerIds=[6400], visible=True) # 이슈라 시네마틱 음성 05 사운드
        set_skip(state=마무리연출05대기)

    def on_tick(self) -> state.State:
        if time_expired(timerId='45'):
            return 마무리연출05대기()


class 마무리연출05대기(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return 마무리연출05()


class 마무리연출05(state.State):
    def on_enter(self):
        set_timer(timerId='46', seconds=5)
        set_effect(triggerIds=[6400], visible=False) # 이슈라 시네마틱 음성 05 사운드
        set_conversation(type=2, spawnId=11001230, script='$52000016_QD__TUTORIAL04__19$', arg4=4)
        set_effect(triggerIds=[6301], visible=True) # 렌듀비앙 시네마틱 음성 02 사운드
        set_skip(state=마무리연출06대기)

    def on_tick(self) -> state.State:
        if time_expired(timerId='46'):
            return 마무리연출06대기()


class 마무리연출06대기(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return 마무리연출06()


class 마무리연출06(state.State):
    def on_enter(self):
        set_timer(timerId='47', seconds=5)
        set_effect(triggerIds=[6301], visible=False) # 렌듀비앙 시네마틱 음성 02 사운드
        set_conversation(type=2, spawnId=11001244, script='$52000016_QD__TUTORIAL04__20$', arg4=4)
        set_effect(triggerIds=[6401], visible=True) # 이슈라 시네마틱 음성 06 사운드
        set_scene_skip()

    def on_tick(self) -> state.State:
        if time_expired(timerId='47'):
            return 마무리연출07대기()


class 마무리연출07대기(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return 마무리연출07()


class 마무리연출07(state.State):
    def on_enter(self):
        set_timer(timerId='48', seconds=5)
        set_effect(triggerIds=[6401], visible=False) # 이슈라 시네마틱 음성 06 사운드
        set_conversation(type=2, spawnId=11001230, script='$52000016_QD__TUTORIAL04__21$', arg4=4)
        set_effect(triggerIds=[6302], visible=True) # 렌듀비앙 시네마틱 음성 03 사운드
        set_skip(state=마무리연출08대기)

    def on_tick(self) -> state.State:
        if time_expired(timerId='48'):
            return 마무리연출08대기()


class 마무리연출08대기(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return 마무리연출08()


class 마무리연출08(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)
        move_npc(spawnId=401, patrolName='MS2PatrolData_4001')
        move_npc(spawnId=102, patrolName='MS2PatrolData_1005')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=9030, spawnIds=[401]):
            return 마무리연출09()


class 마무리연출09(state.State):
    def on_enter(self):
        set_timer(timerId='49', seconds=5)
        destroy_monster(spawnIds=[102,401])
        set_effect(triggerIds=[6302], visible=False) # 렌듀비앙 시네마틱 음성 03 사운드
        set_conversation(type=2, spawnId=11001244, script='$52000016_QD__TUTORIAL04__22$', arg4=3)
        set_effect(triggerIds=[6402], visible=True) # 이슈라 시네마틱 음성 07 사운드
        set_skip(state=퇴장준비01대기)

    def on_tick(self) -> state.State:
        if time_expired(timerId='49'):
            return 퇴장준비01대기()


class 퇴장준비01대기(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return 퇴장준비01()


class 퇴장준비01(state.State):
    def on_enter(self):
        set_timer(timerId='50', seconds=1)
        select_camera(triggerId=604, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='50'):
            return 퇴장준비02()

    def on_exit(self):
        set_effect(triggerIds=[6402], visible=False) # 이슈라 시네마틱 음성 07 사운드
        set_achievement(triggerId=9040, type='trigger', achieve='complete_tombmission')


class 퇴장준비02(state.State):
    def on_enter(self):
        move_npc(spawnId=202, patrolName='MS2PatrolData_2001')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=9030, spawnIds=[202]):
            return 퇴장완료01()


class 퇴장완료01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=10014040, textId=10014040) # 가이드 : 칼리브 요새로 이동하기
        destroy_monster(spawnIds=[202])

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[9040]):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=10014040)


