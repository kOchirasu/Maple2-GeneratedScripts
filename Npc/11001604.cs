using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001604: Oska
/// </summary>
public class _11001604 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0504151707006092$
    // - What seems to be the problem?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0515180307006141$
                // - We've agreed to accept each other as comrades. That means we must trust and respect one another.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
