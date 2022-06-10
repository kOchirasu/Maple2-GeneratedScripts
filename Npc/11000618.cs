using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000618: Jerrol
/// </summary>
public class _11000618 : NpcScript {
    internal _11000618(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002523$ 
                // - Could you help me?
                return true;
            case 10:
                // $script:0831180407002524$ 
                // - How on the world am I supposed to fix these wagons? I can't carry them back to town!
                return true;
            default:
                return true;
        }
    }
}
