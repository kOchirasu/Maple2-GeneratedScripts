using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000065: Marco
/// </summary>
public class _11000065 : NpcScript {
    internal _11000065(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000336$ 
                // - How may I help you? 
                return true;
            case 30:
                // $script:0831180407000338$ 
                // - As the mayor, I have a serious dilemma. Should I make the city great again, or is it already great? 
                return true;
            default:
                return true;
        }
    }
}
