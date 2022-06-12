using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000115: Elly
/// </summary>
public class _11000115 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:0831180407000483$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0831180407000487$
                // - Hmph! Just as well. I hope the road stays destroyed forever.
                switch (selection) {
                    // $script:0831180407000488$
                    // - Why's that?
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:0831180407000489$
                // - Smith left for $map:02000001$ to see the court instead of staying with me for my birthday. I don't need a boyfriend who cares more about the empress than me. I hope he'll never come back. Hmph!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
