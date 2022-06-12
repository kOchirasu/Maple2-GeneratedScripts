using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004045: Erda
/// </summary>
public class _11004045 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0614185307010063$
    // - I'm so very sorry...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0614185307010064$
                // - I'm so very sorry...
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
