using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001537: Ipigio
/// </summary>
public class _11001537 : NpcScript {
    internal _11001537(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0322222107005986$ 
                // - Sh! You'll give me away!  
                return true;
            case 10:
                // $script:0329103507006001$ 
                // - How did you find me...? 
                return true;
            default:
                return true;
        }
    }
}
