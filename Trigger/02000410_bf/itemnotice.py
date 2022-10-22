""" trigger/02000410_bf/itemnotice.xml """
from common import *
import state


class Ready(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=750, boxId=1):
            return 전투시작()


class 전투시작(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='ItemNotice01', value=1):
            return 필수아이템01()


class 필수아이템01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20041008, textId=20041008) # 부활불가 되었고 이제 파티가 전멸되면 게임오버 된다는 내여을 시스템메시지를 통해서 알려줌, 참고로 파티원전멸 체크 트리거는 ClearCheck.xml 이것임

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 다음대기()

    def on_exit(self):
        hide_guide_summary(entityId=20041008)


class 다음대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='ItemNotice02', value=1):
            return 필수아이템02()


class 필수아이템02(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20041009, textId=20041009) # 부활불가 되었고 이제 파티가 전멸되면 게임오버 된다는 내여을 시스템메시지를 통해서 알려줌, 참고로 파티원전멸 체크 트리거는 ClearCheck.xml 이것임

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 종료()

    def on_exit(self):
        hide_guide_summary(entityId=20041009)


class 종료(state.State):
    pass


