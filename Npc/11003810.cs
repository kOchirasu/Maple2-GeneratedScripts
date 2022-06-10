using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003810: 
/// </summary>
public class _11003810 : NpcScript {
    internal _11003810(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1228105615009081$ 
                // - What is it?
                return true;
            case 30:
                // $script:1228105615009084$ 
                // - Don't you want the power of the Devil Tree?
                return true;
            default:
                return true;
        }
    }
}
