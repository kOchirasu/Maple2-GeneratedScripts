""" trigger/02020147_bf/bossdeathmessage.xml """
from common import *
import state


class Ready(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=601, boxId=1):
            return 변수초기화()


class 변수초기화(state.State):
    def on_enter(self):
        set_user_value(key='DeathIshuraRbladerDark', value=0)
        set_user_value(key='DeathRenduebianRbladerDark', value=0)
        set_user_value(key='DeathYuperiaRbladerDark', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 신호받기대기중()


class 신호받기대기중(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='DeathIshuraRbladerDark', value=1):
            return 이슈라죽음알림()
        if user_value(key='DeathRenduebianRbladerDark', value=1):
            return 렌듀비앙죽음알림()
        if user_value(key='DeathYuperiaRbladerDark', value=1):
            return 유페리아죽음알림()


class 이슈라죽음알림(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20051002, textId=20051002) # 이슈라의 죽음을 이 UI 메시지로 알려주기
        set_user_value(key='DeathIshuraRbladerDark', value=0) # 변수 0으로 초기화 하기, 이거 안하면 무한루프에 걸림

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3200): # 이슈라 죽음 메시지 출력 도중에 다른 보스가 죽었을 경우에 대한 처리
            return 신호받기대기중()
        if user_value(key='DeathRenduebianRbladerDark', value=1):
            return 렌듀비앙죽음알림()
        if user_value(key='DeathYuperiaRbladerDark', value=1):
            return 유페리아죽음알림()

    def on_exit(self):
        hide_guide_summary(entityId=20051002)


class 렌듀비앙죽음알림(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20051003, textId=20051003) # 렌듀비앙의 죽음을 이 UI 메시지로 알려주기
        set_user_value(key='DeathRenduebianRbladerDark', value=0) # 변수 0으로 초기화 하기, 이거 안하면 무한루프에 걸림

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3200): # 렌듀비앙 죽음 메시지 출력 도중에 다른 보스가 죽었을 경우에 대한 처리
            return 신호받기대기중()
        if user_value(key='DeathIshuraRbladerDark', value=1):
            return 이슈라죽음알림()
        if user_value(key='DeathYuperiaRbladerDark', value=1):
            return 유페리아죽음알림()

    def on_exit(self):
        hide_guide_summary(entityId=20051003)


class 유페리아죽음알림(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20051004, textId=20051004) # 유페리아의 죽음을 이 UI 메시지로 알려주기
        set_user_value(key='DeathYuperiaRbladerDark', value=0) # 변수 0으로 초기화 하기, 이거 안하면 무한루프에 걸림

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3200): # 유페리아 죽음 메시지 출력 도중에 다른 보스가 죽었을 경우에 대한 처리
            return 신호받기대기중()
        if user_value(key='DeathIshuraRbladerDark', value=1):
            return 이슈라죽음알림()
        if user_value(key='DeathRenduebianRbladerDark', value=1):
            return 렌듀비앙죽음알림()

    def on_exit(self):
        hide_guide_summary(entityId=20051004)


