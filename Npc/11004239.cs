using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004239: Tinchai
/// </summary>
public class _11004239 : NpcScript {
    internal _11004239(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0809223207010935$ 
                // - Is this goodbye? 
                return true;
            case 10:
                // $script:0809223207010936$ 
                // - Is this goodbye? 
                // $script:0809223207010937$ 
                // - You did a great job! 
                // $script:0809223207010938$ 
                // - I wish $npcName:11004238[gender:0]$ felt more like celebrating. I guess he's embarrassed about missing all the action. 
                // $script:0809223207010939$ 
                // - Next time, Guidance will be there to help! Just say the word. 
                return true;
            default:
                return true;
        }
    }
}
