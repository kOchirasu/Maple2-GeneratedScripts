""" trigger/02000253_bf/move.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_breakable(triggerIds=[901,902,903,904,905,906,907,908,909,910,911,912,913,914,915,916,1901,1902,1903,1904,1905,1906,1907,1908,1909,1910,1911,1912,1913,1914,1915,1916,2901,2902,2903,2904,2905,2906,2907,2908,2909,2910,2911,2912,2913,2914,2915,2916,3901,3902,3903,3904,3905,3906,3907,3908,3909,3910,3911,3912,3913,3914,3915,3916], enabled=False)
        set_effect(triggerIds=[8041], visible=False)
        set_effect(triggerIds=[8042], visible=False)
        set_effect(triggerIds=[8043], visible=False)
        set_effect(triggerIds=[8044], visible=False)
        set_interact_object(triggerIds=[10001050], state=2)
        set_interact_object(triggerIds=[10001051], state=2)
        set_interact_object(triggerIds=[10001052], state=2)
        set_interact_object(triggerIds=[10001053], state=2)

    def on_tick(self) -> state.State:
        if count_users(boxId=906, boxId=1):
            return 벨라소환()


class 벨라소환(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벨라이동()


class 벨라이동(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=10)


class 랜덤선택1(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=33):
            return 번1()
        if random_condition(rate=33):
            return 번2()
        if random_condition(rate=34):
            return 번3()
        if random_condition(rate=34):
            return 번4()


class 랜덤선택1To1(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=33):
            return 번2()
        if random_condition(rate=34):
            return 번3()
        if random_condition(rate=34):
            return 번4()


class 랜덤선택1To2(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=33):
            return 번1()
        if random_condition(rate=34):
            return 번3()
        if random_condition(rate=34):
            return 번4()


class 랜덤선택1To3(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=33):
            return 번1()
        if random_condition(rate=34):
            return 번2()
        if random_condition(rate=34):
            return 번4()


class 랜덤선택1To4(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=33):
            return 번1()
        if random_condition(rate=34):
            return 번2()
        if random_condition(rate=34):
            return 번3()


class 번1(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=10)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20002523, textId=20002523)
        # <action name="메쉬를설정한다" arg1="265-296" arg2="0" arg3="0" arg4="200"/>
        set_effect(triggerIds=[8041], visible=True)
        set_breakable(triggerIds=[901,902,903,904,1901,1902,1903,1904,2901,2902,2903,2904,3901,3902,3903,3904], enabled=True)
        set_breakable(triggerIds=[905,906,907,908,909,910,911,912,913,914,915,916,1905,1906,1907,1908,1909,1910,1911,1912,1913,1914,1915,1916,2905,2906,2907,2908,2909,2910,2911,2912,2913,2914,2915,2916,3905,3906,3907,3908,3909,3910,3911,3912,3913,3914,3915,3916], enabled=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            hide_guide_summary(entityId=20002523)
            return To1번1()


class To1번1(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8041], visible=False)
        set_timer(timerId='1', seconds=30, clearAtZero=False)
        create_monster(spawnIds=[3001])

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            destroy_monster(spawnIds=[3001])
            set_interact_object(triggerIds=[10001050], state=2)
            set_interact_object(triggerIds=[10001051], state=2)
            set_interact_object(triggerIds=[10001052], state=2)
            set_interact_object(triggerIds=[10001053], state=2)
            return 랜덤선택1To1()
        if monster_dead(boxIds=[3001]):
            return To2번1()


class To2번1(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=30, clearAtZero=False)
        set_interact_object(triggerIds=[10001052], state=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            destroy_monster(spawnIds=[3001])
            set_interact_object(triggerIds=[10001050], state=2)
            set_interact_object(triggerIds=[10001051], state=2)
            set_interact_object(triggerIds=[10001052], state=2)
            set_interact_object(triggerIds=[10001053], state=2)
            return 랜덤선택1To1()
        if object_interacted(interactIds=[10001052], arg2=0):
            return 끝1()


class 번2(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8042], visible=True)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20002523, textId=20002523)
        set_timer(timerId='1', seconds=10)
        # <action name="메쉬를설정한다" arg1="297-328" arg2="0" arg3="0" arg4="200"/>
        set_breakable(triggerIds=[905,906,907,908,1905,1906,1907,1908,2905,2906,2907,2908,3905,3906,3907,3908], enabled=True)
        set_breakable(triggerIds=[901,902,903,904,909,910,911,912,913,914,915,916,1901,1902,1903,1904,1909,1910,1911,1912,1913,1914,1915,1916,2901,2902,2903,2904,2909,2910,2911,2912,2913,2914,2915,2916,3901,3902,3903,3904,3909,3910,3911,3912,3913,3914,3915,3916], enabled=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            hide_guide_summary(entityId=20002523)
            return To1번2()


class To1번2(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8042], visible=False)
        set_timer(timerId='1', seconds=30, clearAtZero=False)
        create_monster(spawnIds=[3002])

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            destroy_monster(spawnIds=[3002])
            set_interact_object(triggerIds=[10001050], state=2)
            set_interact_object(triggerIds=[10001051], state=2)
            set_interact_object(triggerIds=[10001052], state=2)
            set_interact_object(triggerIds=[10001053], state=2)
            return 랜덤선택1To2()
        if monster_dead(boxIds=[3002]):
            return To2번2()


class To2번2(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=30, clearAtZero=False)
        set_interact_object(triggerIds=[10001051], state=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            destroy_monster(spawnIds=[3004])
            set_interact_object(triggerIds=[10001050], state=2)
            set_interact_object(triggerIds=[10001051], state=2)
            set_interact_object(triggerIds=[10001052], state=2)
            set_interact_object(triggerIds=[10001053], state=2)
            return 랜덤선택1To2()
        if object_interacted(interactIds=[10001051], arg2=0):
            return 끝2()


class 번3(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8044], visible=True)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20002523, textId=20002523)
        set_timer(timerId='1', seconds=10)
        # <action name="메쉬를설정한다" arg1="233-264" arg2="0" arg3="0" arg4="200"/>
        set_breakable(triggerIds=[909,910,911,912,1909,1910,1911,1912,2909,2910,2911,2912,3909,3910,3911,3912], enabled=True)
        set_breakable(triggerIds=[901,902,903,904,905,906,907,908,913,914,915,916,1901,1902,1903,1904,1905,1906,1907,1908,1913,1914,1915,1916,2901,2902,2903,2904,2905,2906,2907,2908,2913,2914,2915,2916,3901,3902,3903,3904,3905,3906,3907,3908,3913,3914,3915,3916], enabled=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            hide_guide_summary(entityId=20002523)
            return To1번3()


class To1번3(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8044], visible=False)
        set_timer(timerId='1', seconds=30, clearAtZero=False)
        create_monster(spawnIds=[3003])

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            destroy_monster(spawnIds=[3003])
            set_interact_object(triggerIds=[10001050], state=2)
            set_interact_object(triggerIds=[10001051], state=2)
            set_interact_object(triggerIds=[10001052], state=2)
            set_interact_object(triggerIds=[10001053], state=2)
            return 랜덤선택1To3()
        if monster_dead(boxIds=[3003]):
            return To2번3()


class To2번3(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=30, clearAtZero=False)
        set_interact_object(triggerIds=[10001050], state=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            destroy_monster(spawnIds=[3004])
            set_interact_object(triggerIds=[10001050], state=2)
            set_interact_object(triggerIds=[10001051], state=2)
            set_interact_object(triggerIds=[10001052], state=2)
            set_interact_object(triggerIds=[10001053], state=2)
            return 랜덤선택1To3()
        if object_interacted(interactIds=[10001050], arg2=0):
            return 끝3()


class 번4(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8043], visible=True)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20002523, textId=20002523)
        set_timer(timerId='1', seconds=10)
        # <action name="메쉬를설정한다" arg1="201-232" arg2="0" arg3="0" arg4="200"/>
        set_breakable(triggerIds=[913,914,915,916,1913,1914,1915,1916,2913,2914,2915,2916,3913,3914,3915,3916], enabled=True)
        set_breakable(triggerIds=[901,902,903,904,905,906,907,908,909,910,911,912,1901,1902,1903,1904,1905,1906,1907,1908,1909,1910,1911,1912,2901,2902,2903,2904,2905,2906,2907,2908,2909,2910,2911,2912,3901,3902,3903,3904,3905,3906,3907,3908,3909,3910,3911,3912], enabled=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            hide_guide_summary(entityId=20002523)
            return To1번4()


class To1번4(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8043], visible=False)
        set_timer(timerId='1', seconds=30, clearAtZero=False)
        create_monster(spawnIds=[3004])

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            destroy_monster(spawnIds=[3004])
            set_interact_object(triggerIds=[10001050], state=2)
            set_interact_object(triggerIds=[10001051], state=2)
            set_interact_object(triggerIds=[10001052], state=2)
            set_interact_object(triggerIds=[10001053], state=2)
            return 랜덤선택1To4()
        if monster_dead(boxIds=[3004]):
            return To2번4()


class To2번4(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=30, clearAtZero=False)
        set_interact_object(triggerIds=[10001053], state=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            destroy_monster(spawnIds=[3004])
            set_interact_object(triggerIds=[10001050], state=2)
            set_interact_object(triggerIds=[10001051], state=2)
            set_interact_object(triggerIds=[10001052], state=2)
            set_interact_object(triggerIds=[10001053], state=2)
            return 랜덤선택1To4()
        if object_interacted(interactIds=[10001053], arg2=0):
            return 끝4()


class 끝1(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=30, clearAtZero=False)
        set_interact_object(triggerIds=[10001050], state=2)
        set_interact_object(triggerIds=[10001051], state=2)
        set_interact_object(triggerIds=[10001052], state=2)
        set_interact_object(triggerIds=[10001053], state=2)
        set_breakable(triggerIds=[901,902,903,904,1901,1902,1903,1904,2901,2902,2903,2904,3901,3902,3903,3904,905,906,907,908,909,910,911,912,913,914,915,916,1905,1906,1907,1908,1909,1910,1911,1912,1913,1914,1915,1916,2905,2906,2907,2908,2909,2910,2911,2912,2913,2914,2915,2916,3905,3906,3907,3908,3909,3910,3911,3912,3913,3914,3915,3916], enabled=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 랜덤선택1To1()


class 끝2(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=30, clearAtZero=False)
        set_interact_object(triggerIds=[10001050], state=2)
        set_interact_object(triggerIds=[10001051], state=2)
        set_interact_object(triggerIds=[10001052], state=2)
        set_interact_object(triggerIds=[10001053], state=2)
        set_breakable(triggerIds=[901,902,903,904,1901,1902,1903,1904,2901,2902,2903,2904,3901,3902,3903,3904,905,906,907,908,909,910,911,912,913,914,915,916,1905,1906,1907,1908,1909,1910,1911,1912,1913,1914,1915,1916,2905,2906,2907,2908,2909,2910,2911,2912,2913,2914,2915,2916,3905,3906,3907,3908,3909,3910,3911,3912,3913,3914,3915,3916], enabled=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 랜덤선택1To2()


class 끝3(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=30, clearAtZero=False)
        set_interact_object(triggerIds=[10001050], state=2)
        set_interact_object(triggerIds=[10001051], state=2)
        set_interact_object(triggerIds=[10001052], state=2)
        set_interact_object(triggerIds=[10001053], state=2)
        set_breakable(triggerIds=[901,902,903,904,1901,1902,1903,1904,2901,2902,2903,2904,3901,3902,3903,3904,905,906,907,908,909,910,911,912,913,914,915,916,1905,1906,1907,1908,1909,1910,1911,1912,1913,1914,1915,1916,2905,2906,2907,2908,2909,2910,2911,2912,2913,2914,2915,2916,3905,3906,3907,3908,3909,3910,3911,3912,3913,3914,3915,3916], enabled=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 랜덤선택1To3()


class 끝4(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=30, clearAtZero=False)
        set_interact_object(triggerIds=[10001050], state=2)
        set_interact_object(triggerIds=[10001051], state=2)
        set_interact_object(triggerIds=[10001052], state=2)
        set_interact_object(triggerIds=[10001053], state=2)
        set_breakable(triggerIds=[901,902,903,904,1901,1902,1903,1904,2901,2902,2903,2904,3901,3902,3903,3904,905,906,907,908,909,910,911,912,913,914,915,916,1905,1906,1907,1908,1909,1910,1911,1912,1913,1914,1915,1916,2905,2906,2907,2908,2909,2910,2911,2912,2913,2914,2915,2916,3905,3906,3907,3908,3909,3910,3911,3912,3913,3914,3915,3916], enabled=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 랜덤선택1To4()


