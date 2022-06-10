using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000984: Naria
/// </summary>
public class _11000984 : NpcScript {
    internal _11000984(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003392$ 
                // - So... bad time travel trip? 
                return true;
            case 20:
                // $script:0831180407003394$ 
                // - I wasn't always so forgetful. On that note... where am I? I don't know what went wrong this time... 
                return true;
            default:
                return true;
        }
    }
}
