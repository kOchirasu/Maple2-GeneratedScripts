using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001242: 
/// </summary>
public class _11001242 : NpcScript {
    protected override void FirstScript() {
        // TODO: RandomPick 30;40;50;60;70;80;90;100;110;120;130;140;150;151;152;153;154;155;156;157;158;159;160;161;162;170;180
        // (Id, Button) = (30, NpcTalkButton.SelectableDistractor);
        // (Id, Button) = (40, NpcTalkButton.SelectableDistractor);
        // (Id, Button) = (50, NpcTalkButton.SelectableDistractor);
        // (Id, Button) = (60, NpcTalkButton.SelectableDistractor);
        // (Id, Button) = (70, NpcTalkButton.SelectableDistractor);
        // (Id, Button) = (80, NpcTalkButton.SelectableDistractor);
        // (Id, Button) = (90, NpcTalkButton.SelectableDistractor);
        // (Id, Button) = (100, NpcTalkButton.SelectableDistractor);
        // (Id, Button) = (110, NpcTalkButton.SelectableDistractor);
        // (Id, Button) = (120, NpcTalkButton.SelectableDistractor);
        // (Id, Button) = (130, NpcTalkButton.SelectableDistractor);
        // (Id, Button) = (140, NpcTalkButton.SelectableDistractor);
        // (Id, Button) = (150, NpcTalkButton.Close);
        // (Id, Button) = (151, NpcTalkButton.Close);
        // (Id, Button) = (152, NpcTalkButton.Close);
        // (Id, Button) = (153, NpcTalkButton.Close);
        // (Id, Button) = (154, NpcTalkButton.Close);
        // (Id, Button) = (155, NpcTalkButton.Close);
        // (Id, Button) = (156, NpcTalkButton.Close);
        // (Id, Button) = (157, NpcTalkButton.Close);
        // (Id, Button) = (158, NpcTalkButton.Close);
        // (Id, Button) = (159, NpcTalkButton.Close);
        // (Id, Button) = (160, NpcTalkButton.Close);
        // (Id, Button) = (161, NpcTalkButton.Close);
        // (Id, Button) = (162, NpcTalkButton.Close);
        // (Id, Button) = (170, NpcTalkButton.SelectableDistractor);
        // (Id, Button) = (180, NpcTalkButton.SelectableDistractor);
    }

    protected override (int, NpcTalkButton) Next(int selection) {
        switch (Id) {
            case 0:
                // $script:1124183307004459$ 
                // - Ooh, how interesting!
                return default;
            case 30:
                // $script:1124183307004462$ 
                // - Excuse me, but I'm a bit busy. Can you come back later?
                switch (selection) {
                    // $script:1124183307004463$
                    // - What are you doing?
                    case 0:
                        return (31, NpcTalkButton.Next);
                    // $script:1124183307004464$
                    // - I'll leave you to it, then.
                    case 1:
                        return (32, NpcTalkButton.Close);
                }
                return default;
            case 31:
                switch (Index++) {
                    case 0:
                        // $script:1124183307004465$ 
                        // - What am I doing...?
                        //   <font color="#909090">($npcName:11001242[gender:0]$ stares at you blankly.)</font>
                        return (31, NpcTalkButton.Close);
                    case 1:
                        // $script:1124183307004466$ 
                        // - I doubt you could comprehend what I'm doing. My research extends far beyond the senses of ordinary people like you.
                        return default;
                }
                break;
            case 32:
                // $script:1124183307004467$ 
                // - Good. For a moment there, I thought you were going to ask me some obvious questions. Now shoo! I have work to do!
                return default;
            case 40:
                // $script:1127160707004576$ 
                // - Hmph. Unless you have something interesting to show me, just leave me alone.
                switch (selection) {
                    // $script:1127160707004577$
                    // - I need a glimmering Balrog's weapon.
                    case 0:
                        // TODO: goto 41
                        // (Id, Button) = (41, NpcTalkButton.SelectableDistractor);
                        // TODO: gotoFail 44
                        // (Id, Button) = (44, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                    // $script:1127160707004578$
                    // - How goes your research on power wavelengths?
                    case 1:
                        return (45, NpcTalkButton.Close);
                }
                return default;
            case 41:
                // $script:1127160707004579$ 
                // - I'm a scientist, not a magician. I can't just whisk such things out of thin air. I don't suppose you actually brought me the materials? 
                switch (selection) {
                    // $script:1127160707004580$
                    // - As it happens, I did! So, can you make it?
                    case 0:
                        // TODO: goto 42
                        // (Id, Button) = (42, NpcTalkButton.Close);
                        // TODO: gotoFail 43
                        // (Id, Button) = (43, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                }
                return default;
            case 42:
                // $script:1127160707004581$ functionID=1 
                // - <font color="#909090">(He grumbles under his breath and puts together your new weapon.)</font>
                //   Here you go. I only made it because you asked so nicely. If you want it polished up, I suggest you get it to a smith right away.
                return default;
            case 43:
                // $script:1127160707004582$ 
                // - What's this? Your bag's full! Why are you wasting my time when you don't even have space for a new weapon?
                return default;
            case 44:
                // $script:1127160707004583$ 
                // - I need raw materials for a job like this! Say, 30 $itemPlural:30000437$ or so. And don't forget the $item:30000432$ and $item:30000433$! 
                return default;
            case 45:
                // $script:1127160707004584$ 
                // - It's keeping me busy. Real busy. As in, "Don't bother me if you're just want to chat" busy. So, unless you've got something real exciting for me, I don't have time for chitchat.
                return default;
            case 50:
                // $script:1127160707004585$ 
                // - Hmph. Unless you have something interesting to show me, just leave me alone.
                switch (selection) {
                    // $script:1127160707004586$
                    // - I need a glimmering Balrog's weapon.
                    case 0:
                        // TODO: goto 51
                        // (Id, Button) = (51, NpcTalkButton.SelectableDistractor);
                        // TODO: gotoFail 54
                        // (Id, Button) = (54, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                    // $script:1127160707004587$
                    // - How goes your research on power wavelengths?
                    case 1:
                        return (55, NpcTalkButton.Close);
                }
                return default;
            case 51:
                // $script:1127160707004588$ 
                // - I'm a scientist, not a magician. I can't just whisk such things out of thin air. I don't suppose you actually brought me the materials? 
                switch (selection) {
                    // $script:1127160707004589$
                    // - As it happens, I did! So, can you make it?
                    case 0:
                        // TODO: goto 52
                        // (Id, Button) = (52, NpcTalkButton.Close);
                        // TODO: gotoFail 53
                        // (Id, Button) = (53, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                }
                return default;
            case 52:
                // $script:1127160707004590$ functionID=2 
                // - <font color="#909090">(He grumbles under his breath and puts together your new weapon.)</font>
                //   Here you go. I only made it because you asked so nicely. If you want it polished up, I suggest you get it to a smith right away.
                return default;
            case 53:
                // $script:1127160707004591$ 
                // - What's this? Your bag's full! Why are you wasting my time when you don't even have space for a new weapon?
                return default;
            case 54:
                // $script:1127160707004592$ 
                // - I need raw materials for a job like this! Say, 30 $itemPlural:30000437$ or so. And don't forget the $item:30000423$ and $item:30000427$! 
                return default;
            case 55:
                // $script:1127160707004593$ 
                // - It's keeping me busy. Real busy. As in, "Don't bother me if you're just want to chat" busy. So, unless you've got something real exciting for me, I don't have time for chitchat.
                return default;
            case 60:
                // $script:1127160707004594$ 
                // - Hmph. Unless you have something interesting to show me, just leave me alone.
                switch (selection) {
                    // $script:1127160707004595$
                    // - I need a glimmering Balrog's weapon.
                    case 0:
                        // TODO: goto 61
                        // (Id, Button) = (61, NpcTalkButton.SelectableDistractor);
                        // TODO: gotoFail 64
                        // (Id, Button) = (64, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                    // $script:1127160707004596$
                    // - How goes your research on power wavelengths?
                    case 1:
                        return (65, NpcTalkButton.Close);
                }
                return default;
            case 61:
                // $script:1127160707004597$ 
                // - I'm a scientist, not a magician. I can't just whisk such things out of thin air. I don't suppose you actually brought me the materials? 
                switch (selection) {
                    // $script:1127160707004598$
                    // - As it happens, I did! So, can you make it?
                    case 0:
                        // TODO: goto 62
                        // (Id, Button) = (62, NpcTalkButton.Close);
                        // TODO: gotoFail 63
                        // (Id, Button) = (63, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                }
                return default;
            case 62:
                // $script:1127160707004599$ functionID=3 
                // - <font color="#909090">(He grumbles under his breath and puts together your new weapon.)</font>
                //   Here you go. I only made it because you asked so nicely. If you want it polished up, I suggest you get it to a smith right away.
                return default;
            case 63:
                // $script:1127160707004600$ 
                // - What's this? Your bag's full! Why are you wasting my time when you don't even have space for a new weapon?
                return default;
            case 64:
                // $script:1127160707004601$ 
                // - I need raw materials for a job like this! Say, 30 $itemPlural:30000437$ or so. And don't forget the $item:30000428$! 
                return default;
            case 65:
                // $script:1127160707004602$ 
                // - It's keeping me busy. Real busy. As in, "Don't bother me if you're just want to chat" busy. So, unless you've got something real exciting for me, I don't have time for chitchat.
                return default;
            case 70:
                // $script:1127160707004603$ 
                // - Hmph. Unless you have something interesting to show me, just leave me alone.
                switch (selection) {
                    // $script:1127160707004604$
                    // - I need a glimmering Balrog's weapon.
                    case 0:
                        // TODO: goto 71
                        // (Id, Button) = (71, NpcTalkButton.SelectableDistractor);
                        // TODO: gotoFail 74
                        // (Id, Button) = (74, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                    // $script:1127160707004605$
                    // - How goes your research on power wavelengths?
                    case 1:
                        return (75, NpcTalkButton.Close);
                }
                return default;
            case 71:
                // $script:1127160707004606$ 
                // - I'm a scientist, not a magician. I can't just whisk such things out of thin air. I don't suppose you actually brought me the materials? 
                switch (selection) {
                    // $script:1127160707004607$
                    // - As it happens, I did! So, can you make it?
                    case 0:
                        // TODO: goto 72
                        // (Id, Button) = (72, NpcTalkButton.Close);
                        // TODO: gotoFail 73
                        // (Id, Button) = (73, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                }
                return default;
            case 72:
                // $script:1127160707004608$ functionID=4 
                // - <font color="#909090">(He grumbles under his breath and puts together your new weapon.)</font>
                //   Here you go. I only made it because you asked so nicely. If you want it polished up, I suggest you get it to a smith right away.
                return default;
            case 73:
                // $script:1127160707004609$ 
                // - What's this? Your bag's full! Why are you wasting my time when you don't even have space for a new weapon?
                return default;
            case 74:
                // $script:1127160707004610$ 
                // - I need raw materials for a job like this! Say, 30 $itemPlural:30000437$ or so. And don't forget the $item:30000430$! 
                return default;
            case 75:
                // $script:1127160707004611$ 
                // - It's keeping me busy. Real busy. As in, "Don't bother me if you're just want to chat" busy. So, unless you've got something real exciting for me, I don't have time for chitchat.
                return default;
            case 80:
                // $script:1127160707004612$ 
                // - Hmph. Unless you have something interesting to show me, just leave me alone.
                switch (selection) {
                    // $script:1127160707004613$
                    // - I need a glimmering Balrog's weapon.
                    case 0:
                        // TODO: goto 81
                        // (Id, Button) = (81, NpcTalkButton.SelectableDistractor);
                        // TODO: gotoFail 84
                        // (Id, Button) = (84, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                    // $script:1127160707004614$
                    // - How goes your research on power wavelengths?
                    case 1:
                        return (85, NpcTalkButton.Close);
                }
                return default;
            case 81:
                // $script:1127160707004615$ 
                // - I'm a scientist, not a magician. I can't just whisk such things out of thin air. I don't suppose you actually brought me the materials? 
                switch (selection) {
                    // $script:1127160707004616$
                    // - As it happens, I did! So, can you make it?
                    case 0:
                        // TODO: goto 82
                        // (Id, Button) = (82, NpcTalkButton.Close);
                        // TODO: gotoFail 83
                        // (Id, Button) = (83, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                }
                return default;
            case 82:
                // $script:1127160707004617$ functionID=5 
                // - <font color="#909090">(He grumbles under his breath and puts together your new weapon.)</font>
                //   Here you go. I only made it because you asked so nicely. If you want it polished up, I suggest you get it to a smith right away.
                return default;
            case 83:
                // $script:1127160707004618$ 
                // - What's this? Your bag's full! Why are you wasting my time when you don't even have space for a new weapon?
                return default;
            case 84:
                // $script:1127160707004619$ 
                // - I need raw materials for a job like this! Say, 30 $itemPlural:30000437$ or so. And don't forget the $item:30000424$ and $item:30000426$! 
                return default;
            case 85:
                // $script:1127160707004620$ 
                // - It's keeping me busy. Real busy. As in, "Don't bother me if you're just want to chat" busy. So, unless you've got something real exciting for me, I don't have time for chitchat.
                return default;
            case 90:
                // $script:1127160707004621$ 
                // - Hmph. Unless you have something interesting to show me, just leave me alone.
                switch (selection) {
                    // $script:1127160707004622$
                    // - I need a glimmering Balrog's weapon.
                    case 0:
                        // TODO: goto 91
                        // (Id, Button) = (91, NpcTalkButton.SelectableDistractor);
                        // TODO: gotoFail 94
                        // (Id, Button) = (94, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                    // $script:1127160707004623$
                    // - How goes your research on power wavelengths?
                    case 1:
                        return (95, NpcTalkButton.Close);
                }
                return default;
            case 91:
                // $script:1127160707004624$ 
                // - I'm a scientist, not a magician. I can't just whisk such things out of thin air. I don't suppose you actually brought me the materials? 
                switch (selection) {
                    // $script:1127160707004625$
                    // - As it happens, I did! So, can you make it?
                    case 0:
                        // TODO: goto 92
                        // (Id, Button) = (92, NpcTalkButton.Close);
                        // TODO: gotoFail 93
                        // (Id, Button) = (93, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                }
                return default;
            case 92:
                // $script:1127160707004626$ functionID=6 
                // - <font color="#909090">(He grumbles under his breath and puts together your new weapon.)</font>
                //   Here you go. I only made it because you asked so nicely. If you want it polished up, I suggest you get it to a smith right away.
                return default;
            case 93:
                // $script:1127160707004627$ 
                // - What's this? Your bag's full! Why are you wasting my time when you don't even have space for a new weapon?
                return default;
            case 94:
                // $script:1127160707004628$ 
                // - I need raw materials for a job like this! Say, 30 $itemPlural:30000437$ or so. And don't forget the $item:30000429$! 
                return default;
            case 95:
                // $script:1127160707004629$ 
                // - It's keeping me busy. Real busy. As in, "Don't bother me if you're just want to chat" busy. So, unless you've got something real exciting for me, I don't have time for chitchat.
                return default;
            case 100:
                // $script:1127160707004630$ 
                // - Hmph. Unless you have something interesting to show me, just leave me alone.
                switch (selection) {
                    // $script:1127160707004631$
                    // - I need a glimmering Balrog's weapon.
                    case 0:
                        // TODO: goto 101
                        // (Id, Button) = (101, NpcTalkButton.SelectableDistractor);
                        // TODO: gotoFail 104
                        // (Id, Button) = (104, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                    // $script:1127160707004632$
                    // - How goes your research on power wavelengths?
                    case 1:
                        return (105, NpcTalkButton.Close);
                }
                return default;
            case 101:
                // $script:1127160707004633$ 
                // - I'm a scientist, not a magician. I can't just whisk such things out of thin air. I don't suppose you actually brought me the materials? 
                switch (selection) {
                    // $script:1127160707004634$
                    // - As it happens, I did! So, can you make it?
                    case 0:
                        // TODO: goto 102
                        // (Id, Button) = (102, NpcTalkButton.Close);
                        // TODO: gotoFail 103
                        // (Id, Button) = (103, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                }
                return default;
            case 102:
                // $script:1127160707004635$ functionID=7 
                // - <font color="#909090">(He grumbles under his breath and puts together your new weapon.)</font>
                //   Here you go. I only made it because you asked so nicely. If you want it polished up, I suggest you get it to a smith right away.
                return default;
            case 103:
                // $script:1127160707004636$ 
                // - What's this? Your bag's full! Why are you wasting my time when you don't even have space for a new weapon?
                return default;
            case 104:
                // $script:1127160707004637$ 
                // - I need raw materials for a job like this! Say, 30 $itemPlural:30000437$ or so. And don't forget the $item:30000431$! 
                return default;
            case 105:
                // $script:1127160707004638$ 
                // - It's keeping me busy. Real busy. As in, "Don't bother me if you're just want to chat" busy. So, unless you've got something real exciting for me, I don't have time for chitchat.
                return default;
            case 110:
                // $script:1127160707004639$ 
                // - Hmph. Unless you have something interesting to show me, just leave me alone.
                switch (selection) {
                    // $script:1127160707004640$
                    // - I need a glimmering Balrog's weapon.
                    case 0:
                        // TODO: goto 111
                        // (Id, Button) = (111, NpcTalkButton.SelectableDistractor);
                        // TODO: gotoFail 114
                        // (Id, Button) = (114, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                    // $script:1127160707004641$
                    // - How goes your research on power wavelengths?
                    case 1:
                        return (115, NpcTalkButton.Close);
                }
                return default;
            case 111:
                // $script:1127160707004642$ 
                // - I'm a scientist, not a magician. I can't just whisk such things out of thin air. I don't suppose you actually brought me the materials? 
                switch (selection) {
                    // $script:1127160707004643$
                    // - As it happens, I did! So, can you make it?
                    case 0:
                        // TODO: goto 112
                        // (Id, Button) = (112, NpcTalkButton.Close);
                        // TODO: gotoFail 113
                        // (Id, Button) = (113, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                }
                return default;
            case 112:
                // $script:1127160707004644$ functionID=8 
                // - <font color="#909090">(He grumbles under his breath and puts together your new weapon.)</font>
                //   Here you go. I only made it because you asked so nicely. If you want it polished up, I suggest you get it to a smith right away.
                return default;
            case 113:
                // $script:1127160707004645$ 
                // - What's this? Your bag's full! Why are you wasting my time when you don't even have space for a new weapon?
                return default;
            case 114:
                // $script:1127160707004646$ 
                // - I need raw materials for a job like this! Say, 30 $itemPlural:30000437$ or so. And don't forget the $item:30000422$! 
                return default;
            case 115:
                // $script:1127160707004647$ 
                // - It's keeping me busy. Real busy. As in, "Don't bother me if you're just want to chat" busy. So, unless you've got something real exciting for me, I don't have time for chitchat.
                return default;
            case 120:
                // $script:1127160707004648$ 
                // - Hmph. Unless you have something interesting to show me, just leave me alone.
                switch (selection) {
                    // $script:1127160707004649$
                    // - I need a glimmering Balrog's weapon.
                    case 0:
                        // TODO: goto 121
                        // (Id, Button) = (121, NpcTalkButton.SelectableDistractor);
                        // TODO: gotoFail 124
                        // (Id, Button) = (124, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                    // $script:1127160707004650$
                    // - How goes your research on power wavelengths?
                    case 1:
                        return (125, NpcTalkButton.Close);
                }
                return default;
            case 121:
                // $script:1127160707004651$ 
                // - I'm a scientist, not a magician. I can't just whisk such things out of thin air. I don't suppose you actually brought me the materials? 
                switch (selection) {
                    // $script:1127160707004652$
                    // - As it happens, I did! So, can you make it?
                    case 0:
                        // TODO: goto 122
                        // (Id, Button) = (122, NpcTalkButton.Close);
                        // TODO: gotoFail 123
                        // (Id, Button) = (123, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                }
                return default;
            case 122:
                // $script:1127160707004653$ functionID=9 
                // - <font color="#909090">(He grumbles under his breath and puts together your new weapon.)</font>
                //   Here you go. I only made it because you asked so nicely. If you want it polished up, I suggest you get it to a smith right away.
                return default;
            case 123:
                // $script:1127160707004654$ 
                // - What's this? Your bag's full! Why are you wasting my time when you don't even have space for a new weapon?
                return default;
            case 124:
                // $script:1127160707004655$ 
                // - I need raw materials for a job like this! Say, 30 $itemPlural:30000437$ or so. And don't forget the $item:30000425$! 
                return default;
            case 125:
                // $script:1127160707004656$ 
                // - It's keeping me busy. Real busy. As in, "Don't bother me if you're just want to chat" busy. So, unless you've got something real exciting for me, I don't have time for chitchat.
                return default;
            case 130:
                // $script:1130105307004661$ 
                // - Do you have $itemPlural:30000437$ for me?
                switch (selection) {
                    // $script:1130105307004662$
                    // - What exactly <i>are</i> $itemPlural:30000437$, anyway?
                    case 0:
                        // TODO: goto 131
                        // (Id, Button) = (131, NpcTalkButton.Next);
                        // TODO: gotoFail 133
                        // (Id, Button) = (133, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                    // $script:1201232607004666$
                    // - I don't actually know what $itemPlural:30000437$ are.
                    case 1:
                        return (132, NpcTalkButton.Close);
                }
                return default;
            case 131:
                switch (Index++) {
                    case 0:
                        // $script:1130105307004663$ 
                        // - I wish I could tell you for sure, but all I've heard are unsubstantiated rumors. I'm not even sure if I need them or not. Would you mind holding onto them for now?
                        return (131, NpcTalkButton.Close);
                    case 1:
                        // $script:1130105307004664$ 
                        // - They may be related to the dark powers I've been studying. I'll let you know when I need $itemPlural:30000437$ to study. In the meantime, don't throw them away, okay?
                        return default;
                }
                break;
            case 132:
                // $script:1201232607004667$ 
                // - How disappointing! You can leave now. I'm busy, anyway.
                return default;
            case 133:
                // $script:1201233507004668$ 
                // - You have questions? Bring me some $itemPlural:30000437$, and maybe we can talk.
                return default;
            case 140:
                // $script:1209200907004863$ 
                // - Hmph. Unless you have something interesting to show me, just leave me alone.
                switch (selection) {
                    // $script:1209200907004864$
                    // - I need a glimmering Balrog's weapon.
                    case 0:
                        // TODO: goto 141
                        // (Id, Button) = (141, NpcTalkButton.SelectableDistractor);
                        // TODO: gotoFail 144
                        // (Id, Button) = (144, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                    // $script:1209200907004865$
                    // - How goes your research on power wavelengths?
                    case 1:
                        return (145, NpcTalkButton.Close);
                }
                return default;
            case 141:
                // $script:1209200907004866$ 
                // - I'm a scientist, not a magician. I can't just whisk such things out of thin air. I don't suppose you actually brought me the materials? 
                switch (selection) {
                    // $script:1209200907004867$
                    // - As it happens, I did! So, can you make it?
                    case 0:
                        // TODO: goto 142
                        // (Id, Button) = (142, NpcTalkButton.Close);
                        // TODO: gotoFail 143
                        // (Id, Button) = (143, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                }
                return default;
            case 142:
                // $script:1209200907004868$ functionID=10 
                // - <font color="#909090">(He grumbles under his breath and puts together your new weapon.)</font>
                //   Here you go. I only made it because you asked so nicely. If you want it polished up, I suggest you get it to a smith right away.
                return default;
            case 143:
                // $script:1209200907004869$ 
                // - What's this? Your bag's full! Why are you wasting my time when you don't even have space for a new weapon?
                return default;
            case 144:
                // $script:1209200907004870$ 
                // - I need raw materials for a job like this! Say, 30 $itemPlural:30000437$ or so. And don't forget the $item:30000450$! 
                return default;
            case 145:
                // $script:1209200907004871$ 
                // - It's keeping me busy. Real busy. As in, "Don't bother me if you're just want to chat" busy. So, unless you've got something real exciting for me, I don't have time for chitchat.
                return default;
            case 150:
                // $script:0218140107005865$ 
                // - I don't have time to chat right now. Come by later, okay?
                return default;
            case 151:
                // $script:0218140107005866$ 
                // - I don't have time to chat right now. Come by later, okay?
                return default;
            case 152:
                // $script:0218140107005867$ 
                // - I don't have time to chat right now. Come by later, okay?
                return default;
            case 153:
                // $script:0218140107005868$ 
                // - I don't have time to chat right now. Come by later, okay?
                return default;
            case 154:
                // $script:0218140107005869$ 
                // - I don't have time to chat right now. Come by later, okay?
                return default;
            case 155:
                // $script:0218140107005870$ 
                // - I don't have time to chat right now. Come by later, okay?
                return default;
            case 156:
                // $script:0218140107005871$ 
                // - I don't have time to chat right now. Come by later, okay?
                return default;
            case 157:
                // $script:0218140107005872$ 
                // - I don't have time to chat right now. Come by later, okay?
                return default;
            case 158:
                // $script:0218140107005873$ 
                // - I don't have time to chat right now. Come by later, okay?
                return default;
            case 159:
                // $script:0218140107005874$ 
                // - I don't have time to chat right now. Come by later, okay?
                return default;
            case 160:
                // $script:0218142507005875$ 
                // - I don't have time to chat right now. Come by later, okay?
                return default;
            case 161:
                // $script:0704154107006572$ 
                // - I don't have time to chat right now. Come by later, okay?
                return default;
            case 162:
                // $script:0704154107006573$ 
                // - I don't have time to chat right now. Come by later, okay?
                return default;
            case 170:
                // $script:0704154107006554$ 
                // - Hmph. Unless you have something interesting to show me, just leave me alone.
                switch (selection) {
                    // $script:0704154107006555$
                    // - I need a glimmering Balrog's weapon.
                    case 0:
                        // TODO: goto 171
                        // (Id, Button) = (171, NpcTalkButton.SelectableDistractor);
                        // TODO: gotoFail 174
                        // (Id, Button) = (174, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                    // $script:0704154107006556$
                    // - How goes your research on power wavelengths?
                    case 1:
                        return (175, NpcTalkButton.Close);
                }
                return default;
            case 171:
                // $script:0704154107006557$ 
                // - I'm a scientist, not a magician. I can't just whisk such things out of thin air. I don't suppose you actually brought me the materials? 
                switch (selection) {
                    // $script:0704154107006558$
                    // - As it happens, I did! So, can you make it?
                    case 0:
                        // TODO: goto 172
                        // (Id, Button) = (172, NpcTalkButton.Close);
                        // TODO: gotoFail 173
                        // (Id, Button) = (173, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                }
                return default;
            case 172:
                // $script:0704154107006559$ functionID=11 
                // - <font color="#909090">(He grumbles under his breath and puts together your new weapon.)</font>
                //   Here you go. I only made it because you asked so nicely. If you want it polished up, I suggest you get it to a smith right away.
                return default;
            case 173:
                // $script:0704154107006560$ 
                // - What's this? Your bag's full! Why are you wasting my time when you don't even have space for a new weapon?
                return default;
            case 174:
                // $script:0704154107006561$ 
                // - I need raw materials for a job like this! Say, 30 $itemPlural:30000437$ or so. And don't forget the $item:30000560$! 
                return default;
            case 175:
                // $script:0704154107006562$ 
                // - It's keeping me busy. Real busy. As in, "Don't bother me if you're just want to chat" busy. So, unless you've got something real exciting for me, I don't have time for chitchat.
                return default;
            case 180:
                // $script:0704154107006563$ 
                // - Hmph. Unless you have something interesting to show me, just leave me alone.
                switch (selection) {
                    // $script:0704154107006564$
                    // - I need a glimmering Balrog's weapon.
                    case 0:
                        // TODO: goto 181
                        // (Id, Button) = (181, NpcTalkButton.SelectableDistractor);
                        // TODO: gotoFail 184
                        // (Id, Button) = (184, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                    // $script:0704154107006565$
                    // - How goes your research on power wavelengths?
                    case 1:
                        return (185, NpcTalkButton.Close);
                }
                return default;
            case 181:
                // $script:0704154107006566$ 
                // - I'm a scientist, not a magician. I can't just whisk such things out of thin air. I don't suppose you actually brought me the materials? 
                switch (selection) {
                    // $script:0704154107006567$
                    // - As it happens, I did! So, can you make it?
                    case 0:
                        // TODO: goto 182
                        // (Id, Button) = (182, NpcTalkButton.Close);
                        // TODO: gotoFail 183
                        // (Id, Button) = (183, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                }
                return default;
            case 182:
                // $script:0704154107006568$ functionID=12 
                // - <font color="#909090">(He grumbles under his breath and puts together your new weapon.)</font>
                //   Here you go. I only made it because you asked so nicely. If you want it polished up, I suggest you get it to a smith right away.
                return default;
            case 183:
                // $script:0704154107006569$ 
                // - What's this? Your bag's full! Why are you wasting my time when you don't even have space for a new weapon?
                return default;
            case 184:
                // $script:0704154107006570$ 
                // - I need raw materials for a job like this! Say, 30 $itemPlural:30000437$ or so. And don't forget the $item:30000561$! 
                return default;
            case 185:
                // $script:0704154107006571$ 
                // - It's keeping me busy. Real busy. As in, "Don't bother me if you're just want to chat" busy. So, unless you've got something real exciting for me, I don't have time for chitchat.
                return default;
        }
        
        return default;
    }
}
