using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001244: Ishura
/// </summary>
public class _11001244 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1203181207004687$
    // - There's a lingering aura of runic magic... I must be close.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1203181207004690$
                // - $MyPCName$?! What are you doing here? You  were a fool to come! 
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
