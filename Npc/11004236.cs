using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004236: Oska
/// </summary>
public class _11004236 : NpcScript {
    internal _11004236(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0809223207010926$ 
                // - Amazing work, $MyPCName$.
                return true;
            case 10:
                // $script:0809223207010927$ 
                // - Amazing work, $MyPCName$.
                // $script:0809223207010928$ 
                // - I wish everybody was more like you.
                return true;
            default:
                return true;
        }
    }
}
