using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000985: Kelkero
/// </summary>
public class _11000985 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407003395$
    // - Please, please leave me alone! I can make it work this time!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407003397$
                // - Research is no simple matter. One can't produce results on a normal schedule. 
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
