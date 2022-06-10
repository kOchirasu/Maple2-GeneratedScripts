using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000959: Darren
/// </summary>
public class _11000959 : NpcScript {
    internal _11000959(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003322$ 
                // - Step back. You stand around gawking like that and you're sure to get eaten.
                return true;
            case 20:
                // $script:0831180407003324$ 
                // - It's hard enough to keep black market dealers from slipping in from $map:02000100$. Now we have to deal with these stupid monsters!
                return true;
            default:
                return true;
        }
    }
}
