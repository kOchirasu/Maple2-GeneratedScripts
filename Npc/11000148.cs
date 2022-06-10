using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000148: Cavan
/// </summary>
public class _11000148 : NpcScript {
    internal _11000148(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000631$ 
                // - What is it?
                return true;
            case 30:
                // $script:0831180407000634$ 
                // - If I wasn't charged with $map:63000004$, I could've joined the delegation. I hate that no one else can fill in for me! 
                return true;
            default:
                return true;
        }
    }
}
