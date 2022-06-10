using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001047: Reker
/// </summary>
public class _11001047 : NpcScript {
    internal _11001047(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003578$ 
                // - This has been a perfect misjudgment.
                return true;
            case 30:
                // $script:0831180407003581$ 
                // - Everyone at  Goldus Industries is a real smooth talker. They say they care about us workers, but if they did we wouldn't be having any problems, would we?
                return true;
            default:
                return true;
        }
    }
}
