using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000850: Akarka
/// </summary>
public class _11000850 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003111$
    // - I can think. I can assess.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003114$
                // - Robots are no longer tools. We are capable of much more than our creators.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
