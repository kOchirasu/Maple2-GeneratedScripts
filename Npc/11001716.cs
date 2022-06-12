using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001716: Junta
/// </summary>
public class _11001716 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0728022507006967$
    // - What?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0728024507007007$
                // - If you have something to say, just say it.
                switch (selection) {
                    // $script:0804030507007029$
                    // - How are your injuries?
                    case 0:
                        return 40;
                }
                return -1;
            case (40, 0):
                // $script:0804030507007030$
                // - They are... instructive.
                switch (selection) {
                    // $script:0804030507007031$
                    // - What does that mean?
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:0804030507007032$
                // - The best victory is a half-victory. The second best is an easy victory. The worst is a complete victory. Do you know why?
                switch (selection) {
                    // $script:0804030507007033$
                    // - No.
                    case 0:
                        return 42;
                    // $script:0804030507007034$
                    // - Victory and defeat are meaningless concepts.
                    case 1:
                        return 50;
                    // $script:0804030507007035$
                    // - I like the victories where I crush my foes.
                    case 2:
                        return 60;
                }
                return -1;
            case (42, 0):
                // $script:0804030507007036$
                // - An easy victory makes you lazy. A complete victory makes you arrogant, and is almost always followed by a crushing defeat. A half-victory, on the other hand, is only half of a defeat. You have a chance to get up and try again.
                return 42;
            case (42, 1):
                // $script:0804030507007037$
                // - I may have been defeated on Halo Mountain, but my small victories gave me the courage—no, a reason—to try again.
                return 42;
            case (42, 2):
                // $script:0804030507007038$
                // - Defeat is just another part of training. The master said that every mistake is a chance to better yourself. Do you understand now?
                //   <font color="#909090">(Junta grins at you.)</font>
                switch (selection) {
                    // $script:0804030507007039$
                    // - Let's talk about something else.
                    case 0:
                        return 30;
                }
                return -1;
            case (50, 0):
                // $script:0804030507007040$
                // - Don't get philosophical on me. A <i>real</i> philosopher once said, "Do not let what you think you know get in the way of what you have yet to learn."
                return 50;
            case (50, 1):
                // $script:0804030507007041$
                // - Every concept, no matter how insignificant, has some value. I suggest you listen carefully. 
                return 50;
            case (50, 2):
                // $script:0804030507007042$
                // - An easy victory makes you lazy. A complete victory makes you arrogant, and is almost always followed by a crushing defeat. A half-victory, on the other hand, is only half of a defeat. You have a chance to get up and try again.
                return 50;
            case (50, 3):
                // $script:0804030507007043$
                // - Defeat is just another part of training. The master said that every mistake is a chance to better yourself. Do you understand now?
                //   <font color="#909090">(Junta watches you closely.)</font>
                return -1;
            case (60, 0):
                // $script:0804030507007044$
                // - A victory like that makes you arrogant, and is almost always followed by a crushing defeat. A half-victory, on the other hand, is only half of a defeat. You have a chance to get up and try again.
                switch (selection) {
                    // $script:0804030507007045$
                    // - Was Halo Mountain your first half-victory?
                    case 0:
                        return 61;
                }
                return -1;
            case (61, 0):
                // $script:0804030507007046$
                // - The world is larger than you think. Even outside of Guidance, there are great warriors to rival my own abilities. There is one in particular that I remember to this day... a champion of a place called $map:02000100$.
                switch (selection) {
                    // $script:0804030507007047$
                    // - An outsider beat you? They must have been a great beast.
                    case 0:
                        return 62;
                }
                return -1;
            case (62, 0):
                // $script:0804030507007048$
                // - Not a beast... a man. And who said I lost?! I'm insulted that you'd think I would lose to a human... Still, this one was my match.
                switch (selection) {
                    // $script:0804030507007049$
                    // - Who was he?
                    case 0:
                        return 63;
                }
                return -1;
            case (63, 0):
                // $script:0804030507007050$
                // - It doesn't matter. I don't even remember his name. All I recall is his long red hair, and the scars that covered his body.
                return 63;
            case (63, 1):
                // $script:0804030507007051$
                // - He was too fast and strong to be a normal human. His punches... It was as if he somehow had command of animus. I wonder what sort of training makes a man like that...
                return 63;
            case (63, 2):
                // $script:0804030507007052$
                // - Well? Do you have anything to say?
                switch (selection) {
                    // $script:0804030507007053$
                    // - It sounds like he had real strength.
                    case 0:
                        return 64;
                }
                return -1;
            case (64, 0):
                // $script:0804030507007054$
                // - He did. And he got that strength on his own, through hard work. You, on the other hand, are only strong because of the master's animus, and you still faint from time to time! So you'd better train just as hard, understand?
                switch (selection) {
                    // $script:0804030507007055$
                    // - Yes.
                    case 0:
                        return 65;
                }
                return -1;
            case (65, 0):
                // $script:0804030507007056$
                // - We're threatened by the strongest enemy we've ever met. We can lay low for now, but eventually we will need to unite our power and take him down. Will you be strong enough to do your part when the time comes?
                return 65;
            case (65, 1):
                // $script:0804030507007057$
                // - You're dismissed.
                switch (selection) {
                    // $script:0804030507007058$
                    // - Let's talk about something else.
                    case 0:
                        return 30;
                }
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.SelectableDistractor,
            (42, 0) => NpcTalkButton.Next,
            (42, 1) => NpcTalkButton.Next,
            (42, 2) => NpcTalkButton.SelectableDistractor,
            (50, 0) => NpcTalkButton.Next,
            (50, 1) => NpcTalkButton.Next,
            (50, 2) => NpcTalkButton.Next,
            (50, 3) => NpcTalkButton.Close,
            (60, 0) => NpcTalkButton.SelectableDistractor,
            (61, 0) => NpcTalkButton.SelectableDistractor,
            (62, 0) => NpcTalkButton.SelectableDistractor,
            (63, 0) => NpcTalkButton.Next,
            (63, 1) => NpcTalkButton.Next,
            (63, 2) => NpcTalkButton.SelectableDistractor,
            (64, 0) => NpcTalkButton.SelectableDistractor,
            (65, 0) => NpcTalkButton.Next,
            (65, 1) => NpcTalkButton.SelectableDistractor,
            _ => NpcTalkButton.None,
        };
    }
}
