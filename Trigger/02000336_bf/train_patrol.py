""" trigger/02000336_bf/train_patrol.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7002], visible=False)
        set_effect(triggerIds=[7003], visible=False)
        set_effect(triggerIds=[7004], visible=False)
        set_mesh(triggerIds=[16004], visible=False, arg4=0, arg5=0) # 벽 해제

    def on_tick(self) -> state.State:
        if count_users(boxId=704, boxId=1):
            return 패트롤_01()
        if count_users(boxId=707, boxId=1):
            return 패트롤_03()


class 패트롤_01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[147,148,149], arg2=False) # 기본 배치 될 몬스터 등장

    def on_tick(self) -> state.State:
        if count_users(boxId=707, boxId=1):
            return 패트롤_03()


class 패트롤_02(state.State):
    pass


class 패트롤_03(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=105, textId=20003361) # 키 몬스터를 처치하세요.
        create_monster(spawnIds=[191,192,193,194,195,196,197,198], arg2=False)
        set_effect(triggerIds=[7002], visible=True)
        set_skill(triggerIds=[5803], isEnable=True) # 벽 날리는 스킬
        set_skill(triggerIds=[5804], isEnable=True) # 벽 날리는 스킬
        set_skill(triggerIds=[5805], isEnable=True) # 벽 날리는 스킬

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[196]):
            return 관문_03_개방()

    def on_exit(self):
        hide_guide_summary(entityId=105)


class 관문_03_개방(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=106, textId=20003362, duration=3000) # 다음 구역으로 이동할 수 있습니다.
        set_mesh(triggerIds=[8030,8031,8032,8033,8034], visible=False, arg4=0, arg5=10) # 벽 해제


