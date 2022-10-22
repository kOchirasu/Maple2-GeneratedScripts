""" trigger/02000352_bf/main.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_portal(portalId=11, visible=False, enabled=False, minimapVisible=False)
        set_effect(triggerIds=[900001], visible=False) # Sound EFfect Off
        set_effect(triggerIds=[900002], visible=False) # Sound EFfect Off
        set_effect(triggerIds=[900003], visible=False) # Sound EFfect Off
        set_effect(triggerIds=[900004], visible=False) # Sound EFfect Off
        set_effect(triggerIds=[900005], visible=False) # Sound EFfect Off
        set_interact_object(triggerIds=[10000822], state=0)

    def on_tick(self) -> state.State:
        if count_users(boxId=701, boxId=1):
            return 관문01_시작()
        if count_users(boxId=703, boxId=1):
            return 관문_03_시작()


class 관문01_시작(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_Space_PopUp_01')
        show_guide_summary(entityId=110, textId=40010) # 적을 모두 처치하세요
        create_monster(spawnIds=[11,12,13,14,15,16,17], arg2=False) # 기본 배치 될 몬스터 등장

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[11,12,13,14,15,16,17]):
            return 관문_01_개방()

    def on_exit(self):
        hide_guide_summary(entityId=110)


class 관문_01_개방(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000822], state=1)

    def on_tick(self) -> state.State:
        if count_users(boxId=702, boxId=1):
            return 관문_02_시작()


class 관문_02_시작(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_Space_PopUp_01')
        show_guide_summary(entityId=110, textId=40010) # 적을 모두 처치하세요
        create_monster(spawnIds=[21,22,23,24,25,26,27,28,29], arg2=False) # 기본 배치 될 몬스터 등장

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[21,22,23,24,25,26,27,28,29]):
            return 관문_02_개방()

    def on_exit(self):
        hide_guide_summary(entityId=110)


class 관문_02_개방(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_Space_PopUp_01')
        show_guide_summary(entityId=111, textId=20000080) # 스위치를 정지하세요
        set_interact_object(triggerIds=[10000823], state=1)
        set_interact_object(triggerIds=[10000824], state=1)

    def on_tick(self) -> state.State:
        if count_users(boxId=703, boxId=1):
            return 관문_03_시작()

    def on_exit(self):
        hide_guide_summary(entityId=111)


class 관문_03_시작(state.State):
    def on_enter(self):
        create_monster(spawnIds=[31,32,33], arg2=False) # 기본 배치 될 몬스터 등장

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[31,32]):
            return 관문_03_개방()


class 관문_03_개방(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[6004], visible=False, arg4=0, arg5=10) # 벽 해제
        set_mesh(triggerIds=[6007], visible=True, arg4=0, arg5=10) # 화살표 표시
        play_system_sound_in_box(sound='System_Space_PopUp_01')
        show_guide_summary(entityId=112, textId=40009) # 포탈을 타세요
        set_portal(portalId=11, visible=True, enabled=True, minimapVisible=True)


