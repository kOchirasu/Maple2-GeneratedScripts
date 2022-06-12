using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001243: Ishura
/// </summary>
public class _11001243 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1203181207004683$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1203181207004686$
                // - Now that the draft is in place, we'd better hurry back to the fortress.
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
