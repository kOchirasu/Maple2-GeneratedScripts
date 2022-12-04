""" trigger/52010056_qd/eventsection_e_monster.xml """
import trigger_api


class Idle(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5501], visible=False)
        self.set_effect(triggerIds=[5502], visible=False)
        self.set_effect(triggerIds=[5503], visible=False)
        self.set_effect(triggerIds=[5504], visible=False)
        self.set_effect(triggerIds=[5505], visible=False)
        self.set_effect(triggerIds=[5506], visible=False)
        self.set_effect(triggerIds=[5507], visible=False)
        self.set_effect(triggerIds=[5508], visible=False)
        self.set_effect(triggerIds=[5509], visible=False)
        self.set_effect(triggerIds=[5510], visible=False)
        self.set_effect(triggerIds=[5511], visible=False)
        self.set_effect(triggerIds=[5512], visible=False)
        self.set_effect(triggerIds=[5513], visible=False)
        self.set_effect(triggerIds=[5514], visible=False)
        self.set_effect(triggerIds=[5515], visible=False)
        self.set_effect(triggerIds=[5516], visible=False)
        self.set_effect(triggerIds=[5517], visible=False)
        self.set_effect(triggerIds=[5518], visible=False)
        self.set_effect(triggerIds=[5519], visible=False)
        self.set_effect(triggerIds=[5520], visible=False)
        self.set_effect(triggerIds=[5521], visible=False)
        self.set_effect(triggerIds=[5522], visible=False)
        self.set_effect(triggerIds=[5523], visible=False)
        self.set_effect(triggerIds=[5524], visible=False)
        self.set_effect(triggerIds=[5525], visible=False)
        self.set_effect(triggerIds=[5526], visible=False)
        self.set_effect(triggerIds=[5527], visible=False)
        self.set_effect(triggerIds=[5528], visible=False)
        self.set_effect(triggerIds=[5529], visible=False)
        self.set_effect(triggerIds=[5530], visible=False)
        self.set_effect(triggerIds=[5531], visible=False)
        self.set_effect(triggerIds=[5532], visible=False)
        self.set_effect(triggerIds=[5533], visible=False)
        self.set_effect(triggerIds=[5534], visible=False)
        self.set_effect(triggerIds=[5535], visible=False)
        self.set_effect(triggerIds=[5536], visible=False)
        self.set_effect(triggerIds=[5537], visible=False)
        self.set_effect(triggerIds=[5538], visible=False)
        self.set_effect(triggerIds=[5539], visible=False)
        self.set_effect(triggerIds=[5540], visible=False)
        self.set_effect(triggerIds=[5541], visible=False)
        self.set_effect(triggerIds=[5542], visible=False)
        self.set_effect(triggerIds=[5543], visible=False)
        self.set_effect(triggerIds=[5544], visible=False)
        self.set_effect(triggerIds=[5545], visible=False)
        self.set_effect(triggerIds=[5546], visible=False)
        self.set_effect(triggerIds=[5547], visible=False)
        self.set_effect(triggerIds=[5548], visible=False)
        self.set_effect(triggerIds=[5549], visible=False)
        self.set_mesh(triggerIds=[9001,9002,9003,9004], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2009], questIds=[91000053], questStates=[2]):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[601], animationEffect=True) # 크림슨 스피어: 29000386
        self.create_monster(spawnIds=[602], animationEffect=True) # 크림슨 스피어: 29000386
        self.create_monster(spawnIds=[603], animationEffect=True) # 크림슨 발록: 29000387
        self.create_monster(spawnIds=[604], animationEffect=True) # 크림슨 스피어: 29000386
        self.create_monster(spawnIds=[605], animationEffect=True) # 크림슨 스피어: 29000386
        self.create_monster(spawnIds=[606], animationEffect=True) # 크림슨 스피어: 29000386

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 크림슨발록_지시(self.ctx)


class 크림슨발록_지시(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=603, msg='$52010056_QD__EventSection_E_Monster__0$', duration=2000, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 크림슨스피어_대답(self.ctx)


class 크림슨스피어_대답(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=601, msg='$52010056_QD__EventSection_E_Monster__1$', duration=1500, delayTick=0)
        self.add_balloon_talk(spawnId=602, msg='$52010056_QD__EventSection_E_Monster__1$', duration=1500, delayTick=0)
        self.add_balloon_talk(spawnId=604, msg='$52010056_QD__EventSection_E_Monster__1$', duration=1500, delayTick=0)
        self.add_balloon_talk(spawnId=605, msg='$52010056_QD__EventSection_E_Monster__1$', duration=1500, delayTick=0)
        self.add_balloon_talk(spawnId=606, msg='$52010056_QD__EventSection_E_Monster__1$', duration=1500, delayTick=0)
        self.set_mesh(triggerIds=[9002,9003,9004], visible=True, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[5501], visible=True)
        self.set_effect(triggerIds=[5502], visible=True)
        self.set_effect(triggerIds=[5503], visible=True)
        self.set_effect(triggerIds=[5504], visible=True)
        self.set_effect(triggerIds=[5505], visible=True)
        self.set_effect(triggerIds=[5506], visible=True)
        self.set_effect(triggerIds=[5507], visible=True)
        self.set_effect(triggerIds=[5508], visible=True)
        self.set_effect(triggerIds=[5509], visible=True)
        self.set_effect(triggerIds=[5510], visible=True)
        self.set_effect(triggerIds=[5511], visible=True)
        self.set_effect(triggerIds=[5512], visible=True)
        self.set_effect(triggerIds=[5513], visible=True)
        self.set_effect(triggerIds=[5514], visible=True)
        self.set_effect(triggerIds=[5515], visible=True)
        self.set_effect(triggerIds=[5516], visible=True)
        self.set_effect(triggerIds=[5517], visible=True)
        self.set_effect(triggerIds=[5518], visible=True)
        self.set_effect(triggerIds=[5519], visible=True)
        self.set_effect(triggerIds=[5520], visible=True)
        self.set_effect(triggerIds=[5521], visible=True)
        self.set_effect(triggerIds=[5522], visible=True)
        self.set_effect(triggerIds=[5523], visible=True)
        self.set_effect(triggerIds=[5524], visible=True)
        self.set_effect(triggerIds=[5525], visible=True)
        self.set_effect(triggerIds=[5526], visible=True)
        self.set_effect(triggerIds=[5527], visible=True)
        self.set_effect(triggerIds=[5528], visible=True)
        self.set_effect(triggerIds=[5529], visible=True)
        self.set_effect(triggerIds=[5530], visible=True)
        self.set_effect(triggerIds=[5531], visible=True)
        self.set_effect(triggerIds=[5532], visible=True)
        self.set_effect(triggerIds=[5533], visible=True)
        self.set_effect(triggerIds=[5534], visible=True)
        self.set_effect(triggerIds=[5535], visible=True)
        self.set_effect(triggerIds=[5536], visible=True)
        self.set_effect(triggerIds=[5537], visible=True)
        self.set_effect(triggerIds=[5538], visible=True)
        self.set_effect(triggerIds=[5539], visible=True)
        self.set_effect(triggerIds=[5540], visible=True)
        self.set_effect(triggerIds=[5541], visible=True)
        self.set_effect(triggerIds=[5542], visible=True)
        self.set_effect(triggerIds=[5543], visible=True)
        self.set_effect(triggerIds=[5544], visible=True)
        self.set_effect(triggerIds=[5545], visible=True)
        self.set_effect(triggerIds=[5546], visible=True)
        self.set_effect(triggerIds=[5547], visible=True)
        self.set_effect(triggerIds=[5548], visible=True)
        self.set_effect(triggerIds=[5549], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[601,602,603,604,605]):
            return MeshOff(self.ctx)


class MeshOff(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5501], visible=False)
        self.set_effect(triggerIds=[5502], visible=False)
        self.set_effect(triggerIds=[5503], visible=False)
        self.set_effect(triggerIds=[5504], visible=False)
        self.set_effect(triggerIds=[5505], visible=False)
        self.set_effect(triggerIds=[5506], visible=False)
        self.set_effect(triggerIds=[5507], visible=False)
        self.set_effect(triggerIds=[5508], visible=False)
        self.set_effect(triggerIds=[5509], visible=False)
        self.set_effect(triggerIds=[5510], visible=False)
        self.set_effect(triggerIds=[5511], visible=False)
        self.set_effect(triggerIds=[5512], visible=False)
        self.set_effect(triggerIds=[5513], visible=False)
        self.set_effect(triggerIds=[5514], visible=False)
        self.set_effect(triggerIds=[5515], visible=False)
        self.set_effect(triggerIds=[5516], visible=False)
        self.set_effect(triggerIds=[5517], visible=False)
        self.set_effect(triggerIds=[5518], visible=False)
        self.set_effect(triggerIds=[5519], visible=False)
        self.set_effect(triggerIds=[5520], visible=False)
        self.set_effect(triggerIds=[5521], visible=False)
        self.set_effect(triggerIds=[5522], visible=False)
        self.set_effect(triggerIds=[5523], visible=False)
        self.set_effect(triggerIds=[5524], visible=False)
        self.set_effect(triggerIds=[5525], visible=False)
        self.set_effect(triggerIds=[5526], visible=False)
        self.set_effect(triggerIds=[5527], visible=False)
        self.set_effect(triggerIds=[5528], visible=False)
        self.set_effect(triggerIds=[5529], visible=False)
        self.set_effect(triggerIds=[5530], visible=False)
        self.set_effect(triggerIds=[5531], visible=False)
        self.set_effect(triggerIds=[5532], visible=False)
        self.set_effect(triggerIds=[5533], visible=False)
        self.set_effect(triggerIds=[5534], visible=False)
        self.set_effect(triggerIds=[5535], visible=False)
        self.set_effect(triggerIds=[5536], visible=False)
        self.set_effect(triggerIds=[5537], visible=False)
        self.set_effect(triggerIds=[5538], visible=False)
        self.set_effect(triggerIds=[5539], visible=False)
        self.set_effect(triggerIds=[5540], visible=False)
        self.set_effect(triggerIds=[5541], visible=False)
        self.set_effect(triggerIds=[5542], visible=False)
        self.set_effect(triggerIds=[5543], visible=False)
        self.set_effect(triggerIds=[5544], visible=False)
        self.set_effect(triggerIds=[5545], visible=False)
        self.set_effect(triggerIds=[5546], visible=False)
        self.set_effect(triggerIds=[5547], visible=False)
        self.set_effect(triggerIds=[5548], visible=False)
        self.set_effect(triggerIds=[5549], visible=False)
        self.set_mesh(triggerIds=[9001,9002,9003,9004], visible=False, arg3=0, delay=0, scale=0)


initial_state = Idle
