using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001001: Fredrik
/// </summary>
public class _11001001 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0424144807008437$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0424144807008438$
                // - Hello, $MyPCName$!
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
