using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003519: Nimeisha
/// </summary>
public class _11003519 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0817044507008869$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0817044507008871$
                // - Can I help you?
                switch (selection) {
                    // $script:0817044507008872$
                    // - Tell me about the five auras.
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0817044507008873$
                // - An aura has no physical form. It's intangible. Still, if you focus hard on one thing, you're bound to reach your peak.
                return 31;
            case (31, 1):
                // $script:0817044507008874$
                // - When you focus one gathering one type of aura, you'll feel it build up. Once it's full, it can be placed in a bowl, like water.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Next,
            (31, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
