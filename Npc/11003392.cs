using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003392: Last of the Vayar
/// </summary>
public class _11003392 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0706160807008589$
    // - 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0706160807008590$
                // - 
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
