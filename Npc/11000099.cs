using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000099: Caprio
/// </summary>
public class _11000099 : NpcScript {
    internal _11000099(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000388$ 
                // - What is it?
                return true;
            case 30:
                // $script:0831180407000391$ 
                // - Hey, $MyPCName$! Have you heard about the hero who collected over 1,000 mesos just by hunting monsters? That's me!
                // $script:0831180407000392$ 
                // - I think I was born to be a hunter. You should find something that you can be good at and have fun doing.
                return true;
            default:
                return true;
        }
    }
}
