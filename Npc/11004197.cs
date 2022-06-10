using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004197: Asimov
/// </summary>
public class _11004197 : NpcScript {
    internal _11004197(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806025707010642$ 
                // - Do you need something? 
                return true;
            case 10:
                // $script:0806025707010643$ 
                // - I'm wise enough to admit I've gotten too old to keep up with the youth of today. When you reach a certain age, you've just got to step out of the way and leave things to the next generation. 
                return true;
            default:
                return true;
        }
    }
}
