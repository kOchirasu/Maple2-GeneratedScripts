using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000284: Arwen
/// </summary>
public class _11000284 : NpcScript {
    internal _11000284(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001109$ 
                // - How may I help you?
                return true;
            case 30:
                // $script:0831180407001112$ 
                // - Getting along with humans is difficult. They're just so different!
                // $script:0831180407001113$ 
                // - I know there are many good humans out there... but it's not easy to find them.
                return true;
            default:
                return true;
        }
    }
}
