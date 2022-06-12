using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004079: Tellah
/// </summary>
public class _11004079 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0620203007010255$
    // - Rain, rain, go away. Go away forever.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0620203007010256$
                // - Rain, rain, go away. Go away forever.
                return 10;
            case (10, 1):
                // $script:0620203007010257$
                // - Oh, a passing adventurer. Why don't you take a break and chat with me?
                switch (selection) {
                    // $script:0620203007010258$
                    // - Okay. Know any stories?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0620203007010259$
                // - Well, I can tell you <i>your</i> story, if you like. You've been pushing forward without rest. But do you really know where you're going?
                switch (selection) {
                    // $script:0620203007010260$
                    // - What do you mean?
                    case 0:
                        return 32;
                }
                return -1;
            case (32, 0):
                // $script:0620203007010261$
                // - I've been here for over a century. I know many things, including things about <i>you</i>. What would you like to know?
                switch (selection) {
                    // $script:0620203007010262$
                    // - Tell me about my future.
                    case 0:
                        return 33;
                    // $script:0620203007010263$
                    // - Will I ever find true love?
                    case 1:
                        return 34;
                    // $script:0620203007010264$
                    // - How did Maple World come to be?
                    case 2:
                        return 35;
                }
                return -1;
            case (33, 0):
                // $script:0620203007010265$
                // - I tell you I know things, and you assume I'm a darned prophet. Ha! Okay, I'll play along. I see much potential in you, my friend. Your future holds many great things.
                switch (selection) {
                    // $script:0626201407010371$
                    // - ...
                    case 0:
                        return 36;
                }
                return -1;
            case (34, 0):
                // $script:0620203007010266$
                // - And what would I know about love? I've been alone my entire life...
                switch (selection) {
                    // $script:0626201407010372$
                    // - Are you making this up?
                    case 0:
                        return 37;
                }
                return -1;
            case (35, 0):
                // $script:0620203007010267$
                // - Why are you asking me? Didn't someone fill you in when you first started your adventure? Something about two goddesses and the birth of $npcName:11000075[gender:1]$.
                switch (selection) {
                    // $script:0626201407010373$
                    // - I think I remember that.
                    case 0:
                        return 40;
                }
                return -1;
            case (36, 0):
                // $script:0626201407010374$
                // - Live long enough, and you begin to lose perspective on good and evil—right and wrong. The hero of yesterday can become the villain of tomorrow.
                return 36;
            case (36, 1):
                // $script:0626201407010375$
                // - I can't say whether the future will be good or bad, but now... for now, you are magnificent.
                return 36;
            case (36, 2):
                // $script:0626201407010376$
                // - I like to think that everything will work out for people who live their lives with conviction and purpose. You may not believe me now, but someday you'll think back on this old turtle's words and understand.
                return -1;
            case (37, 0):
                // $script:0626201407010377$
                // - That's not to say I've never been in love. There was someone in my life... but she passed away in an accident. I never mustered up the courage to tell her how I felt...
                switch (selection) {
                    // $script:0626201407010378$
                    // - Sorry. I didn't mean to stir up bad memories.
                    case 0:
                        return 38;
                }
                return -1;
            case (38, 0):
                // $script:0626201407010379$
                // - Oh, it's all in the past now. Perhaps, when I leave behind this mortal coil, I'll see her again. It's something that gives me hope, anyway.
                switch (selection) {
                    // $script:0626201407010380$
                    // - I'm sure you'll see her again.
                    case 0:
                        return 39;
                }
                return -1;
            case (39, 0):
                // $script:0626201407010381$
                // - That's kind of you to say. If I were to give you any advice, it would be this—don't follow in my footsteps. When you find someone you love, tell them how you feel. Don't live your whole life wondering what could have been...
                return -1;
            case (40, 0):
                // $script:0626201407010382$
                // - The goddess of light may be gone, but the remnants of her power permeate this world. It is up to you to help the empress carry that blessed light on into the future.
                switch (selection) {
                    // $script:0626201407010383$
                    // - How'd you know I'm helping the empress?
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:0626201407010384$
                // - Oh, you don't get to my age without learning how to keep your ears open.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.SelectableDistractor,
            (33, 0) => NpcTalkButton.SelectableDistractor,
            (34, 0) => NpcTalkButton.SelectableDistractor,
            (35, 0) => NpcTalkButton.SelectableDistractor,
            (36, 0) => NpcTalkButton.Next,
            (36, 1) => NpcTalkButton.Next,
            (36, 2) => NpcTalkButton.Close,
            (37, 0) => NpcTalkButton.SelectableDistractor,
            (38, 0) => NpcTalkButton.SelectableDistractor,
            (39, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
