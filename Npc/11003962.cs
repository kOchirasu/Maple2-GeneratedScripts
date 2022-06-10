using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003962: Archer
/// </summary>
public class _11003962 : NpcScript {
    internal _11003962(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0614143707010015$ 
                // - Sigh...
                return true;
            case 20:
                // $script:0614143707010016$ 
                // - Hey. Are you any good at tracking people down?
                return true;
            default:
                return true;
        }
    }
}
