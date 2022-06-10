using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003432: Anne
/// </summary>
public class _11003432 : NpcScript {
    internal _11003432(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0721140007008680$ 
                // - My mind is somewhere else today. 
                return true;
            case 10:
                // $script:0721142007008698$ 
                // - The work never ends. 
                return true;
            default:
                return true;
        }
    }
}
