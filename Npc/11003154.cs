using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003154: Ruly
/// </summary>
public class _11003154 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0306155707008039$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0306155707008042$
                // - If you're troubled, come look at these flowers. It helps. Really!
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
