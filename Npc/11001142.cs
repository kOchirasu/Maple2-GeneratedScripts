using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001142: Meldy
/// </summary>
public class _11001142 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0914192507003920$
    // - Uh. Hi.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0914192507003923$
                // - First the monsters start taking over the forest, and now my friends are all leaving in droves... Hmph. What do I care? I like being alone, anyway!
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
