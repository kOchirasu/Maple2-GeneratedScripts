using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004407: Blackeye
/// </summary>
public class _11004407 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1113161307011831$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1113161307011832$
                // - The alliance needs Dark Wind now more than ever.
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
