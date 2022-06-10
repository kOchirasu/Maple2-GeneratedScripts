using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003453: Evagor's Chest
/// </summary>
public class _11003453 : NpcScript {
    internal _11003453(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0706160807008661$ 
                // - <font color="#909090">($npcName:11003391[gender:0]$'s belongings are a mess.)</font>
                return true;
            case 10:
                // $script:0706160807008662$ 
                // - <font color="#909090">($npcName:11003391[gender:0]$'s belongings are a mess.)</font>
                return true;
            default:
                return true;
        }
    }
}
