using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000063: Kanna
/// </summary>
public class _11000063 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407000294$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000298$
                // - I want to become a great Heavy Gunner like $npcName:11000046[gender:1]$ when I grow up! Pew pew!
                switch (selection) {
                    // $script:0831180407000299$
                    // - Why's that?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0831180407000300$
                // - Well, yesterday I was out playing by the castle and I tripped on a stone. It really hurt and I cried a whole lot! Then $npcName:11000046[gender:1]$ saw me crying and asked why, because she's a HERO.
                return 31;
            case (31, 1):
                // $script:0831180407000301$
                // - I told her all about tripping over the stone, and how I hate stones now! So $npcName:11000046[gender:1]$ took her giant gun... and BLEW UP the stone! Ka-BOOOOSH!
                return 31;
            case (31, 2):
                // $script:0831180407000302$
                // - $npcName:11000046[gender:1]$ said that if something hurts her, she'll hurt it ten times worse! Now those are words to live by, right? Right?
                switch (selection) {
                    // $script:0831180407000303$
                    // - Yes.
                    case 0:
                        return 32;
                    // $script:0831180407000304$
                    // - No.
                    case 1:
                        return 36;
                }
                return -1;
            case (32, 0):
                // $script:0831180407000305$
                // - Hooray, you get it! You know, $npcName:11000046[gender:1]$ and I have a secret now.
                switch (selection) {
                    // $script:0831180407000306$
                    // - What's the secret?
                    case 0:
                        return 33;
                }
                return -1;
            case (33, 0):
                // $script:0831180407000307$
                // - Well, it's a secret... Can you keep it secret?
                switch (selection) {
                    // $script:0831180407000308$
                    // - Of course.
                    case 0:
                        return 34;
                    // $script:0831180407000309$
                    // - I'll decide after you tell me.
                    case 1:
                        return 35;
                }
                return -1;
            case (34, 0):
                // $script:0831180407000310$
                // - This really is a secret... Alright, I'll tell you because you're $MyPCName$.
                return 34;
            case (34, 1):
                // $script:0831180407000311$
                // - When $npcName:11000046[gender:1]$ blew up the stone, she also blew up a bunch of hay and firewood that was lying around.
                return 34;
            case (34, 2):
                // $script:0831180407000312$
                // - No one knows she did it except me. And her. And now you! So $MyPCName$, you'll keep this a secret, right? $npc:11000046[gender:1]$ made me pinky-swear not to tell, so you have to pinky-swear to me.
                return -1;
            case (35, 0):
                // $script:0831180407000313$
                // - No! Then I'm not going to tell you! Hmph!
                return -1;
            case (36, 0):
                // $script:0831180407000314$
                // - Oh $MyPCName$, you don't understand me.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Next,
            (31, 1) => NpcTalkButton.Next,
            (31, 2) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.SelectableDistractor,
            (33, 0) => NpcTalkButton.SelectableDistractor,
            (34, 0) => NpcTalkButton.Next,
            (34, 1) => NpcTalkButton.Next,
            (34, 2) => NpcTalkButton.Close,
            (35, 0) => NpcTalkButton.Close,
            (36, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
