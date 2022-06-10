using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001375: Bolden
/// </summary>
public class _11001375 : NpcScript {
    internal _11001375(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217144507005356$ 
                // - Wah! You startled me! 
                return true;
            case 30:
                // $script:1217144507005359$ 
                // - Welcome! L-look, just ignore them and keep your eyes on me, okay? Eheheh... 
                // $script:1217144507005360$ 
                // - Eager to get out of here? Try the latest model sports car from Tuning Motors. Just start the engine and leave this dump in the dust! 
                return true;
            default:
                return true;
        }
    }
}
