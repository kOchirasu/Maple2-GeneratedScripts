""" trigger/02000551_bf/battlezone.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_tick(self) -> state.State:
        if check_user():
            return 트리거작동시작()


class 트리거작동시작(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=13, spawnIds=[101]):
            return 중앙전투판신호()
        if npc_detected(boxId=12, spawnIds=[101]):
            return 시전투판신호12()
        if npc_detected(boxId=3, spawnIds=[101]):
            return 시전투판신호3()
        if npc_detected(boxId=6, spawnIds=[101]):
            return 시전투판신호6()
        if npc_detected(boxId=9, spawnIds=[101]):
            return 시전투판신호9()
        if npc_detected(boxId=122, spawnIds=[101]):
            return 봄컨셉도로신호()
        if npc_detected(boxId=45, spawnIds=[101]):
            return 여름컨셉도로신호()
        if npc_detected(boxId=78, spawnIds=[101]):
            return 가을컨셉도로신호()
        if npc_detected(boxId=1011, spawnIds=[101]): # arg2은 몬스터 스폰ID 102는 쉬운 난이도
            return 겨울컨셉도로신호()
        if npc_detected(boxId=13, spawnIds=[102]):
            return 중앙전투판신호()
        if npc_detected(boxId=12, spawnIds=[102]):
            return 시전투판신호12()
        if npc_detected(boxId=3, spawnIds=[102]):
            return 시전투판신호3()
        if npc_detected(boxId=6, spawnIds=[102]):
            return 시전투판신호6()
        if npc_detected(boxId=9, spawnIds=[102]):
            return 시전투판신호9()
        if npc_detected(boxId=122, spawnIds=[102]):
            return 봄컨셉도로신호()
        if npc_detected(boxId=45, spawnIds=[102]):
            return 여름컨셉도로신호()
        if npc_detected(boxId=78, spawnIds=[102]):
            return 가을컨셉도로신호()
        if npc_detected(boxId=1011, spawnIds=[102]):
            return 겨울컨셉도로신호()
        if wait_tick(waitTick=2200):
            return 시간경과대기()


class 시간경과대기(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 트리거작동시작()


class 중앙전투판신호(state.State):
    def on_enter(self):
        set_ai_extra_data(key='BattleZonePosition', value=13) # 보스AI에게 이 변수 13 신호를 보내서 보스가 중앙 전투판에 들어셨음을 알림,  즉 AI_CarParadeBlackbean.xml 혹은 AI_CarParadeBlackbeanBroken.xml 혹은 AI_Blackbean_Phase01.xml 에게 보냄

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 트리거작동시작()


class 시전투판신호12(state.State):
    def on_enter(self):
        set_ai_extra_data(key='BattleZonePosition', value=12) # 보스AI에게 이 변수 12 신호를 보내서 보스가 12시쪽 전투판에 들어셨음을 알림,  즉 AI_CarParadeBlackbean.xml 혹은 AI_CarParadeBlackbeanBroken.xml 혹은 AI_Blackbean_Phase01.xml 에게 보냄

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 트리거작동시작()


class 시전투판신호3(state.State):
    def on_enter(self):
        set_ai_extra_data(key='BattleZonePosition', value=3) # 보스AI에게 이 변수 3 신호를 보내서 보스가 3시쪽 전투판에 들어셨음을 알림,  즉 AI_CarParadeBlackbean.xml 혹은 AI_CarParadeBlackbeanBroken.xml 혹은 AI_Blackbean_Phase01.xml 에게 보냄

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 트리거작동시작()


class 시전투판신호6(state.State):
    def on_enter(self):
        set_ai_extra_data(key='BattleZonePosition', value=6) # 보스AI에게 이 변수 6 신호를 보내서 보스가 6시쪽 전투판에 들어셨음을 알림,  즉 AI_CarParadeBlackbean.xml 혹은 AI_CarParadeBlackbeanBroken.xml 혹은 AI_Blackbean_Phase01.xml 에게 보냄

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 트리거작동시작()


class 시전투판신호9(state.State):
    def on_enter(self):
        set_ai_extra_data(key='BattleZonePosition', value=9) # 보스AI에게 이 변수 9 신호를 보내서 보스가 9시쪽 전투판에 들어셨음을 알림,  즉 AI_CarParadeBlackbean.xml 혹은 AI_CarParadeBlackbeanBroken.xml 혹은 AI_Blackbean_Phase01.xml 에게 보냄

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 트리거작동시작()


class 봄컨셉도로신호(state.State):
    def on_enter(self):
        set_ai_extra_data(key='BattleZonePosition', value=122) # 보스AI에게 이 변수 122 신호를 보내서 보스가 봄 컨셉 도로 중앙에 들어셨음을 알림,  즉 AI_CarParadeBlackbean.xml 혹은 AI_CarParadeBlackbeanBroken.xml 혹은 AI_Blackbean_Phase01.xml 에게 보냄

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 트리거작동시작()


class 여름컨셉도로신호(state.State):
    def on_enter(self):
        set_ai_extra_data(key='BattleZonePosition', value=45) # 보스AI에게 이 변수 45 신호를 보내서 보스가 여름 컨셉 도로 중앙에 들어셨음을 알림,  즉 AI_CarParadeBlackbean.xml 혹은 AI_CarParadeBlackbeanBroken.xml 혹은 AI_Blackbean_Phase01.xml 에게 보냄

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 트리거작동시작()


class 가을컨셉도로신호(state.State):
    def on_enter(self):
        set_ai_extra_data(key='BattleZonePosition', value=78) # 보스AI에게 이 변수 78 신호를 보내서 보스가 가을 컨셉 도로 중앙에 들어셨음을 알림,  즉 AI_CarParadeBlackbean.xml 혹은 AI_CarParadeBlackbeanBroken.xml 혹은 AI_Blackbean_Phase01.xml 에게 보냄

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 트리거작동시작()


class 겨울컨셉도로신호(state.State):
    def on_enter(self):
        set_ai_extra_data(key='BattleZonePosition', value=1011) # 보스AI에게 이 변수 1011 신호를 보내서 보스가 겨울 컨셉 도로 중앙에 들어셨음을 알림,  즉 AI_CarParadeBlackbean.xml 혹은 AI_CarParadeBlackbeanBroken.xml 혹은 AI_Blackbean_Phase01.xml 에게 보냄

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 트리거작동시작()


class 종료(state.State):
    pass


