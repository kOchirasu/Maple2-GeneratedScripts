using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000848: Phelan
/// </summary>
public class _11000848 : NpcScript {
    internal _11000848(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003103$ 
                // - What is it? I'm doing something really important. Please don't distract me.
                return true;
            case 30:
                // $script:0831180407003106$ 
                // - The world keeps changing, and our technology and science leads the way. Mark my words, I'll usher in a new era with my work. 
                return true;
            default:
                return true;
        }
    }
}
