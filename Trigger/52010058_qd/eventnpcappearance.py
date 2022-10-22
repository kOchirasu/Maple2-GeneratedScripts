""" trigger/52010058_qd/eventnpcappearance.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_tick(self) -> state.State:
        if true():
            return 보스등장대기()


class 보스등장대기(state.State):
    def on_enter(self):
        create_monster(spawnIds=[111], arg2=True)
        create_monster(spawnIds=[121], arg2=True)
        create_monster(spawnIds=[131], arg2=True)

    def on_tick(self) -> state.State:
        if user_value(key='EventNpcAppearance', value=1):
            return 우호적NPC등장()


class 우호적NPC등장(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[111], arg2=True)
        destroy_monster(spawnIds=[121], arg2=True)
        destroy_monster(spawnIds=[131], arg2=True) # 함교 안에 있었던  우호적 NPC 3인방이 전투판으로 나와 전투를 진행한다는 설정에 맞추어 전투판에 우호적 NPC 3인방을 등장시킴
        create_monster(spawnIds=[11], arg2=True)
        create_monster(spawnIds=[21], arg2=True)
        create_monster(spawnIds=[31], arg2=True) # 참고로 이 우호적 NPC 3인방 제거는 보스 몬스터가 죽을 때 AI 에서 신호 보내서 제거하는 방식을 사용함

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return 대기()


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='EventNpcAppearance', value=2):
            return 시작대기중()


