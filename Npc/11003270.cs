using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003270: Jin
/// </summary>
public class _11003270 : NpcScript {
    internal _11003270(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0403155707008222$ 
                // - What brings you here? 
                return true;
            case 30:
                // $script:0403155707008223$ 
                // - If only Captain Stilton were still alive...  
                return true;
            default:
                return true;
        }
    }
}
