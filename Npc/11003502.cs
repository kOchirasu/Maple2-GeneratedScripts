using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003502: Ramda
/// </summary>
public class _11003502 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40
    }

    // Select 0:
    // $script:0816160115008982$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0816160115008984$
                // - $npcName:11003501[gender:1]$ and I wanna be bigshots in Team Mushroom someday. But it'd be cool to work for Dryad Co., too... What should we do?
                return -1;
            case (40, 0):
                // $script:0816160115008985$
                // - The Team Mushroom is a huge organization, you know!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
