using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004232: Beatrice
/// </summary>
public class _11004232 : NpcScript {
    internal _11004232(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0809223207010913$ 
                // - I knew you would succeed. 
                return true;
            case 10:
                // $script:0809223207010914$ 
                // - I knew you would succeed. 
                // $script:0809223207010915$ 
                // - I know you are powerful, but you still need to look after yourself. 
                return true;
            default:
                return true;
        }
    }
}
