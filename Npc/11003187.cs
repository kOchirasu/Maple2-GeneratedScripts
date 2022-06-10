using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003187: Ralph
/// </summary>
public class _11003187 : NpcScript {
    internal _11003187(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0320132507008113$ 
                // - What do you want? 
                return true;
            case 10:
                // $script:0320132507008114$ 
                // - I call the shots here. 
                return true;
            default:
                return true;
        }
    }
}
