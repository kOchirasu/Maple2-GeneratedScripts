using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000160: Napolie
/// </summary>
public class _11000160 : NpcScript {
    internal _11000160(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;60;70
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000674$ 
                // - Yes? How may I help you?
                return true;
            case 30:
                // $script:0831180407000677$ 
                // - How may I help you, $MyPCName$?
                switch (selection) {
                    // $script:0831180407000678$
                    // - How can I increase my job rank?
                    case 0:
                        Id = 31;
                        return false;
                    // $script:0831180407000679$
                    // - I don't know where I am.
                    case 1:
                        Id = 32;
                        return false;
                }
                return true;
            case 31:
                // $script:0831180407000680$ 
                // - You can talk to the Job Instructors for assistance. They've gathered in $map:02000188$, which you can reach through the entrance right behind me.
                return true;
            case 32:
                // $script:0831180407000681$ 
                // - Oh! Well, that's an easy fix. Just press M to see all of Maple World at a glance in your World Map.
                return true;
            case 60:
                // $script:0303111207007963$ 
                // - How may I help you, $MyPCName$?
                switch (selection) {
                    // $script:0303111207007964$
                    // - I don't know where I am.
                    case 0:
                        Id = 61;
                        return false;
                    // $script:0303111207007965$
                    // - I'm bored.
                    case 1:
                        Id = 62;
                        return false;
                }
                return true;
            case 61:
                // $script:0303111207007966$ 
                // - Oh! Well, that's an easy fix. Just press M to see all of Maple World at a glance in your World Map.
                return true;
            case 62:
                // $script:0303111207007967$ 
                // - Oh, I'm sorry. Hmm... how'd you like to make some friends? I know it can be awkward, but you'll never know what kind of cool people you can meet until you try it. You can also visit houses and leave a message in their Guestbook.
                // $script:0303111207007968$ 
                // - You can invite your friends over to your house for a party, explore dungeons, fish, and play music with them. Everything's more fun when you do it with friends!
                return true;
            case 70:
                // $script:1215102107009677$ 
                // - Oh my, $MyPCName$! What brings you here?
                switch (selection) {
                    // $script:1215102107009678$
                    // - Do you know anything about the rumors going around?
                    case 0:
                        Id = 71;
                        return false;
                }
                return true;
            case 71:
                // $script:1215102107009679$ 
                // - Funny, that knight earlier asked me about the same thing. Well, I guess these days that rumor is all anyone wants to talk about.
                switch (selection) {
                    // $script:1215102107009680$
                    // - Details, please!
                    case 0:
                        Id = 72;
                        return false;
                }
                return true;
            case 72:
                // $script:1215102107009681$ 
                // - It's like a giant shadow that darkens the skies. It looked like... a giant winged airship. Something about it gives me the heebie jeebies.
                switch (selection) {
                    // $script:1215102107009682$
                    // - How come?
                    case 0:
                        Id = 73;
                        return false;
                }
                return true;
            case 73:
                // $script:1215102107009683$ 
                // - I don't know. It just feels ominous, like something horrible is about to happen. Disaster seems to follow anywhere that shadow is spotted!
                // $script:1215102107009684$ 
                // - I'm frightened.
                switch (selection) {
                    // $script:1215102107009685$
                    // - Don't worry. I'll protect you.
                    case 0:
                        Id = 74;
                        return false;
                }
                return true;
            case 74:
                // $script:1215102107009686$ 
                // - Really? Thanks, $MyPCName$.
                return true;
            default:
                return true;
        }
    }
}
