using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004119: Lumiknight Warrior
/// </summary>
public class _11004119 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0720125407010481$
    // - I've got a mission to complete.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0720125407010482$
                // - You have our full support.
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
