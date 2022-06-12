using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003886: Landevian
/// </summary>
public class _11003886 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 20;30
    }

    // Select 0:
    // $script:0515102507009924$
    // - What brings you here?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0515102507009925$
                // - What brings you here?
                return -1;
            case (30, 0):
                // $script:0515102507009926$
                // - You seem pretty handy, considering how you handled those tasks. If only Terrun Calibre had more people like you.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
