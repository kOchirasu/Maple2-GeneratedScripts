using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004020: Junta
/// </summary>
public class _11004020 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0614185307010027$
    // - To think I'd be stuck here, useless...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0614185307010028$
                // - To think I'd be stuck here, useless...
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
