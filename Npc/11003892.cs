using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003892: Turka
/// </summary>
public class _11003892 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 20;30
    }

    // Select 0:
    // $script:0515102507009942$
    // - Hehehe...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0515102507009943$
                // - Hehehe... So you've come to me. Does that mean you're finally ready to accept my terms?
                return -1;
            case (30, 0):
                // $script:0515102507009944$
                // - Who are you to give me orders?
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
