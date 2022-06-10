using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000376: Timmy
/// </summary>
public class _11000376 : NpcScript {
    internal _11000376(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001544$ 
                // - How may I help you? 
                return true;
            case 30:
                // $script:0831180407001547$ 
                // - Do you believe in aliens? I do! There has to be loads of intelligent creatures out there, the universe is huge! You should stop by some night and watch the stars with me. 
                return true;
            default:
                return true;
        }
    }
}
