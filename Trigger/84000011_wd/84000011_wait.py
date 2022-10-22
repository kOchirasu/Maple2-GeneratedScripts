""" trigger/84000011_wd/84000011_wait.xml """
from common import *
import state


class 초기화(state.State):
    def on_enter(self):
        set_user_value(key='Weddingceremonyfail', value=0) # 초기화

    def on_tick(self) -> state.State:
        if true():
            return 시작_타이머설정()


class 시작_타이머설정(state.State):
    def on_enter(self):
        set_timer(timerId='4000', seconds=2100, clearAtZero=True, display=False) # 시간 내 입장 안 하면 취소

    def on_tick(self) -> state.State:
        if true():
            return 위치세팅()


class 위치세팅(state.State):
    def on_enter(self):
        wedding_move_user(entryType='Guest', mapId=84000011, portalIds=[22,23], boxId=701) # 하객들은 22,23번으로 랜덤이동

    def on_tick(self) -> state.State:
        if wedding_entry_in_field(entryType='GroomBride', isInField=True):
            return 둘다입장()
        if time_expired(timerId='4000'):
            return 강퇴안내()


class 위치돌림(state.State):
    def on_enter(self):
        wedding_move_user(entryType='Guest', mapId=84000011, portalIds=[22,23], boxId=701) # 하객들은 22,23번으로 랜덤이동

    def on_tick(self) -> state.State:
        if true():
            return 위치세팅()


class 대기01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=28400131, textId=28400131) # 두사람 입장하길 기다리고 있다는 메시지

    def on_tick(self) -> state.State:
        if wedding_entry_in_field(entryType='GroomBride', isInField=True):
            return 둘다입장()
        if time_expired(timerId='4000'):
            return 강퇴안내()

    def on_exit(self):
        hide_guide_summary(entityId=28400131)


class 둘다입장(state.State):
    def on_enter(self):
        show_guide_summary(entityId=28400133, textId=28400133) # 주례에게 말걸라는 메시지
        set_user_value(key='StartWedding', value=0) # 결혼시작확인 초기화

    def on_tick(self) -> state.State:
        if user_value(key='StartWedding', value=1):
            return 결혼확인띄우기()
        if time_expired(timerId='4000'):
            return 강퇴안내()

    def on_exit(self):
        hide_guide_summary(entityId=28400133)


class 결혼확인띄우기(state.State):
    def on_enter(self):
        wedding_mutual_agree(agreeType='startActing') # 결혼식 시작여부 투표 ui(결혼을 시작하시겠습니까?) 띄우기
        set_user_value(triggerId=4002, key='Weddingceremonystartsready', value=1) # 하객 옮기기 시작하라고 moveguest에 쏘는 신호

    def on_tick(self) -> state.State:
        if true():
            return 결혼시작체크()


class 결혼시작체크(state.State):
    def on_tick(self) -> state.State:
        if wedding_entry_in_field(entryType='GroomBride', isInField=False):
            return 대기01()
        if wedding_mutual_agree_result(agreeType='startActing', success=True):
            return 결혼식연출진행중()
        if wedding_mutual_agree_result(agreeType='startActing', success=False):
            return 대기01()
        if time_expired(timerId='4000'):
            return 강퇴안내()

    def on_exit(self):
        wedding_move_user(entryType='Guest', mapId=84000011, portalIds=[22,23], boxId=701) # 701번 박스(버진로드)에 있는 하객들은 21,22,23번으로 랜덤이동


class 강퇴안내(state.State):
    def on_enter(self):
        show_guide_summary(entityId=28400132, textId=28400132) # 결혼식장 폐쇄 안내
        wedding_broken() # 쌍방 결혼식장 미진입으로 인한 파토 처리 선언 / 로그용

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 강퇴()


class 강퇴(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=28400132)
        move_user(mapId=0, portalId=0)


class 결혼식연출진행중(state.State):
    def on_enter(self):
        set_user_value(triggerId=4001, key='Weddingceremonystarts', value=1) # 연출 시작하라고 main에 쏘는 신호

    def on_tick(self) -> state.State:
        if user_value(key='Weddingceremonyfail', value=1):
            set_user_value(key='Weddingceremonyfail', value=0)
            return 위치세팅()
        if wedding_hall_state(hallState='weddingComplete'):
            return 종료()


class 종료(state.State):
    pass


