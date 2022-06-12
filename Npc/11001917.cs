using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001917: Guard
/// </summary>
public class _11001917 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:1116181807007420$
    // - Oh no...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:1116181807007422$
                // - Tria is under attack!
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
