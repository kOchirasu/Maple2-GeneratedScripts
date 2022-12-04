""" trigger/52010032_qd/main_quest10003078.xml """
import trigger_api


# 무르파고스 신전에 나메드를 만나러 들어오는 퀘스트
class 무르파고스에들어오면(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[202], animationEffect=False) # 퀘스트 나메드: 11000039

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[10003078], questStates=[2]):
            self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.create_monster(spawnIds=[301], animationEffect=True) # 시끄러운 주먹
        self.create_monster(spawnIds=[302], animationEffect=True) # 에바고르
        self.move_user(mapId=52010032, portalId=6001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 무르파고스이동(self.ctx)


class 무르파고스이동(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 무르파고스이동01(self.ctx)


class 무르파고스이동01(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.move_user_path(patrolName='MS2PatrolData_3005')
        self.move_npc(spawnId=301, patrolName='MS2PatrolData_3003')
        self.move_npc(spawnId=302, patrolName='MS2PatrolData_3004')
        self.show_caption(type='VerticalCaption', title='$52010032_QD__MAIN_QUEST10003078__0$', desc='$52010032_QD__MAIN_QUEST10003078__1$', align='centerLeft', offsetRateX=0, offsetRateY=0, duration=3000, scale=2)
        self.add_balloon_talk(spawnId=301, msg='$52010032_QD__MAIN_QUEST10003078__2$', duration=2000, delayTick=1000)
        self.add_balloon_talk(spawnId=302, msg='$52010032_QD__MAIN_QUEST10003078__3$', duration=2000, delayTick=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 나메드에게퀘스트받기(self.ctx)


class 나메드에게퀘스트받기(trigger_api.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return None # Missing State: 


initial_state = 무르파고스에들어오면
