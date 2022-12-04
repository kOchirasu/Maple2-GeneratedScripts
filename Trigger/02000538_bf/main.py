""" trigger/02000538_bf/main.xml """
import trigger_api


# 플레이어 감지
class idle(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[5000], visible=False)
        self.set_skill(triggerIds=[9001], enable=False)
        self.set_skill(triggerIds=[9002], enable=False)
        self.set_skill(triggerIds=[9003], enable=False)
        self.set_skill(triggerIds=[9004], enable=False)
        self.set_skill(triggerIds=[9005], enable=False)
        self.enable_spawn_point_pc(spawnId=0, isEnable=True)
        self.enable_spawn_point_pc(spawnId=1, isEnable=False)
        self.enable_spawn_point_pc(spawnId=2, isEnable=False)
        self.set_onetime_effect(id=101, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=102, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=103, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=104, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=105, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.create_monster(spawnIds=[108], animationEffect=True)
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[801], jobCode=0):
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[5000], visible=False)
        self.set_event_ui(type=1, arg2='$02000538_BF__MAIN__0$', arg3='3000')
        self.set_onetime_effect(id=102, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return ready2(self.ctx)


class ready2(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[108])
        self.side_npc_talk(npcId=11004643, illust='SlaveWoman3_normal', duration=4000, script='$02000538_BF__MAIN__1$')
        self.create_monster(spawnIds=[101,1011,1012,1013,1014], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101,1011,1012,1013,1014]):
            return 방으로이동(self.ctx)


class 방으로이동(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1081], animationEffect=True)
        self.side_npc_talk(npcId=11004644, illust='SlaveMan3_normal', duration=4000, script='$02000538_BF__MAIN__2$')
        self.create_monster(spawnIds=[1015,1016,1017], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[802], jobCode=0):
            return 방몬스터생성(self.ctx)


class 방몬스터생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[102,1021,1022], animationEffect=True)
        self.side_npc_talk(npcId=11004644, illust='SlaveMan3_normal', duration=4000, script='$02000538_BF__MAIN__3$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[102,1021,1022,1015,1016,1017]):
            return 첫번째전투판파괴(self.ctx)


class 첫번째전투판파괴(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1081])
        self.set_onetime_effect(id=101, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_skill(triggerIds=[9001], enable=True)
        self.enable_spawn_point_pc(spawnId=0, isEnable=False)
        self.enable_spawn_point_pc(spawnId=1, isEnable=True)
        self.create_monster(spawnIds=[1023,1024], animationEffect=True)
        self.side_npc_talk(npcId=11004643, illust='SlaveWoman3_normal', duration=4000, script='$02000538_BF__MAIN__4$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[803], jobCode=0):
            return 세번째판몬스터생성(self.ctx)


class 세번째판몬스터생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[103,1031,1032,1033], animationEffect=True)
        self.side_npc_talk(npcId=11004644, illust='SlaveMan3_normal', duration=4000, script='$02000538_BF__MAIN__5$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[103,1031,1032,1033,1023,1024]):
            return 몬스터추가생성감지(self.ctx)


class 몬스터추가생성감지(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[804], jobCode=0):
            return 몬스터추가생성(self.ctx)


class 몬스터추가생성(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=11004643, illust='SlaveWoman3_normal', duration=4000, script='$02000538_BF__MAIN__6$')
        self.create_monster(spawnIds=[104,1041,1042,1043,1044], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[104,1041,1042,1043,1044]):
            return 몬스터추가생성2(self.ctx)


class 몬스터추가생성2(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[107,1071], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[107,1071]):
            return 세번째전투판파괴(self.ctx)


class 세번째전투판파괴(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=103, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_skill(triggerIds=[9003], enable=True)
        self.side_npc_talk(npcId=11004644, illust='SlaveMan3_normal', duration=4000, script='$02000538_BF__MAIN__7$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 다섯번째판몬스터생성(self.ctx)


class 다섯번째판몬스터생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1082], animationEffect=True)
        self.enable_spawn_point_pc(spawnId=1, isEnable=False)
        self.enable_spawn_point_pc(spawnId=2, isEnable=True)
        self.create_monster(spawnIds=[105,1051,1052,1053,1054,1055], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[105,1051,1052,1053,1054,1055]):
            return 엘리트소환체크(self.ctx)


class 엘리트소환체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[806], jobCode=0):
            return 엘리트소환(self.ctx)


class 엘리트소환(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[5000], visible=True)
        self.destroy_monster(spawnIds=[1082])
        self.set_onetime_effect(id=104, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.create_monster(spawnIds=[106], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[106]):
            return 마지막전투판파괴(self.ctx)


class 마지막전투판파괴(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=11004643, illust='SlaveWoman3_normal', duration=4000, script='$02000538_BF__MAIN__8$')
        self.lock_my_pc(isLock=True)
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
        self.set_onetime_effect(id=105, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 마지막전투판파괴2(self.ctx)


class 마지막전투판파괴2(trigger_api.Trigger):
    def on_enter(self):
        self.lock_my_pc(isLock=False)
        self.set_skill(triggerIds=[9005], enable=True)
        self.set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633,634,635,636,637,638,639,640,641,642,643,644,645,646,647,648,649,650,651,652,653,654,655,656,657,658,659,660,661,662,663,664,665,666,667,668,669,670,671,672,673,674,675,676,677,678,679,680,681,682,683,684,685,686,687,688,689,690,691,692,693,694,695,696,697,698,699,700,701,702,703,704,705,706,707,708,709,710,711,712,713,714,715,716,717,718,719,720,721,722,723,724,725,726,727,728,729,730,731,732,733,734,735,736,737,738,739,740,741,742,743,744,745,746,747,748,749,750,751,752,753,754,755,756,757,758,759,760,761,762,763,764,765,766,767], visible=False)


initial_state = idle
