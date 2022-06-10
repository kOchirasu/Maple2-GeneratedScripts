using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001242: 
/// </summary>
public class _11001242 : NpcScript {
    internal _11001242(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40;50;60;70;80;90;100;110;120;130;140;150;151;152;153;154;155;156;157;158;159;160;161;162;170;180
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1124183307004459$ 
                // - Ooh, how interesting!
                return true;
            case 30:
                // $script:1124183307004462$ 
                // - Excuse me, but I'm a bit busy. Can you come back later?
                switch (selection) {
                    // $script:1124183307004463$
                    // - What are you doing?
                    case 0:
                        Id = 31;
                        return false;
                    // $script:1124183307004464$
                    // - I'll leave you to it, then.
                    case 1:
                        Id = 32;
                        return false;
                }
                return true;
            case 31:
                // $script:1124183307004465$ 
                // - What am I doing...?
                //   <font color="#909090">($npcName:11001242[gender:0]$ stares at you blankly.)</font>
                // $script:1124183307004466$ 
                // - I doubt you could comprehend what I'm doing. My research extends far beyond the senses of ordinary people like you.
                return true;
            case 32:
                // $script:1124183307004467$ 
                // - Good. For a moment there, I thought you were going to ask me some obvious questions. Now shoo! I have work to do!
                return true;
            case 40:
                // $script:1127160707004576$ 
                // - Hmph. Unless you have something interesting to show me, just leave me alone.
                switch (selection) {
                    // $script:1127160707004577$
                    // - I need a glimmering Balrog's weapon.
                    case 0:
                        Id = 0; // TODO: 41 | 44
                        return false;
                    // $script:1127160707004578$
                    // - How goes your research on power wavelengths?
                    case 1:
                        Id = 45;
                        return false;
                }
                return true;
            case 41:
                // $script:1127160707004579$ 
                // - I'm a scientist, not a magician. I can't just whisk such things out of thin air. I don't suppose you actually brought me the materials? 
                switch (selection) {
                    // $script:1127160707004580$
                    // - As it happens, I did! So, can you make it?
                    case 0:
                        Id = 0; // TODO: 42 | 43
                        return false;
                }
                return true;
            case 42:
                // $script:1127160707004581$ functionID=1 
                // - <font color="#909090">(He grumbles under his breath and puts together your new weapon.)</font>
                //   Here you go. I only made it because you asked so nicely. If you want it polished up, I suggest you get it to a smith right away.
                return true;
            case 43:
                // $script:1127160707004582$ 
                // - What's this? Your bag's full! Why are you wasting my time when you don't even have space for a new weapon?
                return true;
            case 44:
                // $script:1127160707004583$ 
                // - I need raw materials for a job like this! Say, 30 $itemPlural:30000437$ or so. And don't forget the $item:30000432$ and $item:30000433$! 
                return true;
            case 45:
                // $script:1127160707004584$ 
                // - It's keeping me busy. Real busy. As in, "Don't bother me if you're just want to chat" busy. So, unless you've got something real exciting for me, I don't have time for chitchat.
                return true;
            case 50:
                // $script:1127160707004585$ 
                // - Hmph. Unless you have something interesting to show me, just leave me alone.
                switch (selection) {
                    // $script:1127160707004586$
                    // - I need a glimmering Balrog's weapon.
                    case 0:
                        Id = 0; // TODO: 51 | 54
                        return false;
                    // $script:1127160707004587$
                    // - How goes your research on power wavelengths?
                    case 1:
                        Id = 55;
                        return false;
                }
                return true;
            case 51:
                // $script:1127160707004588$ 
                // - I'm a scientist, not a magician. I can't just whisk such things out of thin air. I don't suppose you actually brought me the materials? 
                switch (selection) {
                    // $script:1127160707004589$
                    // - As it happens, I did! So, can you make it?
                    case 0:
                        Id = 0; // TODO: 52 | 53
                        return false;
                }
                return true;
            case 52:
                // $script:1127160707004590$ functionID=2 
                // - <font color="#909090">(He grumbles under his breath and puts together your new weapon.)</font>
                //   Here you go. I only made it because you asked so nicely. If you want it polished up, I suggest you get it to a smith right away.
                return true;
            case 53:
                // $script:1127160707004591$ 
                // - What's this? Your bag's full! Why are you wasting my time when you don't even have space for a new weapon?
                return true;
            case 54:
                // $script:1127160707004592$ 
                // - I need raw materials for a job like this! Say, 30 $itemPlural:30000437$ or so. And don't forget the $item:30000423$ and $item:30000427$! 
                return true;
            case 55:
                // $script:1127160707004593$ 
                // - It's keeping me busy. Real busy. As in, "Don't bother me if you're just want to chat" busy. So, unless you've got something real exciting for me, I don't have time for chitchat.
                return true;
            case 60:
                // $script:1127160707004594$ 
                // - Hmph. Unless you have something interesting to show me, just leave me alone.
                switch (selection) {
                    // $script:1127160707004595$
                    // - I need a glimmering Balrog's weapon.
                    case 0:
                        Id = 0; // TODO: 61 | 64
                        return false;
                    // $script:1127160707004596$
                    // - How goes your research on power wavelengths?
                    case 1:
                        Id = 65;
                        return false;
                }
                return true;
            case 61:
                // $script:1127160707004597$ 
                // - I'm a scientist, not a magician. I can't just whisk such things out of thin air. I don't suppose you actually brought me the materials? 
                switch (selection) {
                    // $script:1127160707004598$
                    // - As it happens, I did! So, can you make it?
                    case 0:
                        Id = 0; // TODO: 62 | 63
                        return false;
                }
                return true;
            case 62:
                // $script:1127160707004599$ functionID=3 
                // - <font color="#909090">(He grumbles under his breath and puts together your new weapon.)</font>
                //   Here you go. I only made it because you asked so nicely. If you want it polished up, I suggest you get it to a smith right away.
                return true;
            case 63:
                // $script:1127160707004600$ 
                // - What's this? Your bag's full! Why are you wasting my time when you don't even have space for a new weapon?
                return true;
            case 64:
                // $script:1127160707004601$ 
                // - I need raw materials for a job like this! Say, 30 $itemPlural:30000437$ or so. And don't forget the $item:30000428$! 
                return true;
            case 65:
                // $script:1127160707004602$ 
                // - It's keeping me busy. Real busy. As in, "Don't bother me if you're just want to chat" busy. So, unless you've got something real exciting for me, I don't have time for chitchat.
                return true;
            case 70:
                // $script:1127160707004603$ 
                // - Hmph. Unless you have something interesting to show me, just leave me alone.
                switch (selection) {
                    // $script:1127160707004604$
                    // - I need a glimmering Balrog's weapon.
                    case 0:
                        Id = 0; // TODO: 71 | 74
                        return false;
                    // $script:1127160707004605$
                    // - How goes your research on power wavelengths?
                    case 1:
                        Id = 75;
                        return false;
                }
                return true;
            case 71:
                // $script:1127160707004606$ 
                // - I'm a scientist, not a magician. I can't just whisk such things out of thin air. I don't suppose you actually brought me the materials? 
                switch (selection) {
                    // $script:1127160707004607$
                    // - As it happens, I did! So, can you make it?
                    case 0:
                        Id = 0; // TODO: 72 | 73
                        return false;
                }
                return true;
            case 72:
                // $script:1127160707004608$ functionID=4 
                // - <font color="#909090">(He grumbles under his breath and puts together your new weapon.)</font>
                //   Here you go. I only made it because you asked so nicely. If you want it polished up, I suggest you get it to a smith right away.
                return true;
            case 73:
                // $script:1127160707004609$ 
                // - What's this? Your bag's full! Why are you wasting my time when you don't even have space for a new weapon?
                return true;
            case 74:
                // $script:1127160707004610$ 
                // - I need raw materials for a job like this! Say, 30 $itemPlural:30000437$ or so. And don't forget the $item:30000430$! 
                return true;
            case 75:
                // $script:1127160707004611$ 
                // - It's keeping me busy. Real busy. As in, "Don't bother me if you're just want to chat" busy. So, unless you've got something real exciting for me, I don't have time for chitchat.
                return true;
            case 80:
                // $script:1127160707004612$ 
                // - Hmph. Unless you have something interesting to show me, just leave me alone.
                switch (selection) {
                    // $script:1127160707004613$
                    // - I need a glimmering Balrog's weapon.
                    case 0:
                        Id = 0; // TODO: 81 | 84
                        return false;
                    // $script:1127160707004614$
                    // - How goes your research on power wavelengths?
                    case 1:
                        Id = 85;
                        return false;
                }
                return true;
            case 81:
                // $script:1127160707004615$ 
                // - I'm a scientist, not a magician. I can't just whisk such things out of thin air. I don't suppose you actually brought me the materials? 
                switch (selection) {
                    // $script:1127160707004616$
                    // - As it happens, I did! So, can you make it?
                    case 0:
                        Id = 0; // TODO: 82 | 83
                        return false;
                }
                return true;
            case 82:
                // $script:1127160707004617$ functionID=5 
                // - <font color="#909090">(He grumbles under his breath and puts together your new weapon.)</font>
                //   Here you go. I only made it because you asked so nicely. If you want it polished up, I suggest you get it to a smith right away.
                return true;
            case 83:
                // $script:1127160707004618$ 
                // - What's this? Your bag's full! Why are you wasting my time when you don't even have space for a new weapon?
                return true;
            case 84:
                // $script:1127160707004619$ 
                // - I need raw materials for a job like this! Say, 30 $itemPlural:30000437$ or so. And don't forget the $item:30000424$ and $item:30000426$! 
                return true;
            case 85:
                // $script:1127160707004620$ 
                // - It's keeping me busy. Real busy. As in, "Don't bother me if you're just want to chat" busy. So, unless you've got something real exciting for me, I don't have time for chitchat.
                return true;
            case 90:
                // $script:1127160707004621$ 
                // - Hmph. Unless you have something interesting to show me, just leave me alone.
                switch (selection) {
                    // $script:1127160707004622$
                    // - I need a glimmering Balrog's weapon.
                    case 0:
                        Id = 0; // TODO: 91 | 94
                        return false;
                    // $script:1127160707004623$
                    // - How goes your research on power wavelengths?
                    case 1:
                        Id = 95;
                        return false;
                }
                return true;
            case 91:
                // $script:1127160707004624$ 
                // - I'm a scientist, not a magician. I can't just whisk such things out of thin air. I don't suppose you actually brought me the materials? 
                switch (selection) {
                    // $script:1127160707004625$
                    // - As it happens, I did! So, can you make it?
                    case 0:
                        Id = 0; // TODO: 92 | 93
                        return false;
                }
                return true;
            case 92:
                // $script:1127160707004626$ functionID=6 
                // - <font color="#909090">(He grumbles under his breath and puts together your new weapon.)</font>
                //   Here you go. I only made it because you asked so nicely. If you want it polished up, I suggest you get it to a smith right away.
                return true;
            case 93:
                // $script:1127160707004627$ 
                // - What's this? Your bag's full! Why are you wasting my time when you don't even have space for a new weapon?
                return true;
            case 94:
                // $script:1127160707004628$ 
                // - I need raw materials for a job like this! Say, 30 $itemPlural:30000437$ or so. And don't forget the $item:30000429$! 
                return true;
            case 95:
                // $script:1127160707004629$ 
                // - It's keeping me busy. Real busy. As in, "Don't bother me if you're just want to chat" busy. So, unless you've got something real exciting for me, I don't have time for chitchat.
                return true;
            case 100:
                // $script:1127160707004630$ 
                // - Hmph. Unless you have something interesting to show me, just leave me alone.
                switch (selection) {
                    // $script:1127160707004631$
                    // - I need a glimmering Balrog's weapon.
                    case 0:
                        Id = 0; // TODO: 101 | 104
                        return false;
                    // $script:1127160707004632$
                    // - How goes your research on power wavelengths?
                    case 1:
                        Id = 105;
                        return false;
                }
                return true;
            case 101:
                // $script:1127160707004633$ 
                // - I'm a scientist, not a magician. I can't just whisk such things out of thin air. I don't suppose you actually brought me the materials? 
                switch (selection) {
                    // $script:1127160707004634$
                    // - As it happens, I did! So, can you make it?
                    case 0:
                        Id = 0; // TODO: 102 | 103
                        return false;
                }
                return true;
            case 102:
                // $script:1127160707004635$ functionID=7 
                // - <font color="#909090">(He grumbles under his breath and puts together your new weapon.)</font>
                //   Here you go. I only made it because you asked so nicely. If you want it polished up, I suggest you get it to a smith right away.
                return true;
            case 103:
                // $script:1127160707004636$ 
                // - What's this? Your bag's full! Why are you wasting my time when you don't even have space for a new weapon?
                return true;
            case 104:
                // $script:1127160707004637$ 
                // - I need raw materials for a job like this! Say, 30 $itemPlural:30000437$ or so. And don't forget the $item:30000431$! 
                return true;
            case 105:
                // $script:1127160707004638$ 
                // - It's keeping me busy. Real busy. As in, "Don't bother me if you're just want to chat" busy. So, unless you've got something real exciting for me, I don't have time for chitchat.
                return true;
            case 110:
                // $script:1127160707004639$ 
                // - Hmph. Unless you have something interesting to show me, just leave me alone.
                switch (selection) {
                    // $script:1127160707004640$
                    // - I need a glimmering Balrog's weapon.
                    case 0:
                        Id = 0; // TODO: 111 | 114
                        return false;
                    // $script:1127160707004641$
                    // - How goes your research on power wavelengths?
                    case 1:
                        Id = 115;
                        return false;
                }
                return true;
            case 111:
                // $script:1127160707004642$ 
                // - I'm a scientist, not a magician. I can't just whisk such things out of thin air. I don't suppose you actually brought me the materials? 
                switch (selection) {
                    // $script:1127160707004643$
                    // - As it happens, I did! So, can you make it?
                    case 0:
                        Id = 0; // TODO: 112 | 113
                        return false;
                }
                return true;
            case 112:
                // $script:1127160707004644$ functionID=8 
                // - <font color="#909090">(He grumbles under his breath and puts together your new weapon.)</font>
                //   Here you go. I only made it because you asked so nicely. If you want it polished up, I suggest you get it to a smith right away.
                return true;
            case 113:
                // $script:1127160707004645$ 
                // - What's this? Your bag's full! Why are you wasting my time when you don't even have space for a new weapon?
                return true;
            case 114:
                // $script:1127160707004646$ 
                // - I need raw materials for a job like this! Say, 30 $itemPlural:30000437$ or so. And don't forget the $item:30000422$! 
                return true;
            case 115:
                // $script:1127160707004647$ 
                // - It's keeping me busy. Real busy. As in, "Don't bother me if you're just want to chat" busy. So, unless you've got something real exciting for me, I don't have time for chitchat.
                return true;
            case 120:
                // $script:1127160707004648$ 
                // - Hmph. Unless you have something interesting to show me, just leave me alone.
                switch (selection) {
                    // $script:1127160707004649$
                    // - I need a glimmering Balrog's weapon.
                    case 0:
                        Id = 0; // TODO: 121 | 124
                        return false;
                    // $script:1127160707004650$
                    // - How goes your research on power wavelengths?
                    case 1:
                        Id = 125;
                        return false;
                }
                return true;
            case 121:
                // $script:1127160707004651$ 
                // - I'm a scientist, not a magician. I can't just whisk such things out of thin air. I don't suppose you actually brought me the materials? 
                switch (selection) {
                    // $script:1127160707004652$
                    // - As it happens, I did! So, can you make it?
                    case 0:
                        Id = 0; // TODO: 122 | 123
                        return false;
                }
                return true;
            case 122:
                // $script:1127160707004653$ functionID=9 
                // - <font color="#909090">(He grumbles under his breath and puts together your new weapon.)</font>
                //   Here you go. I only made it because you asked so nicely. If you want it polished up, I suggest you get it to a smith right away.
                return true;
            case 123:
                // $script:1127160707004654$ 
                // - What's this? Your bag's full! Why are you wasting my time when you don't even have space for a new weapon?
                return true;
            case 124:
                // $script:1127160707004655$ 
                // - I need raw materials for a job like this! Say, 30 $itemPlural:30000437$ or so. And don't forget the $item:30000425$! 
                return true;
            case 125:
                // $script:1127160707004656$ 
                // - It's keeping me busy. Real busy. As in, "Don't bother me if you're just want to chat" busy. So, unless you've got something real exciting for me, I don't have time for chitchat.
                return true;
            case 130:
                // $script:1130105307004661$ 
                // - Do you have $itemPlural:30000437$ for me?
                switch (selection) {
                    // $script:1130105307004662$
                    // - What exactly <i>are</i> $itemPlural:30000437$, anyway?
                    case 0:
                        Id = 0; // TODO: 131 | 133
                        return false;
                    // $script:1201232607004666$
                    // - I don't actually know what $itemPlural:30000437$ are.
                    case 1:
                        Id = 132;
                        return false;
                }
                return true;
            case 131:
                // $script:1130105307004663$ 
                // - I wish I could tell you for sure, but all I've heard are unsubstantiated rumors. I'm not even sure if I need them or not. Would you mind holding onto them for now?
                // $script:1130105307004664$ 
                // - They may be related to the dark powers I've been studying. I'll let you know when I need $itemPlural:30000437$ to study. In the meantime, don't throw them away, okay?
                return true;
            case 132:
                // $script:1201232607004667$ 
                // - How disappointing! You can leave now. I'm busy, anyway.
                return true;
            case 133:
                // $script:1201233507004668$ 
                // - You have questions? Bring me some $itemPlural:30000437$, and maybe we can talk.
                return true;
            case 140:
                // $script:1209200907004863$ 
                // - Hmph. Unless you have something interesting to show me, just leave me alone.
                switch (selection) {
                    // $script:1209200907004864$
                    // - I need a glimmering Balrog's weapon.
                    case 0:
                        Id = 0; // TODO: 141 | 144
                        return false;
                    // $script:1209200907004865$
                    // - How goes your research on power wavelengths?
                    case 1:
                        Id = 145;
                        return false;
                }
                return true;
            case 141:
                // $script:1209200907004866$ 
                // - I'm a scientist, not a magician. I can't just whisk such things out of thin air. I don't suppose you actually brought me the materials? 
                switch (selection) {
                    // $script:1209200907004867$
                    // - As it happens, I did! So, can you make it?
                    case 0:
                        Id = 0; // TODO: 142 | 143
                        return false;
                }
                return true;
            case 142:
                // $script:1209200907004868$ functionID=10 
                // - <font color="#909090">(He grumbles under his breath and puts together your new weapon.)</font>
                //   Here you go. I only made it because you asked so nicely. If you want it polished up, I suggest you get it to a smith right away.
                return true;
            case 143:
                // $script:1209200907004869$ 
                // - What's this? Your bag's full! Why are you wasting my time when you don't even have space for a new weapon?
                return true;
            case 144:
                // $script:1209200907004870$ 
                // - I need raw materials for a job like this! Say, 30 $itemPlural:30000437$ or so. And don't forget the $item:30000450$! 
                return true;
            case 145:
                // $script:1209200907004871$ 
                // - It's keeping me busy. Real busy. As in, "Don't bother me if you're just want to chat" busy. So, unless you've got something real exciting for me, I don't have time for chitchat.
                return true;
            case 150:
                // $script:0218140107005865$ 
                // - I don't have time to chat right now. Come by later, okay?
                return true;
            case 151:
                // $script:0218140107005866$ 
                // - I don't have time to chat right now. Come by later, okay?
                return true;
            case 152:
                // $script:0218140107005867$ 
                // - I don't have time to chat right now. Come by later, okay?
                return true;
            case 153:
                // $script:0218140107005868$ 
                // - I don't have time to chat right now. Come by later, okay?
                return true;
            case 154:
                // $script:0218140107005869$ 
                // - I don't have time to chat right now. Come by later, okay?
                return true;
            case 155:
                // $script:0218140107005870$ 
                // - I don't have time to chat right now. Come by later, okay?
                return true;
            case 156:
                // $script:0218140107005871$ 
                // - I don't have time to chat right now. Come by later, okay?
                return true;
            case 157:
                // $script:0218140107005872$ 
                // - I don't have time to chat right now. Come by later, okay?
                return true;
            case 158:
                // $script:0218140107005873$ 
                // - I don't have time to chat right now. Come by later, okay?
                return true;
            case 159:
                // $script:0218140107005874$ 
                // - I don't have time to chat right now. Come by later, okay?
                return true;
            case 160:
                // $script:0218142507005875$ 
                // - I don't have time to chat right now. Come by later, okay?
                return true;
            case 161:
                // $script:0704154107006572$ 
                // - I don't have time to chat right now. Come by later, okay?
                return true;
            case 162:
                // $script:0704154107006573$ 
                // - I don't have time to chat right now. Come by later, okay?
                return true;
            case 170:
                // $script:0704154107006554$ 
                // - Hmph. Unless you have something interesting to show me, just leave me alone.
                switch (selection) {
                    // $script:0704154107006555$
                    // - I need a glimmering Balrog's weapon.
                    case 0:
                        Id = 0; // TODO: 171 | 174
                        return false;
                    // $script:0704154107006556$
                    // - How goes your research on power wavelengths?
                    case 1:
                        Id = 175;
                        return false;
                }
                return true;
            case 171:
                // $script:0704154107006557$ 
                // - I'm a scientist, not a magician. I can't just whisk such things out of thin air. I don't suppose you actually brought me the materials? 
                switch (selection) {
                    // $script:0704154107006558$
                    // - As it happens, I did! So, can you make it?
                    case 0:
                        Id = 0; // TODO: 172 | 173
                        return false;
                }
                return true;
            case 172:
                // $script:0704154107006559$ functionID=11 
                // - <font color="#909090">(He grumbles under his breath and puts together your new weapon.)</font>
                //   Here you go. I only made it because you asked so nicely. If you want it polished up, I suggest you get it to a smith right away.
                return true;
            case 173:
                // $script:0704154107006560$ 
                // - What's this? Your bag's full! Why are you wasting my time when you don't even have space for a new weapon?
                return true;
            case 174:
                // $script:0704154107006561$ 
                // - I need raw materials for a job like this! Say, 30 $itemPlural:30000437$ or so. And don't forget the $item:30000560$! 
                return true;
            case 175:
                // $script:0704154107006562$ 
                // - It's keeping me busy. Real busy. As in, "Don't bother me if you're just want to chat" busy. So, unless you've got something real exciting for me, I don't have time for chitchat.
                return true;
            case 180:
                // $script:0704154107006563$ 
                // - Hmph. Unless you have something interesting to show me, just leave me alone.
                switch (selection) {
                    // $script:0704154107006564$
                    // - I need a glimmering Balrog's weapon.
                    case 0:
                        Id = 0; // TODO: 181 | 184
                        return false;
                    // $script:0704154107006565$
                    // - How goes your research on power wavelengths?
                    case 1:
                        Id = 185;
                        return false;
                }
                return true;
            case 181:
                // $script:0704154107006566$ 
                // - I'm a scientist, not a magician. I can't just whisk such things out of thin air. I don't suppose you actually brought me the materials? 
                switch (selection) {
                    // $script:0704154107006567$
                    // - As it happens, I did! So, can you make it?
                    case 0:
                        Id = 0; // TODO: 182 | 183
                        return false;
                }
                return true;
            case 182:
                // $script:0704154107006568$ functionID=12 
                // - <font color="#909090">(He grumbles under his breath and puts together your new weapon.)</font>
                //   Here you go. I only made it because you asked so nicely. If you want it polished up, I suggest you get it to a smith right away.
                return true;
            case 183:
                // $script:0704154107006569$ 
                // - What's this? Your bag's full! Why are you wasting my time when you don't even have space for a new weapon?
                return true;
            case 184:
                // $script:0704154107006570$ 
                // - I need raw materials for a job like this! Say, 30 $itemPlural:30000437$ or so. And don't forget the $item:30000561$! 
                return true;
            case 185:
                // $script:0704154107006571$ 
                // - It's keeping me busy. Real busy. As in, "Don't bother me if you're just want to chat" busy. So, unless you've got something real exciting for me, I don't have time for chitchat.
                return true;
            default:
                return true;
        }
    }
}
