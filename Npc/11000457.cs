using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000457: Yuri
/// </summary>
public class _11000457 : NpcScript {
    internal _11000457(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002034$ 
                // - What? Is there something you want to ask me?
                return true;
            case 30:
                // $script:0831180407002037$ 
                // - It's such a nice day to go for a walk or get some juice, but my dumb lump of a boyfriend wants to stay inside. Look at him, he's not even doing anything! Can you convince him to do something with his life?
                return true;
            default:
                return true;
        }
    }
}
