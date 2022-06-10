using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001007: Lodie
/// </summary>
public class _11001007 : NpcScript {
    internal _11001007(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003433$ 
                // - Who are you? 
                return true;
            case 30:
                // $script:0831180407003436$ 
                // - Can anyone tell me of the world beyond the rainbow? 
                return true;
            default:
                return true;
        }
    }
}
