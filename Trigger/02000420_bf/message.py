""" trigger/02000420_bf/message.xml """
from common import *
import state


class 전투시작(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Message', value=1):
            return 메시지출력01()


class 메시지출력01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20042001, textId=20042001) # "파풀라투스의 보호막은 태엽 폭탄을 던져 제거해야 합니다." 메시지 출력

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 메시지출력02대기()

    def on_exit(self):
        hide_guide_summary(entityId=20042001)


class 메시지출력02대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Message', value=2):
            return 메시지출력02()


class 메시지출력02(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20042002, textId=20042002) # "연산 큐브를 밟아서 보호막 유지 시간을 조절해야 합니다." 메시지 출력

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 메시지출력03대기()

    def on_exit(self):
        hide_guide_summary(entityId=20042002)


class 메시지출력03대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Message', value=3):
            return 메시지출력03()


class 메시지출력03(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20042003, textId=20042003) # "떨어지는 물체로 바닥 유리를 파괴하여 태엽 폭탄을 꺼내야 합니다."  메시지 출력

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 종료()

    def on_exit(self):
        hide_guide_summary(entityId=20042003)


class 종료(state.State):
    pass


