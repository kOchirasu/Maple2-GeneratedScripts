using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000232: George
/// </summary>
public class _11000232 : NpcScript {
    internal _11000232(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000983$ 
                // - How may I help you?
                return true;
            case 30:
                // $script:0831180407000985$ 
                // - Dark Wind has changed since $npcName:11000044[gender:0]$ took charge. Now its members are more interested in getting ahead than protecting $map:02000100$ like they used to.
                // $script:0831180407000986$ 
                // - And the people of $map:02000100$ are walking on eggshells around them.
                return true;
            default:
                return true;
        }
    }
}
