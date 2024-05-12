""" trigger/84000013_wd/84000013_main.xml """
import trigger_api


class 초기화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='Weddingceremonystarts', value=0)
        self.set_portal(portalId=99, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 결혼식연출시작요청대기(self.ctx)


class 결혼식연출시작요청대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.lock_my_pc(isLock=False) # PC 움직임 풀어줌 (초기화)
        # 알수없는오류로결혼식재진행필요하다는안내메시지 삭제 / 스트링 ID 신규발급 필요
        self.hide_guide_summary(entityId=28400140)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Weddingceremonystarts', value=1):
            # 결혼하시겠습니까 입력창 띄우자마자 쏘는 신호 받으면 하객옮기기 트리거 시작되도록
            self.set_user_value(key='Weddingceremonystarts', value=0) # 받자마자 초기화
            self.lock_my_pc(isLock=True) # PC 움직임 락
            return 시작알림(self.ctx)


class 시작알림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entityId=28400134, textId=28400134) # 결혼식 시작한다는 메시지

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 연출시작(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entityId=28400134)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        # 799번 박스(입장구역)에 있는 하객들은 22,23번으로 랜덤이동
        self.wedding_move_user(entryType='Guest', mapId=84000013, portalIds=[22,23], boxId=701)
        # 701번 박스(버진로드)에 있는 하객들은 22,23번으로 랜덤이동
        self.wedding_move_user(entryType='Guest', mapId=84000013, portalIds=[22,23], boxId=703)
        self.wedding_move_user(entryType='Groom', mapId=84000013, portalIds=[11], boxId=702) # 신랑 11번으로
        self.wedding_move_user(entryType='Bride', mapId=84000013, portalIds=[12], boxId=702) # 신부는 12번으로
        # 입,출구포털 활성화	/ 중간탈주 케이스 발생할 경우 나갈 수 있도록
        self.set_portal(portalId=99, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 주례줌인01(self.ctx)


class 주례줌인01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(pathIds=[8002,8001], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 주례줌인02(self.ctx)


class 주례줌인02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npcId=11004724, msg='$84000013_WD__84000013_MAIN__0$', duration=3500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 시선돌리기01(self.ctx)


class 시선돌리기01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 세레나데(self.ctx)


class 세레나데(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[102], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return UI테스트(self.ctx)


class UI테스트(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8007], returnView=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 입장준비01(self.ctx)


class 입장준비01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(pathIds=[8009], returnView=False)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 입장준비02(self.ctx)


class 입장준비02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.wedding_set_user_emotion(entryType='Bride', id=6)
        self.wedding_set_user_emotion(entryType='Groom', id=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 입장01(self.ctx)


class 입장01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8004,8005], returnView=False)
        self.wedding_user_to_patrol(patrolName='MS2PatrolData_2001', entryType='Groom', patrolIndex=1) # 신랑 경로이동
        self.wedding_user_to_patrol(patrolName='MS2PatrolData_2002', entryType='Bride', patrolIndex=2) # 신부 경로이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 카메라이동01(self.ctx)


class 카메라이동01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 임시사운드 : 결혼행진곡 들어가면 좋을 듯
        pass

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=17000):
            return 카메라이동02(self.ctx)


class 카메라이동02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.select_camera_path(pathIds=[8006], returnView=False)
        self.destroy_monster(spawnIds=[102]) # 세레나데 끝

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 주례사(self.ctx)


class 주례사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npcId=11004724, msg='$84000013_WD__84000013_MAIN__1$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4500):
            return 성혼타이핑결과확인(self.ctx)


class 성혼타이핑결과확인(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.wedding_mutual_agree(agreeType='partnerName')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=30000):
            # 부부가 30초간 타이핑을 안하는 경우 다시 시작하도록 한다
            self.wedding_mutual_cancel(agreeType='partnerName') # 투표 취소
            return 미입력으로중단01(self.ctx)
        if self.wedding_entry_in_field(entryType='GroomBride', isInField=False):
            # 신랑신부 중 나간 사람 없나 체크
            self.wedding_mutual_cancel(agreeType='partnerName') # 투표 취소 (방어 트리거)
            return 탈주로중단(self.ctx)
        if self.wedding_mutual_agree_result(agreeType='partnerName', success=False):
            # 타이핑 둘 중 하나라도 안 하면 취소로 감 : 제대로 될 때까지 무한루핑
            return 탈주로중단(self.ctx)
        if self.wedding_mutual_agree_result(agreeType='partnerName', success=True):
            # 타이핑 둘 다 하면 성혼 발표로
            return 성혼발표(self.ctx)


class 탈주로중단(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11004724, msg='$84000013_WD__84000013_MAIN__2$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 탈주로중단선언(self.ctx)


class 탈주로중단선언(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11004724, msg='$84000013_WD__84000013_MAIN__3$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 탈주로중단선언리셋(self.ctx)


class 미입력으로중단01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11004724, msg='$84000013_WD__84000013_MAIN__4$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 미입력으로중단선언(self.ctx)


class 미입력으로중단선언(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11004724, msg='$84000013_WD__84000013_MAIN__5$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 탈주로중단선언리셋(self.ctx)


class 탈주로중단선언리셋(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 탈주로 인한 초기화를 moveguest에 쏘는 신호
        self.set_user_value(triggerId=4002, key='Weddingceremonyfail', value=1)
        self.set_user_value(triggerId=4000, key='Weddingceremonyfail', value=1) # 탈주로 인한 초기화를 wait에 쏘는 신호
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 결혼식연출시작요청대기(self.ctx)


class 성혼발표(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11004724, msg='$84000013_WD__84000013_MAIN__6$', duration=2500)
        # 결혼식 완료 후 신랑신부 보상 부여하는 명령
        self.wedding_vow_complete()
        # 결혼식 완료 후 신랑신부 보상 부여하는 명령
        # 결혼식 완료 후 신랑신부 보상 부여하는 명령
        # 하객 옮기기 그만하라고 moveguest에 쏘는 신호
        self.set_user_value(triggerId=4002, key='WeddingFinished', value=1)
        self.wedding_set_user_look_at(entryType='Bride', lookAtEntryType='Groom', immediate=True)
        self.wedding_set_user_look_at(entryType='Groom', lookAtEntryType='Bride', immediate=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 환호성(self.ctx)


class 환호성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8010], returnView=False)
        self.wedding_set_user_emotion(entryType='Bride', id=4)
        self.wedding_set_user_emotion(entryType='Groom', id=4)
        # 임시사운드 : 박수소리, 환호소리 들어가면 좋을 듯
        self.play_system_sound_in_box(sound='System_WeddingAudience_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 뒷풀이01(self.ctx)


class 뒷풀이01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 보상과결혼상태마지막체크(self.ctx)


class 보상과결혼상태마지막체크(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.lock_my_pc(isLock=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wedding_hall_state(hallState='weddingComplete', success=True):
            return 뒷풀이02(self.ctx)
        if self.true():
            return 보상결혼상태체크실패(self.ctx)


class 보상결혼상태체크실패(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 탈주로 인한 초기화를 moveguest에 쏘는 신호
        self.set_user_value(triggerId=4002, key='Weddingceremonyfail', value=1)
        self.set_user_value(triggerId=4000, key='Weddingceremonyfail', value=1) # 탈주로 인한 초기화를 wait에 쏘는 신호
        # 알수없는오류로결혼식재진행필요하다는안내메시지 / 스트링 ID 신규발급 필요
        self.show_guide_summary(entityId=28400140)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 결혼식연출시작요청대기(self.ctx)


class 뒷풀이02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entityId=28400135, textId=28400135) # 기념촬영과뒷풀이 즐기세요 메시지
        self.set_portal(portalId=99, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 뒷풀이03(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entityId=28400135)


class 뒷풀이03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entityId=28400136, textId=28400136) # 주례에게 말 걸어 결혼식 끝내라는 메시지
        self.set_user_value(key='EndWedding', value=0) # 결혼종료확인 초기화

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='EndWedding', value=1):
            return 결혼종료확인(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entityId=28400136)


class 결혼종료확인(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 결혼식 종료여부 투표 ui 띄우기? / npc한테 말을 걸었는지 아닌지를 이걸로 체크할 수 있나? / 시간제한은 어떻게 체크하나?
        self.wedding_mutual_agree(agreeType='endActing')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wedding_entry_in_field(entryType='GroomBride', isInField=False):
            # 신랑신부 중 나간 사람 있으면 바로 결혼식장 폐쇄(종료)로
            return 종료알림(self.ctx)
        if self.wedding_mutual_agree_result(agreeType='endActing', success=True):
            # 결혼식 종료에 동의했으면 바로 결혼식장 폐쇄(종료)로
            return 종료알림(self.ctx)
        """
        if self.time_expired(timerId='8400131'):
            return None # Missing State: 강퇴안내
        """
        if self.wedding_mutual_agree_result(agreeType='endActing', success=False):
            # 결혼식 종료에 동의 안했으면 안내메시지 출력하면서 종료 체크 계속 하도록 직전 스테이트로 돌려보냄
            return 뒷풀이03(self.ctx)

    def on_exit(self) -> None:
        # self.hide_guide_summary(entityId=28400133)
        pass


class 종료알림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entityId=28400137, textId=28400137) # 결혼식장 폐쇄한다는 메시지

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=20000):
            return 끄읏(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entityId=28400137)


class 끄읏(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(mapId=0, portalId=0)


initial_state = 초기화
