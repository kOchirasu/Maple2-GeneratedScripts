using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003874: Miner
/// </summary>
public class _11003874 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0417135107009864$
    // - All this hard work is for my lovely wife and kid! Just wait a little longer, family!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0417135107009865$
                // - Daddy's got to put food on the table.
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
