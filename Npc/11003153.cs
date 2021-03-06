using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003153: Rudy
/// </summary>
public class _11003153 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0306155707008035$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0306155707008038$
                // - $MyPCName$, did you come to enjoy the flowers? So did I!
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
