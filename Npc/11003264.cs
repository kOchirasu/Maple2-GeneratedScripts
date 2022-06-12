using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003264: Anne
/// </summary>
public class _11003264 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0403155707008208$
    // - I can't believe this happened to $map:02000023$. 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0403155707008209$
                // - We should have been ready for this. It was naive to think Ellinel was safe...
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
