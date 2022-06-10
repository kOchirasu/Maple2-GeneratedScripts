using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003822: Balrog
/// </summary>
public class _11003822 : NpcScript {
    internal _11003822(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0112184707009747$ 
                // - What is it?
                return true;
            case 10:
                // $script:0112184707009748$ 
                // - Those slimeballs...
                return true;
            default:
                return true;
        }
    }
}
