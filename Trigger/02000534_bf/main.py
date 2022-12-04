""" trigger/02000534_bf/main.xml """
import trigger_api


# 오닉스 타워 3층
class idle(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_mesh(triggerIds=[7000], visible=True)
        self.set_mesh(triggerIds=[7001], visible=True)
        self.set_mesh(triggerIds=[7002], visible=True)
        self.set_mesh(triggerIds=[7003], visible=True)
        self.set_mesh(triggerIds=[7004], visible=True)
        self.set_mesh(triggerIds=[7005], visible=True)
        self.set_mesh(triggerIds=[7006], visible=True)
        self.set_mesh(triggerIds=[7007], visible=True)
        self.set_mesh(triggerIds=[7008], visible=True)
        self.set_effect(triggerIds=[8000], visible=False)
        self.set_effect(triggerIds=[8001], visible=False)
        self.set_effect(triggerIds=[8002], visible=False)
        self.set_effect(triggerIds=[8003], visible=False)
        self.set_effect(triggerIds=[8004], visible=False)
        self.set_effect(triggerIds=[8005], visible=False)
        self.set_effect(triggerIds=[8006], visible=False)
        self.set_effect(triggerIds=[8007], visible=False)
        self.set_effect(triggerIds=[8008], visible=False)
        self.set_effect(triggerIds=[8009], visible=False)
        self.create_monster(spawnIds=[508,509,510,511], animationEffect=True)
        self.create_monster(spawnIds=[716,715,713,717,718], animationEffect=True)
        self.create_monster(spawnIds=[701,702,703,704,705,706,707,708,709,710,711,712], animationEffect=True)
        self.move_npc(spawnId=508, patrolName='MS2PatrolData_4000')
        self.move_npc(spawnId=509, patrolName='MS2PatrolData_4001')
        self.move_npc(spawnId=511, patrolName='MS2PatrolData_4002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[701], jobCode=0):
            return start(self.ctx)


class start(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_event_ui(type=1, arg2='$02000534_BF__MAIN__0$', arg3='3000')
        self.set_portal(portalId=2, visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 첫번째몬스터전투시작(self.ctx)


class 첫번째몬스터전투시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10003132], state=0)
        self.set_interact_object(triggerIds=[10003133], state=0)
        self.set_interact_object(triggerIds=[10003134], state=0)
        self.set_interact_object(triggerIds=[10003135], state=0)
        self.create_monster(spawnIds=[501,520,521,522,523], animationEffect=True)
        self.add_balloon_talk(spawnId=523, msg='$02000534_BF__MAIN__1$', duration=3500, delayTick=0)
        self.add_balloon_talk(spawnId=520, msg='$02000534_BF__MAIN__2$', duration=3500, delayTick=0)
        self.add_balloon_talk(spawnId=521, msg='$02000534_BF__MAIN__3$', duration=3500, delayTick=1500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[501,520,521,522,523]):
            return 첫번째몬스터처치(self.ctx)


class 첫번째몬스터처치(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8000], visible=True)
        self.set_mesh(triggerIds=[7000], visible=False)
        self.side_npc_talk(npcId=11004639, illust='Jay_normal', duration=4000, script='$02000534_BF__MAIN__4$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[707], jobCode=0):
            return 하렌등장(self.ctx)


class 하렌등장(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=23300001, illust='Haren_smile', duration=4000, script='$02000534_BF__MAIN__5$')
        self.create_monster(spawnIds=[502,524,525,526,527], animationEffect=True, animationDelay=100)
        self.add_balloon_talk(spawnId=502, msg='$02000534_BF__MAIN__6$', duration=3500, delayTick=0)
        self.add_balloon_talk(spawnId=527, msg='$02000534_BF__MAIN__7$', duration=3500, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 하렌등장2(self.ctx)


class 하렌등장2(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=23300001, illust='Jay_normal', duration=4000, script='$02000534_BF__MAIN__8$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 하렌등장3(self.ctx)


class 하렌등장3(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=23300001, illust='Haren_smile', duration=4000, script='$02000534_BF__MAIN__9$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[502,524,525,526,527]):
            return 두번째몬스터처치(self.ctx)


class 두번째몬스터처치(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8005], visible=True)
        self.set_mesh(triggerIds=[7005], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[703], jobCode=0):
            return 첫번째연구실몬스터정리(self.ctx)


class 첫번째연구실몬스터정리(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=713, msg='$02000534_BF__MAIN__10$', duration=3500, delayTick=2000)
        self.create_monster(spawnIds=[518,519,528], animationEffect=True, animationDelay=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[518,519,528]):
            return 오브젝트설명1(self.ctx)


class 오브젝트설명1(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=713, msg='$02000534_BF__MAIN__11$', duration=3500, delayTick=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 방해1(self.ctx)


class 방해1(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=0, msg='$02000534_BF__MAIN__12$', duration=3500, delayTick=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 첫번째연구실나오기(self.ctx)


class 첫번째연구실나오기(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[7001], visible=False)
        self.set_effect(triggerIds=[8001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[708], jobCode=0):
            return 두번째전투판몬스터생성(self.ctx)


class 두번째전투판몬스터생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[503,529,530,531,532], animationEffect=True, animationDelay=500)
        self.add_balloon_talk(spawnId=503, msg='$02000534_BF__MAIN__13$', duration=3500, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[503,529,530,531,532]):
            return 두번째연구소이동(self.ctx)


class 두번째연구소이동(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[714], animationEffect=True)
        self.set_effect(triggerIds=[8006], visible=True)
        self.set_mesh(triggerIds=[7006], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[704], jobCode=0):
            return 두번째연구실몬스터정리(self.ctx)


class 두번째연구실몬스터정리(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=714, msg='$02000534_BF__MAIN__14$', duration=3500, delayTick=500)
        self.move_npc(spawnId=714, patrolName='MS2PatrolData_4003')
        self.create_monster(spawnIds=[516,517,5516], animationEffect=True, animationDelay=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[516,517,5516]):
            return 두번째연구실몬스터정리2(self.ctx)


class 두번째연구실몬스터정리2(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[714])
        self.set_interact_object(triggerIds=[10003133], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10003133], stateValue=0):
            return 오브젝트설명2(self.ctx)


class 오브젝트설명2(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10003133], state=0)
        self.add_balloon_talk(spawnId=0, msg='$02000534_BF__MAIN__15$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return 두번째연구실나오기(self.ctx)


class 두번째연구실나오기(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=0, msg='$02000534_BF__MAIN__16$', duration=3500, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 세번째전투판(self.ctx)


class 세번째전투판(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[7002], visible=False)
        self.set_effect(triggerIds=[8002], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[709], jobCode=0):
            return 세번째전투판몬스터생성(self.ctx)


class 세번째전투판몬스터생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[504,533], animationEffect=True, animationDelay=500)
        self.add_balloon_talk(spawnId=504, msg='$02000534_BF__MAIN__17$', duration=3500, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[504,533]):
            return 세번째몬스터처치(self.ctx)


class 세번째몬스터처치(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8007], visible=True)
        self.set_mesh(triggerIds=[7007], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[705], jobCode=0):
            return 세번째연구소이동(self.ctx)


class 세번째연구소이동(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[514,515], animationEffect=False)
        self.add_balloon_talk(spawnId=718, msg='$02000534_BF__MAIN__18$', duration=3500)
        self.add_balloon_talk(spawnId=715, msg='$02000534_BF__MAIN__19$', duration=3500, delayTick=500)
        self.add_balloon_talk(spawnId=715, msg='$02000534_BF__MAIN__20$', duration=3500, delayTick=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[514,515]):
            return 방해3(self.ctx)


class 방해3(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=717, msg='$02000534_BF__MAIN__21$', duration=3500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 방해33(self.ctx)


class 방해33(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=0, msg='$02000534_BF__MAIN__22$', duration=3500, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 네번째전투판(self.ctx)


class 네번째전투판(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[7003], visible=False)
        self.set_effect(triggerIds=[8003], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[710], jobCode=0):
            return 네번째몬스터처치(self.ctx)


class 네번째몬스터처치(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[505,534,535,536,537], animationEffect=False)
        self.add_balloon_talk(spawnId=536, msg='$02000534_BF__MAIN__23$', duration=3500, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[505,534,535,536,537]):
            return 네번째연구소로이동(self.ctx)


class 네번째연구소로이동(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8008], visible=True)
        self.set_mesh(triggerIds=[7008], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[706], jobCode=0):
            return 네번째연구소정리(self.ctx)


class 네번째연구소정리(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[512,513,5513], animationEffect=True)
        self.add_balloon_talk(spawnId=716, msg='$02000534_BF__MAIN__24$', duration=3500, delayTick=1000)
        self.add_balloon_talk(spawnId=716, msg='$02000534_BF__MAIN__25$', duration=3500, delayTick=4500)
        self.side_npc_talk(npcId=11004639, illust='Jay_normal', duration=4000, script='$02000534_BF__MAIN__26$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 컴퓨터조사하기(self.ctx)


class 컴퓨터조사하기(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=23300001, illust='Haren_smile', duration=4000, script='$02000534_BF__MAIN__27$')
        self.add_balloon_talk(spawnId=716, msg='$02000534_BF__MAIN__28$', duration=3500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[512,513,5513]):
            return 번연구실모두정리4(self.ctx)


class 번연구실모두정리4(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10003135], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10003135], stateValue=0):
            return 오브젝트설명4(self.ctx)


class 오브젝트설명4(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.add_balloon_talk(spawnId=0, msg='$02000534_BF__MAIN__29$', duration=3000)
        self.add_balloon_talk(spawnId=0, msg='$02000534_BF__MAIN__30$', duration=3500, delayTick=3000)
        self.set_scene_skip(state=방해4, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5500):
            return 방해4(self.ctx)


class 방해4(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.remove_balloon_talk(spawnId=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 방해44(self.ctx)


class 방해44(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=11004639, illust='Jay_normal', duration=4000, script='$02000534_BF__MAIN__31$')
        self.add_balloon_talk(spawnId=0, msg='$02000534_BF__MAIN__32$', duration=3500, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 마지막전투판(self.ctx)


class 마지막전투판(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[7004], visible=False)
        self.set_effect(triggerIds=[8004], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[702], jobCode=0):
            return 보스등장(self.ctx)


class 보스등장(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[7004], visible=True)
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.side_npc_talk(npcId=11004639, illust='Jay_normal', duration=4000, script='$02000534_BF__MAIN__33$')
        self.create_monster(spawnIds=[507], animationEffect=True)
        self.add_balloon_talk(spawnId=507, msg='$02000534_BF__MAIN__34$', duration=3500, delayTick=1500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_npc_hp(compare='lowerEqual', value=50, spawnId=507, isRelative=True):
            return 업그레이드시작(self.ctx)
        if self.monster_dead(boxIds=[507]):
            return 포탈생성(self.ctx)


class 업그레이드시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=15, interval=1)
        self.create_monster(spawnIds=[9901,9902,9903,9904], animationEffect=False)
        self.add_balloon_talk(spawnId=507, msg='$02000534_BF__MAIN__35$', duration=3500, delayTick=500)
        self.set_event_ui(type=1, arg2='$02000534_BF__MAIN__36$', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=15000):
            return 업그레이드성공체크(self.ctx)


class 업그레이드성공체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 자폭스킬(self.ctx)
        if self.monster_dead(boxIds=[9901,9902,9903,9904]):
            return 실패(self.ctx)
        if self.monster_dead(boxIds=[507]):
            return 포탈생성(self.ctx)


class 자폭스킬(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=507, msg='$02000534_BF__MAIN__37$', duration=3500, delayTick=500)
        self.set_ai_extra_data(key='bomb', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[507]):
            return 포탈생성(self.ctx)


class 실패(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=507, msg='$02000534_BF__MAIN__38$', duration=3500, delayTick=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[507]):
            return 포탈생성(self.ctx)


class 포탈생성(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=15, interval=0)
        self.side_npc_talk(npcId=11004639, illust='Jay_normal', duration=3000, script='$02000534_BF__MAIN__39$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 포탈생성2(self.ctx)


class 포탈생성2(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000534_BF__MAIN__40$', arg3='3000')
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)


initial_state = idle
