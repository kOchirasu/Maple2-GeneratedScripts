using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000060: Betty
/// </summary>
public class _11000060 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407000269$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000272$
                // - $MyPCName$, are you also going to the mainland?
                switch (selection) {
                    // $script:0831180407000273$
                    // - That's right.
                    case 0:
                        return 31;
                    // $script:0831180407000274$
                    // - I don't know.
                    case 1:
                        return 32;
                }
                return -1;
            case (31, 0):
                // $script:0831180407000275$
                // - You've made a good decision. I've stayed on this small island my whole life, but I want you to go see more of the this world.
                return 31;
            case (31, 1):
                // $script:0831180407000276$
                // - While you're there at the court, you might as well explore the rest of the mainland. I'd love for you to come back with tales of the things you saw.
                return -1;
            case (32, 0):
                // $script:0831180407000277$
                // - Cross the sea to the mainland to experience more of what this world can offer.Go on, don't be afraid.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Next,
            (31, 1) => NpcTalkButton.Close,
            (32, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
