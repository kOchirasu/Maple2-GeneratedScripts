using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004035: Orde
/// </summary>
public class _11004035 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0614185307010055$
    // - It's not like I want to be here. But I've got a debt to repay.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0614185307010056$
                // - It's not like I want to be here. But I've got a debt to repay.
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
