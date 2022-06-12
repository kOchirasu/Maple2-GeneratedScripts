using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000211: Zeta
/// </summary>
public class _11000211 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407000897$
    // - What do you want?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407000899$
                // - What? Stop bothering me. Don't you have anything better to do?
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
