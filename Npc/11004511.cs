using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004511: Mannstad Patrolman
/// </summary>
public class _11004511 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1228182607012461$
    // - Ugh... I'm ready to pass out on my feet...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1228182607012462$
                // - Ugh... I'm ready to pass out on my feet...
                return 10;
            case (10, 1):
                // $script:1228182607012463$
                // - AAAAH! Ugh, you startled me.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
