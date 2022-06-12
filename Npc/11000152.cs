using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000152: Mary
/// </summary>
public class _11000152 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407000647$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407000649$
                // - Everyone's in a festive mood because of the court, and they're not even on the mainland where the court is being held. I wonder how excited the mainlanders must be!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
