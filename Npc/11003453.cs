using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003453: Evagor's Chest
/// </summary>
public class _11003453 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0706160807008661$
    // - <font color="#909090">($npcName:11003391[gender:0]$'s belongings are a mess.)</font>
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0706160807008662$
                // - <font color="#909090">($npcName:11003391[gender:0]$'s belongings are a mess.)</font>
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
