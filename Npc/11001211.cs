using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001211: 
/// </summary>
public class _11001211 : NpcScript {
    internal _11001211(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40;50;60;70;80;90;100;110;120;130;140;150
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1022122107004255$ 
                // - There's one weapon I'd love to create, but I don't have the right materials. 
                return true;
            case 30:
                // $script:1022122107004258$ 
                // - My dream is to forge a weapon unlike anything the world has ever seen. Of course, the same could be said for any other Blacksmith on $map:2000203$. But none among them have the skill to create what I have in mind. 
                switch (selection) {
                    // $script:1022122107004259$
                    // - What makes you so confident in your craft?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:1022122107004260$ 
                // - The quality of any weapon is determined by the materials used for its creation. But having superior materials is not enough on its own. The true test of a blacksmith is knowing how to best make use of these materials. 
                // $script:1022122107004261$ 
                // - I happen to have mastered my family's secret technique for creating weapons of the highest caliber. I can't help but be confident! However, without the right materials, all of that is moot. 
                switch (selection) {
                    // $script:1022122107004262$
                    // - What sort of materials do you need?
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:1022122107004263$ 
                // - I intend to imbue the weapon with magical power, such that it will never grow dull, and grant strength to its wielder. Finding a material with those kinds of properties hasn't been easy... 
                // $script:1022122107004264$ 
                // - I've tried all kinds of crystals and objects of power, but none of them could match up to the material that I envisioned in my mind's eye. Besides, those materials had a limit to their power. They didn't last long and they were pathetically weak. 
                // $script:1022122107004265$ 
                // - Perhaps the material I seek doesn't even exist. But it must exist somewhere... Something that generates an endless supply of power... 
                return true;
            case 40:
                // $script:1127105607004522$ 
                // - What brings you here, $MyPCName$?  
                switch (selection) {
                    // $script:1127105607004523$
                    // - I want a sealed Balrog's weapon.
                    case 0:
                        Id = 0; // TODO: 41 | 44
                        return false;
                    // $script:1127105607004524$
                    // - Any news about the weapon?
                    case 1:
                        Id = 45;
                        return false;
                }
                return true;
            case 41:
                // $script:1127105607004525$ 
                // - Right. You're the one who wanted to take one of $npcName:23090005[gender:0]$'s weapons and imbue it with his power. Give me a minute. If you have the spoils of your victory, I can imbue the weapon for you.  
                switch (selection) {
                    // $script:1127105607004526$
                    // - Take your time.
                    case 0:
                        Id = 0; // TODO: 42 | 43
                        return false;
                }
                return true;
            case 42:
                // $script:1127105607004527$ functionID=1 
                // - It's done. There you go.  
                return true;
            case 43:
                // $script:1127105607004528$ 
                // - It looks like your bag is full. Make some room, if you'd be so kind.  
                return true;
            case 44:
                // $script:1127105607004529$ 
                // - Well, this is awkward. You do know that you need 36 $itemPlural:30000420$ and 5 $itemPlural:30000421$, don't you? Come back when you have them. 
                return true;
            case 45:
                // $script:1127105607004530$ 
                // - I've asked around everywhere, but I haven't heard anything. I'll find a solution, though. It's just a matter of time. Say... do you happen to know a man named $npcName:11001212[gender:0]$? I hear he deals in $itemPlural:30000421$. You might ask him to see if he knows anything.  
                return true;
            case 50:
                // $script:1127160607004531$ 
                // - What brings you here, $MyPCName$?  
                switch (selection) {
                    // $script:1127160607004532$
                    // - I want a sealed Balrog's weapon.
                    case 0:
                        Id = 0; // TODO: 51 | 54
                        return false;
                    // $script:1127160607004533$
                    // - Any news about the weapon?
                    case 1:
                        Id = 55;
                        return false;
                }
                return true;
            case 51:
                // $script:1127160607004534$ 
                // - Right. You're the one who wanted to take one of $npcName:23090005[gender:0]$'s weapons and imbue it with his power. Give me a minute. If you have the spoils of your victory, I can imbue the weapon for you.  
                switch (selection) {
                    // $script:1127160607004535$
                    // - Take your time.
                    case 0:
                        Id = 0; // TODO: 52 | 53
                        return false;
                }
                return true;
            case 52:
                // $script:1127160607004536$ functionID=2 
                // - It's done. There you go.  
                return true;
            case 53:
                // $script:1127160607004537$ 
                // - It looks like your bag is full. Make some room, if you'd be so kind.  
                return true;
            case 54:
                // $script:1127160607004538$ 
                // - Well, this is awkward. You do know that you need 36 $itemPlural:30000420$ and 5 $itemPlural:30000421$, don't you? Come back when you have them. 
                return true;
            case 55:
                // $script:1127160607004539$ 
                // - I've asked around everywhere, but I haven't heard anything. I'll find a solution, though. It's just a matter of time. Say... do you happen to know a man named $npcName:11001212[gender:0]$? I hear he deals in $itemPlural:30000421$. You might ask him to see if he knows anything.  
                return true;
            case 60:
                // $script:1127160607004540$ 
                // - What brings you here, $MyPCName$?  
                switch (selection) {
                    // $script:1127160607004541$
                    // - I want a sealed Balrog's weapon.
                    case 0:
                        Id = 0; // TODO: 61 | 64
                        return false;
                    // $script:1127160607004542$
                    // - Any news about the weapon?
                    case 1:
                        Id = 65;
                        return false;
                }
                return true;
            case 61:
                // $script:1127160607004543$ 
                // - Right. You're the one who wanted to take one of $npcName:23090005[gender:0]$'s weapons and imbue it with his power. Give me a minute. If you have the spoils of your victory, I can imbue the weapon for you.  
                switch (selection) {
                    // $script:1127160607004544$
                    // - Take your time.
                    case 0:
                        Id = 0; // TODO: 62 | 63
                        return false;
                }
                return true;
            case 62:
                // $script:1127160607004545$ functionID=3 
                // - It's done. There you go.  
                return true;
            case 63:
                // $script:1127160607004546$ 
                // - It looks like your bag is full. Make some room, if you'd be so kind.  
                return true;
            case 64:
                // $script:1127160607004547$ 
                // - Well, this is awkward. You do know that you need 36 $itemPlural:30000420$ and 5 $itemPlural:30000421$, don't you? Come back when you have them. 
                return true;
            case 65:
                // $script:1127160607004548$ 
                // - I've asked around everywhere, but I haven't heard anything. I'll find a solution, though. It's just a matter of time. Say... do you happen to know a man named $npcName:11001212[gender:0]$? I hear he deals in $itemPlural:30000421$. You might ask him to see if he knows anything.  
                return true;
            case 70:
                // $script:1127160607004549$ 
                // - What brings you here, $MyPCName$?  
                switch (selection) {
                    // $script:1127160607004550$
                    // - I want a sealed Balrog's weapon.
                    case 0:
                        Id = 0; // TODO: 71 | 74
                        return false;
                    // $script:1127160607004551$
                    // - Any news about the weapon?
                    case 1:
                        Id = 75;
                        return false;
                }
                return true;
            case 71:
                // $script:1127160607004552$ 
                // - Right. You're the one who wanted to take one of $npcName:23090005[gender:0]$'s weapons and imbue it with his power. Give me a minute. If you have the spoils of your victory, I can imbue the weapon for you.  
                switch (selection) {
                    // $script:1127160607004553$
                    // - Take your time.
                    case 0:
                        Id = 0; // TODO: 72 | 73
                        return false;
                }
                return true;
            case 72:
                // $script:1127160607004554$ functionID=4 
                // - It's done. There you go.  
                return true;
            case 73:
                // $script:1127160607004555$ 
                // - It looks like your bag is full. Make some room, if you'd be so kind.  
                return true;
            case 74:
                // $script:1127160607004556$ 
                // - Well, this is awkward. You do know that you need 36 $itemPlural:30000420$ and 5 $itemPlural:30000421$, don't you? Come back when you have them. 
                return true;
            case 75:
                // $script:1127160607004557$ 
                // - I've asked around everywhere, but I haven't heard anything. I'll find a solution, though. It's just a matter of time. Say... do you happen to know a man named $npcName:11001212[gender:0]$? I hear he deals in $itemPlural:30000421$. You might ask him to see if he knows anything.  
                return true;
            case 80:
                // $script:1127160707004531$ 
                // - What brings you here, $MyPCName$?  
                switch (selection) {
                    // $script:1127160707004532$
                    // - I want a sealed Balrog's weapon.
                    case 0:
                        Id = 0; // TODO: 81 | 84
                        return false;
                    // $script:1127160707004533$
                    // - Any news about the weapon?
                    case 1:
                        Id = 85;
                        return false;
                }
                return true;
            case 81:
                // $script:1127160707004534$ 
                // - Right. You're the one who wanted to take one of $npcName:23090005[gender:0]$'s weapons and imbue it with his power. Give me a minute. If you have the spoils of your victory, I can imbue the weapon for you.  
                switch (selection) {
                    // $script:1127160707004535$
                    // - Take your time.
                    case 0:
                        Id = 0; // TODO: 82 | 83
                        return false;
                }
                return true;
            case 82:
                // $script:1127160707004536$ functionID=5 
                // - It's done. There you go.  
                return true;
            case 83:
                // $script:1127160707004537$ 
                // - It looks like your bag is full. Make some room, if you'd be so kind.  
                return true;
            case 84:
                // $script:1127160707004538$ 
                // - Well, this is awkward. You do know that you need 36 $itemPlural:30000420$ and 5 $itemPlural:30000421$, don't you? Come back when you have them. 
                return true;
            case 85:
                // $script:1127160707004539$ 
                // - I've asked around everywhere, but I haven't heard anything. I'll find a solution, though. It's just a matter of time. Say... do you happen to know a man named $npcName:11001212[gender:0]$? I hear he deals in $itemPlural:30000421$. You might ask him to see if he knows anything.  
                return true;
            case 90:
                // $script:1127160707004540$ 
                // - What brings you here, $MyPCName$?  
                switch (selection) {
                    // $script:1127160707004541$
                    // - I want a sealed Balrog's weapon.
                    case 0:
                        Id = 0; // TODO: 91 | 94
                        return false;
                    // $script:1127160707004542$
                    // - Any news about the weapon?
                    case 1:
                        Id = 95;
                        return false;
                }
                return true;
            case 91:
                // $script:1127160707004543$ 
                // - Right. You're the one who wanted to take one of $npcName:23090005[gender:0]$'s weapons and imbue it with his power. Give me a minute. If you have the spoils of your victory, I can imbue the weapon for you.  
                switch (selection) {
                    // $script:1127160707004544$
                    // - Take your time.
                    case 0:
                        Id = 0; // TODO: 92 | 93
                        return false;
                }
                return true;
            case 92:
                // $script:1127160707004545$ functionID=6 
                // - It's done. There you go.  
                return true;
            case 93:
                // $script:1127160707004546$ 
                // - It looks like your bag is full. Make some room, if you'd be so kind.  
                return true;
            case 94:
                // $script:1127160707004547$ 
                // - Well, this is awkward. You do know that you need 36 $itemPlural:30000420$ and 5 $itemPlural:30000421$, don't you? Come back when you have them. 
                return true;
            case 95:
                // $script:1127160707004548$ 
                // - I've asked around everywhere, but I haven't heard anything. I'll find a solution, though. It's just a matter of time. Say... do you happen to know a man named $npcName:11001212[gender:0]$? I hear he deals in $itemPlural:30000421$. You might ask him to see if he knows anything.  
                return true;
            case 100:
                // $script:1127160707004549$ 
                // - What brings you here, $MyPCName$?  
                switch (selection) {
                    // $script:1127160707004550$
                    // - I want a sealed Balrog's weapon.
                    case 0:
                        Id = 0; // TODO: 101 | 104
                        return false;
                    // $script:1127160707004551$
                    // - Any news about the weapon?
                    case 1:
                        Id = 105;
                        return false;
                }
                return true;
            case 101:
                // $script:1127160707004552$ 
                // - Right. You're the one who wanted to take one of $npcName:23090005[gender:0]$'s weapons and imbue it with his power. Give me a minute. If you have the spoils of your victory, I can imbue the weapon for you.  
                switch (selection) {
                    // $script:1127160707004553$
                    // - Take your time.
                    case 0:
                        Id = 0; // TODO: 102 | 103
                        return false;
                }
                return true;
            case 102:
                // $script:1127160707004554$ functionID=7 
                // - It's done. There you go.  
                return true;
            case 103:
                // $script:1127160707004555$ 
                // - It looks like your bag is full. Make some room, if you'd be so kind.  
                return true;
            case 104:
                // $script:1127160707004556$ 
                // - Well, this is awkward. You do know that you need 36 $itemPlural:30000420$ and 5 $itemPlural:30000421$, don't you? Come back when you have them. 
                return true;
            case 105:
                // $script:1127160707004557$ 
                // - I've asked around everywhere, but I haven't heard anything. I'll find a solution, though. It's just a matter of time. Say... do you happen to know a man named $npcName:11001212[gender:0]$? I hear he deals in $itemPlural:30000421$. You might ask him to see if he knows anything.  
                return true;
            case 110:
                // $script:1127160707004558$ 
                // - What brings you here, $MyPCName$?  
                switch (selection) {
                    // $script:1127160707004559$
                    // - I want a sealed Balrog's weapon.
                    case 0:
                        Id = 0; // TODO: 111 | 114
                        return false;
                    // $script:1127160707004560$
                    // - Any news about the weapon?
                    case 1:
                        Id = 115;
                        return false;
                }
                return true;
            case 111:
                // $script:1127160707004561$ 
                // - Right. You're the one who wanted to take one of $npcName:23090005[gender:0]$'s weapons and imbue it with his power. Give me a minute. If you have the spoils of your victory, I can imbue the weapon for you.  
                switch (selection) {
                    // $script:1127160707004562$
                    // - Take your time.
                    case 0:
                        Id = 0; // TODO: 112 | 113
                        return false;
                }
                return true;
            case 112:
                // $script:1127160707004563$ functionID=8 
                // - It's done. There you go.  
                return true;
            case 113:
                // $script:1127160707004564$ 
                // - It looks like your bag is full. Make some room, if you'd be so kind.  
                return true;
            case 114:
                // $script:1127160707004565$ 
                // - Well, this is awkward. You do know that you need 36 $itemPlural:30000420$ and 5 $itemPlural:30000421$, don't you? Come back when you have them. 
                return true;
            case 115:
                // $script:1127160707004566$ 
                // - I've asked around everywhere, but I haven't heard anything. I'll find a solution, though. It's just a matter of time. Say... do you happen to know a man named $npcName:11001212[gender:0]$? I hear he deals in $itemPlural:30000421$. You might ask him to see if he knows anything.  
                return true;
            case 120:
                // $script:1127160707004567$ 
                // - What brings you here, $MyPCName$?  
                switch (selection) {
                    // $script:1127160707004568$
                    // - I want a sealed Balrog's weapon.
                    case 0:
                        Id = 0; // TODO: 121 | 124
                        return false;
                    // $script:1127160707004569$
                    // - Any news about the weapon?
                    case 1:
                        Id = 125;
                        return false;
                }
                return true;
            case 121:
                // $script:1127160707004570$ 
                // - Right. You're the one who wanted to take one of $npcName:23090005[gender:0]$'s weapons and imbue it with his power. Give me a minute. If you have the spoils of your victory, I can imbue the weapon for you.  
                switch (selection) {
                    // $script:1127160707004571$
                    // - Take your time.
                    case 0:
                        Id = 0; // TODO: 122 | 123
                        return false;
                }
                return true;
            case 122:
                // $script:1127160707004572$ functionID=9 
                // - It's done. There you go.  
                return true;
            case 123:
                // $script:1127160707004573$ 
                // - It looks like your bag is full. Make some room, if you'd be so kind.  
                return true;
            case 124:
                // $script:1127160707004574$ 
                // - Well, this is awkward. You do know that you need 36 $itemPlural:30000420$ and 5 $itemPlural:30000421$, don't you? Come back when you have them. 
                return true;
            case 125:
                // $script:1127160707004575$ 
                // - I've asked around everywhere, but I haven't heard anything. I'll find a solution, though. It's just a matter of time. Say... do you happen to know a man named $npcName:11001212[gender:0]$? I hear he deals in $itemPlural:30000421$. You might ask him to see if he knows anything.  
                return true;
            case 130:
                // $script:1209201207004872$ 
                // - What brings you here, $MyPCName$?  
                switch (selection) {
                    // $script:1209201207004873$
                    // - I want a sealed Balrog's weapon.
                    case 0:
                        Id = 0; // TODO: 131 | 134
                        return false;
                    // $script:1209201207004874$
                    // - Any news about the weapon?
                    case 1:
                        Id = 135;
                        return false;
                }
                return true;
            case 131:
                // $script:1209201207004875$ 
                // - Right. You're the one who wanted to take one of $npcName:23090005[gender:0]$'s weapons and imbue it with his power. Give me a minute. If you have the spoils of your victory, I can imbue the weapon for you.  
                switch (selection) {
                    // $script:1209201207004876$
                    // - Take your time.
                    case 0:
                        Id = 0; // TODO: 132 | 133
                        return false;
                }
                return true;
            case 132:
                // $script:1209201207004877$ functionID=10 
                // - It's done. There you go.  
                return true;
            case 133:
                // $script:1209201207004878$ 
                // - It looks like your bag is full. Make some room, if you'd be so kind.  
                return true;
            case 134:
                // $script:1209201207004879$ 
                // - Well, this is awkward. You do know that you need 36 $itemPlural:30000420$ and 5 $itemPlural:30000421$, don't you? Come back when you have them. 
                return true;
            case 135:
                // $script:1209201207004880$ 
                // - I've asked around everywhere, but I haven't heard anything. I'll find a solution, though. It's just a matter of time. Say... do you happen to know a man named $npcName:11001212[gender:0]$? I hear he deals in $itemPlural:30000421$. You might ask him to see if he knows anything.  
                return true;
            case 140:
                // $script:0704154107006536$ 
                // - What brings you here, $MyPCName$?  
                switch (selection) {
                    // $script:0704154107006537$
                    // - I want a sealed Balrog's weapon.
                    case 0:
                        Id = 0; // TODO: 141 | 144
                        return false;
                    // $script:0704154107006538$
                    // - Any news about the weapon?
                    case 1:
                        Id = 145;
                        return false;
                }
                return true;
            case 141:
                // $script:0704154107006539$ 
                // - Right. You're the one who wanted to take one of $npcName:23090005[gender:0]$'s weapons and imbue it with his power. Give me a minute. If you have the spoils of your victory, I can imbue the weapon for you.  
                switch (selection) {
                    // $script:0704154107006540$
                    // - Take your time.
                    case 0:
                        Id = 0; // TODO: 142 | 143
                        return false;
                }
                return true;
            case 142:
                // $script:0704154107006541$ functionID=11 
                // - It's done. There you go.  
                return true;
            case 143:
                // $script:0704154107006542$ 
                // - It looks like your bag is full. Make some room, if you'd be so kind.  
                return true;
            case 144:
                // $script:0704154107006543$ 
                // - Well, this is awkward. You do know that you need 36 $itemPlural:30000420$ and 5 $itemPlural:30000421$, don't you? Come back when you have them. 
                return true;
            case 145:
                // $script:0704154107006544$ 
                // - I've asked around everywhere, but I haven't heard anything. I'll find a solution, though. It's just a matter of time. Say... do you happen to know a man named $npcName:11001212[gender:0]$? I hear he deals in $itemPlural:30000421$. You might ask him to see if he knows anything.  
                return true;
            case 150:
                // $script:0704154107006545$ 
                // - What brings you here, $MyPCName$?  
                switch (selection) {
                    // $script:0704154107006546$
                    // - I want a sealed Balrog's weapon.
                    case 0:
                        Id = 0; // TODO: 151 | 154
                        return false;
                    // $script:0704154107006547$
                    // - Any news about the weapon?
                    case 1:
                        Id = 155;
                        return false;
                }
                return true;
            case 151:
                // $script:0704154107006548$ 
                // - Right. You're the one who wanted to take one of $npcName:23090005[gender:0]$'s weapons and imbue it with his power. Give me a minute. If you have the spoils of your victory, I can imbue the weapon for you.  
                switch (selection) {
                    // $script:0704154107006549$
                    // - Take your time.
                    case 0:
                        Id = 0; // TODO: 152 | 153
                        return false;
                }
                return true;
            case 152:
                // $script:0704154107006550$ functionID=12 
                // - It's done. There you go.  
                return true;
            case 153:
                // $script:0704154107006551$ 
                // - It looks like your bag is full. Make some room, if you'd be so kind.  
                return true;
            case 154:
                // $script:0704154107006552$ 
                // - Well, this is awkward. You do know that you need 36 $itemPlural:30000420$ and 5 $itemPlural:30000421$, don't you? Come back when you have them. 
                return true;
            case 155:
                // $script:0704154107006553$ 
                // - I've asked around everywhere, but I haven't heard anything. I'll find a solution, though. It's just a matter of time. Say... do you happen to know a man named $npcName:11001212[gender:0]$? I hear he deals in $itemPlural:30000421$. You might ask him to see if he knows anything.  
                return true;
            default:
                return true;
        }
    }
}
