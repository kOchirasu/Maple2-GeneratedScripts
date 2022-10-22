""" trigger/02010086_bf/boss.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=799, boxId=1):
            return 시작()


class 시작(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[995,999,998])
        create_monster(spawnIds=[199], arg2=True) # (임시) 보스몹 스폰
        set_timer(timerId='10', seconds=10)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[199]):
            return 포탈_개방()
        if time_expired(timerId='10'):
            return 소환_01()


class 소환_01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[181,188], arg2=True) # (임시) 보스몹 스폰
        set_timer(timerId='10', seconds=10)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[199]):
            return 포탈_개방()
        if time_expired(timerId='10'):
            return 소환_02()


class 소환_02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[182,187], arg2=True) # (임시) 보스몹 스폰
        set_timer(timerId='10', seconds=10)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[199]):
            return 포탈_개방()
        if time_expired(timerId='10'):
            return 소환_03()


class 소환_03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[183,186], arg2=True) # (임시) 보스몹 스폰
        set_timer(timerId='10', seconds=10)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[199]):
            return 포탈_개방()
        if time_expired(timerId='10'):
            return 소환_04()


class 소환_04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[184,185], arg2=True) # (임시) 보스몹 스폰
        set_timer(timerId='20', seconds=20)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[199]):
            return 포탈_개방()
        if time_expired(timerId='20'):
            return 소환_05()


class 소환_05(state.State):
    def on_enter(self):
        create_monster(spawnIds=[996], arg2=True) # (임시) 보스몹 스폰

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[199]):
            return 포탈_개방()


class 포탈_개방(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[181,182,183,184,185,186,187,188,997,996,995])
        play_system_sound_in_box(sound='System_Space_PopUp_01')
        show_guide_summary(entityId=112, textId=40009) # 포탈을 타세요
        set_mesh(triggerIds=[1098], visible=False, arg4=0, arg5=10) # 벽 해제
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True) # 포탈 개방

    def on_exit(self):
        hide_guide_summary(entityId=112)


