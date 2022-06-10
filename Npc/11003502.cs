using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003502: Ramda
/// </summary>
public class _11003502 : NpcScript {
    internal _11003502(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0816160115008982$ 
                // - How may I help you?
                return true;
            case 30:
                // $script:0816160115008984$ 
                // - $npcName:11003501[gender:1]$ and I wanna be bigshots in Team Mushroom someday. But it'd be cool to work for Dryad Co., too... What should we do?
                return true;
            case 40:
                // $script:0816160115008985$ 
                // - The Team Mushroom is a huge organization, you know!
                return true;
            default:
                return true;
        }
    }
}
