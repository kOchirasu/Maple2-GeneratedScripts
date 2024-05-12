""" trigger/84000016_wd/84000016_wait.xml """
import trigger_api


class 초기화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='Weddingceremonyfail', value=0) # 초기화

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 시작_타이머설정(self.ctx)


class 시작_타이머설정(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='4000', seconds=2100, startDelay=1, interval=0) # 시간 내 입장 안 하면 취소

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 위치세팅(self.ctx)


class 위치세팅(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.wedding_move_user(entryType='Guest', mapId=84000016, portalIds=[22,23], boxId=701) # 하객들은 22,23번으로 랜덤이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.wedding_entry_in_field(entryType='GroomBride', isInField=True):
            # 신랑신부 모두 입장했나 체크
            return 둘다입장(self.ctx)
        if self.time_expired(timerId='4000'):
            # 트리거모델4000(여기 맨 위에 설정한 10분)에서 건 타이머 시간 내에 결혼식이 시작 안 되면 결혼식장 폐쇄 준비
            return 강퇴안내(self.ctx)


class 위치돌림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.wedding_move_user(entryType='Guest', mapId=84000016, portalIds=[22,23], boxId=701) # 하객들은 22,23번으로 랜덤이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 위치세팅(self.ctx)


class 대기01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entityId=28400131, textId=28400131) # 두사람 입장하길 기다리고 있다는 메시지

    def on_tick(self) -> trigger_api.Trigger:
        if self.wedding_entry_in_field(entryType='GroomBride', isInField=True):
            # 신랑신부 모두 입장했나 체크
            return 둘다입장(self.ctx)
        if self.time_expired(timerId='4000'):
            # 트리거모델4000(여기 맨 위에 설정한 10분)에서 건 타이머 시간 내에 결혼식이 시작 안 되면 결혼식장 폐쇄 준비
            return 강퇴안내(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entityId=28400131)


class 둘다입장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entityId=28400133, textId=28400133) # 주례에게 말걸라는 메시지
        self.set_user_value(key='StartWedding', value=0) # 결혼시작확인 초기화

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StartWedding', value=1):
            # 주례에게 말 걸어 결혼식 시작하기로 할 때 npcscriptfunction에서 triggervalue 컬럼에 입력된 값을 쏨(setuservalue와 같은 역할). 이 값을 받은 경우 다음 state로 넘긴다.
            return 결혼확인띄우기(self.ctx)
        if self.time_expired(timerId='4000'):
            # 트리거모델4000(여기 맨 위에 설정한 10분)에서 건 타이머 시간 내에 결혼식이 시작 안 되면 결혼식장 폐쇄 준비
            return 강퇴안내(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entityId=28400133)


class 결혼확인띄우기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 결혼식 시작여부 투표 ui(결혼을 시작하시겠습니까?) 띄우기
        self.wedding_mutual_agree(agreeType='startActing')
        # 하객 옮기기 시작하라고 moveguest에 쏘는 신호
        self.set_user_value(triggerId=4002, key='Weddingceremonystartsready', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 결혼시작체크(self.ctx)


class 결혼시작체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wedding_entry_in_field(entryType='GroomBride', isInField=False):
            # 신랑신부 중 나간 사람 없나 체크. 만약 나간 사람이 있으면
            return 대기01(self.ctx)
        if self.wedding_mutual_agree_result(agreeType='startActing', success=True):
            # 결혼식 시작에 동의했으면 wait xml에서 10분 타이머, 신랑신부 입장체크는 완전 종료시킴
            return 결혼식연출진행중(self.ctx)
        if self.wedding_mutual_agree_result(agreeType='startActing', success=False):
            # 결혼식 시작에 동의 안했으면 wait xml에서 10분 타이머, 신랑신부 입장체크 계속 하도록 돌려보냄
            return 대기01(self.ctx)
        if self.time_expired(timerId='4000'):
            # 트리거모델4000(여기 맨 위에 설정한 10분)에서 건 타이머 시간 내에 결혼식이 완료 안 되면
            return 강퇴안내(self.ctx)

    def on_exit(self) -> None:
        self.wedding_move_user(entryType='Guest', mapId=84000016, portalIds=[22,23], boxId=701)
        # 701번 박스(버진로드)에 있는 하객들은 21,22,23번으로 랜덤이동


class 강퇴안내(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entityId=28400132, textId=28400132) # 결혼식장 폐쇄 안내
        # 쌍방 결혼식장 미진입으로 인한 파토 처리 선언 / 로그용
        self.wedding_broken()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 강퇴(self.ctx)


class 강퇴(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entityId=28400132)
        self.move_user(mapId=0, portalId=0)


class 결혼식연출진행중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=4001, key='Weddingceremonystarts', value=1) # 연출 시작하라고 main에 쏘는 신호

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Weddingceremonyfail', value=1):
            # 결혼 실패
            self.set_user_value(key='Weddingceremonyfail', value=0) # 초기화
            return 위치세팅(self.ctx)
        if self.wedding_hall_state(hallState='weddingComplete'):
            # 결혼 연출 끝나서 보상받고 종료
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 초기화
