""" trigger/02000336_bf/boss.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90,92,93])
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False) # 보상으로 연결되는 포탈 제어 (끔)
        set_effect(triggerIds=[7001], visible=False)

    def on_tick(self) -> state.State:
        if count_users(boxId=701, boxId=1):
            return 시작_01()


class 시작_01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7015], visible=True)
        create_monster(spawnIds=[101])

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 조직원등장()


class 조직원등장(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7001], visible=True)
        set_mesh(triggerIds=[8041,8042,8043,8044], visible=False, arg4=0, arg5=10) # 벽 해제
        set_skill(triggerIds=[5801], isEnable=True) # 벽 날리는 스킬
        create_monster(spawnIds=[181,182,183])
        set_timer(timerId='2', seconds=2, display=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 웨이홍_대사01()


class 웨이홍_대사01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91])
        destroy_monster(spawnIds=[90])
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=8001, enable=True)
        set_conversation(type=2, spawnId=11003124, script='$02000336_BF__BOSS__0$', arg4=3) # 웨이홍 대사
        set_skip(state=웨이홍_대사02)
        set_timer(timerId='3', seconds=3, display=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 웨이홍_대사02()

    def on_exit(self):
        remove_cinematic_talk()


class 웨이홍_대사02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11003124, script='$02000336_BF__BOSS__1$', arg4=3) # 웨이홍 대사
        set_skip(state=종료)
        set_timer(timerId='3', seconds=3, display=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 종료()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=7)


class 종료(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=112, textId=40009) # 포탈을 타세요
        select_camera(triggerId=8001, enable=False)
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True) # 보상으로 연결되는 포탈 제어 (켬)


