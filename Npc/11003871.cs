using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003871: Mighton
/// </summary>
public class _11003871 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0417135107009858$
    // - Are you supposed to be here?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0417135107009859$
                // - I hate, hate, <i>hate</i> managing people!
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
