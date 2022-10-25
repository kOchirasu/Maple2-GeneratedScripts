""" trigger/02000535_bf/main.xml """
import common


# 플레이어 감지
class idle(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_effect(triggerIds=[801], visible=False)
        self.set_effect(triggerIds=[802], visible=False)
        self.set_mesh(triggerIds=[4002], visible=True)
        self.set_mesh(triggerIds=[4003], visible=True)
        self.set_mesh(triggerIds=[4004], visible=True)
        self.set_mesh(triggerIds=[4005], visible=True)
        self.set_mesh(triggerIds=[4006], visible=True)
        self.set_mesh(triggerIds=[4007], visible=True)
        self.set_mesh(triggerIds=[4008], visible=True)
        self.set_mesh(triggerIds=[4009], visible=True)
        self.set_mesh(triggerIds=[4010], visible=True)
        self.set_mesh(triggerIds=[4011], visible=True)
        self.set_mesh(triggerIds=[4012], visible=True)
        self.set_mesh(triggerIds=[4013], visible=True)
        self.set_mesh(triggerIds=[4014], visible=True)
        self.set_mesh(triggerIds=[4015], visible=True)
        self.set_mesh(triggerIds=[4016], visible=True)
        self.set_mesh(triggerIds=[4017], visible=True)
        self.set_mesh(triggerIds=[4018], visible=True)
        self.set_mesh(triggerIds=[4019], visible=True)
        self.set_interact_object(triggerIds=[10003145], state=0)
        self.set_interact_object(triggerIds=[10003146], state=0)
        self.set_interact_object(triggerIds=[10003136], state=0)
        self.set_interact_object(triggerIds=[10003137], state=0)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[701], jobCode=0):
            return ready(self.ctx)


class ready(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[5522,5523,5524,5525,5526,5527,5528,5529,5530], animationEffect=True)
        self.create_monster(spawnIds=[9902,9903,9904,9905], animationEffect=True)
        self.create_monster(spawnIds=[5500,5501,5502,5503,5504,5505,5506,5507,5508,5509,5510,5511,5512,5513,5514,5515,5516,5517,5518,5519,5520,5521], animationEffect=True)
        self.create_monster(spawnIds=[506,507,508,509,510,511,512,513,519,518,517,516,515,514,670,671], animationEffect=True)
        self.create_monster(spawnIds=[5532], animationEffect=True)
        self.move_npc(spawnId=5532, patrolName='MS2PatrolData_8000')
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=100):
            return 시작(self.ctx)


class 시작(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[5531], animationEffect=True)
        self.add_balloon_talk(spawnId=5531, msg='$02000535_BF__MAIN__0$', duration=3500, delayTick=0)
        self.add_balloon_talk(spawnId=5531, msg='$02000535_BF__MAIN__1$', duration=3500, delayTick=3500)
        self.add_balloon_talk(spawnId=5523, msg='$02000535_BF__MAIN__2$', duration=3500, delayTick=4500)
        self.add_balloon_talk(spawnId=5530, msg='$02000535_BF__MAIN__3$', duration=3500, delayTick=1500)
        self.set_npc_emotion_loop(spawnId=5531, sequenceName='Attack_Idle_A', duration=7000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 첫번째전투(self.ctx)


class 첫번째전투(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[5523,5524,5525,5526,5527,5528,5529,5530,5531])
        self.create_monster(spawnIds=[523,524,525,526,527,528,529,530,531], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[523,524,525,526,527,528,529,530,531]):
            return 다음으로이동(self.ctx)


# 이동
class 다음으로이동(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10003146], state=1)
        self.destroy_monster(spawnIds=[523,524,525,526,527,528,529,530,531])
        self.add_balloon_talk(spawnId=0, msg='$02000535_BF__MAIN__4$', duration=3500)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[706], jobCode=0):
            return 너무많아(self.ctx)


class 너무많아(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10003146], stateValue=0):
            return 머리를쓰자(self.ctx)


class 머리를쓰자(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=0, msg='$02000535_BF__MAIN__5$', duration=3500)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2500):
            return 바닥을보여주자(self.ctx)


class 바닥을보여주자(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[802], visible=True)
        self.set_event_ui(type=1, arg2='$02000535_BF__MAIN__6$', arg3='5000')
        self.set_interact_object(triggerIds=[10003136], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10003136], stateValue=0):
            return 타이밍맞추기1(self.ctx)


class 타이밍맞추기1(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[4000], visible=False)
        self.set_interact_object(triggerIds=[10003136], state=0)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[709], jobCode=0):
            return 머리를쓰자2(self.ctx)


class 머리를쓰자2(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=5532, msg='$02000535_BF__MAIN__7$', duration=3500, delayTick=300)
        self.add_balloon_talk(spawnId=5501, msg='$02000535_BF__MAIN__8$', duration=3500, delayTick=800)
        self.add_balloon_talk(spawnId=5502, msg='$02000535_BF__MAIN__9$', duration=3500, delayTick=800)
        self.add_balloon_talk(spawnId=5503, msg='$02000535_BF__MAIN__10$', duration=3500, delayTick=1000)
        self.add_balloon_talk(spawnId=5504, msg='$02000535_BF__MAIN__11$', duration=3500, delayTick=1000)
        self.add_balloon_talk(spawnId=5505, msg='$02000535_BF__MAIN__12$', duration=3500, delayTick=1000)
        self.add_balloon_talk(spawnId=5522, msg='$02000535_BF__MAIN__13$', duration=3500, delayTick=300)
        self.add_balloon_talk(spawnId=5520, msg='$02000535_BF__MAIN__14$', duration=3500, delayTick=300)
        self.add_balloon_talk(spawnId=5521, msg='$02000535_BF__MAIN__15$', duration=3500, delayTick=1500)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2500):
            return 통로이동1(self.ctx)


class 통로이동1(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=5520, msg='$02000535_BF__MAIN__16$', duration=5500, delayTick=4500)
        self.add_balloon_talk(spawnId=5522, msg='$02000535_BF__MAIN__17$', duration=5500, delayTick=7500)
        self.add_balloon_talk(spawnId=5505, msg='$02000535_BF__MAIN__18$', duration=5500, delayTick=8500)
        self.add_balloon_talk(spawnId=5522, msg='$02000535_BF__MAIN__19$', duration=5500, delayTick=12500)
        self.create_monster(spawnIds=[5000,5001,5002,5003,5004], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[702], jobCode=0):
            return 메이드대사(self.ctx)


class 메이드대사(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=670, msg='$02000535_BF__MAIN__20$', duration=3500, delayTick=1500)
        self.add_balloon_talk(spawnId=671, msg='$02000535_BF__MAIN__21$', duration=3500)
        self.set_npc_emotion_loop(spawnId=670, sequenceName='Attack_Idle_A', duration=5000)
        self.set_npc_emotion_loop(spawnId=671, sequenceName='Attack_Idle_A', duration=5000)
        self.destroy_monster(spawnIds=[5000,5001,5002,5003,5004])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return 흑성회스폰(self.ctx)


class 흑성회스폰(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[670,671])
        self.create_monster(spawnIds=[601,602,603,604,605], animationEffect=True)
        self.create_monster(spawnIds=[680,681], animationEffect=True)
        self.add_balloon_talk(spawnId=604, msg='$02000535_BF__MAIN__22$', duration=3500, delayTick=500)
        self.add_balloon_talk(spawnId=602, msg='$02000535_BF__MAIN__23$', duration=3500, delayTick=1500)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[601,602,603,604,605,680,681]):
            return 간부들엿보기(self.ctx)


class 간부들엿보기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[705], jobCode=0):
            return 간부들엿보기2(self.ctx)


class 간부들엿보기2(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=0, msg='$02000535_BF__MAIN__24$', duration=3500)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return 간부들대화2(self.ctx)


class 간부들대화2(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_scene_skip(state=카메라리셋시키기2, action='nextState')
        self.select_camera_path(pathIds=[2005], returnView=False)
        self.add_balloon_talk(spawnId=9902, msg='$02000535_BF__MAIN__25$', duration=3500)
        self.add_balloon_talk(spawnId=9903, msg='$02000535_BF__MAIN__26$', duration=3500, delayTick=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 카메라리셋시키기2(self.ctx)


class 카메라리셋시키기2(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=1)
        self.lock_my_pc(isLock=False)
        self.set_event_ui(type=1, arg2='$02000535_BF__MAIN__27$', arg3='5000')
        self.set_effect(triggerIds=[801], visible=True)
        self.set_interact_object(triggerIds=[10003137], state=1)
        self.add_balloon_talk(spawnId=0, msg='$02000535_BF__MAIN__28$', duration=3500)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10003137], stateValue=0):
            return 통로오픈(self.ctx)


class 통로오픈(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[4001], visible=False)
        self.side_npc_talk(npcId=11004659, illust='BreedMin_normal', duration=4000, script='$02000535_BF__MAIN__29$')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 통로오픈2(self.ctx)


class 통로오픈2(common.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=11004659, illust='BreedMin_normal', duration=4000, script='$02000535_BF__MAIN__30$')

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[708], jobCode=0):
            return 테라스몬스터생성(self.ctx)


class 테라스몬스터생성(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[606,6606,608,6608], animationEffect=True)
        self.add_balloon_talk(spawnId=606, msg='$02000535_BF__MAIN__31$', duration=5500, delayTick=500)
        self.add_balloon_talk(spawnId=608, msg='$02000535_BF__MAIN__32$', duration=5500, delayTick=1500)
        self.side_npc_talk(npcId=11004660, illust='Armand_normal', duration=4000, script='$02000535_BF__MAIN__33$')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 테라스몬스터생성2(self.ctx)


class 테라스몬스터생성2(common.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=11004661, illust='Kyle_normal', duration=4000, script='$02000535_BF__MAIN__34$')

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[704], jobCode=0):
            return 테라스몬스터생성3(self.ctx)


class 테라스몬스터생성3(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[607,6607,609,610], animationEffect=True)
        self.add_balloon_talk(spawnId=607, msg='$02000535_BF__MAIN__35$', duration=5500, delayTick=500)
        self.add_balloon_talk(spawnId=610, msg='$02000535_BF__MAIN__36$', duration=5500, delayTick=2000)
        self.side_npc_talk(npcId=11004660, illust='Armand_normal', duration=4000, script='$02000535_BF__MAIN__37$')

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[606,6606,608,6608,607,6607,609,610]):
            return 포탈생성(self.ctx)


class 포탈생성(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000535_BF__MAIN__38$', arg3='5000')
        self.set_mesh(triggerIds=[4019], visible=False)
        self.set_interact_object(triggerIds=[10003145], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10003145], stateValue=0):
            return 보안게임시작(self.ctx)


class 보안게임시작(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='GameLogicEnd', value=999)
        self.widget_action(type='Round', func='InitWidgetRound')
        self.set_user_value(triggerId=9002, key='GameLogicStart', value=999)
        self.lock_my_pc(isLock=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 문열기시작2(self.ctx)


class 문열기시작2(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000535_BF__MAIN__39$', arg3='4000')
        self.lock_my_pc(isLock=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            self.set_user_value(triggerId=9002, key='GameLogicStart', value=1)
            return 게임로직종료대기(self.ctx)


class 게임로직종료대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='GameLogicEnd', value=1):
            return 게임로직종료및성공(self.ctx)
        if self.user_value(key='GameLogicEnd', value=2):
            return 게임로직종료및실패(self.ctx)


class 게임로직종료및성공(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.true():
            return 게임로직종료(self.ctx)


class 게임로직종료및실패(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.true():
            return 실패게임로직종료(self.ctx)


class 게임로직종료(common.Trigger):
    def on_enter(self):
        self.set_pc_emotion_loop(sequenceName='Idle_A', duration=3000)
        self.set_event_ui(type=1, arg2='$02000535_BF__MAIN__40$', arg3='3000')
        self.lock_my_pc(isLock=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 이동하자(self.ctx)


class 실패게임로직종료(common.Trigger):
    def on_enter(self):
        self.set_pc_emotion_loop(sequenceName='Idle_A', duration=3000)
        self.set_event_ui(type=1, arg2='$02000535_BF__MAIN__41$', arg3='3000')
        self.add_balloon_talk(spawnId=0, msg='$02000535_BF__MAIN__42$', duration=3500)
        self.lock_my_pc(isLock=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 문부시기안내(self.ctx)


class 문부시기안내(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_event_ui(type=1, arg2='$02000535_BF__MAIN__43$', arg3='5000')
        self.lock_my_pc(isLock=False)
        self.create_monster(spawnIds=[611], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[611]):
            return 이동하자(self.ctx)


class 이동하자(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.lock_my_pc(isLock=False)
        self.side_npc_talk(npcId=23300001, illust='Haren_smile', duration=4000, script='$02000535_BF__MAIN__44$')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 이동하자2(self.ctx)


class 이동하자2(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=2, visible=True)
        self.add_balloon_talk(spawnId=0, msg='$02000535_BF__MAIN__45$', duration=3500)


initial_state = idle
