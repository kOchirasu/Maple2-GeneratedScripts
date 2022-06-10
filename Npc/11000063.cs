using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000063: Kanna
/// </summary>
public class _11000063 : NpcScript {
    internal _11000063(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000294$ 
                // - How may I help you?
                return true;
            case 30:
                // $script:0831180407000298$ 
                // - I want to become a great Heavy Gunner like $npcName:11000046[gender:1]$ when I grow up! Pew pew!
                switch (selection) {
                    // $script:0831180407000299$
                    // - Why's that?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0831180407000300$ 
                // - Well, yesterday I was out playing by the castle and I tripped on a stone. It really hurt and I cried a whole lot! Then $npcName:11000046[gender:1]$ saw me crying and asked why, because she's a HERO.
                // $script:0831180407000301$ 
                // - I told her all about tripping over the stone, and how I hate stones now! So $npcName:11000046[gender:1]$ took her giant gun... and BLEW UP the stone! Ka-BOOOOSH!
                // $script:0831180407000302$ 
                // - $npcName:11000046[gender:1]$ said that if something hurts her, she'll hurt it ten times worse! Now those are words to live by, right? Right?
                switch (selection) {
                    // $script:0831180407000303$
                    // - Yes.
                    case 0:
                        Id = 32;
                        return false;
                    // $script:0831180407000304$
                    // - No.
                    case 1:
                        Id = 36;
                        return false;
                }
                return true;
            case 32:
                // $script:0831180407000305$ 
                // - Hooray, you get it! You know, $npcName:11000046[gender:1]$ and I have a secret now.
                switch (selection) {
                    // $script:0831180407000306$
                    // - What's the secret?
                    case 0:
                        Id = 33;
                        return false;
                }
                return true;
            case 33:
                // $script:0831180407000307$ 
                // - Well, it's a secret... Can you keep it secret?
                switch (selection) {
                    // $script:0831180407000308$
                    // - Of course.
                    case 0:
                        Id = 34;
                        return false;
                    // $script:0831180407000309$
                    // - I'll decide after you tell me.
                    case 1:
                        Id = 35;
                        return false;
                }
                return true;
            case 34:
                // $script:0831180407000310$ 
                // - This really is a secret... Alright, I'll tell you because you're $MyPCName$.
                // $script:0831180407000311$ 
                // - When $npcName:11000046[gender:1]$ blew up the stone, she also blew up a bunch of hay and firewood that was lying around.
                // $script:0831180407000312$ 
                // - No one knows she did it except me. And her. And now you! So $MyPCName$, you'll keep this a secret, right? $npc:11000046[gender:1]$ made me pinky-swear not to tell, so you have to pinky-swear to me.
                return true;
            case 35:
                // $script:0831180407000313$ 
                // - No! Then I'm not going to tell you! Hmph!
                return true;
            case 36:
                // $script:0831180407000314$ 
                // - Oh $MyPCName$, you don't understand me.
                return true;
            default:
                return true;
        }
    }
}
