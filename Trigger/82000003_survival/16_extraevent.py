""" trigger/82000003_survival/16_extraevent.xml """
from common import *
import state


class Setting(state.State):
    def on_enter(self):
        add_buff(boxIds=[9000], skillId=70001101, level=1, arg4=False, arg5=False) # 변신 탈 것 해제용 버프
        set_gravity(gravity=0)
        remove_buff(boxId=9000, skillId=71000075)
        remove_buff(boxId=9000, skillId=71000052)
        remove_buff(boxId=9000, skillId=71000076)
        set_user_value(key='ExtraEventCheck', value=0)
        set_user_value(key='ExtraEventOff', value=0)
        set_user_value(key='ExtraEventTestOn', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='ExtraEventTestOn', value=1): # ExtraEventOn / ExtraEventRandomDelay01 / ExtraEvent01_Fast / ExtraEvent02_MapHack / ExtraEvent03_RobotSpawn / ExtraEvent04_DogEverywhere / ExtraEvent05_SkillCoolDownTimeReduce / ExtraEvent06_NoMoreFarming
            return ExtraEventOn()
        if user_value(key='ExtraEventCheck', value=1):
            return ExtraEventOccurrenceProbability()


class ExtraEventOccurrenceProbability(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=60):
            return ExtraEventOff()
        if random_condition(rate=40):
            return ExtraEventOn()
        if user_value(key='ExtraEventOff', value=1):
            return Quit()


class ExtraEventOff(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='ExtraEventOff', value=1):
            return Quit()


class ExtraEventOn(state.State):
    def on_enter(self):
        write_log(logName='Survival', arg3='MokumEventOn') # 모쿰 이벤트 로그 - 모쿰 소환 됨

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return RelicLeft05()


class RelicLeft05(state.State):
    def on_enter(self):
        set_user_value(triggerId=11, key='RelicMobSpawn', value=1)
        set_user_value(triggerId=12, key='RelicMobSpawn', value=1)
        set_user_value(triggerId=13, key='RelicMobSpawn', value=1)
        set_user_value(triggerId=14, key='RelicMobSpawn', value=1)
        set_user_value(triggerId=15, key='RelicMobSpawn', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='RelicMobRedDie', value=1):
            return RelicLeft04_NoRed()
        if user_value(key='RelicMobSkyblueDie', value=1):
            return RelicLeft04_NoSkyblue()
        if user_value(key='RelicMobGreenDie', value=1):
            return RelicLeft04_NoGreen()
        if user_value(key='RelicMobYellowDie', value=1):
            return RelicLeft04_NoYellow()
        if user_value(key='RelicMobGreyDie', value=1):
            return RelicLeft04_NoGrey()
        if user_value(key='ExtraEventOff', value=1):
            return Quit()

    def on_exit(self):
        play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        play_system_sound_in_box(sound='System_Mokum_Die_01')
        show_guide_summary(entityId=28200002, textId=28200002, duration=4000) # 가이드 : [b:첫 번째] 모쿰이 잡혔습니다!
        side_npc_talk(npcId=21001019, type='talkbottom', illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__0$')


#  4 마리 남음 
class RelicLeft04_NoRed(state.State):
    def on_enter(self):
        write_log(logName='Survival', arg3='MokumKill_01') # 모쿰 이벤트 로그 - 4마리 남음

    def on_tick(self) -> state.State:
        if user_value(key='RelicMobSkyblueDie', value=1):
            return RelicLeft03_NoRed_NoSkyblue()
        if user_value(key='RelicMobGreenDie', value=1):
            return RelicLeft03_NoRed_NoGreen()
        if user_value(key='RelicMobYellowDie', value=1):
            return RelicLeft03_NoRed_NoYellow()
        if user_value(key='RelicMobGreyDie', value=1):
            return RelicLeft03_NoRed_NoGrey()
        if user_value(key='ExtraEventOff', value=1):
            return Quit()

    def on_exit(self):
        play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        play_system_sound_in_box(sound='System_Mokum_Die_01')
        show_guide_summary(entityId=28200003, textId=28200003, duration=3000) # 가이드 : [b:두 번째] 모쿰이 잡혔습니다!
        side_npc_talk(npcId=21001019, type='talkbottom', illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__1$')


class RelicLeft04_NoSkyblue(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='RelicMobRedDie', value=1):
            return RelicLeft03_NoRed_NoSkyblue()
        if user_value(key='RelicMobGreenDie', value=1):
            return RelicLeft03_NoSkyblue_NoGreen()
        if user_value(key='RelicMobYellowDie', value=1):
            return RelicLeft03_NoSkyblue_NoYellow()
        if user_value(key='RelicMobGreyDie', value=1):
            return RelicLeft03_NoSkyblue_NoGrey()
        if user_value(key='ExtraEventOff', value=1):
            return Quit()

    def on_exit(self):
        play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        play_system_sound_in_box(sound='System_Mokum_Die_01')
        show_guide_summary(entityId=28200003, textId=28200003, duration=3000) # 가이드 : [b:두 번째] 모쿰이 잡혔습니다!
        side_npc_talk(npcId=21001019, type='talkbottom', illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__1$')


class RelicLeft04_NoGreen(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='RelicMobRedDie', value=1):
            return RelicLeft03_NoRed_NoGreen()
        if user_value(key='RelicMobSkyblueDie', value=1):
            return RelicLeft03_NoSkyblue_NoGreen()
        if user_value(key='RelicMobYellowDie', value=1):
            return RelicLeft03_NoGreen_NoYellow()
        if user_value(key='RelicMobGreyDie', value=1):
            return RelicLeft03_NoGreen_NoGrey()
        if user_value(key='ExtraEventOff', value=1):
            return Quit()

    def on_exit(self):
        play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        play_system_sound_in_box(sound='System_Mokum_Die_01')
        show_guide_summary(entityId=28200003, textId=28200003, duration=3000) # 가이드 : [b:두 번째] 모쿰이 잡혔습니다!
        side_npc_talk(npcId=21001019, type='talkbottom', illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__1$')


class RelicLeft04_NoYellow(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='RelicMobRedDie', value=1):
            return RelicLeft03_NoRed_NoYellow()
        if user_value(key='RelicMobSkyblueDie', value=1):
            return RelicLeft03_NoSkyblue_NoYellow()
        if user_value(key='RelicMobGreenDie', value=1):
            return RelicLeft03_NoGreen_NoYellow()
        if user_value(key='RelicMobGreyDie', value=1):
            return RelicLeft03_NoYellow_NoGrey()
        if user_value(key='ExtraEventOff', value=1):
            return Quit()

    def on_exit(self):
        play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        play_system_sound_in_box(sound='System_Mokum_Die_01')
        show_guide_summary(entityId=28200003, textId=28200003, duration=3000) # 가이드 : [b:두 번째] 모쿰이 잡혔습니다!
        side_npc_talk(npcId=21001019, type='talkbottom', illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__1$')


class RelicLeft04_NoGrey(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='RelicMobRedDie', value=1):
            return RelicLeft03_NoRed_NoGrey()
        if user_value(key='RelicMobSkyblueDie', value=1):
            return RelicLeft03_NoSkyblue_NoGrey()
        if user_value(key='RelicMobGreenDie', value=1):
            return RelicLeft03_NoGreen_NoGrey()
        if user_value(key='RelicMobYellowDie', value=1):
            return RelicLeft03_NoYellow_NoGrey()
        if user_value(key='ExtraEventOff', value=1):
            return Quit()

    def on_exit(self):
        play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        play_system_sound_in_box(sound='System_Mokum_Die_01')
        show_guide_summary(entityId=28200003, textId=28200003, duration=3000) # 가이드 : [b:두 번째] 모쿰이 잡혔습니다!
        side_npc_talk(npcId=21001019, type='talkbottom', illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__1$')


#  3 마리 남음 
class RelicLeft03_NoRed_NoSkyblue(state.State):
    def on_enter(self):
        write_log(logName='Survival', arg3='MokumKill_02') # 모쿰 이벤트 로그 - 3마리 남음

    def on_tick(self) -> state.State:
        if user_value(key='RelicMobGreenDie', value=1):
            return RelicLeft02_NoRed_NoSkyblue_NoGreen()
        if user_value(key='RelicMobYellowDie', value=1):
            return RelicLeft02_NoRed_NoSkyblue_NoYellow()
        if user_value(key='RelicMobGreyDie', value=1):
            return RelicLeft02_NoRed_NoSkyblue_NoGrey()
        if user_value(key='ExtraEventOff', value=1):
            return Quit()

    def on_exit(self):
        play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        play_system_sound_in_box(sound='System_Mokum_Die_01')
        show_guide_summary(entityId=28200004, textId=28200004, duration=3000) # 가이드 : [b:세 번째] 모쿰이 잡혔습니다!
        side_npc_talk(npcId=21001019, type='talkbottom', illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__2$')


class RelicLeft03_NoRed_NoGreen(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='RelicMobSkyblueDie', value=1):
            return RelicLeft02_NoRed_NoSkyblue_NoGreen()
        if user_value(key='RelicMobYellowDie', value=1):
            return RelicLeft02_NoRed_NoGreen_NoYellow()
        if user_value(key='RelicMobGreyDie', value=1):
            return RelicLeft02_NoRed_NoGreen_NoGrey()
        if user_value(key='ExtraEventOff', value=1):
            return Quit()

    def on_exit(self):
        play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        play_system_sound_in_box(sound='System_Mokum_Die_01')
        show_guide_summary(entityId=28200004, textId=28200004, duration=3000) # 가이드 : [b:세 번째] 모쿰이 잡혔습니다!
        side_npc_talk(npcId=21001019, type='talkbottom', illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__2$')


class RelicLeft03_NoRed_NoYellow(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='RelicMobSkyblueDie', value=1):
            return RelicLeft02_NoRed_NoSkyblue_NoYellow()
        if user_value(key='RelicMobGreenDie', value=1):
            return RelicLeft02_NoRed_NoGreen_NoYellow()
        if user_value(key='RelicMobGreyDie', value=1):
            return RelicLeft02_NoRed_NoYellow_NoGrey()
        if user_value(key='ExtraEventOff', value=1):
            return Quit()

    def on_exit(self):
        play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        play_system_sound_in_box(sound='System_Mokum_Die_01')
        show_guide_summary(entityId=28200004, textId=28200004, duration=3000) # 가이드 : [b:세 번째] 모쿰이 잡혔습니다!
        side_npc_talk(npcId=21001019, type='talkbottom', illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__2$')


class RelicLeft03_NoRed_NoGrey(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='RelicMobSkyblueDie', value=1):
            return RelicLeft02_NoRed_NoSkyblue_NoGrey()
        if user_value(key='RelicMobGreenDie', value=1):
            return RelicLeft02_NoRed_NoGreen_NoGrey()
        if user_value(key='RelicMobYellowDie', value=1):
            return RelicLeft02_NoRed_NoYellow_NoGrey()
        if user_value(key='ExtraEventOff', value=1):
            return Quit()

    def on_exit(self):
        play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        play_system_sound_in_box(sound='System_Mokum_Die_01')
        show_guide_summary(entityId=28200004, textId=28200004, duration=3000) # 가이드 : [b:세 번째] 모쿰이 잡혔습니다!
        side_npc_talk(npcId=21001019, type='talkbottom', illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__2$')


class RelicLeft03_NoSkyblue_NoGreen(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='RelicMobRedDie', value=1):
            return RelicLeft02_NoRed_NoSkyblue_NoGreen()
        if user_value(key='RelicMobYellowDie', value=1):
            return RelicLeft02_NoSkyblue_NoGreen_NoYellow()
        if user_value(key='RelicMobGreyDie', value=1):
            return RelicLeft02_NoSkyblue_NoGreen_NoGrey()
        if user_value(key='ExtraEventOff', value=1):
            return Quit()

    def on_exit(self):
        play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        play_system_sound_in_box(sound='System_Mokum_Die_01')
        show_guide_summary(entityId=28200004, textId=28200004, duration=3000) # 가이드 : [b:세 번째] 모쿰이 잡혔습니다!
        side_npc_talk(npcId=21001019, type='talkbottom', illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__2$')


class RelicLeft03_NoSkyblue_NoYellow(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='RelicMobRedDie', value=1):
            return RelicLeft02_NoRed_NoSkyblue_NoYellow()
        if user_value(key='RelicMobGreenDie', value=1):
            return RelicLeft02_NoSkyblue_NoGreen_NoYellow()
        if user_value(key='RelicMobGreyDie', value=1):
            return RelicLeft02_NoSkyblue_NoYellow_NoGrey()
        if user_value(key='ExtraEventOff', value=1):
            return Quit()

    def on_exit(self):
        play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        play_system_sound_in_box(sound='System_Mokum_Die_01')
        show_guide_summary(entityId=28200004, textId=28200004, duration=3000) # 가이드 : [b:세 번째] 모쿰이 잡혔습니다!
        side_npc_talk(npcId=21001019, type='talkbottom', illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__2$')


class RelicLeft03_NoSkyblue_NoGrey(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='RelicMobRedDie', value=1):
            return RelicLeft02_NoRed_NoSkyblue_NoGrey()
        if user_value(key='RelicMobGreenDie', value=1):
            return RelicLeft02_NoSkyblue_NoGreen_NoGrey()
        if user_value(key='RelicMobYellowDie', value=1):
            return RelicLeft02_NoSkyblue_NoYellow_NoGrey()
        if user_value(key='ExtraEventOff', value=1):
            return Quit()

    def on_exit(self):
        play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        play_system_sound_in_box(sound='System_Mokum_Die_01')
        show_guide_summary(entityId=28200004, textId=28200004, duration=3000) # 가이드 : [b:세 번째] 모쿰이 잡혔습니다!
        side_npc_talk(npcId=21001019, type='talkbottom', illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__2$')


class RelicLeft03_NoGreen_NoYellow(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='RelicMobRedDie', value=1):
            return RelicLeft02_NoRed_NoGreen_NoYellow()
        if user_value(key='RelicMobSkyblueDie', value=1):
            return RelicLeft02_NoSkyblue_NoGreen_NoYellow()
        if user_value(key='RelicMobGreyDie', value=1):
            return RelicLeft02_NoGreen_NoYellow_NoGrey()
        if user_value(key='ExtraEventOff', value=1):
            return Quit()

    def on_exit(self):
        play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        play_system_sound_in_box(sound='System_Mokum_Die_01')
        show_guide_summary(entityId=28200004, textId=28200004, duration=3000) # 가이드 : [b:세 번째] 모쿰이 잡혔습니다!
        side_npc_talk(npcId=21001019, type='talkbottom', illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__2$')


class RelicLeft03_NoGreen_NoGrey(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='RelicMobRedDie', value=1):
            return RelicLeft02_NoRed_NoGreen_NoGrey()
        if user_value(key='RelicMobSkyblueDie', value=1):
            return RelicLeft02_NoSkyblue_NoGreen_NoGrey()
        if user_value(key='RelicMobYellowDie', value=1):
            return RelicLeft02_NoGreen_NoYellow_NoGrey()
        if user_value(key='ExtraEventOff', value=1):
            return Quit()

    def on_exit(self):
        play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        play_system_sound_in_box(sound='System_Mokum_Die_01')
        show_guide_summary(entityId=28200004, textId=28200004, duration=3000) # 가이드 : [b:세 번째] 모쿰이 잡혔습니다!
        side_npc_talk(npcId=21001019, type='talkbottom', illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__2$')


class RelicLeft03_NoYellow_NoGrey(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='RelicMobRedDie', value=1):
            return RelicLeft02_NoRed_NoYellow_NoGrey()
        if user_value(key='RelicMobSkyblueDie', value=1):
            return RelicLeft02_NoSkyblue_NoYellow_NoGrey()
        if user_value(key='RelicMobGreenDie', value=1):
            return RelicLeft02_NoGreen_NoYellow_NoGrey()
        if user_value(key='ExtraEventOff', value=1):
            return Quit()

    def on_exit(self):
        play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        play_system_sound_in_box(sound='System_Mokum_Die_01')
        show_guide_summary(entityId=28200004, textId=28200004, duration=3000) # 가이드 : [b:세 번째] 모쿰이 잡혔습니다!
        side_npc_talk(npcId=21001019, type='talkbottom', illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__2$')


#  2 마리 남음 
class RelicLeft02_NoRed_NoSkyblue_NoGreen(state.State):
    def on_enter(self):
        write_log(logName='Survival', arg3='MokumKill_03') # 모쿰 이벤트 로그 - 2마리 남음

    def on_tick(self) -> state.State:
        if user_value(key='RelicMobYellowDie', value=1):
            return RelicLeft01_OnlyGrey()
        if user_value(key='RelicMobGreyDie', value=1):
            return RelicLeft01_OnlyYellow()
        if user_value(key='ExtraEventOff', value=1):
            return Quit()

    def on_exit(self):
        play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        play_system_sound_in_box(sound='System_Mokum_Die_01')
        show_guide_summary(entityId=28200005, textId=28200005, duration=3000) # 가이드 : [b:네 번째] 모쿰이 잡혔습니다!
        side_npc_talk(npcId=21001019, type='talkbottom', illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__3$')


class RelicLeft02_NoRed_NoSkyblue_NoYellow(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='RelicMobGreenDie', value=1):
            return RelicLeft01_OnlyGrey()
        if user_value(key='RelicMobGreyDie', value=1):
            return RelicLeft01_OnlyGreen()
        if user_value(key='ExtraEventOff', value=1):
            return Quit()

    def on_exit(self):
        play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        play_system_sound_in_box(sound='System_Mokum_Die_01')
        show_guide_summary(entityId=28200005, textId=28200005, duration=3000) # 가이드 : [b:네 번째] 모쿰이 잡혔습니다!
        side_npc_talk(npcId=21001019, type='talkbottom', illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__3$')


class RelicLeft02_NoRed_NoSkyblue_NoGrey(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='RelicMobGreenDie', value=1):
            return RelicLeft01_OnlyYellow()
        if user_value(key='RelicMobYellowDie', value=1):
            return RelicLeft01_OnlyGreen()
        if user_value(key='ExtraEventOff', value=1):
            return Quit()

    def on_exit(self):
        play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        play_system_sound_in_box(sound='System_Mokum_Die_01')
        show_guide_summary(entityId=28200005, textId=28200005, duration=3000) # 가이드 : [b:네 번째] 모쿰이 잡혔습니다!
        side_npc_talk(npcId=21001019, type='talkbottom', illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__3$')


class RelicLeft02_NoRed_NoGreen_NoYellow(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='RelicMobSkyblueDie', value=1):
            return RelicLeft01_OnlyGrey()
        if user_value(key='RelicMobGreyDie', value=1):
            return RelicLeft01_OnlySkyblue()
        if user_value(key='ExtraEventOff', value=1):
            return Quit()

    def on_exit(self):
        play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        play_system_sound_in_box(sound='System_Mokum_Die_01')
        show_guide_summary(entityId=28200005, textId=28200005, duration=3000) # 가이드 : [b:네 번째] 모쿰이 잡혔습니다!
        side_npc_talk(npcId=21001019, type='talkbottom', illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__3$')


class RelicLeft02_NoRed_NoGreen_NoGrey(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='RelicMobSkyblueDie', value=1):
            return RelicLeft01_OnlyYellow()
        if user_value(key='RelicMobYellowDie', value=1):
            return RelicLeft01_OnlySkyblue()
        if user_value(key='ExtraEventOff', value=1):
            return Quit()

    def on_exit(self):
        play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        play_system_sound_in_box(sound='System_Mokum_Die_01')
        show_guide_summary(entityId=28200005, textId=28200005, duration=3000) # 가이드 : [b:네 번째] 모쿰이 잡혔습니다!
        side_npc_talk(npcId=21001019, type='talkbottom', illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__3$')


class RelicLeft02_NoRed_NoYellow_NoGrey(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='RelicMobSkyblueDie', value=1):
            return RelicLeft01_OnlyGreen()
        if user_value(key='RelicMobGreenDie', value=1):
            return RelicLeft01_OnlySkyblue()
        if user_value(key='ExtraEventOff', value=1):
            return Quit()

    def on_exit(self):
        play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        play_system_sound_in_box(sound='System_Mokum_Die_01')
        show_guide_summary(entityId=28200005, textId=28200005, duration=3000) # 가이드 : [b:네 번째] 모쿰이 잡혔습니다!
        side_npc_talk(npcId=21001019, type='talkbottom', illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__3$')


class RelicLeft02_NoSkyblue_NoGreen_NoYellow(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='RelicMobRedDie', value=1):
            return RelicLeft01_OnlyGrey()
        if user_value(key='RelicMobGreyDie', value=1):
            return RelicLeft01_OnlyRed()
        if user_value(key='ExtraEventOff', value=1):
            return Quit()

    def on_exit(self):
        play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        play_system_sound_in_box(sound='System_Mokum_Die_01')
        show_guide_summary(entityId=28200005, textId=28200005, duration=3000) # 가이드 : [b:네 번째] 모쿰이 잡혔습니다!
        side_npc_talk(npcId=21001019, type='talkbottom', illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__3$')


class RelicLeft02_NoSkyblue_NoGreen_NoGrey(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='RelicMobRedDie', value=1):
            return RelicLeft01_OnlyYellow()
        if user_value(key='RelicMobYellowDie', value=1):
            return RelicLeft01_OnlyRed()
        if user_value(key='ExtraEventOff', value=1):
            return Quit()

    def on_exit(self):
        play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        play_system_sound_in_box(sound='System_Mokum_Die_01')
        show_guide_summary(entityId=28200005, textId=28200005, duration=3000) # 가이드 : [b:네 번째] 모쿰이 잡혔습니다!
        side_npc_talk(npcId=21001019, type='talkbottom', illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__3$')


class RelicLeft02_NoSkyblue_NoYellow_NoGrey(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='RelicMobRedDie', value=1):
            return RelicLeft01_OnlyGreen()
        if user_value(key='RelicMobGreenDie', value=1):
            return RelicLeft01_OnlyRed()
        if user_value(key='ExtraEventOff', value=1):
            return Quit()

    def on_exit(self):
        play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        play_system_sound_in_box(sound='System_Mokum_Die_01')
        show_guide_summary(entityId=28200005, textId=28200005, duration=3000) # 가이드 : [b:네 번째] 모쿰이 잡혔습니다!
        side_npc_talk(npcId=21001019, type='talkbottom', illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__3$')


class RelicLeft02_NoGreen_NoYellow_NoGrey(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='RelicMobRedDie', value=1):
            return RelicLeft01_OnlySkyblue()
        if user_value(key='RelicMobSkyblueDie', value=1):
            return RelicLeft01_OnlyRed()
        if user_value(key='ExtraEventOff', value=1):
            return Quit()

    def on_exit(self):
        play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        play_system_sound_in_box(sound='System_Mokum_Die_01')
        show_guide_summary(entityId=28200005, textId=28200005, duration=3000) # 가이드 : [b:네 번째] 모쿰이 잡혔습니다!
        side_npc_talk(npcId=21001019, type='talkbottom', illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__3$')


#  1 마리 남음 
class RelicLeft01_OnlyRed(state.State):
    def on_enter(self):
        write_log(logName='Survival', arg3='MokumKill_04') # 모쿰 이벤트 로그 - 1마리 남음

    def on_tick(self) -> state.State:
        if user_value(key='RelicMobRedDie', value=1):
            return ExtraEventRandomDelay01()
        if user_value(key='ExtraEventOff', value=1):
            return Quit()

    def on_exit(self):
        play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        play_system_sound_in_box(sound='System_Mokum_Die_01')
        show_guide_summary(entityId=28200006, textId=28200006, duration=3000) # 가이드 : [b:마지막] 모쿰이 잡혔습니다!
        side_npc_talk(npcId=21001019, type='talkbottom', illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__4$')


class RelicLeft01_OnlySkyblue(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='RelicMobSkyblueDie', value=1):
            return ExtraEventRandomDelay01()
        if user_value(key='ExtraEventOff', value=1):
            return Quit()

    def on_exit(self):
        play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        play_system_sound_in_box(sound='System_Mokum_Die_01')
        show_guide_summary(entityId=28200006, textId=28200006, duration=3000) # 가이드 : [b:마지막] 모쿰이 잡혔습니다!
        side_npc_talk(npcId=21001019, type='talkbottom', illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__4$')


class RelicLeft01_OnlyGreen(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='RelicMobGreenDie', value=1):
            return ExtraEventRandomDelay01()
        if user_value(key='ExtraEventOff', value=1):
            return Quit()

    def on_exit(self):
        play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        play_system_sound_in_box(sound='System_Mokum_Die_01')
        show_guide_summary(entityId=28200006, textId=28200006, duration=3000) # 가이드 : [b:마지막] 모쿰이 잡혔습니다!
        side_npc_talk(npcId=21001019, type='talkbottom', illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__4$')


class RelicLeft01_OnlyYellow(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='RelicMobYellowDie', value=1):
            return ExtraEventRandomDelay01()
        if user_value(key='ExtraEventOff', value=1):
            return Quit()

    def on_exit(self):
        play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        play_system_sound_in_box(sound='System_Mokum_Die_01')
        show_guide_summary(entityId=28200006, textId=28200006, duration=3000) # 가이드 : [b:마지막] 모쿰이 잡혔습니다!
        side_npc_talk(npcId=21001019, type='talkbottom', illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__4$')


class RelicLeft01_OnlyGrey(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='RelicMobGreyDie', value=1):
            return ExtraEventRandomDelay01()
        if user_value(key='ExtraEventOff', value=1):
            return Quit()

    def on_exit(self):
        play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        play_system_sound_in_box(sound='System_Mokum_Die_01')
        show_guide_summary(entityId=28200006, textId=28200006, duration=3000) # 가이드 : [b:마지막] 모쿰이 잡혔습니다!
        side_npc_talk(npcId=21001019, type='talkbottom', illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__16_ExtraEvent__4$')


class ExtraEventRandomDelay01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return ExtraEventRandomDelay02()
        if user_value(key='ExtraEventOff', value=1):
            return Quit()


class ExtraEventRandomDelay02(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_Mokum_Message_01')
        side_npc_talk(npcId=21001019, type='talkbottom', illust='MushroomRichPorter_normal', duration=8000, script='$82000002_survival__16_ExtraEvent__5$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return ExtraEventRandomDelay03()
        if user_value(key='ExtraEventOff', value=1):
            return Quit()


class ExtraEventRandomDelay03(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')
        show_guide_summary(entityId=28200007, textId=28200007, duration=4000) # 가이드 : 모쿰의 장난이 시작됩니다!
        write_log(logName='Survival', arg3='MokumEventStart') # 모쿰 이벤트 로그 - 이벤트 시작

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return ExtraEventRandom()
        if user_value(key='ExtraEventOff', value=1):
            return Quit()


class ExtraEventRandom(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=20):
            return ExtraEvent01_Fast()
        if random_condition(rate=20):
            return ExtraEvent02_MapHack()
        if random_condition(rate=20):
            return ExtraEvent03_RobotSpawn()
        if random_condition(rate=20):
            return ExtraEvent04_SkillCoolDownTimeReduce()
        if random_condition(rate=20):
            return ExtraEvent05_NoMoreFarming()
        if user_value(key='ExtraEventOff', value=1):
            return Quit()


class ExtraEvent01_Fast(state.State):
    def on_enter(self):
        write_log(logName='Survival', arg3='MokumEvent_01') # 모쿰 이벤트 로그 1
        play_system_sound_in_box(sound='System_Mokum_Completion_01')
        side_npc_talk(npcId=21001019, type='talkbottom', illust='MushroomRichPorter_normal', duration=8000, script='$82000002_survival__16_ExtraEvent__6$')
        add_buff(boxIds=[9000], skillId=71000075, level=1, arg4=False, arg5=False)
        set_gravity(gravity=30)

    def on_tick(self) -> state.State:
        if user_value(key='ExtraEventOff', value=1):
            return Quit()


class ExtraEvent02_MapHack(state.State):
    def on_enter(self):
        write_log(logName='Survival', arg3='MokumEvent_02') # 모쿰 이벤트 로그 2
        remove_buff(boxId=9000, skillId=71000052)
        play_system_sound_in_box(sound='System_Mokum_Completion_01')
        side_npc_talk(npcId=21001019, type='talkbottom', illust='MushroomRichPorter_normal', duration=8000, script='$82000002_survival__16_ExtraEvent__7$')
        add_buff(boxIds=[9000], skillId=71000052, level=2, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if user_value(key='ExtraEventOff', value=1):
            return Quit()


class ExtraEvent03_RobotSpawn(state.State):
    def on_enter(self):
        write_log(logName='Survival', arg3='MokumEvent_03') # 모쿰 이벤트 로그 3
        play_system_sound_in_box(sound='System_Mokum_Completion_01')
        side_npc_talk(npcId=21001019, type='talkbottom', illust='MushroomRichPorter_normal', duration=8000, script='$82000002_survival__16_ExtraEvent__8$')
        set_user_value(triggerId=10, key='BattleRidingOnCount', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='ExtraEventOff', value=1):
            return Quit()

    def on_exit(self):
        set_user_value(triggerId=10, key='BattleRidingOff', value=1)


class ExtraEvent04_SkillCoolDownTimeReduce(state.State):
    def on_enter(self):
        write_log(logName='Survival', arg3='MokumEvent_04') # 모쿰 이벤트 로그 4
        play_system_sound_in_box(sound='System_Mokum_Completion_01')
        side_npc_talk(npcId=21001019, type='talkbottom', illust='MushroomRichPorter_normal', duration=8000, script='$82000002_survival__16_ExtraEvent__9$')
        add_buff(boxIds=[9000], skillId=71000076, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if user_value(key='ExtraEventOff', value=1):
            return Quit()


class ExtraEvent05_NoMoreFarming(state.State):
    def on_enter(self):
        write_log(logName='Survival', arg3='MokumEvent_05') # 모쿰 이벤트 로그 5
        play_system_sound_in_box(sound='System_Mokum_Completion_01')
        side_npc_talk(npcId=21001019, type='talkbottom', illust='MushroomRichPorter_normal', duration=8000, script='$82000002_survival__16_ExtraEvent__10$')
        start_combine_spawn(groupId=[355,356,357,358,359,360,361,362,363,364,365,366,367,368,369,370,371,372,373,374,375,376,377,378,379,380,381,382,383,384,385,386,387,388,389,390,391,392,393,394,395,396,397,398,399,400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,419,420,421,422,423,424,425,426,427,428,429,430,431,432,433,434,435,436,437,438,439,440,441,442,443,444,445,446,447,448,449,450,451,452,453,454,455,456,457,458,459,460,461,462,463,464,465,466,467,468,469,470,471,472,473,474,475,476,477], isStart=False) # 나태 버섯 Normal Mob
        start_combine_spawn(groupId=[10000342,10000343,10000344,10000345,10000346,10000347,10000348,10000349,10000350,10000351,10000352,10000353,10000354,10000355,10000356,10000357,10000358,10000359,10000360,10000361,10000362,10000363,10000364,10000365,10000366,10000367,10000368,10000369,10000370,10000371,10000372,10000373,10000374,10000375,10000376,10000377,10000378,10000379,10000380,10000381], isStart=False) # groupId="10000342-10000381" 황금 상자 Rare Box
        start_combine_spawn(groupId=[319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354], isStart=False) # 축복의 슬라임 Rare Mob
        start_combine_spawn(groupId=[10000382,10000383,10000384,10000385,10000386,10000387,10000388,10000389,10000390,10000391,10000392,10000393,10000394,10000395,10000396,10000397,10000398,10000399,10000400,10000401,10000402,10000403,10000404,10000405,10000406,10000407,10000408,10000409,10000410,10000411,10000412,10000413,10000414,10000415,10000416,10000417,10000418,10000419,10000420,10000421,10000422,10000423,10000424,10000425,10000426,10000427,10000428,10000429,10000430,10000431,10000432,10000433,10000434,10000435,10000436,10000437,10000438,10000439,10000440,10000441,10000442,10000443,10000444,10000445,10000446,10000447,10000448,10000449,10000450,10000451,10000452,10000453,10000454,10000455,10000456,10000457,10000458,10000459,10000460,10000461,10000462,10000463,10000464,10000465,10000466,10000467,10000468,10000469,10000470,10000471,10000472,10000473,10000474,10000475,10000476,10000477,10000478,10000479,10000480,10000481,10000482,10000483,10000484,10000485,10000486,10000487,10000488,10000489,10000490,10000491,10000492,10000493,10000494,10000495,10000496,10000497,10000498,10000499,10000500,10000501,10000502,10000503,10000504,10000505,10000506], isStart=False) # 10000040-10000506 나무 상자 Normal Box
        set_user_value(triggerId=5, key='RareBoxOff', value=1)
        set_user_value(triggerId=8, key='RareMobOff', value=1)
        set_user_value(triggerId=9, key='NormaBoxOff', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='ExtraEventOff', value=1):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        set_user_value(triggerId=11, key='RelicMobRemove', value=1)
        set_user_value(triggerId=12, key='RelicMobRemove', value=1)
        set_user_value(triggerId=13, key='RelicMobRemove', value=1)
        set_user_value(triggerId=14, key='RelicMobRemove', value=1)
        set_user_value(triggerId=15, key='RelicMobRemove', value=1)


