using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000867: Prussell
/// </summary>
public class _11000867 : NpcScript {
    internal _11000867(INpcScriptContext context) : base(context) {
        Id = 40;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003133$ 
                // - Feel free to take a look around.
                return true;
            case 40:
                // $script:0831180407003137$ 
                // - Bugs love delicious fruit. Just look at all these flies in my shop! That should tell you how sweet my fruit is.
                // $script:0831180407003138$ 
                // - My prices are lower than any supermarket's. Here, come try some samples.
                return true;
            default:
                return true;
        }
    }
}
