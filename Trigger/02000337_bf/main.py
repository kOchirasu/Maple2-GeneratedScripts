""" trigger/02000337_bf/main.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=False) # 기본 배치 될 몬스터 등장
        set_effect(triggerIds=[7301], visible=False)
        set_effect(triggerIds=[7302], visible=False)
        set_effect(triggerIds=[7303], visible=False)
        set_effect(triggerIds=[7304], visible=False)
        set_effect(triggerIds=[7305], visible=False)
        set_effect(triggerIds=[7310], visible=True)

    def on_tick(self) -> state.State:
        if count_users(boxId=701, boxId=1):
            return 폭발01()


class 폭발01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7301], visible=True) # 폭발 이펙트
        set_skill(triggerIds=[8301], isEnable=True) # 벽 날리는 스킬

    def on_tick(self) -> state.State:
        if count_users(boxId=702, boxId=1):
            return 폭발02()


class 폭발02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7302], visible=True) # 폭발 이펙트
        set_skill(triggerIds=[8302], isEnable=True) # 벽 날리는 스킬

    def on_tick(self) -> state.State:
        if count_users(boxId=703, boxId=1):
            return 폭발03()


class 폭발03(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7303], visible=True) # 폭발 이펙트
        set_effect(triggerIds=[7304], visible=True) # 폭발 이펙트
        set_skill(triggerIds=[8303], isEnable=True) # 벽 날리는 스킬
        set_skill(triggerIds=[8304], isEnable=True) # 벽 날리는 스킬

    def on_tick(self) -> state.State:
        if count_users(boxId=704, boxId=1):
            return 폭발04()


class 폭발04(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7305], visible=True) # 폭발 이펙트
        set_skill(triggerIds=[8305], isEnable=True) # 벽 날리는 스킬

    def on_tick(self) -> state.State:
        if count_users(boxId=705, boxId=1):
            return 폭발04()


