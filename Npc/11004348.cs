using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004348: Claus
/// </summary>
public class _11004348 : NpcScript {
    internal _11004348(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1109213607011755$ 
                // - I hope this hasn't been too hard on poor $npcName:11004345[gender:1]$... 
                return true;
            case 10:
                // $script:1109213607011756$ 
                // - Is my family safe? What a stressful season this has been. 
                return true;
            default:
                return true;
        }
    }
}
