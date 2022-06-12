using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001301: Ereve
/// </summary>
public class _11001301 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1215203907005018$
    // - $MyPCName$, what brings you to me?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1215203907005019$
                // - Were it not for the lumarigons, we would not have defeated the Demon King. We must go to Drachenheim's aid.
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
