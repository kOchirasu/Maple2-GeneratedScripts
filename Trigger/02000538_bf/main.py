""" trigger/02000538_bf/main.xml """
from common import *
import state


#  플레이어 감지 
class idle(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[5000], visible=False)
        set_skill(triggerIds=[9001], isEnable=False)
        set_skill(triggerIds=[9002], isEnable=False)
        set_skill(triggerIds=[9003], isEnable=False)
        set_skill(triggerIds=[9004], isEnable=False)
        set_skill(triggerIds=[9005], isEnable=False)
        enable_spawn_point_pc(spawnId=0, isEnable=True)
        enable_spawn_point_pc(spawnId=1, isEnable=False)
        enable_spawn_point_pc(spawnId=2, isEnable=False)
        set_onetime_effect(id=101, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_onetime_effect(id=102, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_onetime_effect(id=103, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_onetime_effect(id=104, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_onetime_effect(id=105, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        create_monster(spawnIds=[108], arg2=True)
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[801], jobCode=0):
            return ready()


class ready(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[5000], visible=False)
        set_event_ui(type=1, arg2='$02000538_BF__MAIN__0$', arg3='3000')
        set_onetime_effect(id=102, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return ready2()


class ready2(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[108])
        side_npc_talk(npcId=11004643, illust='SlaveWoman3_normal', duration=4000, script='$02000538_BF__MAIN__1$')
        create_monster(spawnIds=[101,1011,1012,1013,1014], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101,1011,1012,1013,1014]):
            return 방으로이동()


class 방으로이동(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1081], arg2=True)
        side_npc_talk(npcId=11004644, illust='SlaveMan3_normal', duration=4000, script='$02000538_BF__MAIN__2$')
        create_monster(spawnIds=[1015,1016,1017], arg2=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[802], jobCode=0):
            return 방몬스터생성()


class 방몬스터생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[102,1021,1022], arg2=True)
        side_npc_talk(npcId=11004644, illust='SlaveMan3_normal', duration=4000, script='$02000538_BF__MAIN__3$')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[102,1021,1022,1015,1016,1017]):
            return 첫번째전투판파괴()


class 첫번째전투판파괴(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1081])
        set_onetime_effect(id=101, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_skill(triggerIds=[9001], isEnable=True)
        enable_spawn_point_pc(spawnId=0, isEnable=False)
        enable_spawn_point_pc(spawnId=1, isEnable=True)
        create_monster(spawnIds=[1023,1024], arg2=True)
        side_npc_talk(npcId=11004643, illust='SlaveWoman3_normal', duration=4000, script='$02000538_BF__MAIN__4$')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[803], jobCode=0):
            return 세번째판몬스터생성()


class 세번째판몬스터생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[103,1031,1032,1033], arg2=True)
        side_npc_talk(npcId=11004644, illust='SlaveMan3_normal', duration=4000, script='$02000538_BF__MAIN__5$')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[103,1031,1032,1033,1023,1024]):
            return 몬스터추가생성감지()


class 몬스터추가생성감지(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[804], jobCode=0):
            return 몬스터추가생성()


class 몬스터추가생성(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11004643, illust='SlaveWoman3_normal', duration=4000, script='$02000538_BF__MAIN__6$')
        create_monster(spawnIds=[104,1041,1042,1043,1044], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[104,1041,1042,1043,1044]):
            return 몬스터추가생성2()


class 몬스터추가생성2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[107,1071], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[107,1071]):
            return 세번째전투판파괴()


class 세번째전투판파괴(state.State):
    def on_enter(self):
        set_onetime_effect(id=103, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_skill(triggerIds=[9003], isEnable=True)
        side_npc_talk(npcId=11004644, illust='SlaveMan3_normal', duration=4000, script='$02000538_BF__MAIN__7$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 다섯번째판몬스터생성()


class 다섯번째판몬스터생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1082], arg2=True)
        enable_spawn_point_pc(spawnId=1, isEnable=False)
        enable_spawn_point_pc(spawnId=2, isEnable=True)
        create_monster(spawnIds=[105,1051,1052,1053,1054,1055], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[105,1051,1052,1053,1054,1055]):
            return 엘리트소환체크()


class 엘리트소환체크(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[806], jobCode=0):
            return 엘리트소환()


class 엘리트소환(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[5000], visible=True)
        destroy_monster(spawnIds=[1082])
        set_onetime_effect(id=104, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        create_monster(spawnIds=[106], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[106]):
            return 마지막전투판파괴()


class 마지막전투판파괴(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11004643, illust='SlaveWoman3_normal', duration=4000, script='$02000538_BF__MAIN__8$')
        lock_my_pc(isLock=True)
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)
        set_onetime_effect(id=105, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 마지막전투판파괴2()


class 마지막전투판파괴2(state.State):
    def on_enter(self):
        lock_my_pc(isLock=False)
        set_skill(triggerIds=[9005], isEnable=True)
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633,634,635,636,637,638,639,640,641,642,643,644,645,646,647,648,649,650,651,652,653,654,655,656,657,658,659,660,661,662,663,664,665,666,667,668,669,670,671,672,673,674,675,676,677,678,679,680,681,682,683,684,685,686,687,688,689,690,691,692,693,694,695,696,697,698,699,700,701,702,703,704,705,706,707,708,709,710,711,712,713,714,715,716,717,718,719,720,721,722,723,724,725,726,727,728,729,730,731,732,733,734,735,736,737,738,739,740,741,742,743,744,745,746,747,748,749,750,751,752,753,754,755,756,757,758,759,760,761,762,763,764,765,766,767], visible=False)


