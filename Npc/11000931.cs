using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000931: Kaveki
/// </summary>
public class _11000931 : NpcScript {
    internal _11000931(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003305$ 
                // - It's too late for regrets... 
                return true;
            case 20:
                // $script:0831180407003307$ 
                // - Sometimes I hate being able to see things that others can't. 
                return true;
            default:
                return true;
        }
    }
}
