using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001473: Kovin
/// </summary>
public class _11001473 : NpcScript {
    internal _11001473(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1224110207005582$ 
                // - What brings you?
                return true;
            case 30:
                // $script:1228134707005720$ 
                // - Nothing is more precious than the ruins and artifacts that our ancestors have left behind. Today, I'm especially proud to be an archaeologist!
                return true;
            default:
                return true;
        }
    }
}
