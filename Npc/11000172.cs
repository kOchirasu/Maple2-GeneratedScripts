using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000172: Mikey
/// </summary>
public class _11000172 : NpcScript {
    internal _11000172(INpcScriptContext context) : base(context) {
        Id = 50;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000719$ 
                // - What seems to be the problem?
                return true;
            case 50:
                // $script:0831180407000722$ 
                // - This is my first job. That might not seem like a big deal, but I'm proud to be a $map:02000064$ guard. I take my responsibility to the people of $map:02000064$ very seriously.
                return true;
            default:
                return true;
        }
    }
}
