using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000629: Kimo
/// </summary>
public class _11000629 : NpcScript {
    internal _11000629(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002530$ 
                // - Screeeeech!
                return true;
            case 20:
                // $script:0831180407002532$ 
                // - $map:02000051$ is a great place to raise a family like mine. Its highlands are safe from monsters on the ground, and my children can practice flying!
                return true;
            default:
                return true;
        }
    }
}
