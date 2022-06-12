using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000616: Maroon
/// </summary>
public class _11000616 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407002517$
    // - What seems to be the problem?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407002519$
                // - Don't compare us to the empire. They care more about their hierarchy than the safety of their charges. Their hypocrisy is disgusting.
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
