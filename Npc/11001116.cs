using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001116: Valle
/// </summary>
public class _11001116 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0908154107003746$
    // - What brings you to this place?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0908154107003749$
                // - Did Mom send you to bring me home? I feel bad saying this, but I can't leave yet. Not until the garden is back to normal.
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
