""" trigger/84000006_wd/84000006_wd_main.xml """
from common import *
import state


# 플로우
# 		1. 입장하면 콘대르가 반겨준다.
# 		2. 유니콘 피냐타에 악령이 깃든다.
# 		3. 입장 이후, 강철 유니콘 피냐타를 박터트리기 느낌으로 웨폰 오브젝트, 조개껍데기를 집어던지면서 팬다.
# 		4. 강철 유니콘 피냐타를 쓰러트리면, 악마가 빠져나가면서 레인보우 유니콘 피냐타로 변한다.
# 		5. 레인보우 유니콘 피냐타가 고마워하면서 결혼을 축하해준다. 이때 불꽃놀이 등 화려한 이펙트를 연출하여 축제느낌을 전달한다.
# 		6. 유저들끼리 x분간 자유시간. 이때 그냥 귀찮으면 미리 결혼식장 복귀 가능하게 해줌
# 		7. x분 후 자동으로 결혼식장 복귀
# 수정 플로우 : 웨폰 오브젝트, 몬스터 리소스 신청 못함
# 		1. 입장하면 콘대르가 반겨준다.
# 		2. 유니콘 피냐타에 악령이 깃든다.
# 		3. 열심히 훔쳐먹으며 시간을 끌어주면, 마법의 달팽이를 던질 수 있게 된다.
# 		4. 강철 유니콘 피냐타를 쓰러트리면, 악마가 빠져나가면서 레인보우 유니콘 피냐타로 변한다.
# 		5. 레인보우 유니콘 피냐타가 고마워하면서 결혼을 축하해준다. 이때 불꽃놀이 등 화려한 이펙트를 연출하여 축제느낌을 전달한다.
# 		6. 유저들끼리 x분간 자유시간. 이때 그냥 귀찮으면 미리 결혼식장 복귀 가능하게 해줌
# 		7. x분 후 자동으로 결혼식장 복귀
# 유저 입장
class Reception(state.State):
    def on_enter(self):
        set_portal(portalId=10001, visible=True, enabled=True, minimapVisible=True) # 결혼식장 복귀 포탈 설정
        set_portal(portalId=10002, visible=False, enabled=False, minimapVisible=False) # 결혼식장 복귀 포탈 설정
        create_monster(spawnIds=[102], arg2=False) # NPC생성 : 어렴풋이 레인보우 피냐타가 보이게
        set_effect(triggerIds=[3000], visible=False) # 이펙트off : 불꽃놀이
        set_effect(triggerIds=[3001], visible=False) # 이펙트off : 레인보우 피냐타 이펙트 꺼둠
        set_effect(triggerIds=[3002], visible=False) # 이펙트off : 강철 피냐타 꺼둠

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return EntryDelay()


# 시작 대기
class EntryDelay(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=40, clearAtZero=True, display=False) # 테스트 가능 지점 : 라이브 시 60초로 수정
        create_monster(spawnIds=[101], arg2=False) # 몬스터 생성 : 어렴풋이 레인보우 피냐타가 보이게

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return openingscene_start()
        if count_users(boxId=9000, boxId=70):
            return openingscene_start()


# 연출 시작
class openingscene_start(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1) # 화면 보정
        set_cinematic_ui(type=3) # 화면 보정
        visible_my_pc(isVisible=False) # 연출 위해 PC 숨김
        select_camera_path(pathIds=[5004,5003], returnView=True) # 연출용 카메라 2개

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return openingscene_1_1()


# 연출1: 레인보우 피냐타 자기소개
class openingscene_1_1(state.State):
    def on_enter(self):
        set_effect(triggerIds=[3001], visible=True) # 이펙트on : 레인보우 피냐타 하트
        add_balloon_talk(spawnId=101, msg='$84000006_WD__84000006_WD_MAIN__0$', duration=3000, delayTick=500) # npc대사 : 애프터파티에 오신 것을 환영해요!
        add_balloon_talk(spawnId=101, msg='$84000006_WD__84000006_WD_MAIN__1$', duration=3000, delayTick=3500) # npc대사 : 제 이름은 레인보우 피냐타!

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6500):
            return openingscene_1_2()


# 연출2: 레인보우 피냐타 상태 이상
class openingscene_1_2(state.State):
    def on_enter(self):
        set_effect(triggerIds=[3001], visible=True) # 이펙트on : 레인보우 피냐타 하트
        add_balloon_talk(spawnId=101, msg='$84000006_WD__84000006_WD_MAIN__2$', duration=3000, delayTick=500) # npc대사 : 이제 곧 파티를 시작... 으윽!

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return openingscene_1_3()

    def on_exit(self):
        destroy_monster(spawnIds=[101])


# 연출3: 피냐타에 노총각 악령 빙의
class openingscene_1_3(state.State):
    def on_enter(self):
        set_ambient_light(primary=[150,150,150]) # 화면 살짝 어둡게
        create_monster(spawnIds=[201], arg2=False, arg3=30000) # 몬스터 등장: 피냐타에 빙의
        set_effect(triggerIds=[3002], visible=True) # 이펙트 on: 악령 피냐타
        add_balloon_talk(spawnId=201, msg='$84000006_WD__84000006_WD_MAIN__3$', duration=4000, delayTick=1000) # npc대사 : 결혼식...\n망친다...
        add_balloon_talk(spawnId=201, msg='$84000006_WD__84000006_WD_MAIN__4$', duration=4000, delayTick=5000) # npc대사 : 남의 행복...\n나의 불행...

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return GameGuide01()


# 가이드1: 콘대르가 상황 정리
class GameGuide01(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=1) # 카메라 강제 리셋
        add_buff(boxIds=[9002], skillId=99940044, level=1, arg4=False, arg5=True) # 훔쳐먹기 페이즈: 텅빈 스킬셋. 장난감은 사용 가능
        set_cinematic_ui(type=0) # 연출용 화면 보정 off
        set_cinematic_ui(type=2) # 연출용 화면 보정 off
        visible_my_pc(isVisible=True) # 연출 후 PC 재노출
        side_npc_talk(npcId=11004772, illust='Conder_normal', duration=4000, script='$84000006_WD__84000006_WD_MAIN__5$') # 콘대르 사이드톡: 이런 젠장! 리스항구의 노총각 악령이다!
        set_npc_emotion_loop(spawnId=102, sequenceName='Talk_A', duration=20000) # 연출 후 PC 재노출

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return GameGuide02()


# 가이드2: 콘대르가 상황 정리2
class GameGuide02(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11004772, illust='Conder_normal', duration=4000, script='$84000006_WD__84000006_WD_MAIN__6$') # 콘대르 사이드톡: 내 귀여운 피냐타에 깃들어 버리다니...

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return GameGuide03()


# 가이드3: 콘대르가 몬스터 약점 파악
class GameGuide03(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11004772, illust='Conder_normal', duration=4000, script='$84000006_WD__84000006_WD_MAIN__7$') # 콘대르 사이드톡: 저 녀석은 식탐이 매우 강한 녀석이야!

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return GameGuide04()


# 가이드4: 콘대르가 미션 제공
class GameGuide04(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11004772, illust='Conder_normal', duration=4000, script='$84000006_WD__84000006_WD_MAIN__8$') # 콘대르 사이드톡: 파티장의 음식들을 훔쳐먹으면서 악령의 시선을 끌어다오.

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return GameGuide05()


# 가이드5: 콘대르가 미션 제공2
class GameGuide05(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11004772, illust='Conder_normal', duration=4000, script='$84000006_WD__84000006_WD_MAIN__9$') # 콘대르 사이드톡: 시선을 끌어주는 동안, 내가 해결책을 찾아내지.

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return GameGuide06()


# 가이드6: 미션 카운트 다운 및 미션 재확인
class GameGuide06(state.State):
    def on_enter(self):
        set_event_ui(type=2, arg2='$84000006_WD__84000006_WD_MAIN__10$', arg3='0,3', arg4='0') # 카운트다운UI: 지금부터 음식을 훔쳐먹으며 시간을 벌자!

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Pinata_Ready()


# 전투 페이즈1: 훔쳐먹기 60초
class Pinata_Ready(state.State):
    def on_enter(self):
        set_user_value(triggerId=1004, key='Interaction', value=1) # 센서: Object.xml의 상호작용 시작
        destroy_monster(spawnIds=[102]) # 콘대르 아저씨 해결책 찾기 위해 퇴장
        set_mesh(triggerIds=[8000,8001,8002,8003,8004,8005,8006,8007,8008,8009,8010,8011], visible=False, arg3=0, arg4=0, arg5=0) # 메쉬 끄기
        start_mini_game(boxId=9001, round=1, isShowResultUI=False, gameName='PinataWD') # 미니게임 시작 선언 보상UI 꺼둠
        add_balloon_talk(spawnId=201, msg='$84000006_WD__84000006_WD_MAIN__11$', duration=8000, delayTick=1000) # 음식들...\n건들지마...
        show_guide_summary(entityId=28500010, textId=28500010, duration=5000) # 가이드 : 오브젝트 상호작용해서 보상수령하셈

    def on_tick(self) -> state.State:
        if user_value(key='Steal', value=1):
            return Pinata_Fight()


# 전투 페이즈1-1: 콘대르가 해결책 제시
class Pinata_Fight(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11004772, illust='Conder_normal', duration=4000, script='$84000006_WD__84000006_WD_MAIN__12$') # 콘대르 사이드톡: 자 지금이라네! 무지개 달팽이 공격!

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Pinata_Fight2()


# 전투 페이즈2: 악령잡기
class Pinata_Fight2(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=60, display=True) # 타이머3 설정 : 전투 페이즈 60초
        set_event_ui(type=1, arg2='$84000006_WD__84000006_WD_MAIN__13$', arg3='3000') # 이벤트UI : 무지개 달팽이를 던져 악령을 공격하세요!

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[201]):
            add_balloon_talk(spawnId=201, msg='$84000006_WD__84000006_WD_MAIN__14$', duration=3000, delayTick=1000)
            set_timer(timerId='4', seconds=20, clearAtZero=False, display=False)
            return Pinata_Kill()
        if time_expired(timerId='3'):
            add_balloon_talk(spawnId=201, msg='$84000006_WD__84000006_WD_MAIN__15$', duration=3000, delayTick=1000)
            set_timer(timerId='4', seconds=20, clearAtZero=False, display=False)
            return Pinata_noKill()


# 전투종료 : 악령퇴치 성공
class Pinata_Kill(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[201]) # 악령 피냐타 사라짐
        end_mini_game_round(winnerBoxId=9001, expRate=0.1) # 라운드 승리: EXP지급량 ME10%
        end_mini_game(winnerBoxId=9001, gameName='PinataWD') # 미니게임 승리 및 로그생성
        add_buff(boxIds=[9001], skillId=70000019, level=1) # 15분버프:에레브 여제의 가호

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return Pinata_Revive()


#  전투종료 : 악령퇴치 실패 
class Pinata_noKill(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[201]) # 악령 피냐타 사라짐
        end_mini_game_round(winnerBoxId=9002, expRate=0.1) # 라운드 패배
        end_mini_game(winnerBoxId=9002, gameName='PinataWD') # 미니게임 패배 및 로그생성

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return Pinata_Revive2()


# 성공 후 레인보우 유니콘 피냐타 리젠
class Pinata_Revive(state.State):
    def on_enter(self):
        set_ambient_light(primary=[255,255,255]) # 조명 원상 복구
        set_user_value(triggerId=1004, key='Interaction', value=2) # UV발사: IntObj OFF
        set_event_ui(type=3, arg2='$84000006_WD__84000006_WD_MAIN__16$', arg3='3000', arg4='9001') # 승리UI
        set_event_ui(type=4, arg2='$84000006_WD__84000006_WD_MAIN__17$', arg3='3000', arg4='!9001') # 패배UI
        create_monster(spawnIds=[101], arg2=False) # NPC 레인보우 피냐타 리젠
        create_monster(spawnIds=[103], arg2=False) # NPC 콘대르 리젠
        set_effect(triggerIds=[3001], visible=True) # NPC 레인보우 피냐타 이펙트
        add_balloon_talk(spawnId=101, msg='$84000006_WD__84000006_WD_MAIN__18$', duration=5000, delayTick=100) # NPC 레인보우 피냐타 대사: 구해주셔서 고마워요!\n결혼 축하해요!
        add_balloon_talk(spawnId=103, msg='$84000006_WD__84000006_WD_MAIN__19$', duration=20000, delayTick=1000) # NPC 콘대르 대사 : 오늘도 승리로군!
        set_ambient_light(primary=[255,255,255])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return Pinata_Fireworks()


# 실패 후 레인보우 유니콘 피냐타 리젠
class Pinata_Revive2(state.State):
    def on_enter(self):
        set_ambient_light(primary=[255,255,255]) # 조명 원상 복구
        set_user_value(triggerId=1004, key='Interaction', value=2) # UV발사: IntObj OFF
        set_event_ui(type=3, arg2='$84000006_WD__84000006_WD_MAIN__20$', arg3='3000', arg4='9002') # 승리 UI
        set_event_ui(type=4, arg2='$84000006_WD__84000006_WD_MAIN__21$', arg3='3000', arg4='!9002') # 패배 UI
        create_monster(spawnIds=[101], arg2=False) # NPC 레인보우 피냐타 리젠
        create_monster(spawnIds=[103], arg2=False) # NPC 콘대르 리젠
        set_effect(triggerIds=[3001], visible=True) # NPC 레인보우 피냐타 이펙트
        add_balloon_talk(spawnId=101, msg='$84000006_WD__84000006_WD_MAIN__22$', duration=5000, delayTick=100) # NPC 레인보우 피냐타 대사: 구해주셔서 고마워요!\n결혼 축하해요!
        add_balloon_talk(spawnId=103, msg='$84000006_WD__84000006_WD_MAIN__23$', duration=20000, delayTick=1000) # NPC 콘대르 대사 : 오늘도 승리로군!

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return Pinata_Fireworks()


#  불꽃놀이 타임
class Pinata_Fireworks(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[5002,5001], returnView=True) # 불꽃놀이 전용 카메라 경로 이동
        set_user_value(triggerId=1002, key='Fireworks', value=1) # 센서: Fireworks.xml의 불꽃놀이 연출 시작

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=11000):
            return Finale()


#  마무리 사교시간 
class Finale(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8022,8023,8024], visible=False, arg3=0, arg4=0, arg5=0) # 입장문 개방 : 메쉬를 끄는 방식
        set_portal(portalId=10001, visible=False, enabled=False, minimapVisible=False) # 결혼식장 복귀 포탈 설정
        set_portal(portalId=10002, visible=True, enabled=True, minimapVisible=True) # 결혼식장 복귀 포탈 설정
        set_user_value(triggerId=1001, key='Conder', value=1) # 콘대르 대사 셋 변경
        add_buff(boxIds=[9002], skillId=99940042, level=1, arg4=False, arg5=True) # 불꽃놀이 스킬셋 제공
        set_event_ui(type=1, arg2='$84000006_WD__84000006_WD_MAIN__24$', arg3='3000') # UI 팝업 : 잠시 후 애프터파티가 종료됩니다
        set_timer(timerId='5', seconds=150, clearAtZero=False, display=True) # 타이머5 설정 : 60초. 현재는 테스트 때문에 10초
        add_balloon_talk(spawnId=101, msg='$84000006_WD__84000006_WD_MAIN__25$', duration=5000, delayTick=3000) # NPC 레인보우 피냐타: 남은 시간,\n친구들과 재밌게 보내세요!
        add_balloon_talk(spawnId=103, msg='$84000006_WD__84000006_WD_MAIN__26$', duration=5000, delayTick=3000) # NPC 콘대르 : 하하하! 지금부터 파티타임!
        set_photo_studio(isEnable=True) # 신규개발기능: 자유 사진 촬영 기능 ON

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return Return()


#  결혼식장 복귀 
class Return(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            room_expire()
            return EndGame()


class EndGame(state.State):
    pass


