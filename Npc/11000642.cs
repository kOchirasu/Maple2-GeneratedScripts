using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000642: Prisoner 150124
/// </summary>
public class _11000642 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 40;50
    }

    // Select 0:
    // $script:0831180407002617$
    // - Did you call me?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0831180407002621$
                // - I know all the guards, and you ain't one of them.
                switch (selection) {
                    // $script:0831180407002622$
                    // - How did you end up in here?
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:0831180407002623$
                // - I made a T-shirt with a sexy picture on it, so what? That's not a crime!
                return -1;
            case (50, 0):
                // $script:1210061907004906$
                // - I know all the guards, and you ain't one of them.
                switch (selection) {
                    // $script:1210061907004907$
                    // - Do you know someone named $npcName:11001231[gender:0]$?
                    case 0:
                        return 51;
                }
                return -1;
            case (51, 0):
                // $script:1210061907004908$
                // - What's it to you?
                //   <font color="#909090">(He narrows his eyes at you.)</font>
                switch (selection) {
                    // $script:1210061907004909$
                    // - I'm working with him.
                    case 0:
                        return 52;
                }
                return -1;
            case (52, 0):
                // $script:1210061907004910$
                // - Hm... Yeah, you don't look like no ordinary tourist. Tell him not to worry. Everything's right on schedule.
                switch (selection) {
                    // $script:1210061907004911$
                    // - I need to see the supervisor.
                    case 0:
                        return 53;
                }
                return -1;
            case (53, 0):
                // $script:1210061907004912$
                // - Yeah, yeah, sure. That's $npcName:11000651[gender:0]$. But he won't talk to you unless you know the password.
                switch (selection) {
                    // $script:1210061907004913$
                    // - What's the password?
                    case 0:
                        return 54;
                }
                return -1;
            case (54, 0):
                // $script:1210061907004914$
                // - Hold your horses. I wrote it down somewhere...
                return 54;
            case (54, 1):
                // $script:1210061907004915$
                // - Here we go. "Thick shadows have been cast..." ...something something... "...illuminate light..." Dang, who smudged up the password?
                return 54;
            case (54, 2):
                // $script:1210061907004916$
                // - Sorry, $male:buddy,female:lady$. You got to get the rest from someone else.
                switch (selection) {
                    // $script:1214232607004979$
                    // - Why can't I just talk to the supervisor?
                    case 0:
                        return 55;
                }
                return -1;
            case (55, 0):
                // $script:1214232607004980$
                // - Listen, the supervisor won't even talk to <i>me</i> without the password. You don't stand a chance without it.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.SelectableDistractor,
            (51, 0) => NpcTalkButton.SelectableDistractor,
            (52, 0) => NpcTalkButton.SelectableDistractor,
            (53, 0) => NpcTalkButton.SelectableDistractor,
            (54, 0) => NpcTalkButton.Next,
            (54, 1) => NpcTalkButton.Next,
            (54, 2) => NpcTalkButton.SelectableDistractor,
            (55, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
