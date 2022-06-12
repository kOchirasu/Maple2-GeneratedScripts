using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003513: Latisha
/// </summary>
public class _11003513 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0817044507008806$
    // - What brings you here?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0817044507008809$
                // - What brings you here?
                switch (selection) {
                    // $script:0817044507008810$
                    // - Tell me about the five auras.
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0817044507008811$
                // - The Vayar live in the mountains to the northeast. Break a Vayar apart, and you'll get some Steadfast Will. It isn't easy...
                switch (selection) {
                    // $script:0817044507008812$
                    // - Tell me about the Vayar.
                    case 0:
                        return 32;
                }
                return -1;
            case (32, 0):
                // $script:0817044507008813$
                // - They're solid. And tough. Magic doesn't work on them, either. You've got to fight them up close!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
