using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004052: Allon
/// </summary>
public class _11004052 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0614185307010077$
    // - The full might of the empire stands behind the Frontier Foundation. We too will stand against the darkness.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0614185307010078$
                // - The full might of the empire stands behind the Frontier Foundation. We too will stand against the darkness.
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
