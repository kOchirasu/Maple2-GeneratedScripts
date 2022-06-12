using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000502: Armano
/// </summary>
public class _11000502 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0831180407002182$
    // - Why did you call me?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0831180407002183$
                // - I want to go home... 
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
