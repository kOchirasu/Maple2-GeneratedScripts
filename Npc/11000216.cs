using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000216: Humphrey
/// </summary>
public class _11000216 : NpcScript {
    internal _11000216(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000944$ 
                // - What is it? 
                return true;
            case 20:
                // $script:0831180407000946$ 
                // - Money, money, money! That's always the problem. $npcName:11000252[gender:0]$ is obsessed with money, and $npcName:11000065[gender:0]$ only cares about development. If they really got together to fool the citizens, we'll make them pay for it! 
                return true;
            default:
                return true;
        }
    }
}
