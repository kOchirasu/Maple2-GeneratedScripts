""" trigger/02000334_bf/cannonspawn.xml """
import common


class Idle(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='CannonSpawn', value=1):
            return CannonSpawn(self.ctx)


class CannonSpawn(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=190, script='$02000334_BF__WAVE__12$', arg4=3, arg5=1) # 보스 대사
        self.set_conversation(type=1, spawnId=199, script='$02000334_BF__MAIN__12$', arg4=3, arg5=3) # 오스칼 대사
        self.set_timer(timerId='3', seconds=3, interval=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='3'):
            return CannonSpawn_start(self.ctx)


class CannonSpawn_start(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=9999131, key='cannon_01', value=1)
        self.set_user_value(triggerId=9999132, key='cannon_02', value=1)
        self.set_user_value(triggerId=9999133, key='cannon_03', value=1)
        self.create_monster(spawnIds=[301,302,303], animationEffect=False) # 대포 생성
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=102, textId=20000020) # 대포를 쏘세요
        self.set_effect(triggerIds=[90021], visible=True) # 이벤트 UI 에 맞는 사운드

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[190]):
            return Clear(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=102) # 대포를 쏘세요


class Clear(common.Trigger):
    pass


initial_state = Idle
