using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001468: Gurio
/// </summary>
public class _11001468 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1223035407005532$
    // - Stop bothering me.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1223035407005535$
                // - You like my safety helmet? Two stripes from front to back is the latest fashion.
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
