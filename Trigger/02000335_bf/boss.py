""" trigger/02000335_bf/boss.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        enable_spawn_point_pc(spawnId=0, isEnable=False)
        enable_spawn_point_pc(spawnId=991, isEnable=True)
        enable_spawn_point_pc(spawnId=992, isEnable=False)
        set_mesh(triggerIds=[6311,6312,6313,6314,6315], visible=True, arg4=1, arg5=1) # 벽 생성
        set_effect(triggerIds=[6921], visible=False) # BG\Common\Eff_Com_ObjectShake.xml
        create_monster(spawnIds=[149], arg2=False) # 기본 배치 될 NPC 등장

    def on_tick(self) -> state.State:
        if count_users(boxId=710, boxId=1):
            return 시작()


class 시작(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=105, textId=20003361) # 키 몬스터를 처치하세요.

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[149]):
            return 화물문_개방()

    def on_exit(self):
        hide_guide_summary(entityId=105)


class 화물문_개방(state.State):
    def on_enter(self):
        enable_spawn_point_pc(spawnId=0, isEnable=False)
        enable_spawn_point_pc(spawnId=991, isEnable=False)
        enable_spawn_point_pc(spawnId=992, isEnable=True)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=106, textId=20003362) # 다음 구역으로 이동할 수 있습니다.
        set_mesh(triggerIds=[7991,7992,7993], visible=False, arg4=0, arg5=0) # 문 파괴
        set_timer(timerId='3', seconds=3, display=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 화물문_개방_종료()
        if count_users(boxId=711, boxId=1):
            return 보스등장연출_00()

    def on_exit(self):
        hide_guide_summary(entityId=106)


class 화물문_개방_종료(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=711, boxId=1):
            return 보스등장연출_00()


class 보스등장연출_00(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000335_BF__BOSS__0$', arg3='3000')
        set_effect(triggerIds=[6921], visible=True) # BG\Common\Eff_Com_ObjectShake.xml
        set_timer(timerId='3', seconds=3, display=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 보스등장연출_01()


class 보스등장연출_01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[141,142,143,144,145,146,147,148]) # 기본 배치 된 NPC 삭제
        set_skill(triggerIds=[5801], isEnable=True) # 벽 날리는 스킬
        set_skill(triggerIds=[5802], isEnable=True) # 벽 날리는 스킬
        set_effect(triggerIds=[6911], visible=True)
        set_effect(triggerIds=[6912], visible=True)
        create_monster(spawnIds=[199], arg2=False) # 보스 몬스터 등장
        move_npc(spawnId=199, patrolName='MS2PatrolData_1003')
        set_timer(timerId='1', seconds=1, display=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 보스등장연출_02()
        if monster_dead(boxIds=[199]):
            return 포탈_개방()


class 보스등장연출_02(state.State):
    def on_enter(self):
        set_skill(triggerIds=[5803], isEnable=True) # 벽 날리는 스킬
        set_skill(triggerIds=[5804], isEnable=True) # 벽 날리는 스킬
        set_effect(triggerIds=[6913], visible=True)
        set_effect(triggerIds=[6914], visible=True)
        set_timer(timerId='1', seconds=1, display=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 보스등장연출_03()
        if monster_dead(boxIds=[199]):
            return 포탈_개방()


class 보스등장연출_03(state.State):
    def on_enter(self):
        set_skill(triggerIds=[5805], isEnable=True) # 벽 날리는 스킬
        set_skill(triggerIds=[5806], isEnable=True) # 벽 날리는 스킬
        set_effect(triggerIds=[6915], visible=True)
        set_effect(triggerIds=[6916], visible=True)
        set_timer(timerId='1', seconds=1, display=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[199]):
            return 포탈_개방()


class 포탈_개방(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_Space_PopUp_01')
        show_guide_summary(entityId=112, textId=40009) # 포탈을 타세요
        set_mesh(triggerIds=[6311,6312,6313,6314,6315], visible=False, arg4=0, arg5=10) # 벽 해제
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True) # 포탈 개방

    def on_exit(self):
        hide_guide_summary(entityId=112)


