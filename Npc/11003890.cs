using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003890: Katvan
/// </summary>
public class _11003890 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 20;30
    }

    // Select 0:
    // $script:0515102507009936$
    // - It's been a while, Red Cape.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0515102507009937$
                // - It's been a while, Red Cape.
                return -1;
            case (30, 0):
                // $script:0515102507009938$
                // - I would give my life for the $npc:11003891[gender:0]$. He is the only reason I still live.
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
