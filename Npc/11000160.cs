using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000160: Napolie
/// </summary>
public class _11000160 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;60;70
    }

    // Select 0:
    // $script:0831180407000674$
    // - Yes? How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000677$
                // - How may I help you, $MyPCName$?
                switch (selection) {
                    // $script:0831180407000678$
                    // - How can I increase my job rank?
                    case 0:
                        return 31;
                    // $script:0831180407000679$
                    // - I don't know where I am.
                    case 1:
                        return 32;
                }
                return -1;
            case (31, 0):
                // $script:0831180407000680$
                // - You can talk to the Job Instructors for assistance. They've gathered in $map:02000188$, which you can reach through the entrance right behind me.
                return -1;
            case (32, 0):
                // $script:0831180407000681$
                // - Oh! Well, that's an easy fix. Just press M to see all of Maple World at a glance in your World Map.
                return -1;
            case (60, 0):
                // $script:0303111207007963$
                // - How may I help you, $MyPCName$?
                switch (selection) {
                    // $script:0303111207007964$
                    // - I don't know where I am.
                    case 0:
                        return 61;
                    // $script:0303111207007965$
                    // - I'm bored.
                    case 1:
                        return 62;
                }
                return -1;
            case (61, 0):
                // $script:0303111207007966$
                // - Oh! Well, that's an easy fix. Just press M to see all of Maple World at a glance in your World Map.
                return -1;
            case (62, 0):
                // $script:0303111207007967$
                // - Oh, I'm sorry. Hmm... how'd you like to make some friends? I know it can be awkward, but you'll never know what kind of cool people you can meet until you try it. You can also visit houses and leave a message in their Guestbook.
                return 62;
            case (62, 1):
                // $script:0303111207007968$
                // - You can invite your friends over to your house for a party, explore dungeons, fish, and play music with them. Everything's more fun when you do it with friends!
                return -1;
            case (70, 0):
                // $script:1215102107009677$
                // - Oh my, $MyPCName$! What brings you here?
                switch (selection) {
                    // $script:1215102107009678$
                    // - Do you know anything about the rumors going around?
                    case 0:
                        return 71;
                }
                return -1;
            case (71, 0):
                // $script:1215102107009679$
                // - Funny, that knight earlier asked me about the same thing. Well, I guess these days that rumor is all anyone wants to talk about.
                switch (selection) {
                    // $script:1215102107009680$
                    // - Details, please!
                    case 0:
                        return 72;
                }
                return -1;
            case (72, 0):
                // $script:1215102107009681$
                // - It's like a giant shadow that darkens the skies. It looked like... a giant winged airship. Something about it gives me the heebie jeebies.
                switch (selection) {
                    // $script:1215102107009682$
                    // - How come?
                    case 0:
                        return 73;
                }
                return -1;
            case (73, 0):
                // $script:1215102107009683$
                // - I don't know. It just feels ominous, like something horrible is about to happen. Disaster seems to follow anywhere that shadow is spotted!
                return 73;
            case (73, 1):
                // $script:1215102107009684$
                // - I'm frightened.
                switch (selection) {
                    // $script:1215102107009685$
                    // - Don't worry. I'll protect you.
                    case 0:
                        return 74;
                }
                return -1;
            case (74, 0):
                // $script:1215102107009686$
                // - Really? Thanks, $MyPCName$.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            (32, 0) => NpcTalkButton.Close,
            (60, 0) => NpcTalkButton.SelectableDistractor,
            (61, 0) => NpcTalkButton.Close,
            (62, 0) => NpcTalkButton.Next,
            (62, 1) => NpcTalkButton.Close,
            (70, 0) => NpcTalkButton.SelectableDistractor,
            (71, 0) => NpcTalkButton.SelectableDistractor,
            (72, 0) => NpcTalkButton.SelectableDistractor,
            (73, 0) => NpcTalkButton.Next,
            (73, 1) => NpcTalkButton.SelectableDistractor,
            (74, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
