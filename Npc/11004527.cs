using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004527: Richard
/// </summary>
public class _11004527 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;50
    }

    // Select 0:
    // $script:0103163407012512$
    // - Oh?!
    // Select 40:
    // $script:0104140207012578$
    // - Aaaah.
    protected override int Select() => Random(0, 40);

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0103163407012513$
                // - Ah... Hello there.
                switch (selection) {
                    // $script:0103163407012514$
                    // - How's the research going?
                    case 0:
                        return 20;
                }
                return -1;
            case (20, 0):
                // $script:0103163407012515$
                // - V-very well. As you can see, I'm burning the midnight oil. Eheheh...
                return 20;
            case (20, 1):
                // $script:0103163407012516$
                // - If you could see our results, why, they'd knock your socks off!
                return 20;
            case (20, 2):
                // $script:0103163407012517$
                // - S-so you go and tell $npcName:11004438[gender:0]$ that we're working hard, okay?
                switch (selection) {
                    // $script:0103163407012518$
                    // - It doesn't look like you're working <i>that</i> hard.
                    case 0:
                        return 30;
                }
                return -1;
            case (30, 0):
                // $script:0103163407012519$
                // - I-I am, and I have the overtime sheets to show it! L-later. I'll have them later. You'll see...
                return -1;
            case (50, 0):
                // $script:0104140207012579$
                // - Isn't this place lovely? I get to enjoy this wonderful nature while I work.
                switch (selection) {
                    // $script:0104140207012580$
                    // - I see the "enjoy" part, but what about the "work" part?
                    case 0:
                        return 60;
                }
                return -1;
            case (60, 0):
                // $script:0104140207012581$
                // - I can't help it if I have resting "relaxed" face. Trust me when I say that we're working hard over here.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (20, 0) => NpcTalkButton.Next,
            (20, 1) => NpcTalkButton.Next,
            (20, 2) => NpcTalkButton.SelectableDistractor,
            (30, 0) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.SelectableDistractor,
            (60, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
