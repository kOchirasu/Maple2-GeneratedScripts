using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001138: Neroa
/// </summary>
public class _11001138 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0911192907003893$
    // - Have you seen any monsters outside?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0911192907003896$
                // - As long as I don't give up hope, all this will be behind me one day... I really wish I could believe that...
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
