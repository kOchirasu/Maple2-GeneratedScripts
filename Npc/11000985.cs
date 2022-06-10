using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000985: Kelkero
/// </summary>
public class _11000985 : NpcScript {
    internal _11000985(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003395$ 
                // - Please, please leave me alone! I can make it work this time! 
                return true;
            case 20:
                // $script:0831180407003397$ 
                // - Research is no simple matter. One can't produce results on a normal schedule.  
                return true;
            default:
                return true;
        }
    }
}
