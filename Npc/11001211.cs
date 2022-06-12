using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001211: 
/// </summary>
public class _11001211 : NpcScript {
    protected override void FirstScript() {
        // TODO: RandomPick 30;40;50;60;70;80;90;100;110;120;130;140;150
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
        // (Id, Button) = (150, NpcTalkButton.SelectableDistractor);
    }

    protected override (int, NpcTalkButton) Next(int selection) {
        switch (Id) {
            case 0:
                // $script:1022122107004255$ 
                // - There's one weapon I'd love to create, but I don't have the right materials.
                return default;
            case 30:
                // $script:1022122107004258$ 
                // - My dream is to forge a weapon unlike anything the world has ever seen. Of course, the same could be said for any other Blacksmith on $map:2000203$. But none among them have the skill to create what I have in mind.
                switch (selection) {
                    // $script:1022122107004259$
                    // - What makes you so confident in your craft?
                    case 0:
                        return (31, NpcTalkButton.Next);
                }
                return default;
            case 31:
                switch (Index++) {
                    case 0:
                        // $script:1022122107004260$ 
                        // - The quality of any weapon is determined by the materials used for its creation. But having superior materials is not enough on its own. The true test of a blacksmith is knowing how to best make use of these materials.
                        return (31, NpcTalkButton.SelectableDistractor);
                    case 1:
                        // $script:1022122107004261$ 
                        // - I happen to have mastered my family's secret technique for creating weapons of the highest caliber. I can't help but be confident! However, without the right materials, all of that is moot.
                        switch (selection) {
                            // $script:1022122107004262$
                            // - What sort of materials do you need?
                            case 0:
                                return (32, NpcTalkButton.Next);
                        }
                        return default;
                }
                break;
            case 32:
                switch (Index++) {
                    case 0:
                        // $script:1022122107004263$ 
                        // - I intend to imbue the weapon with magical power, such that it will never grow dull, and grant strength to its wielder. Finding a material with those kinds of properties hasn't been easy...
                        return (32, NpcTalkButton.Next);
                    case 1:
                        // $script:1022122107004264$ 
                        // - I've tried all kinds of crystals and objects of power, but none of them could match up to the material that I envisioned in my mind's eye. Besides, those materials had a limit to their power. They didn't last long and they were pathetically weak.
                        return (32, NpcTalkButton.Close);
                    case 2:
                        // $script:1022122107004265$ 
                        // - Perhaps the material I seek doesn't even exist. But it must exist somewhere... Something that generates an endless supply of power...
                        return default;
                }
                break;
            case 40:
                // $script:1127105607004522$ 
                // - What brings you here, $MyPCName$? 
                switch (selection) {
                    // $script:1127105607004523$
                    // - I want a sealed Balrog's weapon.
                    case 0:
                        // TODO: goto 41
                        // (Id, Button) = (41, NpcTalkButton.SelectableDistractor);
                        // TODO: gotoFail 44
                        // (Id, Button) = (44, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                    // $script:1127105607004524$
                    // - Any news about the weapon?
                    case 1:
                        return (45, NpcTalkButton.Close);
                }
                return default;
            case 41:
                // $script:1127105607004525$ 
                // - Right. You're the one who wanted to take one of $npcName:23090005[gender:0]$'s weapons and imbue it with his power. Give me a minute. If you have the spoils of your victory, I can imbue the weapon for you. 
                switch (selection) {
                    // $script:1127105607004526$
                    // - Take your time.
                    case 0:
                        // TODO: goto 42
                        // (Id, Button) = (42, NpcTalkButton.Close);
                        // TODO: gotoFail 43
                        // (Id, Button) = (43, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                }
                return default;
            case 42:
                // $script:1127105607004527$ functionID=1 
                // - It's done. There you go. 
                return default;
            case 43:
                // $script:1127105607004528$ 
                // - It looks like your bag is full. Make some room, if you'd be so kind. 
                return default;
            case 44:
                // $script:1127105607004529$ 
                // - Well, this is awkward. You do know that you need 36 $itemPlural:30000420$ and 5 $itemPlural:30000421$, don't you? Come back when you have them.
                return default;
            case 45:
                // $script:1127105607004530$ 
                // - I've asked around everywhere, but I haven't heard anything. I'll find a solution, though. It's just a matter of time. Say... do you happen to know a man named $npcName:11001212[gender:0]$? I hear he deals in $itemPlural:30000421$. You might ask him to see if he knows anything. 
                return default;
            case 50:
                // $script:1127160607004531$ 
                // - What brings you here, $MyPCName$? 
                switch (selection) {
                    // $script:1127160607004532$
                    // - I want a sealed Balrog's weapon.
                    case 0:
                        // TODO: goto 51
                        // (Id, Button) = (51, NpcTalkButton.SelectableDistractor);
                        // TODO: gotoFail 54
                        // (Id, Button) = (54, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                    // $script:1127160607004533$
                    // - Any news about the weapon?
                    case 1:
                        return (55, NpcTalkButton.Close);
                }
                return default;
            case 51:
                // $script:1127160607004534$ 
                // - Right. You're the one who wanted to take one of $npcName:23090005[gender:0]$'s weapons and imbue it with his power. Give me a minute. If you have the spoils of your victory, I can imbue the weapon for you. 
                switch (selection) {
                    // $script:1127160607004535$
                    // - Take your time.
                    case 0:
                        // TODO: goto 52
                        // (Id, Button) = (52, NpcTalkButton.Close);
                        // TODO: gotoFail 53
                        // (Id, Button) = (53, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                }
                return default;
            case 52:
                // $script:1127160607004536$ functionID=2 
                // - It's done. There you go. 
                return default;
            case 53:
                // $script:1127160607004537$ 
                // - It looks like your bag is full. Make some room, if you'd be so kind. 
                return default;
            case 54:
                // $script:1127160607004538$ 
                // - Well, this is awkward. You do know that you need 36 $itemPlural:30000420$ and 5 $itemPlural:30000421$, don't you? Come back when you have them.
                return default;
            case 55:
                // $script:1127160607004539$ 
                // - I've asked around everywhere, but I haven't heard anything. I'll find a solution, though. It's just a matter of time. Say... do you happen to know a man named $npcName:11001212[gender:0]$? I hear he deals in $itemPlural:30000421$. You might ask him to see if he knows anything. 
                return default;
            case 60:
                // $script:1127160607004540$ 
                // - What brings you here, $MyPCName$? 
                switch (selection) {
                    // $script:1127160607004541$
                    // - I want a sealed Balrog's weapon.
                    case 0:
                        // TODO: goto 61
                        // (Id, Button) = (61, NpcTalkButton.SelectableDistractor);
                        // TODO: gotoFail 64
                        // (Id, Button) = (64, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                    // $script:1127160607004542$
                    // - Any news about the weapon?
                    case 1:
                        return (65, NpcTalkButton.Close);
                }
                return default;
            case 61:
                // $script:1127160607004543$ 
                // - Right. You're the one who wanted to take one of $npcName:23090005[gender:0]$'s weapons and imbue it with his power. Give me a minute. If you have the spoils of your victory, I can imbue the weapon for you. 
                switch (selection) {
                    // $script:1127160607004544$
                    // - Take your time.
                    case 0:
                        // TODO: goto 62
                        // (Id, Button) = (62, NpcTalkButton.Close);
                        // TODO: gotoFail 63
                        // (Id, Button) = (63, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                }
                return default;
            case 62:
                // $script:1127160607004545$ functionID=3 
                // - It's done. There you go. 
                return default;
            case 63:
                // $script:1127160607004546$ 
                // - It looks like your bag is full. Make some room, if you'd be so kind. 
                return default;
            case 64:
                // $script:1127160607004547$ 
                // - Well, this is awkward. You do know that you need 36 $itemPlural:30000420$ and 5 $itemPlural:30000421$, don't you? Come back when you have them.
                return default;
            case 65:
                // $script:1127160607004548$ 
                // - I've asked around everywhere, but I haven't heard anything. I'll find a solution, though. It's just a matter of time. Say... do you happen to know a man named $npcName:11001212[gender:0]$? I hear he deals in $itemPlural:30000421$. You might ask him to see if he knows anything. 
                return default;
            case 70:
                // $script:1127160607004549$ 
                // - What brings you here, $MyPCName$? 
                switch (selection) {
                    // $script:1127160607004550$
                    // - I want a sealed Balrog's weapon.
                    case 0:
                        // TODO: goto 71
                        // (Id, Button) = (71, NpcTalkButton.SelectableDistractor);
                        // TODO: gotoFail 74
                        // (Id, Button) = (74, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                    // $script:1127160607004551$
                    // - Any news about the weapon?
                    case 1:
                        return (75, NpcTalkButton.Close);
                }
                return default;
            case 71:
                // $script:1127160607004552$ 
                // - Right. You're the one who wanted to take one of $npcName:23090005[gender:0]$'s weapons and imbue it with his power. Give me a minute. If you have the spoils of your victory, I can imbue the weapon for you. 
                switch (selection) {
                    // $script:1127160607004553$
                    // - Take your time.
                    case 0:
                        // TODO: goto 72
                        // (Id, Button) = (72, NpcTalkButton.Close);
                        // TODO: gotoFail 73
                        // (Id, Button) = (73, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                }
                return default;
            case 72:
                // $script:1127160607004554$ functionID=4 
                // - It's done. There you go. 
                return default;
            case 73:
                // $script:1127160607004555$ 
                // - It looks like your bag is full. Make some room, if you'd be so kind. 
                return default;
            case 74:
                // $script:1127160607004556$ 
                // - Well, this is awkward. You do know that you need 36 $itemPlural:30000420$ and 5 $itemPlural:30000421$, don't you? Come back when you have them.
                return default;
            case 75:
                // $script:1127160607004557$ 
                // - I've asked around everywhere, but I haven't heard anything. I'll find a solution, though. It's just a matter of time. Say... do you happen to know a man named $npcName:11001212[gender:0]$? I hear he deals in $itemPlural:30000421$. You might ask him to see if he knows anything. 
                return default;
            case 80:
                // $script:1127160707004531$ 
                // - What brings you here, $MyPCName$? 
                switch (selection) {
                    // $script:1127160707004532$
                    // - I want a sealed Balrog's weapon.
                    case 0:
                        // TODO: goto 81
                        // (Id, Button) = (81, NpcTalkButton.SelectableDistractor);
                        // TODO: gotoFail 84
                        // (Id, Button) = (84, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                    // $script:1127160707004533$
                    // - Any news about the weapon?
                    case 1:
                        return (85, NpcTalkButton.Close);
                }
                return default;
            case 81:
                // $script:1127160707004534$ 
                // - Right. You're the one who wanted to take one of $npcName:23090005[gender:0]$'s weapons and imbue it with his power. Give me a minute. If you have the spoils of your victory, I can imbue the weapon for you. 
                switch (selection) {
                    // $script:1127160707004535$
                    // - Take your time.
                    case 0:
                        // TODO: goto 82
                        // (Id, Button) = (82, NpcTalkButton.Close);
                        // TODO: gotoFail 83
                        // (Id, Button) = (83, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                }
                return default;
            case 82:
                // $script:1127160707004536$ functionID=5 
                // - It's done. There you go. 
                return default;
            case 83:
                // $script:1127160707004537$ 
                // - It looks like your bag is full. Make some room, if you'd be so kind. 
                return default;
            case 84:
                // $script:1127160707004538$ 
                // - Well, this is awkward. You do know that you need 36 $itemPlural:30000420$ and 5 $itemPlural:30000421$, don't you? Come back when you have them.
                return default;
            case 85:
                // $script:1127160707004539$ 
                // - I've asked around everywhere, but I haven't heard anything. I'll find a solution, though. It's just a matter of time. Say... do you happen to know a man named $npcName:11001212[gender:0]$? I hear he deals in $itemPlural:30000421$. You might ask him to see if he knows anything. 
                return default;
            case 90:
                // $script:1127160707004540$ 
                // - What brings you here, $MyPCName$? 
                switch (selection) {
                    // $script:1127160707004541$
                    // - I want a sealed Balrog's weapon.
                    case 0:
                        // TODO: goto 91
                        // (Id, Button) = (91, NpcTalkButton.SelectableDistractor);
                        // TODO: gotoFail 94
                        // (Id, Button) = (94, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                    // $script:1127160707004542$
                    // - Any news about the weapon?
                    case 1:
                        return (95, NpcTalkButton.Close);
                }
                return default;
            case 91:
                // $script:1127160707004543$ 
                // - Right. You're the one who wanted to take one of $npcName:23090005[gender:0]$'s weapons and imbue it with his power. Give me a minute. If you have the spoils of your victory, I can imbue the weapon for you. 
                switch (selection) {
                    // $script:1127160707004544$
                    // - Take your time.
                    case 0:
                        // TODO: goto 92
                        // (Id, Button) = (92, NpcTalkButton.Close);
                        // TODO: gotoFail 93
                        // (Id, Button) = (93, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                }
                return default;
            case 92:
                // $script:1127160707004545$ functionID=6 
                // - It's done. There you go. 
                return default;
            case 93:
                // $script:1127160707004546$ 
                // - It looks like your bag is full. Make some room, if you'd be so kind. 
                return default;
            case 94:
                // $script:1127160707004547$ 
                // - Well, this is awkward. You do know that you need 36 $itemPlural:30000420$ and 5 $itemPlural:30000421$, don't you? Come back when you have them.
                return default;
            case 95:
                // $script:1127160707004548$ 
                // - I've asked around everywhere, but I haven't heard anything. I'll find a solution, though. It's just a matter of time. Say... do you happen to know a man named $npcName:11001212[gender:0]$? I hear he deals in $itemPlural:30000421$. You might ask him to see if he knows anything. 
                return default;
            case 100:
                // $script:1127160707004549$ 
                // - What brings you here, $MyPCName$? 
                switch (selection) {
                    // $script:1127160707004550$
                    // - I want a sealed Balrog's weapon.
                    case 0:
                        // TODO: goto 101
                        // (Id, Button) = (101, NpcTalkButton.SelectableDistractor);
                        // TODO: gotoFail 104
                        // (Id, Button) = (104, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                    // $script:1127160707004551$
                    // - Any news about the weapon?
                    case 1:
                        return (105, NpcTalkButton.Close);
                }
                return default;
            case 101:
                // $script:1127160707004552$ 
                // - Right. You're the one who wanted to take one of $npcName:23090005[gender:0]$'s weapons and imbue it with his power. Give me a minute. If you have the spoils of your victory, I can imbue the weapon for you. 
                switch (selection) {
                    // $script:1127160707004553$
                    // - Take your time.
                    case 0:
                        // TODO: goto 102
                        // (Id, Button) = (102, NpcTalkButton.Close);
                        // TODO: gotoFail 103
                        // (Id, Button) = (103, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                }
                return default;
            case 102:
                // $script:1127160707004554$ functionID=7 
                // - It's done. There you go. 
                return default;
            case 103:
                // $script:1127160707004555$ 
                // - It looks like your bag is full. Make some room, if you'd be so kind. 
                return default;
            case 104:
                // $script:1127160707004556$ 
                // - Well, this is awkward. You do know that you need 36 $itemPlural:30000420$ and 5 $itemPlural:30000421$, don't you? Come back when you have them.
                return default;
            case 105:
                // $script:1127160707004557$ 
                // - I've asked around everywhere, but I haven't heard anything. I'll find a solution, though. It's just a matter of time. Say... do you happen to know a man named $npcName:11001212[gender:0]$? I hear he deals in $itemPlural:30000421$. You might ask him to see if he knows anything. 
                return default;
            case 110:
                // $script:1127160707004558$ 
                // - What brings you here, $MyPCName$? 
                switch (selection) {
                    // $script:1127160707004559$
                    // - I want a sealed Balrog's weapon.
                    case 0:
                        // TODO: goto 111
                        // (Id, Button) = (111, NpcTalkButton.SelectableDistractor);
                        // TODO: gotoFail 114
                        // (Id, Button) = (114, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                    // $script:1127160707004560$
                    // - Any news about the weapon?
                    case 1:
                        return (115, NpcTalkButton.Close);
                }
                return default;
            case 111:
                // $script:1127160707004561$ 
                // - Right. You're the one who wanted to take one of $npcName:23090005[gender:0]$'s weapons and imbue it with his power. Give me a minute. If you have the spoils of your victory, I can imbue the weapon for you. 
                switch (selection) {
                    // $script:1127160707004562$
                    // - Take your time.
                    case 0:
                        // TODO: goto 112
                        // (Id, Button) = (112, NpcTalkButton.Close);
                        // TODO: gotoFail 113
                        // (Id, Button) = (113, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                }
                return default;
            case 112:
                // $script:1127160707004563$ functionID=8 
                // - It's done. There you go. 
                return default;
            case 113:
                // $script:1127160707004564$ 
                // - It looks like your bag is full. Make some room, if you'd be so kind. 
                return default;
            case 114:
                // $script:1127160707004565$ 
                // - Well, this is awkward. You do know that you need 36 $itemPlural:30000420$ and 5 $itemPlural:30000421$, don't you? Come back when you have them.
                return default;
            case 115:
                // $script:1127160707004566$ 
                // - I've asked around everywhere, but I haven't heard anything. I'll find a solution, though. It's just a matter of time. Say... do you happen to know a man named $npcName:11001212[gender:0]$? I hear he deals in $itemPlural:30000421$. You might ask him to see if he knows anything. 
                return default;
            case 120:
                // $script:1127160707004567$ 
                // - What brings you here, $MyPCName$? 
                switch (selection) {
                    // $script:1127160707004568$
                    // - I want a sealed Balrog's weapon.
                    case 0:
                        // TODO: goto 121
                        // (Id, Button) = (121, NpcTalkButton.SelectableDistractor);
                        // TODO: gotoFail 124
                        // (Id, Button) = (124, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                    // $script:1127160707004569$
                    // - Any news about the weapon?
                    case 1:
                        return (125, NpcTalkButton.Close);
                }
                return default;
            case 121:
                // $script:1127160707004570$ 
                // - Right. You're the one who wanted to take one of $npcName:23090005[gender:0]$'s weapons and imbue it with his power. Give me a minute. If you have the spoils of your victory, I can imbue the weapon for you. 
                switch (selection) {
                    // $script:1127160707004571$
                    // - Take your time.
                    case 0:
                        // TODO: goto 122
                        // (Id, Button) = (122, NpcTalkButton.Close);
                        // TODO: gotoFail 123
                        // (Id, Button) = (123, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                }
                return default;
            case 122:
                // $script:1127160707004572$ functionID=9 
                // - It's done. There you go. 
                return default;
            case 123:
                // $script:1127160707004573$ 
                // - It looks like your bag is full. Make some room, if you'd be so kind. 
                return default;
            case 124:
                // $script:1127160707004574$ 
                // - Well, this is awkward. You do know that you need 36 $itemPlural:30000420$ and 5 $itemPlural:30000421$, don't you? Come back when you have them.
                return default;
            case 125:
                // $script:1127160707004575$ 
                // - I've asked around everywhere, but I haven't heard anything. I'll find a solution, though. It's just a matter of time. Say... do you happen to know a man named $npcName:11001212[gender:0]$? I hear he deals in $itemPlural:30000421$. You might ask him to see if he knows anything. 
                return default;
            case 130:
                // $script:1209201207004872$ 
                // - What brings you here, $MyPCName$? 
                switch (selection) {
                    // $script:1209201207004873$
                    // - I want a sealed Balrog's weapon.
                    case 0:
                        // TODO: goto 131
                        // (Id, Button) = (131, NpcTalkButton.SelectableDistractor);
                        // TODO: gotoFail 134
                        // (Id, Button) = (134, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                    // $script:1209201207004874$
                    // - Any news about the weapon?
                    case 1:
                        return (135, NpcTalkButton.Close);
                }
                return default;
            case 131:
                // $script:1209201207004875$ 
                // - Right. You're the one who wanted to take one of $npcName:23090005[gender:0]$'s weapons and imbue it with his power. Give me a minute. If you have the spoils of your victory, I can imbue the weapon for you. 
                switch (selection) {
                    // $script:1209201207004876$
                    // - Take your time.
                    case 0:
                        // TODO: goto 132
                        // (Id, Button) = (132, NpcTalkButton.Close);
                        // TODO: gotoFail 133
                        // (Id, Button) = (133, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                }
                return default;
            case 132:
                // $script:1209201207004877$ functionID=10 
                // - It's done. There you go. 
                return default;
            case 133:
                // $script:1209201207004878$ 
                // - It looks like your bag is full. Make some room, if you'd be so kind. 
                return default;
            case 134:
                // $script:1209201207004879$ 
                // - Well, this is awkward. You do know that you need 36 $itemPlural:30000420$ and 5 $itemPlural:30000421$, don't you? Come back when you have them.
                return default;
            case 135:
                // $script:1209201207004880$ 
                // - I've asked around everywhere, but I haven't heard anything. I'll find a solution, though. It's just a matter of time. Say... do you happen to know a man named $npcName:11001212[gender:0]$? I hear he deals in $itemPlural:30000421$. You might ask him to see if he knows anything. 
                return default;
            case 140:
                // $script:0704154107006536$ 
                // - What brings you here, $MyPCName$? 
                switch (selection) {
                    // $script:0704154107006537$
                    // - I want a sealed Balrog's weapon.
                    case 0:
                        // TODO: goto 141
                        // (Id, Button) = (141, NpcTalkButton.SelectableDistractor);
                        // TODO: gotoFail 144
                        // (Id, Button) = (144, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                    // $script:0704154107006538$
                    // - Any news about the weapon?
                    case 1:
                        return (145, NpcTalkButton.Close);
                }
                return default;
            case 141:
                // $script:0704154107006539$ 
                // - Right. You're the one who wanted to take one of $npcName:23090005[gender:0]$'s weapons and imbue it with his power. Give me a minute. If you have the spoils of your victory, I can imbue the weapon for you. 
                switch (selection) {
                    // $script:0704154107006540$
                    // - Take your time.
                    case 0:
                        // TODO: goto 142
                        // (Id, Button) = (142, NpcTalkButton.Close);
                        // TODO: gotoFail 143
                        // (Id, Button) = (143, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                }
                return default;
            case 142:
                // $script:0704154107006541$ functionID=11 
                // - It's done. There you go. 
                return default;
            case 143:
                // $script:0704154107006542$ 
                // - It looks like your bag is full. Make some room, if you'd be so kind. 
                return default;
            case 144:
                // $script:0704154107006543$ 
                // - Well, this is awkward. You do know that you need 36 $itemPlural:30000420$ and 5 $itemPlural:30000421$, don't you? Come back when you have them.
                return default;
            case 145:
                // $script:0704154107006544$ 
                // - I've asked around everywhere, but I haven't heard anything. I'll find a solution, though. It's just a matter of time. Say... do you happen to know a man named $npcName:11001212[gender:0]$? I hear he deals in $itemPlural:30000421$. You might ask him to see if he knows anything. 
                return default;
            case 150:
                // $script:0704154107006545$ 
                // - What brings you here, $MyPCName$? 
                switch (selection) {
                    // $script:0704154107006546$
                    // - I want a sealed Balrog's weapon.
                    case 0:
                        // TODO: goto 151
                        // (Id, Button) = (151, NpcTalkButton.SelectableDistractor);
                        // TODO: gotoFail 154
                        // (Id, Button) = (154, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                    // $script:0704154107006547$
                    // - Any news about the weapon?
                    case 1:
                        return (155, NpcTalkButton.Close);
                }
                return default;
            case 151:
                // $script:0704154107006548$ 
                // - Right. You're the one who wanted to take one of $npcName:23090005[gender:0]$'s weapons and imbue it with his power. Give me a minute. If you have the spoils of your victory, I can imbue the weapon for you. 
                switch (selection) {
                    // $script:0704154107006549$
                    // - Take your time.
                    case 0:
                        // TODO: goto 152
                        // (Id, Button) = (152, NpcTalkButton.Close);
                        // TODO: gotoFail 153
                        // (Id, Button) = (153, NpcTalkButton.Close);
                        return (0, NpcTalkButton.None);
                }
                return default;
            case 152:
                // $script:0704154107006550$ functionID=12 
                // - It's done. There you go. 
                return default;
            case 153:
                // $script:0704154107006551$ 
                // - It looks like your bag is full. Make some room, if you'd be so kind. 
                return default;
            case 154:
                // $script:0704154107006552$ 
                // - Well, this is awkward. You do know that you need 36 $itemPlural:30000420$ and 5 $itemPlural:30000421$, don't you? Come back when you have them.
                return default;
            case 155:
                // $script:0704154107006553$ 
                // - I've asked around everywhere, but I haven't heard anything. I'll find a solution, though. It's just a matter of time. Say... do you happen to know a man named $npcName:11001212[gender:0]$? I hear he deals in $itemPlural:30000421$. You might ask him to see if he knows anything. 
                return default;
        }
        
        return default;
    }
}
